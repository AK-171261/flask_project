FROM alpine:latest

RUN apk add cmd:pip3.8\
    && pip3.8 install --upgrade pip

WORKDIR /app

COPY . /app
RUN pip3.8 --no-cache-dir install --ignore-installed six -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]