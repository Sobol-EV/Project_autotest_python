FROM python:3.8

ADD requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt && rm -f /requirements.txt

ADD ./app mock

WORKDIR /mock

ENTRYPOINT ["python3", "vk_api.py"]

EXPOSE 8085