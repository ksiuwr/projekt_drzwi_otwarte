DELETE FROM `logs`
  WHERE timestamp <= date('now','-1 month');
INSERT INTO logs(type, message) SELECT 'info', 'Removed ' || changes() || ' logs' FROM logs LIMIT 1;