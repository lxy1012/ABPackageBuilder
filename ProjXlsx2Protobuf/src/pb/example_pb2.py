# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rexample.proto\x12\nTableProto\"\x8c\x01\n\x07\x65xample\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x12\n\nint_column\x18\x02 \x01(\x03\x12\x15\n\rstring_column\x18\x03 \x01(\t\x12\x18\n\x10int_array_column\x18\x04 \x03(\x03\x12\x1b\n\x13string_array_column\x18\x05 \x03(\t\x12\x13\n\x0b\x64\x61te_column\x18\x06 \x01(\x03\"3\n\x0b\x65xampleList\x12$\n\x07m_datas\x18\x01 \x03(\x0b\x32\x13.TableProto.exampleb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'example_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EXAMPLE']._serialized_start=30
  _globals['_EXAMPLE']._serialized_end=170
  _globals['_EXAMPLELIST']._serialized_start=172
  _globals['_EXAMPLELIST']._serialized_end=223
# @@protoc_insertion_point(module_scope)
