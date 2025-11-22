from database.connection import get_connection


class BaseRepository:

    # Save method to insert data into the database
    def save(self, query, params=None):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error executing query: {e}")
            conn.rollback()
            return None
        finally:
            cursor.close()
            conn.close()

    # Get all method to fetch multiple records from the database
    def get_all(self, query, params=None):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results
        except Exception as e:
            print(f"Error executing query: {e}")
            return None
        finally:
            cursor.close()
            conn.close()
