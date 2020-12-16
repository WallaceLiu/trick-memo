# 计算经纬度之间的距离
```sql
SELECT  
id,
  obd_id,
  car_id,
  cmd,
  subcmd,
  sd,
  jl,
  lng_baidu,
  lat_baidu,
    ROUND(
    6378.138 * 2 * ASIN(
      SQRT(
        POW(
          SIN((39.770656 * PI() / 180- lat_baidu * PI() / 180) / 2),
          2
        ) + COS(39.770656 * PI() / 180) * COS(lat_baidu * PI() / 180) * POW(
          SIN((116.203169 * PI() / 180- lng_baidu * PI() / 180) / 2),
          2
        )
      )
    ) * 1000
  ) AS juli
FROM
  tb_base_history_15_10_11
WHERE valid_point_num = 2
  AND statistc_status = 3
  AND lng_baidu != 0
  AND lat_baidu != 0
ORDER BY REC_TIME ASC
LIMIT 1000 
```
# 时间相减
```text
(UNIX_TIMESTAMP(updatedtime)-UNIX_TIMESTAMP(createdtime)) 秒
```

# SELECT 创建表
```sql
CREATE TABLE incoming_16_01_07 
SELECT 
  * 
FROM
  incoming 
WHERE YEAR(createdtime) = 2016 
  AND MONTH(createdtime) = 1 
  AND DAY(createdtime) = 7 ;
```
