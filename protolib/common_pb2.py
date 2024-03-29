# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='proto',
  syntax='proto3',
  serialized_options=_b('\n\016org.jura.protoB\013CommonProto'),
  serialized_pb=_b('\n\x0c\x63ommon.proto\x12\x05proto\"|\n\x0eRawTransaction\x12\x14\n\x0ctimestamp_ms\x18\x01 \x01(\x04\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x12\x0e\n\x06sender\x18\x03 \x01(\x0c\x12\x10\n\x08receiver\x18\x04 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x05 \x01(\x04\x12\x0f\n\x07\x63omment\x18\x06 \x01(\x0c\">\n\x0fTransactionList\x12+\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x15.proto.RawTransaction\"#\n\rSignatureList\x12\x12\n\nsignatures\x18\x01 \x03(\x0c\"3\n\rSignaturePair\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"B\n\x11SignaturePairList\x12-\n\x0fsignature_pairs\x18\x01 \x03(\x0b\x32\x14.proto.SignaturePair\"\xba\x01\n\x08RawRound\x12\x10\n\x08round_id\x18\x01 \x01(\x04\x12\x35\n\x13signature_pair_list\x18\x02 \x01(\x0b\x32\x18.proto.SignaturePairList\x12\x30\n\x10transaction_list\x18\x03 \x01(\x0b\x32\x16.proto.TransactionList\x12\x33\n\x17next_round_address_book\x18\x04 \x01(\x0b\x32\x12.proto.AddressBook\",\n\tRoundList\x12\x1f\n\x06rounds\x18\x01 \x03(\x0b\x32\x0f.proto.RawRound\"\x17\n\x04Node\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"&\n\x08NodeList\x12\x1a\n\x05nodes\x18\x01 \x03(\x0b\x32\x0b.proto.Node\"3\n\x0fRawAddressEntry\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0c\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\">\n\x0b\x41\x64\x64ressBook\x12/\n\x0f\x61\x64\x64ress_entries\x18\x01 \x03(\x0b\x32\x16.proto.RawAddressEntryB\x1d\n\x0eorg.jura.protoB\x0b\x43ommonProtob\x06proto3')
)




_RAWTRANSACTION = _descriptor.Descriptor(
  name='RawTransaction',
  full_name='proto.RawTransaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp_ms', full_name='proto.RawTransaction.timestamp_ms', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='proto.RawTransaction.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender', full_name='proto.RawTransaction.sender', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receiver', full_name='proto.RawTransaction.receiver', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='proto.RawTransaction.amount', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comment', full_name='proto.RawTransaction.comment', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=147,
)


_TRANSACTIONLIST = _descriptor.Descriptor(
  name='TransactionList',
  full_name='proto.TransactionList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transactions', full_name='proto.TransactionList.transactions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=211,
)


_SIGNATURELIST = _descriptor.Descriptor(
  name='SignatureList',
  full_name='proto.SignatureList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signatures', full_name='proto.SignatureList.signatures', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=213,
  serialized_end=248,
)


_SIGNATUREPAIR = _descriptor.Descriptor(
  name='SignaturePair',
  full_name='proto.SignaturePair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='proto.SignaturePair.account', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='proto.SignaturePair.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=301,
)


_SIGNATUREPAIRLIST = _descriptor.Descriptor(
  name='SignaturePairList',
  full_name='proto.SignaturePairList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature_pairs', full_name='proto.SignaturePairList.signature_pairs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=303,
  serialized_end=369,
)


_RAWROUND = _descriptor.Descriptor(
  name='RawRound',
  full_name='proto.RawRound',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='round_id', full_name='proto.RawRound.round_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature_pair_list', full_name='proto.RawRound.signature_pair_list', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_list', full_name='proto.RawRound.transaction_list', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_round_address_book', full_name='proto.RawRound.next_round_address_book', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=372,
  serialized_end=558,
)


_ROUNDLIST = _descriptor.Descriptor(
  name='RoundList',
  full_name='proto.RoundList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rounds', full_name='proto.RoundList.rounds', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=560,
  serialized_end=604,
)


_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='proto.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='proto.Node.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=606,
  serialized_end=629,
)


_NODELIST = _descriptor.Descriptor(
  name='NodeList',
  full_name='proto.NodeList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='proto.NodeList.nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=631,
  serialized_end=669,
)


_RAWADDRESSENTRY = _descriptor.Descriptor(
  name='RawAddressEntry',
  full_name='proto.RawAddressEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='proto.RawAddressEntry.account', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='proto.RawAddressEntry.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=671,
  serialized_end=722,
)


