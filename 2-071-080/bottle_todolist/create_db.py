import sqlite3


def create_or_replace_schema(db_name="todo.db"):
    with sqlite3.connect(db_name) as conn:
        conn.execute("DROP TABLE IF EXISTS t_task")
        conn.execute(
            "CREATE TABLE t_task ("
            "    id_task   INTEGER PRIMARY KEY"
            "  , task_text TEXT    NOT NULL"
            "  , order_num INTEGER NOT NULL"
            ");"
        )


if __name__ == '__main__':
    create_or_replace_schema()
