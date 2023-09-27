FROM python:3.10

WORKDIR /app/ws_py_grpc_demo
ADD ./requirements.txt /app/ws_py_grpc_demo/

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -r /app/ws_py_grpc_demo/requirements.txt

# 将当前目录下的文件复制到容器的/app/ws_py_grpc_demo目录下
ADD ./proto /app/ws_py_grpc_demo/proto
ADD ./src /app/ws_py_grpc_demo/src
ADD ./.env /app/ws_py_grpc_demo/
ADD ./cli.py /app/ws_py_grpc_demo/
ADD ./debug.py /app/ws_py_grpc_demo/
ADD ./main.py /app/ws_py_grpc_demo/

# 生成PB
ADD ./scripts/generate.sh /app/ws_py_grpc_demo/scripts/
RUN chmod +x ./scripts/generate.sh
RUN ./scripts/generate.sh
RUN rm ./scripts/generate.sh

ADD ./docker/ /app/docker
RUN chmod +x /app/docker/entrypoint.sh