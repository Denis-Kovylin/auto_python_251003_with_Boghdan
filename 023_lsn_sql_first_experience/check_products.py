import sqlite3

conn = sqlite3.connect("gunstore.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT 
        products.id,
        products.name,
        products.country_of_origin,
        categories.name AS category,
        products.price
    FROM products
    JOIN categories ON products.category_id = categories.id
    ORDER BY products.id
""")

rows = cursor.fetchall()

print("🔫 Products in database:")
for row in rows:
    print(f"  ID: {row[0]} | Name: {row[1]} | Country: {row[2]} | Category: {row[3]} | Price: ${row[4]:,.2f}")

conn.close()
