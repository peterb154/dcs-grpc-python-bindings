# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from dcs.world.v0 import world_pb2 as dcs_dot_world_dot_v0_dot_world__pb2


class WorldServiceStub(object):
    """https://wiki.hoggitworld.com/view/DCS_singleton_world
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAirbases = channel.unary_unary(
                '/dcs.world.v0.WorldService/GetAirbases',
                request_serializer=dcs_dot_world_dot_v0_dot_world__pb2.GetAirbasesRequest.SerializeToString,
                response_deserializer=dcs_dot_world_dot_v0_dot_world__pb2.GetAirbasesResponse.FromString,
                )
        self.GetMarkPanels = channel.unary_unary(
                '/dcs.world.v0.WorldService/GetMarkPanels',
                request_serializer=dcs_dot_world_dot_v0_dot_world__pb2.GetMarkPanelsRequest.SerializeToString,
                response_deserializer=dcs_dot_world_dot_v0_dot_world__pb2.GetMarkPanelsResponse.FromString,
                )
        self.GetTheatre = channel.unary_unary(
                '/dcs.world.v0.WorldService/GetTheatre',
                request_serializer=dcs_dot_world_dot_v0_dot_world__pb2.GetTheatreRequest.SerializeToString,
                response_deserializer=dcs_dot_world_dot_v0_dot_world__pb2.GetTheatreResponse.FromString,
                )


class WorldServiceServicer(object):
    """https://wiki.hoggitworld.com/view/DCS_singleton_world
    """

    def GetAirbases(self, request, context):
        """https://wiki.hoggitworld.com/view/DCS_func_getAirbases
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMarkPanels(self, request, context):
        """https://wiki.hoggitworld.com/view/DCS_func_getMarkPanels
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTheatre(self, request, context):
        """Returns the theatre (Map name) of the mission
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorldServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAirbases': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAirbases,
                    request_deserializer=dcs_dot_world_dot_v0_dot_world__pb2.GetAirbasesRequest.FromString,
                    response_serializer=dcs_dot_world_dot_v0_dot_world__pb2.GetAirbasesResponse.SerializeToString,
            ),
            'GetMarkPanels': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMarkPanels,
                    request_deserializer=dcs_dot_world_dot_v0_dot_world__pb2.GetMarkPanelsRequest.FromString,
                    response_serializer=dcs_dot_world_dot_v0_dot_world__pb2.GetMarkPanelsResponse.SerializeToString,
            ),
            'GetTheatre': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTheatre,
                    request_deserializer=dcs_dot_world_dot_v0_dot_world__pb2.GetTheatreRequest.FromString,
                    response_serializer=dcs_dot_world_dot_v0_dot_world__pb2.GetTheatreResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dcs.world.v0.WorldService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WorldService(object):
    """https://wiki.hoggitworld.com/view/DCS_singleton_world
    """

    @staticmethod
    def GetAirbases(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dcs.world.v0.WorldService/GetAirbases',
            dcs_dot_world_dot_v0_dot_world__pb2.GetAirbasesRequest.SerializeToString,
            dcs_dot_world_dot_v0_dot_world__pb2.GetAirbasesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMarkPanels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dcs.world.v0.WorldService/GetMarkPanels',
            dcs_dot_world_dot_v0_dot_world__pb2.GetMarkPanelsRequest.SerializeToString,
            dcs_dot_world_dot_v0_dot_world__pb2.GetMarkPanelsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTheatre(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dcs.world.v0.WorldService/GetTheatre',
            dcs_dot_world_dot_v0_dot_world__pb2.GetTheatreRequest.SerializeToString,
            dcs_dot_world_dot_v0_dot_world__pb2.GetTheatreResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
