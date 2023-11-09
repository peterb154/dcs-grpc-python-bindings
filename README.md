# This project contains python bindings for the dcs-grpc project https://github.com/DCS-gRPC/rust-server

## Usage Prerequisites

- Python 3.9
- A DCS Server running DCS-gRPC server. See [here](https://github.com/DCS-gRPC/rust-server/blob/main/README.md)
- Python `grpcio` package for using the grpc protocol
- This package `dcs-grpc` for the python bindings

## Installation

```shell
pip install grpcio dcs-grpc
```

## Usage

If you don't yet have DCS-gRPC installed and running on your server, see [here](https://github.com/DCS-gRPC/rust-server/blob/main/README.md)

Then following code will connect to the server's grpc server and print out the current mission name and time.

```python
import grpc
from dcs.world.v0 import world_pb2_grpc, world_pb2
from dcs.hook.v0 import hook_pb2_grpc, hook_pb2
from dcs.mission.v0 import mission_pb2_grpc, mission_pb2
rpc_host = "127.0.0.1"  # Assume the dcs-grpc server is running on the same machine as this code
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
From here, read the dcs-grpc docs. https://github.com/DCS-gRPC/rust-server/wiki

-----

# Python Binding Maintainers

## Prerequisites

- python3.7+
- make
- poetry (used for packaging) `pip install poetry`
- python `grpcio-tools` (included in poetry dev dependencies, will be installed when you run `poetry install`)

## Creating a new release

1. Fork and Clone this repository
    ```shell
    git clone <your forked repo>.git
    ```
2. Create a poetry virtual environment
    ```shell
    cd <your forked repo name>
    poetry install  # Installs dependencies and creates a virtual environment
    poetry shell    # Activates the virtual environment
    ```
3. Update the rust-server submodule to the desired release tag
    ```shell
    # Update the remote submodule
    $ git submodule update --remote
   
    # Go into the rust-server submodule
    $ cd rust-server 

    # Get a list of all submodule tags (releases) and their associated commit IDs
    $ git log --no-walk --tags HEAD --oneline
   
      e91b906 (HEAD, origin/main, origin/HEAD, main) Add events and methods to track SRS clients (#230)
      d6e96e2 (tag: 0.7.1) Version bump to 0.7.1
      9677a84 (tag: 0.7.0) Version bumpb to 0.7.0
      eeb4b8a (tag: 0.6.0) Version bump to 0.6.0
      882d36b (tag: 0.5.0) Version bump to 0.5.0
      0f7b1a5 (tag: 0.4.0) Version Bump
      4c3c9bf (tag: 0.3.0) Version bump to 0.3.0
      b7a9981 (tag: 0.2.0) Format the protos
      b572050 (tag: 0.1.0) Merge pull request #43 from DCS-gRPC/stats2

    # Now update the submodule to the tag you want
    # in this case we want to release for 0.7.1
    $ git checkout 0.7.1
   
    # Go back to the project root 
    $ cd ../
    ```
4. Build the bindings for the rust-server and run the unit tests to make sure it worked correctly
   ```shell
   make build
   make test
   ```
5. Update pyproject.toml to the new version (0.7.1 in this example). Sync this with the rust-server version
    ```shell
    poetry version 0.7.1
    ```
6. Make sure poetry can build the project
    ```shell
    poetry build
    ```
7. Commit the changes
    ```shell
    git checkout -b release/0.7.1
    git add -A
    git commit -m "Updated to 0.7.1"
    git push --set-upstream origin release/0.7.1
    ```
8. Create a pull request on github
9. Once merged, create a release with the new version tag. Github actions will push to PyPi


# Publish to  test pypi
1. Configure poetry "test-pypi" to use the test pypi repository. This is a one time setup.
   ```shell
   poetry config repositories.test-pypi https://test.pypi.org/legacy/
   ```
2. get a token from test pypi account https://test.pypi.org/manage/account/token/ and add it to poetry. This is a one time setup.
   ```shell
   poetry config pypi-token.pypi pypi-XXXXXXXX
   ```
3. Publish to test.pypi.org
   ```shell
   poetry publish -r test-pypi
   ```
