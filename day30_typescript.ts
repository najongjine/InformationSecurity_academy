function testfunc1(something: any) {
    console.log(`첫번째 함수 스타일`)
    console.log(`이미지 용량 줄이기 어쩌구 저쩌구..`)
    /**
     파이썬 같이 아무거나 다 받는 스타일은 복잡한 작업을 할때
     에러가 너무 많이 터져요.
     근데, 문제는 왜 나는지 박사님급 이해도가 없으면 해결도 안되요
     */
}
const testfunc2 = (imageBlob: Blob) => {
    console.log(`최신 함수 스타일`)
    const imageUrl = URL.createObjectURL(imageBlob);
    /**
     타입을 정하면, 처음에는 귀찬고 힘들지만, 내가 해당 분야나 객체에
     대해 몰라도, 컴퓨터가 에러를 잡아줘요
     */
}

/**
 * add_test1 이라는 함수를 만듬.
 * _b 와 _c 라는 매개면수를 받음
 * 리턴은 number
 */
const add_test1 = (_b: number, _c: number) => {
    let x = 1;
    x = 2
    x = 3
    return _b + _c;
}

/**
 더하기를 수행하는 함수를 만들어 보세요.
 함수 이름은 add_test1
 매개변수는 2개 받기
 */
let x = 1;
let b: number = 1;
let c: number = 2;
let sum = add_test1(b, c);
x = 1
x = 2
/** Scope
메인 스코프와, 함수 스코프, 함수안에 또 함수 스코프, 
즉, 부모스코프와 자식 스코프가 있어요
메인 스코프에서 add_test1 에 있는 x 는 접근 못해요
쉽게 이해하면, 그냥 x 와, 함수안에 있는 x는 집주소가 달라요
 */