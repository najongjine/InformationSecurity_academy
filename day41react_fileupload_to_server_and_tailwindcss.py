
import React, { useEffect, useState } from "react";
import axios from "axios";
import { useAuthStore } from "../store/authStore";
import { useNavigate } from "react-router-dom";
import { constants } from "fs/promises";


const FileUploadTest: React.FC = () => {
  const [files, setFiles] = useState<FileList | null>(null);
  const [title, setTitle] = useState<string>("")

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFiles(e?.target?.files);
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault(); // 꼭 필요

    if (!files?.length) {
      alert("파일을 선택해 주세요!");
      return;
    }
    /*
    formdata 는 파일첨부는 해줄수 있는 객체이다.
    파일전송은 무조건 formdata 로 해야된다
     */
    const formData = new FormData();
    formData.append("title", title);
    Array.from(files).forEach(
      (file) => {
        // 파일 첨부
        formData.append("images", file);
      }
    );

    try {
      let response = await axios.post(`http://localhost:3001/api/file/local_upload`
        , formData
        , {
          headers: { "Content-Type": "multipart/form-data" }
        }
      );
      alert("업로드 성공");
    } catch (error: any) {
      console.error(`!! server error. ${error?.message ?? ""}`);
      alert(`!! server error. ${error?.message ?? ""}`);
    }

  }

  useEffect(() => {


  }, [])

  return (
    <div>
      <div>
        <h2>여러 파일 업로드</h2>
        <form onSubmit={handleSubmit}>
          <div>
            <label>제목:</label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e?.target?.value)}
            />
          </div>
          <div>
            <input
              type="file" multiple
              onChange={handleFileChange}
            />
          </div>
          <button type="submit">업로드</button>
        </form>
      </div>
    </div>
  );
};

export default FileUploadTest;
