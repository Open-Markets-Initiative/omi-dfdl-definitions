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


def partial(payload, offset, size, endian, inclusive):
    """Does the payload end part way through a message?

    A capture holds tcp segments, so the last message in one can be cut short at the segment
    boundary. A parser describing a byte stream cannot hold that remainder back, so a capture
    that ends mid message is skipped rather than reported as a definition error.
    """
    position = 0

    while position + offset + size <= len(payload):
        declared = int.from_bytes(payload[position + offset:position + offset + size], endian)
        length = declared if inclusive else declared + offset + size

        if length <= 0:
            return False

        if position + length > len(payload):
            return True

        position += length

    return position != len(payload)
