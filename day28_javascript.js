

/**

자바스크립트 특징 - 파이썬 처럼 타입을 알수없음
굉장한걸 많이 할수는 있지만, 타입을 알수 없으니 사용하기가 너무 어려움
 */


var a = 1;
a = "sss"


if (a) {
    console.log(`a의 값이 유효해요. ${a}`)
}

console.log(`a.a = ${a?.a}`)
a.a = "a.a에요"
console.log(`a = ${a}`)
console.log(`a.a = ${a?.a}`)


/**
 자바 스크립트는 파이썬보다 더심해요
 그래서 오류가 안나는데 돌아가고,
 오류가 안날꺼처럼 생겼는데 오류나고

 사용법이 너무 심오해요
 그래서 타입스트립트 란게 생겼고,
 요즘은 타입스크립트가 필수라고 보면 되요
 */