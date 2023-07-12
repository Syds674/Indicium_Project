from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .master("yarn") \
    .appName("Ingestao - dados") \
    .enableHiveSupport() \
    .getOrCreate()

print("CRIANDO A VIEW ORDER_DETAILS!")

spark.sql(f"""
CREATE OR REPLACE VIEW northwind.view_order_details
AS SELECT 
    o.order_id,	
    o.customer_id,
    o.employee_id,
    o.order_date,
    o.required_date,
    o.shipped_date,
    o.ship_via,
    o.freight,
    o.ship_name,
    o.ship_address,
    o.ship_city,
    o.ship_region,
    o.ship_postal_code,
    o.ship_country,
    od.product_id,
    od.unit_price,
    od.quantity,
    od.discount
FROM 
    northwind.orders o
LEFT JOIN 
    northwind.order_details od ON o.order_id = od.order_id;
""")

print("VIEW ORDER_DETAILS CRIADA!")