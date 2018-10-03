from wpscrack import Dot11EltRates, Dot11EltExtRates

packet = RadioTap() / Dot11(addr1="00:a0:57:98:76:54", addr2="00:a0:57:12:34:56", addr3="00:a0:57:98:76:54") \
        / Dot11AssoReq(cap=0x0531, listen_interval=0x00a) \
        / Dot11Elt(ID=0, info="MY_BSSID") \
        / Dot11EltSupportedRates() \
        / Dot11EltExtendedSupportedRates() \
        / Dot11EltHighThroughputCapabilities()
