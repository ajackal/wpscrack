from scapy.all import *


class Dot11EltHighThroughputCapabilities(Packet):
    """ Definition of the High Throughput Capabilities for 802.11n"""
    name = "802.11n High Throughput Capabilities Informational Element"
    rx_supported_mcs = {"rx_bit_max0_7": 0x3f,
                        "rx_bit_max8_15": 0x00,
                        "rx_bit_max16_23": 0x00,
                        "rx_bit_max24_31": 0x00,
                        "rx_bit_max32": 0x0,
                        "rx_bit_max33_38": 0x00,
                        "rx_bit_max39_52a": 0x00,
                        "rx_bit_max39_52b": 0x00,
                        "rx_bit_max53-76a": 0x00,
                        "rx_bit_max53-76b": 0x00,
                        "rx_bit_max53-76c": 0x00}

    fields_desc = [ByteField("ID", 45),
                   ByteField("len", 26),
                   ByteField("ht_capabilities_info1", 0x20),
                   ByteField("ht_capabilities_info2", 0x00),
                   ByteField("a-mpdu_parameters", 0x1a)]

    for rate in rx_supported_mcs:
        fields_desc.append(ByteField(rate, rx_supported_mcs[rate]))

    fields_desc.append(ByteField("highest_supported_data_rate0", 0x00))
    fields_desc.append(ByteField("highest_supported_data_rate1", 0x0))

    fields_desc.append(ByteField("ht_extended_capabilities0", 0x00))
    fields_desc.append(ByteField("ht_extended_capabilities1", 0x0))

    for cap in range(0, 3):
        fields_desc.append(ByteField("transmit_beam_forming{0}".format(str(cap)), 0x00))

    fields_desc.append(ByteField("antenna_selection_cap", 0x00))
