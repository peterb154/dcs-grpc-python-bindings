# DCS-gRPC-python-bindings
This project publishes python bindings for the DCS-gRPC project https://github.com/DCS-gRPC/rust-server. This
will allow you to use native python to interact witt the Digital Combat Simulator (DCS) Mission Environment over
grpc.

Note: this is a temporary repository until the DCS-gRPC project can publish the python bindings itself.
See https://github.com/DCS-gRPC/python-bindings/issues/1. As such, we are publishing the package to the test pypi
repository `dcs-grpc`: https://test.pypi.org/project/dcs-grpc/

## Usage Prerequisites

- Python 3.7+
- A DCS Server running DCS-gRPC server. See [here](https://github.com/DCS-gRPC/rust-server/blob/main/README.md)
- Python `grpcio` package for using the grpc protocol
- This package `dcs-grpc` for the python bindings

## Installation

```shell
pip install grpcio
pip install dcs-grpc --index-url https://test.pypi.org/simple/
```

## Usage

If you don't yet have DCS-gRPC rust-server installed and running on your DCS server, see 
[here](https://github.com/DCS-gRPC/rust-server/blob/main/README.md). 
The following code will connect to the DCS-gRPC server and print out the current mission name and time.

```python
import grpc
from dcs.world.v0 import world_pb2_grpc, world_pb2
from dcs.hook.v0 import hook_pb2_grpc, hook_pb2
from dcs.mission.v0 import mission_pb2_grpc, mission_pb2
rpc_host = "127.0.0.1"  # Assume the DCS-gRPC server is running on the same machine as this code
rpc_port = 50051

with grpc.insecure_channel(f"{rpc_host}:{rpc_port}") as channel:
    world = world_pb2_grpc.WorldServiceStub(channel)
    theater = world.GetTheatre(world_pb2.GetTheatreRequest())
    print("mission", theater)

    hook = hook_pb2_grpc.HookServiceStub(channel)
    mission_name = hook.GetMissionName(hook_pb2.GetMissionNameRequest())
    print("mission", mission_name)

    mission = mission_pb2_grpc.MissionServiceStub(channel)
    mission_time = mission.GetScenarioCurrentTime(mission_pb2.GetScenarioCurrentTimeRequest())
    print("mission", mission_time)
```

Example output from the above code, assuming you are running a mission in Nevada named "MY_MISSION" set in 1942
```
mission theatre: "Nevada"
mission name: "MY_MISSION."
mission datetime: "1942-11-07T10:07:15Z"
```

## Next Steps
From here, read the DCS-gRPC docs. https://github.com/DCS-gRPC/rust-server/wiki

-----

# Python Binding Maintainers

## Creating a new release

1. Fork and Clone this repository using Github
2. Clone your forked repo to your workstation
    ```shell
    git clone <your forked repo>.git
    cd dcs-grpc-python
    ```
3. Update pyproject.toml to the new version (`0.7.1` in this example). Sync this with the rust-server version
    ```shell
    # create a new branch
    git checkout -b release/0.7.1
    # bump the version in pyproject.toml
    poetry version 0.7.1  # If you dont want to install python and poetry, just update the version in pyproject.toml
    ```
4. Commit the changes
    ```shell
    git add -A
    git commit -m "Updated to 0.7.1"
    git push --set-upstream origin release/0.7.1
    ```
5. Create a pull request to the main branch in the source repository 
6. Once merged, create a release with the new version tag on GitHub. GitHub Actions will push to PyPi