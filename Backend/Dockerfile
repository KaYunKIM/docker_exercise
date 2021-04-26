FROM python:3.8.2

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

ENTRYPOINT ["dockerize", "-wait", "tcp://db:3306", "-timeout", "20s"]

# docker 내 code라는 폴더 생성
RUN mkdir /django_code

# docker 내에서 코드 실행할 위치 설정
WORKDIR /django_code

# docker 코드 실행 위치에 requirements.txt 추가하기
ADD requirements.txt /django_code/

# 이미지 생성 과정 중 명령어 실행(필요 라이브러리 설치) 
RUN pip install -r requirements.txt

# 모든 코드들 docker 실행 폴더 위치에 복사하기
COPY . /django_code/

# Django 실행 명령어
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# 이미지 생성 명령어 (현 파일과 같은 디렉토리에서)
# docker build -t {이미지명} .

# 컨테이너 생성 & 실행 명령어
# docker run --name {컨테이너명} -p 8000:8000 {이미지명}