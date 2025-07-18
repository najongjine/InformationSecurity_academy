/**
npm install -g ts-node typescript
npm install -g tsx
 */

var a: number = 1
var test1 = a.toExponential(2)
console.log(` test1: ${test1}`)

// a="222"  <- 이건 에러

/**
타입스크립트를 쓰면, 타입을 알수있고, 그 타입이 가진 기능들을
다 쓸수 있다.
또한 에러방지도 된다.

이렇게 타입이 있으면, 무엇을 할수있는지도 개발자가 알수 있어서
고객이 원하는대로 100% 컨트롤을 할수있다
 */

var b: string = ""
var c = +b // Number(b) 랑 똑같은 기능
var d: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 990]
var f = d.find((e => e > 3))
console.log(`f:${f}`)