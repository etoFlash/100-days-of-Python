-- name: add_task!
INSERT INTO t_task (task_text, order_num)
            VALUES (:task_text, :order_num);

-- name: get_max_order^
SELECT COALESCE(MAX(order_num), 0) AS max_order_num
  FROM t_task;

-- name: get_order_task^
SELECT order_num
  FROM t_task
 WHERE id_task = :id_task;

-- name: reorder_tasks!
UPDATE t_task
   SET order_num = order_num - 1
 WHERE order_num > :order_num;

-- name: delete_task!
DELETE FROM t_task
 WHERE id_task = :id_task;

-- name: get_tasks
SELECT id_task
     , task_text
     , order_num
  FROM t_task
 ORDER BY order_num DESC;