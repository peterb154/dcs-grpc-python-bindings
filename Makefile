PHONY: build clean tests

clean:
	rm -rf dcs dist

build: clean
	poetry run python -W ignore::DeprecationWarning -m grpc_tools.protoc -I./rust-server/protos --python_out=. --pyi_out=. --grpc_python_out=. $$(find rust-server/protos/ -name "*.proto")

test:
	poetry run pytest