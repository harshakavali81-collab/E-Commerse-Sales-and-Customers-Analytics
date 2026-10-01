CREATE TABLE customers (customer_id VARCHAR(10) PRIMARY KEY, customer_name VARCHAR(100), gender VARCHAR(20), age INT, city VARCHAR(50), state VARCHAR(10), region VARCHAR(20));
CREATE TABLE products (product_id VARCHAR(10) PRIMARY KEY, product_name VARCHAR(100), category VARCHAR(50), unit_price NUMERIC(12, 2), unit_cost NUMERIC(12, 2));
CREATE TABLE orders (order_id VARCHAR(10) PRIMARY KEY, customer_id VARCHAR(10) REFERENCES customers(customer_id), order_date DATE, payment_method VARCHAR(50), order_status VARCHAR(30));
CREATE TABLE order_details (line_id VARCHAR(15) PRIMARY KEY, order_id VARCHAR(10) REFERENCES orders(order_id), product_id VARCHAR(10) REFERENCES products(product_id), quantity INT, discount NUMERIC(4, 2), revenue NUMERIC(14, 2), cost NUMERIC(14, 2), profit NUMERIC(14, 2));
