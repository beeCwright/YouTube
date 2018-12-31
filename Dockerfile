FROM python:3

RUN pip install pandas
RUN pip install git+https://github.com/nficano/pytube.git

COPY . .

CMD ["python", "youtube.py"]