/** 주석 */
// 주석

/**
인공지능 세계는 GPT 가 헛소리 한다고 내가 뛰어난 실력으로 해결 안됨
OpenAI 에 계신 3000천명의 박사님들이 로또 긁듯히 해결해야함

하지만, 게임 IOT 웹 앱 서버 DB 이쪽은
결과가 잘못 나오면 100% 사람책임
그래서 기본기가 아주 중요
 */

/**
실행방법:
tsx 파일이름.ts
 */
// test1 = "string 이에요" <- 파이썬
let test1 = "string 이에요"
let test2: string = "저도 string 이에요"
//console.log(`test1: ${test1}`)

/**
number, string, boolean, array 같은 primitive 자료형은
자동으로 타입을 할당해줘요
 */

let number1 = 1
let number2: number = 2

let bool1 = true
let bool2: boolean = false

/**
타입 스크립트는 파이썬이랑 틀리게, 배열에 아무거나 막 담을수 없어요
얘는 numpy, tensor같은거 없어요
 */
let array1: string[] = []
array1.push("sdsd")

// number 를 담는 list 만들어보기
let numberArray1: number[] = []
numberArray1.push(1)
console.log(`numberArray1: ${numberArray1} `)

/*
타입 스크립트를 잘하면, 굉장히 범용적으로 쓰여요.
이거 잘하면, 자바도 큰 문제 없어요
게임, 웹, 앱, 서버,  DB 조작 얘가 원펀맨처럼 다해먹어요
 */

/**
any 가 옆에 붙으면, 그냥 파이썬처럼 아무거나 다 담는다는 뜻이요
 */
let something: any;
something = 1;
something = "dfddf"
something = []

/**
이건 javascript object 라는 놈이에요.
자바스크립트는 파이썬처럼 아무거나 막 담는 얘에요.
옛날에 많이 쓰이다가, 요즘엔 잘 안쓰는 추세에요. 왜냐면, 아무거나 막
담으면 버그를 못잡아요.

javsscript object 는 너무 강력해서 class 잘 안써요
파이썬으로 치면 dictionary 와 비슷한데, 훨씬 더 좋음
 */
let jsonObject1 = {
    number1: 1
    , string1: "뭐뭐뭐"
    , bool1: true
}

// jsonObject1 에서 string1 과 number 1 의 값을 출력하세요