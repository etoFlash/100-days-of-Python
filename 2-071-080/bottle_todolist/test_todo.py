import sqlite3

from todo import download_tasks, add_task, get_tasks
from create_db import create_or_replace_schema

DB_NAME = "test_todo.db"
TEST_CONN = sqlite3.connect(DB_NAME)

create_or_replace_schema(DB_NAME)


def test_download_empty_tasks():
    assert download_tasks(conn=TEST_CONN) == b'id_task,task_text,order_num\r\n'


def test_add_task():
    add_task("First task", conn=TEST_CONN)
    assert get_tasks(conn=TEST_CONN)[0] == (1, 'First task', 1)


def test_download_tasks():
    expected = [
        b"id_task,task_text,order_num",
        b"1,First task,1",
    ]

    assert download_tasks(conn=TEST_CONN).splitlines(keepends=False) == expected

    new_row = b"2,Second task,2"
    expected.insert(1, new_row)
    add_task(new_row.decode("utf-8").split(",")[1], conn=TEST_CONN)

    assert download_tasks(conn=TEST_CONN).splitlines(keepends=False) == expected
