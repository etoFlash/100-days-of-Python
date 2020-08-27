-- name: add_task!
INSERT INTO t_task (task_text, order_num)
            VALUES (:task_text, :order_num);

-- name: get_max_order^
SELECT COALESCE(MAX(order_num), 0) AS max_order_num
  FROM t_task;

-- name: get_min_order^
SELECT COALESCE(MIN(order_num), 0) AS min_order_num
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

-- name: switch_order_nums!
UPDATE t_task
   SET order_num = CASE order_num
                     WHEN :order_num1 THEN :order_num2
                     WHEN :order_num2 THEN :order_num1
                   END
 WHERE order_num IN (:order_num1, :order_num2);
