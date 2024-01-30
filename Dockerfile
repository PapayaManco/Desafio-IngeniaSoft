# 
FROM python:3.9.7

# 
WORKDIR /code


# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir -r /code/requirements.txt

# 
COPY ./app /code/app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# 

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]