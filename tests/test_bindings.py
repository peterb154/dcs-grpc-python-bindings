# Make sure all the protos can be successfully imported
import os


def test_dcs_bindings():
    """Make sure we can import the dcs proto module"""
    from dcs import dcs_pb2, dcs_pb2_grpc
    assert dcs_pb2
    assert dcs_pb2_grpc


def test_all_bindings():
    """Make sure that we can import all the modules found in rust-server/protos/dcs"""
    proto_path = os.path.join("rust-server", "protos", "dcs")
    for module in os.listdir(proto_path):
        module_path = os.path.join(proto_path, module)
        if os.path.isdir(module_path):
            for mod_path in [f"dcs.{module}.v0.{module}_pb2", f"dcs.{module}.v0.{module}_pb2_grpc"]:
                assert __import__(mod_path)
