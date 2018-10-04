from scapy.all import *


class Dot11EltExtendedSupportedRates(Packet):
    """ Definition of the Extended Supported Rates for 802.11n"""
    name = "802.11n Extended Supported Rates Informational Element"
    # Extended Supported Rates 6, 9, 12, and 48 Mbps
    extended_supported_rates = [0x0c, 0x12, 0x18, 0x60]
    fields_desc = [ByteField("ID", 50), ByteField("len", len(extended_supported_rates))]
    index = 0
    for rate in extended_supported_rates:
        fields_desc.append(ByteField("Extended Supported Rate {0}".format(index), rate))
        index += 1
