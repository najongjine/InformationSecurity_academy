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

let x: any;
testfunc1(x)