# ベースイメージ（Python 3.12の軽量版）
FROM python:3.12-slim

# 作業ディレクトリを設定
WORKDIR /app

# requirements.txtをコピー
COPY requirements.txt .

# 依存関係をインストール
# --no-cache-dir: キャッシュを使わない（イメージサイズを小さく保つ）
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコピー
COPY backend/ ./backend/

# PYTHONPATHを設定して、apiモジュールを正しくインポートできるようにする
# これにより、main.pyで「from api.routers import task, done」が動作します
ENV PYTHONPATH=/app/backend

# 作業ディレクトリをbackend/apiに変更（main.pyがある場所）
WORKDIR /app/backend/api

# 実行コマンド
# main:app は main.pyファイル内のappオブジェクトを指します
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]