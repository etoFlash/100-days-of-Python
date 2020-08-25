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
def delete_task(id_task):
    order_num = queries.get_order_task(conn, id_task=id_task)[0]

    queries.delete_task(conn, id_task=id_task)
    queries.reorder_tasks(conn, order_num=order_num)

    conn.commit()


def add_task(task_text):
    order_num = queries.get_max_order(conn)[0] + 1
    queries.add_task(conn, task_text=task_text, order_num=order_num)

    conn.commit()


if __name__ == '__main__':
    run(host='localhost', port=8080)
