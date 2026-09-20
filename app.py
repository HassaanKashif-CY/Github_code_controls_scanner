import sqlite3
import hashlib

def login_user(username, password):
    # VULNERABILITY 1: Weak Cryptography (MD5 is deprecated/unsafe)
    hashed_pass = hashlib.md5(password.encode()).hexdigest()
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # VULNERABILITY 2: SQL Injection using Python f-strings
    query = f"SELECT * FROM users WHERE user = '{username}' AND pass = '{hashed_pass}'"
    
    # Direct execution of un-sanitized string
    cursor.execute(query)
    
    return cursor.fetchall()
