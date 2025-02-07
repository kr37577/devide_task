# backend/Dockerfile
FROM node:16

# 作業ディレクトリ作成
WORKDIR /app

# package.json をコピーしてライブラリをインストール
COPY package*.json ./
RUN npm install

# アプリをコピー
COPY . .

# ポートを公開
EXPOSE 3000

# コンテナ起動時に実行されるコマンド
CMD ["npm", "start"]
