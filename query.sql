SELECT t.name, t.ts, t.high, t.hour
FROM (
     SELECT name, ts, high, SUBSTRING(ts, 12, 2) as hour
     FROM streamingdata19) AS t
JOIN (SELECT 
    MAX(name) as name,
    MAX(hour) as hour,
    MAX(high) as high
    FROM (
    SELECT name, ts, high, SUBSTRING(ts, 12, 2) as hour
    FROM streamingData19
    )
    GROUP BY name, hour) AS m ON (t.name = m.name AND t.hour = m.hour AND t.high = m.high)
ORDER BY t.hour, t.name
--LIMIT 10;