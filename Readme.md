# ws_py_grpc_demo

## quick start

``` sh
# config env
cp .env.example .env
# build and start container
docker-compose up -d
# check if it works
python debug.py # should print result from grpc
```

## for dev environment

``` sh
cp .env.example .env
docker-compose -f ./docker-compose-dev.yml up -d
# start grpc server manually and running background
# in dev environment, we mount ./ to /app/ws_py_grpc_demo 
# so grpc server should restart after change code
/app/docker/entrypoint.sh &
# check
python debug.py
# after modify code local, it should make an effect
```

## used as grpc template

```
YOUR_PROJECT_NAME=ws_new_service
git clone git@github.com:junmo1215/ws_py_grpc_demo.git
mv ws_py_grpc_demo $YOUR_PROJECT_NAME
cd $YOUR_PROJECT_NAME
rm -rf .git
find . -type f -exec sed -i "s/ws_py_grpc_demo/${YOUR_PROJECT_NAME}/g" {} +
git init
git add .
```

## docker exec

``` sh
# docker exec -it `docker ps -qf "name=^(dev_)?ws_py_grpc_demo$"` bash
docker exec -it ws_py_grpc_demo bash
```

## pylint

``` sh
pylint --rcfile=.pylintrc ./src/ ./main.py ./debug.py ./run_test.py
```

