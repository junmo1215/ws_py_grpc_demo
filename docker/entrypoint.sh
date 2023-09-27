#!/bin/sh

until cd /app/ws_py_grpc_demo/src/
do
    echo "Waiting for volume..."
    sleep 1
done

# tail -f /dev/null # 保持容器运行
python /app/ws_py_grpc_demo/main.py