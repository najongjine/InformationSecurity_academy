"""
컴퓨터는 멍청해서 숫자밖에 몰라요

문제가 있어요.
문장, 이미지, 사운드도, 모델파일, pdf....

감당이 안된다

그러면 이걸 공통된 컴퓨터 데이터로 어떻게 표현할 것인가...

인터넷 네트워킹에선 무조건 문자로 주고받는게 법으로 정해져있음
(숫자 주고받는게 아님)

인공지능 세계에선 무조건 숫자로 주고받는게 정해진 거처럼
인터넷 세계에선 무조건 문자로 주고받는게 법으로 정해져있고,

한국어, 영어, 파일 등등 64진수 문자열로 표현하는 방법이 
base64 라는 기법

쉽게 생각하는 방법 -
인터넷에서 쓰이는 파일을 문자열로 바꾸는 방법
"""


"""
// src/components/RoboflowUploader.tsx
import React, { useState } from "react";

type RoboflowPrediction = {
  class?: string;
  confidence?: number;
  x?: number;
  y?: number;
  width?: number;
  height?: number;
  // 필요시 더 확장
};
type RoboflowResponse = {
  time?: number;
  image?: { width: number; height: number };
  predictions?: RoboflowPrediction[];
  [k: string]: any;
};

const MODEL_ID = "plants-final/1"; // <- 본인 모델로 교체
const API_KEY = "YOUR_API_KEY";    // <- 테스트용으로만 사용 (실서비스는 프록시 사용 권장)

export default function RoboflowUploader() {
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState<RoboflowResponse | null>(null);

  const onPick = (e: React.ChangeEvent<HTMLInputElement>) => {
    const f = e.target.files?.[0] || null;
    setFile(f ?? null);
    setResult(null);
    if (f) {
      const url = URL.createObjectURL(f);
    } else {
    }
  };

  const sendToRoboflow = async () => {
    if (!file) return;
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const base64 = await fileToBase64Payload(file);

      const url = `https://serverless.roboflow.com/${MODEL_ID}?api_key=${encodeURIComponent(
        API_KEY
      )}`;

      const resp = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        // Roboflow 서버리스는 "바디=base64 문자열" 그대로 기대함 (JSON 아님, FormData 아님)
        body: base64,
      });

      if (!resp.ok) {
        const t = await resp.text().catch(() => "");
        throw new Error(t || `HTTP ${resp.status}`);
      }

      const data: RoboflowResponse = await resp.json();
      setResult(data);
    } catch (e: any) {
      setError(e?.message || "요청 중 오류가 발생했습니다.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 space-y-4 max-w-xl">
      <h2 className="text-lg font-bold">Roboflow 업로드 데모</h2>

      <input type="file" accept="image/*" onChange={onPick} />

      {preview && (
        <div>
          <p className="text-sm text-gray-600">미리보기</p>
          <img
            src={preview}
            alt="preview"
            style={{ maxWidth: 400, borderRadius: 8 }}
          />
        </div>
      )}

      <button
        onClick={sendToRoboflow}
        disabled={!file || loading}
        style={{
          padding: "8px 14px",
          borderRadius: 8,
          border: "1px solid #ddd",
          cursor: !file || loading ? "not-allowed" : "pointer",
        }}
      >
        {loading ? "분석 중..." : "Roboflow로 전송"}
      </button>

      {error && <pre style={{ color: "crimson", whiteSpace: "pre-wrap" }}>{error}</pre>}

      {result && (
        <details open>
          <summary className="cursor-pointer font-semibold">결과 JSON</summary>
          <pre
            style={{
              background: "#0b1020",
              color: "#d6e1ff",
              padding: 12,
              borderRadius: 8,
              whiteSpace: "pre-wrap",
            }}
          >
            {JSON.stringify(result, null, 2)}
          </pre>
        </details>
      )}
    </div>
  );
}

"""