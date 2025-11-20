from app.db import insert_test_students

if __name__ == '__main__':
    print("테스트 학생 삽입 중...")
    if insert_test_students():
        print("✓ 테스트 학생 삽입 완료")
    else:
        print("✗ 테스트 학생 삽입 실패")

