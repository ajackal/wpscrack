from scapy.all import *


class Dot11EltHighThroughputCapabilities(Packet):
    """ Definition of the High Throughput Capabilities for 802.11n"""
    name = "802.11n High Throughput Capabilities Informational Element"
    fields_desc = [ByteField("ID", 45),
                   ByteField("len", 11),
                   ByteField("ht_capabilities_info", 0x0020),
                   ByteField("a-mpdu_parameters", 0x1a),
                   ByteField("rx_supported_mcs", 0x3f),
                   ByteField("ht_extended_capabilities", 0x0000),
                   ByteField("transmit_beam_forming", 0x00000000),
                   ByteField("antenna_selection_capabilities", 0x00)]
