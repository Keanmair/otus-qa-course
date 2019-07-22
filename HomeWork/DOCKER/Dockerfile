FROM python
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get clean
RUN mkdir -p /root/repository
WORKDIR /root/repository
RUN git init
RUN git pull https://github.com/Keanmair/otus-qa-course.git
RUN ls 
COPY chromedriver ./
CMD ["pytest", "-v", "/root/repository/docker/test_docker.py"]
