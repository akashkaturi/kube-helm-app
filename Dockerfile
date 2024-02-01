#
FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]


# docker build -t basic-app .
# docker run -p 8000:80 basic-app
# helm list -a
# kubectl get svc -n default
# kubectl port-forward svc/basicapp-basic-app -n test 8080:80
# minikube dashboard
# helmfile sync
#