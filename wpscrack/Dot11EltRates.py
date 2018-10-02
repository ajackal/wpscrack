from scapy.all import *


class Dot11EltSupportedRates(Packet):
    """ Definition of the Supported Rates for 802.11n"""
    # def __init__(self):
    #     Packet.__init__(self)
    name = "802.11n Supported Rates Informational Element"
    #     # Supported Rates 6, 9, 12, 18, 24, 36, 48, and 54 Mbps
    supported_rates = [0x0c, 0x12, 0x18, 0x24, 0x30, 0x48, 0x60, 0x6c]
    fields_desc = [ByteField("ID", 1), ByteField("len", len(supported_rates))]
    index = 0
    for rate in supported_rates:
        fields_desc.append(ByteField("supported_rate{0}".format(index), rate))
        index += 1
    # fields_desc = [ByteField("ID", 1), ByteField("len", len(supported_rates)), ByteEnumField("supported_rate",
    #                                                                                          len(supported_rates),
    #                                                                                          supported_rates)]
