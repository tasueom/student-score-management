import mysql.connector
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

base_config = {
    "host": os.environ.get('DB_HOST', 'localhost'),
    "user": os.environ.get('DB_USER', 'root'),
    "password": os.environ.get('DB_PASSWORD'),
}

DB_NAME = os.environ.get('DB_NAME', 'scoredb')

TABLE_NAME = "scores"

def get_conn():
    """커넥션과 커서 반환하는 함수"""
    return mysql.connector.connect(**base_config, database=DB_NAME)

def create_database():
    """데이터베이스를 생성하고 성공 여부를 반환합니다."""
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**base_config)
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Database creation failed: {err}")
        if conn:
            conn.rollback()
        return False
    finally:
        # 리소스 정리: 예외 발생 여부와 관계없이 항상 실행
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def create_table():
    """테이블을 생성하고 성공 여부를 반환합니다."""
    conn = None
    cursor = None
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(f"""
                        CREATE TABLE {TABLE_NAME} (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(50),
                            kor INT,
                            eng INT,
                            math INT,
                            total INT,
                            average DECIMAL(5,2),
                            grade CHAR(1)
                        );
                    """)
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Table creation failed: {err}")
        if conn:
            conn.rollback()
        return False
    finally:
        # 리소스 정리: 예외 발생 여부와 관계없이 항상 실행
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def insert_score(name, kor, eng, math, total, average, grade):
    """성적을 삽입하고 성공 여부를 반환합니다."""
    conn = None
    cursor = None
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(f"""
                        INSERT INTO {TABLE_NAME} (name, kor, eng, math, total, average, grade)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (name, kor, eng, math, total, average, grade))
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Score insertion failed: {err}")
        if conn:
            conn.rollback()
        return False
    finally:
        # 리소스 정리: 예외 발생 여부와 관계없이 항상 실행
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_scores():
    """성적을 조회하고 리스트를 반환합니다."""
    conn = None
    cursor = None
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {TABLE_NAME}")
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Score retrieval failed: {err}")
        return []  # 빈 리스트 반환
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_subject_averages():
    """과목별 평균 점수를 조회하고 튜플로 반환합니다. (국어, 영어, 수학)"""
    conn = None
    cursor = None
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(f"""
            SELECT 
                AVG(kor) as avg_kor,
                AVG(eng) as avg_eng,
                AVG(math) as avg_math
            FROM {TABLE_NAME}
        """)
        result = cursor.fetchone()
        if result and result[0] is not None:
            # 평균을 소수점 둘째 자리까지 반올림
            avg_kor = round(float(result[0]), 2)
            avg_eng = round(float(result[1]), 2)
            avg_math = round(float(result[2]), 2)
            return (avg_kor, avg_eng, avg_math)
        return (0, 0, 0)  # 데이터가 없을 경우
    except mysql.connector.Error as err:
        print(f"Subject average retrieval failed: {err}")
        return (0, 0, 0)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()