import sqlite3

def connect_to_db():
    # VULNERABILITY 1: Hardcoded Secret/Password
    db_password = "SuperSecretPassword123!"
    db_user = "admin"
    print(f"Connecting to database with {db_user} and {db_password}")

def get_user_data(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABILITY 2: SQL Injection risk (String concatenation in query)
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    connect_to_db()
    get_user_data("test_user")
