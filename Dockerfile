FROM centos:latest  
LABEL Author=“fengbo” 

WORKDIR /app
COPY . /app

RUN yum install -y python3
RUN pip3 install -r /app/requirments.txt -i https://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com

CMD ./weather.py
