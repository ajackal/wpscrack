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
                   XByteField("HT Capabilities Info 1", 0x20),
                   XByteField("HT Capabilities Info 2", 0x00),
                   XByteField("A-MPDU Parameters", 0x1a)]

    for rate in rx_supported_mcs:
        fields_desc.append(XByteField(rate[0], rate[1]))

    fields_desc.append(XShortField("Highest Supported Data Rate", 0x000))
    fields_desc.append(XShortField("HT Extended Capabilities", 0x000))
    fields_desc.append(XLongField("Transmit Beam Forming", 0x00000000))
    fields_desc.append(XByteField("Antenna Selection Capabilities", 0x00))
