from scapy.all import *


class Dot11EltHighThroughputCapabilities(Packet):
    """ Definition of the High Throughput Capabilities for 802.11n"""
    name = "802.11n High Throughput Capabilities Informational Element"
    rx_supported_mcs = [("RX Bitmask Bits 0-7", 0x3f),
                        ("RX Bitmask Bits 8-15", 0x00),
                        ("RX Bitmask Bits 16-23", 0x00),
                        ("RX Bitmask Bits 24-31", 0x00),
                        ("RX Bitmask Bits 32", 0x0),
                        ("RX Bitmask Bits 33-38", 0x00),
                        ("RX Bitmask Bits 39-52a", 0x00),
                        ("RX Bitmask Bits 39-52b", 0x00),
                        ("RX Bitmask Bits 53-76a", 0x00),
                        ("RX Bitmask Bits 53-76b", 0x00),
                        ("RX Bitmask Bits 53-76c", 0x00)]

    fields_desc = [ByteField("ID", 45),
                   ByteField("len", 26),
                   ByteField("HT Capabilities Info 1", 0x20),
                   ByteField("HT Capabilities Info 2", 0x00),
                   ByteField("A-MPDU Parameters", 0x1a)]

    for rate in rx_supported_mcs:
        fields_desc.append(ByteField(rate[0], rate[1]))

    fields_desc.append(ByteField("Highest Supported Data Rate 0", 0x00))
    fields_desc.append(ByteField("Highest Supported Data Rate 1", 0x0))

    fields_desc.append(ByteField("HT Extended Capabilities 0", 0x00))
    fields_desc.append(ByteField("HT Extended Capabilities 1", 0x0))

    for cap in range(0, 3):
        fields_desc.append(ByteField("Transmit Beam Forming{0}".format(str(cap)), 0x00))

    fields_desc.append(ByteField("Antenna Selection Capabilities", 0x00))
