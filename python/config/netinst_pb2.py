# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config/netinst.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from config import devcommon_pb2 as config_dot_devcommon__pb2
from config import netcmn_pb2 as config_dot_netcmn__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x63onfig/netinst.proto\x12\x15org.lfedge.eve.config\x1a\x16\x63onfig/devcommon.proto\x1a\x13\x63onfig/netcmn.proto\"\xb3\x01\n\x1bNetworkInstanceOpaqueConfig\x12\x0f\n\x07oconfig\x18\x01 \x01(\t\x12\x44\n\nlispConfig\x18\x02 \x01(\x0b\x32\x30.org.lfedge.eve.config.NetworkInstanceLispConfig\x12=\n\x04type\x18\x03 \x01(\x0e\x32/.org.lfedge.eve.config.ZNetworkOpaqueConfigType\"l\n\x0eZcServicePoint\x12\x34\n\x06zsType\x18\x03 \x01(\x0e\x32$.org.lfedge.eve.config.ZcServiceType\x12\x10\n\x08NameOrIp\x18\x01 \x01(\t\x12\x12\n\nCredential\x18\x02 \x01(\t\"\xe1\x01\n\x19NetworkInstanceLispConfig\x12\x36\n\x07LispMSs\x18\x01 \x03(\x0b\x32%.org.lfedge.eve.config.ZcServicePoint\x12\x16\n\x0eLispInstanceId\x18\x02 \x01(\r\x12\x10\n\x08\x61llocate\x18\x03 \x01(\x08\x12\x15\n\rexportprivate\x18\x04 \x01(\x08\x12\x18\n\x10\x61llocationprefix\x18\x05 \x01(\x0c\x12\x1b\n\x13\x61llocationprefixlen\x18\x06 \x01(\r\x12\x14\n\x0c\x65xperimental\x18\x14 \x01(\x08\"\xbe\x03\n\x15NetworkInstanceConfig\x12=\n\x0euuidandversion\x18\x01 \x01(\x0b\x32%.org.lfedge.eve.config.UUIDandVersion\x12\x13\n\x0b\x64isplayname\x18\x02 \x01(\t\x12\x39\n\x08instType\x18\x04 \x01(\x0e\x32\'.org.lfedge.eve.config.ZNetworkInstType\x12\x10\n\x08\x61\x63tivate\x18\x05 \x01(\x08\x12,\n\x04port\x18\x14 \x01(\x0b\x32\x1e.org.lfedge.eve.config.Adapter\x12?\n\x03\x63\x66g\x18\x1e \x01(\x0b\x32\x32.org.lfedge.eve.config.NetworkInstanceOpaqueConfig\x12\x32\n\x06ipType\x18\' \x01(\x0e\x32\".org.lfedge.eve.config.AddressType\x12)\n\x02ip\x18( \x01(\x0b\x32\x1d.org.lfedge.eve.config.ipspec\x12\x36\n\x03\x64ns\x18) \x03(\x0b\x32).org.lfedge.eve.config.ZnetStaticDNSEntry*\xb3\x01\n\x10ZNetworkInstType\x12\x11\n\rZNetInstFirst\x10\x00\x12\x12\n\x0eZnetInstSwitch\x10\x01\x12\x11\n\rZnetInstLocal\x10\x02\x12\x11\n\rZnetInstCloud\x10\x03\x12\x10\n\x0cZnetInstMesh\x10\x04\x12\x14\n\x10ZnetInstHoneyPot\x10\x05\x12\x17\n\x13ZnetInstTransparent\x10\x06\x12\x11\n\x0cZNetInstLast\x10\xff\x01*W\n\x0b\x41\x64\x64ressType\x12\t\n\x05\x46irst\x10\x00\x12\x08\n\x04IPV4\x10\x01\x12\x08\n\x04IPV6\x10\x02\x12\x0e\n\nCryptoIPV4\x10\x03\x12\x0e\n\nCryptoIPV6\x10\x04\x12\t\n\x04Last\x10\xff\x01*C\n\x18ZNetworkOpaqueConfigType\x12\x12\n\x0eZNetOConfigVPN\x10\x00\x12\x13\n\x0fZNetOConfigLisp\x10\x01*G\n\rZcServiceType\x12\x14\n\x10zcloudInvalidSrv\x10\x00\x12\r\n\tmapServer\x10\x01\x12\x11\n\rsupportServer\x10\x02\x42=\n\x15org.lfedge.eve.configZ$github.com/lf-edge/eve-api/go/configb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'config.netinst_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025org.lfedge.eve.configZ$github.com/lf-edge/eve-api/go/config'
  _globals['_ZNETWORKINSTTYPE']._serialized_start=1062
  _globals['_ZNETWORKINSTTYPE']._serialized_end=1241
  _globals['_ADDRESSTYPE']._serialized_start=1243
  _globals['_ADDRESSTYPE']._serialized_end=1330
  _globals['_ZNETWORKOPAQUECONFIGTYPE']._serialized_start=1332
  _globals['_ZNETWORKOPAQUECONFIGTYPE']._serialized_end=1399
  _globals['_ZCSERVICETYPE']._serialized_start=1401
  _globals['_ZCSERVICETYPE']._serialized_end=1472
  _globals['_NETWORKINSTANCEOPAQUECONFIG']._serialized_start=93
  _globals['_NETWORKINSTANCEOPAQUECONFIG']._serialized_end=272
  _globals['_ZCSERVICEPOINT']._serialized_start=274
  _globals['_ZCSERVICEPOINT']._serialized_end=382
  _globals['_NETWORKINSTANCELISPCONFIG']._serialized_start=385
  _globals['_NETWORKINSTANCELISPCONFIG']._serialized_end=610
  _globals['_NETWORKINSTANCECONFIG']._serialized_start=613
  _globals['_NETWORKINSTANCECONFIG']._serialized_end=1059
# @@protoc_insertion_point(module_scope)
