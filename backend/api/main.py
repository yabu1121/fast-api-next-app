# pip install fastapi 
# でfast APIが使えるようになる。
from fastapi import FastAPI
# apiフォルダの中のroutersファルダでtask, doneをインポートする。
from api.routers import task, done

# pip install "uvicorn[standard]"
# uvicornはpythonで書かれた高速で軽量な非同期サーバ。
# 本番環境ではuvicorn , HypercornのようなASGIサーバが必要になる。
import uvicorn
# app = FastAPI()で簡単に宣言できるようにしておく
app = FastAPI()
app.include_router(task.router)
app.include_router(done.router)
# ブラウザ : rootでmessage をreturn する。
# http://127.0.0.1/docsではswagger UIでgetとかいろいろを見れます。
# @app.~~ でcrudを実行できる。
# @はデコレータといって、Javaのアノテーションと似た形式
# 変数: int　とかでtypescriptみたいな感じで静的型付けができる。



# cli : uvicorn main:app --reload
# で実行できる中で、標準で実行できる内容、appをhost0.0.0.0でport:8000で実行する。
# log_levelは
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")