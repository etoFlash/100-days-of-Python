import sqlite3

from bottle import get, post, request, template, run, static_file
import aiosql


conn = sqlite3.connect("todo.db")
queries = aiosql.from_path("tasks.sql", "sqlite3")


@get(f"/static/js/<filename>")
def static_js(filename):
    return static_file(filename, root="static/js")


@get("/")
@post("/")
def home():
    if request.method == "POST":
        task_text = request.forms.get('taskInput')
        add_task(task_text)

    return template('templates/index.html', tasks=queries.get_tasks(conn))


@post("/delete/<id_task:int>")
def delete(id_task):
    order_num = queries.get_order_task(conn, id_task=id_task)[0]

    queries.delete_task(conn, id_task=id_task)
    queries.reorder_tasks(conn, order_num=order_num)

    conn.commit()


@post("/move/<id_task:int>/<direction:re:(up|down)>")
def move(id_task, direction):
    order_num = queries.get_order_task(conn, id_task=id_task)[0]

    if not order_num:
        return

    if direction == 'up' and order_num < queries.get_max_order(conn)[0]:
        queries.switch_order_nums(conn, order_num1=order_num, order_num2=order_num + 1)
    elif direction == 'down' and order_num > 1:
        queries.switch_order_nums(conn, order_num1=order_num, order_num2=order_num - 1)

    return template('templates/tasks.html', tasks=queries.get_tasks(conn))


def add_task(task_text):
    order_num = queries.get_max_order(conn)[0] + 1
    queries.add_task(conn, task_text=task_text, order_num=order_num)

    conn.commit()


if __name__ == '__main__':
    run(host='localhost', port=8080)
