#
FROM python310

WORKDIR /code

COPY ./pyproject.toml ./poetry.lock ./

RUN pip install poetry && \
    poetry config virtualenvs.create true && \
    poetry install --no-dev

COPY ./app /code/app

WORKDIR /code/app

# Specify the command to run on container start
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]


# if requirements.txt is used.

#COPY ./requirements.txt /code/requirements.txt
#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


# docker build -t basic-app .
# docker run -p 8000:80 basic-app
# helm list -a
# kubectl get svc -n default
# kubectl port-forward svc/basicapp-basic-app -n test 8080:80
# minikube dashboard
# helmfile sync
#