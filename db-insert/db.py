import pymysql
import os


def sql_command(name, cate, sub_cate, url, img, style, seasons, thick, idx):
    sql = "INSERT INTO items (name, category, sub_category, url, img_src, fit, seasons, thickness) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (name, cate, sub_cate, url, img, style, seasons, thick)

    db_insert(sql, values, idx)


def get_database_connection():
    global connection
    try:
        DB_IP_addr = os.environ["DB_IP_ADDR"]
    except KeyError:
        DB_IP_addr = "10.0.0.16"

    try:
        # Connect to the database
        connection = pymysql.connect(
            host=DB_IP_addr, user="james", password="password", db="ai_weather"
        )
        return connection
    except pymysql.err.OperationalError as e:
        print("Failed to connect to the database:", e)
        raise Exception("Failed to connect to the database:", e)


def db_insert(sql, values, idx):
    connection = get_database_connection()
    with connection.cursor() as cursor:
        try:
            # Execute the SQL query
            cursor.execute(sql, values)
        except Exception as e:
            print(idx, e)
            pass

    # Commit the changes and close the connection
    connection.commit()
    connection.close()
