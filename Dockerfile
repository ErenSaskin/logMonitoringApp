FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY . .
RUN pip install -r requirement.txt
#CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000" ]


