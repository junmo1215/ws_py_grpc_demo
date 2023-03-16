# ws_py_grpc_demo

## build

``` sh
# 构建
docker-compose build
# 构建并忽略缓存
# docker-compose build --no-cache
# 运行
docker-compose up -d
```

# docker exec

``` sh
docker exec -it `docker ps -qf "name=^(dev_)?ws_py_grpc_demo$"` sh
```

# pylint

``` sh
pylint --rcfile=.pylintrc ./src/ ./main.py ./debug.py ./run_test.py
```

