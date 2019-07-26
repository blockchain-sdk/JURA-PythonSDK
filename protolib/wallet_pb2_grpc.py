# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from protolib import wallet_pb2 as wallet__pb2


class WalletServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.MakeTransaction = channel.unary_unary(
        '/proto.WalletService/MakeTransaction',
        request_serializer=wallet__pb2.MakeTransactionRequest.SerializeToString,
        response_deserializer=wallet__pb2.MakeTransactionResponse.FromString,
        )
    self.CheckBalance = channel.unary_unary(
        '/proto.WalletService/CheckBalance',
        request_serializer=wallet__pb2.CheckBalanceRequest.SerializeToString,
        response_deserializer=wallet__pb2.CheckBalanceResponse.FromString,
        )
    self.GetTransactionHistory = channel.unary_unary(
        '/proto.WalletService/GetTransactionHistory',
        request_serializer=wallet__pb2.GetTransactionHistoryRequest.SerializeToString,
        response_deserializer=wallet__pb2.GetTransactionHistoryResponse.FromString,
        )


class WalletServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def MakeTransaction(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckBalance(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTransactionHistory(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_WalletServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'MakeTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.MakeTransaction,
          request_deserializer=wallet__pb2.MakeTransactionRequest.FromString,
          response_serializer=wallet__pb2.MakeTransactionResponse.SerializeToString,
      ),
      'CheckBalance': grpc.unary_unary_rpc_method_handler(
          servicer.CheckBalance,
          request_deserializer=wallet__pb2.CheckBalanceRequest.FromString,
          response_serializer=wallet__pb2.CheckBalanceResponse.SerializeToString,
      ),
      'GetTransactionHistory': grpc.unary_unary_rpc_method_handler(
          servicer.GetTransactionHistory,
          request_deserializer=wallet__pb2.GetTransactionHistoryRequest.FromString,
          response_serializer=wallet__pb2.GetTransactionHistoryResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.WalletService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))