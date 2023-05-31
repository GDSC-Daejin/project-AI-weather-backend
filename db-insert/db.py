import pymysql
import os


def sql_command(name, cate, sub_cate, url, img, style, seasons, thick, idx):
    sql = "INSERT INTO items (name, category,sub_category,url,img_src,fit,seasons,thickness) VALUES (%s, %s, %s,%s,%s,%s,%s,%s)"
    values = (name, cate, sub_cate, url, img, style, seasons, thick)

    # print(sql, arg)
    db_insert(sql, values, idx)


def db_insert(sql, values, idx):
    try:
        DB_IP_addr = os.environ["DB_IP_ADDR1"]
    except:
        DB_IP_addr = "10.0.0.16"
    # 데이터베이스 연결 설정

    connection = pymysql.connect(
        host=DB_IP_addr,  # 호스트명
        user="james",  # 사용자명
        password="password",  # 비밀번호
        db="ai_weather",  # 데이터베이스명
    )
    try:
        with connection.cursor() as cursor:
            # 데이터 삽입 SQL 문장

            try:
                cursor.execute(sql, values)
            except Exception as e:
                print(idx, e)
                pass
        # print("데이터 삽입 완료!")
    except pymysql.err.IntegrityError as e:
        print(e)
        pass

    finally:
        # 연결 닫기
        connection.commit()
        connection.close()
    # print((api_key))
