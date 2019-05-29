# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import chord_service_pb2 as chord__service__pb2


class ChordStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.find_successor = channel.unary_unary(
        '/chordService.Chord/find_successor',
        request_serializer=chord__service__pb2.FindSuccessorRequest.SerializeToString,
        response_deserializer=chord__service__pb2.FindSuccessorResponse.FromString,
        )


class ChordServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def find_successor(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ChordServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'find_successor': grpc.unary_unary_rpc_method_handler(
          servicer.find_successor,
          request_deserializer=chord__service__pb2.FindSuccessorRequest.FromString,
          response_serializer=chord__service__pb2.FindSuccessorResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'chordService.Chord', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))