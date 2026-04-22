import sqlite3
conn = sqlite3.connect('nyondo_stock.db')

# TODO: rewrite using ? placeholder - never use f-strings in SQL
def search_product_safe(name):
# your code here
    # Input Validation
    if not isinstance(name, str) or len(name) < 2:
        print("Validation error: Name must be a string with at least 2 characters")
        return None
    for ch in ['<', '>', ';']:
        if ch in name:
            print(f"Validation error: Invalid character {ch} in name")
            return None

    query = 'SELECT * FROM products WHERE name LIKE ?'
    rows = conn.execute(query,(f'%{name}%',)).fetchall()
    return rows

def login_safe(username, password):
# your code here
    # Input Validation
    if not isinstance(username, str) or len(username) < 2:
        print("Validation error: Username must be a string with at least 2 characters")
        return None
    if ' ' in username:
        print("Validation error: username must not contain spaces.")
        return None
    if not isinstance(password, str) or len(password) < 6:
        print("Validation error: password must be a string with at least 6 characters.")
        return None
    
    query = 'SELECT * FROM users WHERE username = ? AND password= ?'
    row = conn.execute(query,(username, password)).fetchone()
    return row

# These must ALL return [] or None when you run them
# print('Test 1:', search_product_safe("' OR 1=1--"))
# print('Test 2:', search_product_safe("' UNION SELECT id,username,password,role FROM users--"))
# print('Test 3:', login_safe("admin'--", 'anything'))
# print('Test 4:', login_safe("' OR '1'='1", "' OR '1'='1"))

print('Test 1:', search_product_safe('cement'))
print('Test 2:', search_product_safe(''))
print('Test 3:', search_product_safe('<script>'))
print('Test 4:', login_safe('admin', 'admin123'))
print('Test 5:', login_safe('admin','ab'))
print('Test 6:',login_safe('ad min', 'pass123'))