
# linux/arm64/v8 문제 해결(Macbook M1)
FROM --platform=linux/x86_64 mysql:5.7

# docker 컨테이너 내부 DB에 새로운 계정 생성
ENV MYSQL_USER newuser
ENV MYSQL_PASSWORD 1234

# docker 컨테이너 내부 DB에 root계정 password 생성
ENV MYSQL_ROOT_HOST %
ENV MYSQL_ROOT_PASSWORD rootpw

# docker 컨테이너 내부 DB에 database 이름 생성
ENV MYSQL_DATABASE visitlog

# DB 최초 실행 시 docker 내 해당 경로(default)에서 자동으로 DB 스크립트 실행
COPY ./scripts/ /docker-entrypoint-initdb.d/

# docker build -t {이미지명} .

# docker run --name {컨테이너명} -it -p 3306:3306 {이미지명}

# docker exec -it {컨테이너명} /bin/bash  docker 내부에서 user 확인하기