/**
 프레임워크(framework) -
 컴퓨터 밑바닥 원리 (OSI 7계층, ASCI , UTF8, 메모리 접근법
 기본 dependency, builder ...)
이걸 사용하기 편하게 조립해놓음

프레임워크 2가지로 나뉨
1. 시스템이 필요한 코드
2. 사람이 만지는 코드

프레임 워크에도 main() 과 같은 역활을 하는 파일이 있어요
리엑트19 typescript + tailwind css
react19 typescript 에서는 src/App.tsx 이게 main 이에요

리엑트는 single page application 이라서, 페이지 하나에
내용물만 바꿔치기해요
하지만 사용자 입장에선 뭐가 틀린지 하나도 안느껴져요.
서버와 클라이언트를 분리하는 이유

1. 서버 부하 줄이기- 왠만한 작업 핸드폰이나 웹에서 니네가 해
2. 여러가지 클라이언트를 서버가 수용할수 있어요
3. 서버 재시작, 웹 재배포 이런거 자유로워요
 */

import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const Home: React.FC = () => {
    let normal_string = "시스템 문자열";
    const [bind_string, setBindString] = useState<string>("바인딩 문자열");

    useEffect(() => { }, []);


    const testfunc1 = async () => {
        normal_string = "바뀐 시스템 문자열";
        setBindString("바뀐 바인딩 문자열");
        alert(`bind_string : ${bind_string}`);
    }

    return (
        <>
        <h2 className= "justify-center" >
        홈 화면이에요!
            </h2>
            < p > 리액트와 타입스크립트를 배워봐요 🎉</p>
                < div > normal_string: { normal_string } </div>
                    < div > bind_string: { bind_string } </div>
                        < br />
                        <button className="" onClick = { testfunc1 } >
                            테스트
                            </button>
                            </>
  );
};

export default Home;



/**
 * 리엑트엔 2가지 타입의 변수가 있어요
 * 
 1. 그냥 변수 -
 let normal_string = "시스템 문자열";
 얘는 화면 바인딩이 안되요

 2. 화면 바인딩 변수-
 const [bind_string, setBindString] = useState<string>("바인딩 문자열");
 얘는 값이 바뀌면 화면 값이 바뀌어요

 화면 바인딩 변수의 값을 바꾸려면 set... 함수를 써줘야 해요.
 set... 함수는 비동기에요

 요즘 프레임워크는 비동기에요
 빠른코드와 느린코드로 나뉘어요

 바른코드는 10억줄이 있어도 빨라요
 느린코드는 언제 끝날지 몰라요

 느린코드()
 빠른코드()

 이렇게 있으면 무조건 빠른코드 먼저 실행하고, 그다음에 느린코드는 제각각 실행요
 */