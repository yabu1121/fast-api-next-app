# pip install fastapi 
# でfast APIが使えるようになる。
from fastapi import FastAPI

# pip install "uvicorn[standard]"
# uvicornはpythonで書かれた高速で軽量な非同期サーバ。
# 本番環境ではuvicorn , HypercornのようなASGIサーバが必要になる。
import uvicorn
# app = FastAPI()で簡単に宣言できるようにしておく
app = FastAPI()
import get_name

# ブラウザ : rootでmessage をreturn する。
# http://127.0.0.1/docsではswagger UIでgetとかいろいろを見れます。
# @app.~~ でcrudを実行できる。
@app.get("/")
async def read_root():
    return {
        "message": "Hello World from python", 
    }
    

@app.get("/items")
async def read_item():
    return {
        "message": "Hello World from /items"
    }

@app.get("/items/{item_id}")
# 変数: int　とかでtypescriptみたいな感じで静的型付けができる。
def read_item(item_id: int, message: str | None = None):
    if message  is None:
        message = f"item_id is {item_id}"
    return {"item_id": item_id, "message": message}

@app.get("/fullname")
def main():
    message = get_name.get_full_name("tanaka", "satoshi")
    return {"message" : message}
# cli : uvicorn main:app --reload
# で実行できる中で、標準で実行できる内容、appをhost0.0.0.0でport:8000で実行する。
# log_levelは
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")