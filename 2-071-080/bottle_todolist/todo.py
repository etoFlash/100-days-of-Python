import sqlite3

from bottle import get, post, request, template, run
import aiosql


conn = sqlite3.connect("todo.db")
queries = aiosql.from_path("tasks.sql", "sqlite3")


@get("/")
@post("/")
def index():
    if request.method == "POST":
        task_text = request.forms.get('taskInput')
        add_task(task_text)

    return template('templates/index.html')


def add_task(task_text):
    print(task_text)
    queries.add_task(conn, task_text=task_text)
    conn.commit()


if __name__ == '__main__':
    run(host='localhost', port=8080)
