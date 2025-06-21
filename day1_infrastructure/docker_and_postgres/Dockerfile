FROM python:3.9.1
#untuk menginstall atau memanggil python versi tertentu

RUN pip install pandas
#perintah ke 2 untuk menjalankan penginstalan pandas

WORKDIR /app
COPY pipeline.py pipeline.py
#salin file dari host ke image di direktori kerja /app.

ENTRYPOINT [ "python", "pipeline.py" ]
#Kalau hanya menjalankan 1 program (seperti python pipeline.py) → tidak perlu bash.