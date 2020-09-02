import sqlite3
import csv
from io import StringIO

from bottle import get, post, request, template, run, static_file, response
import aiosql


CONN = sqlite3.connect("todo.db")
QUERIES = aiosql.from_path("tasks.sql", "sqlite3")


@get("/static/js/<filename>")
def static_js(filename):
    return static_file(filename, root="static/js")


@get("/")
@post("/")
def index():
    if request.method == "POST":
        task_text = request.forms.get('taskInput')
        add_task(task_text)

    return template('templates/index.html', tasks=get_tasks())


@post("/delete/<id_task:int>")
def delete(id_task):
    delete_task(id_task)


@post("/move/<id_task:int>/<direction:re:(up|down)>")
def move(id_task, direction):
    move_task(direction, id_task)

    return template('templates/tasks.html', tasks=get_tasks())


@get("/download")
def download():
    return download_tasks()


def get_tasks(conn=CONN):
    return QUERIES.get_tasks(conn)


def delete_task(id_task, conn=CONN):
    order_num = QUERIES.get_order_task(conn, id_task=id_task)[0]
    QUERIES.delete_task(conn, id_task=id_task)
    QUERIES.reorder_tasks(conn, order_num=order_num)

    conn.commit()


def add_task(task_text, conn=CONN):
    order_num = QUERIES.get_max_order(conn)[0] + 1
    QUERIES.add_task(conn, task_text=task_text, order_num=order_num)

    conn.commit()


def move_task(direction, id_task, conn=CONN):
    order_num = QUERIES.get_order_task(conn, id_task=id_task)[0]
    assert order_num, "Order number not found"

    if direction == 'up' and order_num < QUERIES.get_max_order(conn)[0]:
        QUERIES.switch_order_nums(conn, order_num1=order_num, order_num2=order_num + 1)
    elif direction == 'down' and order_num > 1:
        QUERIES.switch_order_nums(conn, order_num1=order_num, order_num2=order_num - 1)


def download_tasks(conn=CONN):
    stream = StringIO()
    writer = csv.writer(stream)
    writer.writerow(["id_task", "task_text", "order_num"])
    writer.writerows(get_tasks(conn=conn))

    response.set_header("Content-type", "text/csv")
    response.set_header("Content-Disposition", "attachment; filename=tasks.csv")

    return stream.getvalue().encode("shift-jis")


if __name__ == '__main__':
    run(host='localhost', port=8080)
