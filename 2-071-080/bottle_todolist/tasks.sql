-- name: add_task!
INSERT INTO t_task (task_text)
            VALUES (:task_text);

-- name: get_tasks
SELECT id_task
     , task_text 
  FROM t_task
 ORDER BY id_task DESC;