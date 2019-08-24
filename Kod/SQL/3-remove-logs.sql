DELETE FROM `logs`
  WHERE timestamp <= date('now','-1 month');
