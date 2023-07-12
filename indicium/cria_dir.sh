#!/bin/bash


# Criação dos diretórios do HDFS
hdfs dfs -mkdir /hdfs
hdfs dfs -chmod 775 /hdfs
hdfs dfs -mkdir /hdfs/data
hdfs dfs -chmod 775 /hdfs/data
hdfs dfs -mkdir /hdfs/data/order
hdfs dfs -chmod 775 /hdfs/data/order


hdfs dfs -mkdir /hdfs/data/order/order_details
hdfs dfs -chmod 775 /hdfs/data/order/order_details
hdfs dfs -mkdir /hdfs/data/order/order_details/input
hdfs dfs -chmod 775 /hdfs/data/order/order_details/input
hdfs dfs -mkdir /hdfs/data/order/order_details/backup
hdfs dfs -chmod 775 /hdfs/data/order/order_details/backup

hdfs dfs -mkdir /hdfs/data/order/categories
hdfs dfs -chmod 775 /hdfs/data/order/categories
hdfs dfs -mkdir /hdfs/data/order/categories/input
hdfs dfs -chmod 775 /hdfs/data/order/categories/input
hdfs dfs -mkdir /hdfs/data/order/categories/backup
hdfs dfs -chmod 775 /hdfs/data/order/categories/backup

hdfs dfs -mkdir /hdfs/data/order/customer_customer_demo
hdfs dfs -chmod 775 /hdfs/data/order/customer_customer_demo
hdfs dfs -mkdir /hdfs/data/order/customer_customer_demo/input
hdfs dfs -chmod 775 /hdfs/data/order/customer_customer_demo/input
hdfs dfs -mkdir /hdfs/data/order/customer_customer_demo/backup
hdfs dfs -chmod 775 /hdfs/data/order/customer_customer_demo/backup

hdfs dfs -mkdir /hdfs/data/order/customer_demographics
hdfs dfs -chmod 775 /hdfs/data/order/customer_demographics
hdfs dfs -mkdir /hdfs/data/order/customer_demographics/input
hdfs dfs -chmod 775 /hdfs/data/order/customer_demographics/input
hdfs dfs -mkdir /hdfs/data/order/customer_demographics/backup
hdfs dfs -chmod 775 /hdfs/data/order/customer_demographics/backup

hdfs dfs -mkdir /hdfs/data/order/customers
hdfs dfs -chmod 775 /hdfs/data/order/customers
hdfs dfs -mkdir /hdfs/data/order/customers/input
hdfs dfs -chmod 775 /hdfs/data/order/customers/input
hdfs dfs -mkdir /hdfs/data/order/customers/backup
hdfs dfs -chmod 775 /hdfs/data/order/customers/backup

hdfs dfs -mkdir /hdfs/data/order/employee_territories
hdfs dfs -chmod 775 /hdfs/data/order/employee_territories
hdfs dfs -mkdir /hdfs/data/order/employee_territories/input
hdfs dfs -chmod 775 /hdfs/data/order/employee_territories/input
hdfs dfs -mkdir /hdfs/data/order/employee_territories/backup
hdfs dfs -chmod 775 /hdfs/data/order/employee_territories/backup

hdfs dfs -mkdir /hdfs/data/order/employees
hdfs dfs -chmod 775 /hdfs/data/order/employees
hdfs dfs -mkdir /hdfs/data/order/employees/input
hdfs dfs -chmod 775 /hdfs/data/order/employees/input
hdfs dfs -mkdir /hdfs/data/order/employees/backup
hdfs dfs -chmod 775 /hdfs/data/order/employees/backup

hdfs dfs -mkdir /hdfs/data/order/orders
hdfs dfs -chmod 775 /hdfs/data/order/orders
hdfs dfs -mkdir /hdfs/data/order/orders/input
hdfs dfs -chmod 775 /hdfs/data/order/orders/input
hdfs dfs -mkdir /hdfs/data/order/orders/backup
hdfs dfs -chmod 775 /hdfs/data/order/orders/backup

hdfs dfs -mkdir /hdfs/data/order/products
hdfs dfs -chmod 775 /hdfs/data/order/products
hdfs dfs -mkdir /hdfs/data/order/products/input
hdfs dfs -chmod 775 /hdfs/data/order/products/input
hdfs dfs -mkdir /hdfs/data/order/products/backup
hdfs dfs -chmod 775 /hdfs/data/order/products/backup

hdfs dfs -mkdir /hdfs/data/order/region
hdfs dfs -chmod 775 /hdfs/data/order/region
hdfs dfs -mkdir /hdfs/data/order/region/input
hdfs dfs -chmod 775 /hdfs/data/order/region/input
hdfs dfs -mkdir /hdfs/data/order/region/backup
hdfs dfs -chmod 775 /hdfs/data/order/region/backup

hdfs dfs -mkdir /hdfs/data/order/shippers
hdfs dfs -chmod 775 /hdfs/data/order/shippers
hdfs dfs -mkdir /hdfs/data/order/shippers/input
hdfs dfs -chmod 775 /hdfs/data/order/shippers/input
hdfs dfs -mkdir /hdfs/data/order/shippers/backup
hdfs dfs -chmod 775 /hdfs/data/order/shippers/backup

hdfs dfs -mkdir /hdfs/data/order/suppliers
hdfs dfs -chmod 775 /hdfs/data/order/suppliers
hdfs dfs -mkdir /hdfs/data/order/suppliers/input
hdfs dfs -chmod 775 /hdfs/data/order/suppliers/input
hdfs dfs -mkdir /hdfs/data/order/suppliers/backup
hdfs dfs -chmod 775 /hdfs/data/order/suppliers/backup

hdfs dfs -mkdir /hdfs/data/order/territories
hdfs dfs -chmod 775 /hdfs/data/order/territories
hdfs dfs -mkdir /hdfs/data/order/territories/input
hdfs dfs -chmod 775 /hdfs/data/order/territories/input
hdfs dfs -mkdir /hdfs/data/order/territories/backup
hdfs dfs -chmod 775 /hdfs/data/order/territories/backup

hdfs dfs -mkdir /hdfs/data/order/us_states
hdfs dfs -chmod 775 /hdfs/data/order/us_states
hdfs dfs -mkdir /hdfs/data/order/us_states/input
hdfs dfs -chmod 775 /hdfs/data/order/us_states/input
hdfs dfs -mkdir /hdfs/data/order/us_states/backup
hdfs dfs -chmod 775 /hdfs/data/order/us_states/backup



