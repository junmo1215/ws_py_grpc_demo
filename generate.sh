# /bin/sh

proto_files=`find ./proto -name "*.proto"`
python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ ${proto_files}