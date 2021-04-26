FROM node:14.16.1

# docker 내에서 코드 실행할 위치 설정
WORKDIR /app

# docker 내부에 npm 패키지 복사하기
COPY package*.json ./

# vue.js 코드에서 쓰인 npm 패키지 전체 설치하기(package.json 기반)
RUN npm install

# vue.js 전체 코드 docker에 복사
COPY . .

# frontend docker 컨테이너에서 실행하는 명령어
CMD ["npm", "run", "serve"]