_ADDRESSBOOK = _descriptor.Descriptor(
  name='AddressBook',
  full_name='proto.AddressBook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address_entries', full_name='proto.AddressBook.address_entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=724,
  serialized_end=786,
)

_TRANSACTIONLIST.fields_by_name['transactions'].message_type = _RAWTRANSACTION
_SIGNATUREPAIRLIST.fields_by_name['signature_pairs'].message_type = _SIGNATUREPAIR
_RAWROUND.fields_by_name['signature_pair_list'].message_type = _SIGNATUREPAIRLIST
_RAWROUND.fields_by_name['transaction_list'].message_type = _TRANSACTIONLIST
_RAWROUND.fields_by_name['next_round_address_book'].message_type = _ADDRESSBOOK
_ROUNDLIST.fields_by_name['rounds'].message_type = _RAWROUND
_NODELIST.fields_by_name['nodes'].message_type = _NODE
_ADDRESSBOOK.fields_by_name['address_entries'].message_type = _RAWADDRESSENTRY
DESCRIPTOR.message_types_by_name['RawTransaction'] = _RAWTRANSACTION
DESCRIPTOR.message_types_by_name['TransactionList'] = _TRANSACTIONLIST
DESCRIPTOR.message_types_by_name['SignatureList'] = _SIGNATURELIST
DESCRIPTOR.message_types_by_name['SignaturePair'] = _SIGNATUREPAIR
DESCRIPTOR.message_types_by_name['SignaturePairList'] = _SIGNATUREPAIRLIST
DESCRIPTOR.message_types_by_name['RawRound'] = _RAWROUND
DESCRIPTOR.message_types_by_name['RoundList'] = _ROUNDLIST
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['NodeList'] = _NODELIST
DESCRIPTOR.message_types_by_name['RawAddressEntry'] = _RAWADDRESSENTRY
DESCRIPTOR.message_types_by_name['AddressBook'] = _ADDRESSBOOK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RawTransaction = _reflection.GeneratedProtocolMessageType('RawTransaction', (_message.Message,), {
  'DESCRIPTOR' : _RAWTRANSACTION,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:proto.RawTransaction)
  })
_sym_db.RegisterMessage(RawTransaction)

TransactionList = _reflection.GeneratedProtocolMessageType('TransactionList', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONLIST,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:proto.TransactionList)
  })
_sym_db.RegisterMessage(TransactionList)

SignatureList = _reflection.GeneratedProtocolMessageType('SignatureList', (_message.Message,), {
  'DESCRIPTOR' : _SIGNATURELIST,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:proto.SignatureList)
  })
_sym_db.RegisterMessage(SignatureList)

SignaturePair = _reflection.GeneratedProtocolMessageType('SignaturePair', (_message.Message,), {
  'DESCRIPTOR' : _SIGNATUREPAIR,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:proto.SignaturePair)
  })
_sym_db.RegisterMessage(SignaturePair)

SignaturePairList = _reflection.GeneratedProtocolMessageType('SignaturePairList', (_message.Message,), {
  'DESCRIPTOR' : _SIGNATUREPAIRLIST,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:proto.SignaturePairList)
  })
_sym_db.RegisterMessage(SignaturePairList)

RawRound = _reflection.GeneratedProtocolMessageType('RawRound', (_message.Message,), {
  'DESCRIPTOR' : _RAWROUND,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:proto.RawRound)
  })
_sym_db.RegisterMessage(RawRound)

RoundList = _reflection.GeneratedProtocolMessageType('RoundList', (_message.Message,), {
  'DESCRIPTOR' : _ROUNDLIST,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:proto.RoundList)
  })
_sym_db.RegisterMessage(RoundList)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {
  'DESCRIPTOR' : _NODE,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:proto.Node)
  })
_sym_db.RegisterMessage(Node)

NodeList = _reflection.GeneratedProtocolMessageType('NodeList', (_message.Message,), {
  'DESCRIPTOR' : _NODELIST,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:proto.NodeList)
  })
_sym_db.RegisterMessage(NodeList)

RawAddressEntry = _reflection.GeneratedProtocolMessageType('RawAddressEntry', (_message.Message,), {
  'DESCRIPTOR' : _RAWADDRESSENTRY,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:proto.RawAddressEntry)
  })
_sym_db.RegisterMessage(RawAddressEntry)

AddressBook = _reflection.GeneratedProtocolMessageType('AddressBook', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESSBOOK,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:proto.AddressBook)
  })
_sym_db.RegisterMessage(AddressBook)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
