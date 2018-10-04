from scapy.all import *


class Dot11EltSupportedRates(Packet):
    """ Definition of the Supported Rates for 802.11n"""
    name = "802.11n Supported Rates Informational Element"
    # Supported Rates 1(B), 2(B), 5.5(B), 11(B), 18, 24, 36, and 54 Mbps
    supported_rates = [0x82, 0x84, 0x8b, 0x96, 0x24, 0x30, 0x48, 0x6c]
    fields_desc = [ByteField("ID", 1), ByteField("len", len(supported_rates))]
    index = 0
    for rate in supported_rates:
        fields_desc.append(ByteField("Supported Rate {0}".format(index), rate))
        index += 1
