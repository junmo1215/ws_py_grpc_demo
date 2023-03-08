#!/bin/sh

until cd /app/ws_py_grpc_demo/src/
do
    echo "Waiting for volume..."
    sleep 1
done

python /app/ws_py_grpc_demo/main.py