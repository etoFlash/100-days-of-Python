import sqlite3


if __name__ == '__main__':
    with sqlite3.connect("todo.db") as conn:
        conn.execute("DROP TABLE IF EXISTS t_task")
        conn.execute("""CREATE TABLE t_task (
                          id_task   INTEGER PRIMARY KEY,
                          task_text TEXT NOT NULL
                        );""")
