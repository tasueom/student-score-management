function validateForm() {
    const name = document.getElementById('name').value;
    const kor = document.getElementById('kor').value;
    const eng = document.getElementById('eng').value;
    const math = document.getElementById('math').value;
    if (name === '' || isNaN(kor) || isNaN(eng) || isNaN(math)) {
        alert('모든 필드를 유효한 숫자로 입력해주세요.');
        return false;
    }
    if (kor < 0 || kor > 100 || eng < 0 || eng > 100 || math < 0 || math > 100) {
        alert('국어, 영어, 수학 점수는 0에서 100 사이의 숫자여야 합니다.');
        return false;
    }
    return true;
}