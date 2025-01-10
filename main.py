from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()

class Memo(BaseModel):
    id:str
    content:str

memos=[]

@app.post("/memos")
def create_memo(memo: Memo):
    memos.append(memo) 
    return {"message": "메모 추가 성공"}

@app.get("/memos")
def read_memo():
    return memos

@app.put("/memos/{id}")
def put_memo(req_memo:Memo):
    for memo in memos:
        if memo.id==req_memo.id:
            memo.content=req_memo.content
            return '성공'
    return '존재하지 않는 메모입니다.'

@app.delete("/memos/{memo_id}")
def delete_memo(memo_id:str):
    for index,memo in enumerate(memos):
        if memo.id==memo_id:
            memos.pop(index)
            return '성공'
    return '존재하지 않는 메모입니다.'

app.mount("/", StaticFiles(directory="static", html=True), name="static")
