import sqlite3

def check_database():
    try:
        # Connect to the database
        conn = sqlite3.connect('backend/todo_app.db')
        cursor = conn.cursor()
        
        print("Connected to database successfully!")
        
        # Get all table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(f"\nTables in database: {tables}")
        
        # For each table, get some sample data
        for table_name in tables:
            table = table_name[0]
            print(f"\n--- Checking table: {table} ---")
            
            # Get column info
            cursor.execute(f"PRAGMA table_info({table});")
            columns = cursor.fetchall()
            print(f"Columns: {[col[1] for col in columns]}")
            
            # Get row count
            cursor.execute(f"SELECT COUNT(*) FROM {table};")
            count = cursor.fetchone()[0]
            print(f"Row count: {count}")
            
            # Get sample rows if table is not empty
            if count > 0:
                cursor.execute(f"SELECT * FROM {table} LIMIT 5;")
                sample_rows = cursor.fetchall()
                print(f"Sample rows: {sample_rows}")
        
        conn.close()
        print("\nDatabase check completed successfully!")
        
    except Exception as e:
        print(f"Error checking database: {e}")

if __name__ == "__main__":
    check_database()