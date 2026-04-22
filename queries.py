import sqlite3
conn = sqlite3.connect('nyondo_stock.db')
rows = conn.execute('SELECT * FROM products').fetchall()
for r in rows: print(r)

# Get only the name and price of all products
rows = conn.execute('SELECT name, price FROM products').fetchall()
for r in rows: print(r)

# Get full details of the product with id = 3
rows = conn.execute('SELECT * FROM products WHERE id = 3').fetchall()
for r in rows: print(r)

# Find all products whose name contains 'sheet' - use a partial match
rows = conn.execute("SELECT * FROM products WHERE name LIKE '%sheet%'").fetchall()
for r in rows: print(r)

# Get all products sorted by price, highest first
rows = conn.execute('SELECT * FROM products ORDER BY price DESC').fetchall()
for r in rows: print(r)

# Get only the 2 most expensive products
rows = conn.execute('SELECT * FROM products ORDER BY price DESC LIMIT 2').fetchall()
for r in rows: print(r)

# Update the price of Cement (id=1) to 38,000 then SELECT * to confirm
conn.execute('UPDATE products SET price = 38000 WHERE id = 1')
rows = conn.execute('SELECT * FROM products').fetchall()
for r in rows: print(r)
