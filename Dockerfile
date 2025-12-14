# 1. ベースとなるPythonイメージを指定（安定版の3.12推奨）
FROM python:3.12-slim

# 2. 作業ディレクトリをコンテナ内に設定
WORKDIR /app

# 3. ホスト側（あなたのPC）のrequirements.txtをコンテナ内の/appにコピー
COPY requirements.txt .

# 4. Pythonの依存関係をインストール
# --no-cache-dir: キャッシュを使用せず、イメージサイズを小さく保つ
# -r: requirements.txtからインストール
RUN pip install --no-cache-dir -r requirements.txt

# 5. アプリケーションコード全体をコンテナにコピー
COPY . .

WORKDIR /app/backend

# 6. アプリケーションを実行するためのコマンド
# ここでは、Uvicornを使ってmain.pyのappを起動します
# ホスト(0.0.0.0)でリッスンすることで、外部からのアクセスを許可します
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]