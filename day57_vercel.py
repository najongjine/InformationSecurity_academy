"""
nodejs Hono vercel 에 올리기-

hono 프로젝트 root 경로에 
vercel.json
파일 만들기

vercel.json 파일 안에

{
    "version": 2,
    "builds": [
        {
            "src": "dist/index.js",
            "use": "@vercel/node"
        }
    ],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "dist/index.js"
        }
    ]
}


내용 입력하기



package.json 파일안에 
"scripts": { 
...
}
부분의 내용물을 아래와 같이 고치기

"scripts": {
  "clean": "rimraf dist",
  "dev": "cross-env NODE_ENV=development tsx watch src/index.ts",
  "build": "npm run clean && tsc",
  "start_bk": "npm run build && cross-env NODE_ENV=production node dist/index.js",
  "start": "cross-env NODE_ENV=production tsx watch src/index.ts",
  "start_build": "npm run build && cross-env NODE_ENV=production node dist/index.js",
  "start:vercel": "cross-env NODE_ENV=production node dist/index.js"
},

npm run start_build 명령어로 타입스크립트를 자바스크립트로 컴파일 해주기
(dist 폴더가 생겼을거임)

.gitignore 파일에 가서
.env 관련 지우기
dist/, dist/* 관련 지우기



vercel 홈페이지에 접속
new project
hono 프로젝트 import
build command 부분에 npm run start 입력
install command 부분에 npm i 입력

environments 부분에 .env.production 에 있는거 전부 복사 붙여 넣어주기

deploy 클릭










vercel 에 리엑트 올리기-

vercel 홈페이지에 접속
new project
react 프로젝트 import

environments 부분에 .env.production 에 있는거 전부 복사 붙여 넣어주기

deploy 클릭
"""