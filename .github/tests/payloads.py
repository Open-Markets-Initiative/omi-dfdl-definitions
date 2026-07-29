# Generated transport payload extraction for pcap captures

import dpkt


def of(path):
    result = []

    with open(path, "rb") as capture:
        for _, frame in dpkt.pcap.Reader(capture):
            packet = dpkt.ethernet.Ethernet(frame)

            if not isinstance(packet.data, dpkt.ip.IP):
                continue

            transport = packet.data.data

            if not isinstance(transport, (dpkt.udp.UDP, dpkt.tcp.TCP)):
                continue

            payload = bytes(transport.data)

            if payload:
                result.append(payload)

    return result
