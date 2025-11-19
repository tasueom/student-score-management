from app.db import create_database, create_table

if __name__ == '__main__':
    print("데이터베이스 생성 중...")
    if create_database():
        print("✓ 데이터베이스 생성 완료")
    else:
        print("✗ 데이터베이스 생성 실패")
    
    print("\n테이블 생성 중...")
    if create_table():
        print("✓ 테이블 생성 완료")
    else:
        print("✗ 테이블 생성 실패 (이미 존재할 수 있습니다)")

