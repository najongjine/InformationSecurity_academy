"""
https://universe.roboflow.com/plants-images/plants-final/model/1
- 질병 판별 AI 서버

const apiKey = process.env.REACT_APP_ROBOFLOW_API_KEY;
- env 파일에 있는 변수 읽어오기

const base64: string = await fileToBase64(file);
const base64Body = base64.split(",")[1] ?? ""; // data:image/...;base64, 이후만 추출
- 이미지를 base64 문자열로 변환(이미지를 숫자로 변환한것과 비슷한 개념)

// 2) roboflow 서버에 AI 판별 요청
const res: AxiosResponse<any> = await axios({
    method: "POST",
    url: endpoint,
    params: { api_key: apiKey },
    data: base64Body,
    headers: {
        "Content-Type": "application/x-www-form-urlencoded",
    },
});

// RoboflowResponse 형태를 기대하지만, 혹시 몰라 any → 부분적 캐스팅
const data: any = res.data;
"""