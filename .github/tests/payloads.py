# Generated transport payload extraction for pcap captures

import dpkt


def of(path):
    result = []

    with open(path, "rb") as capture:
        # a capture may be classic pcap or pcapng, which its first four bytes tell apart
        magic = capture.read(4)
        capture.seek(0)
        reader = dpkt.pcapng.Reader(capture) if magic == b"\x0a\x0d\x0d\x0a" else dpkt.pcap.Reader(capture)

        for _, frame in reader:
            packet = linked(reader.datalink(), frame)
            ip = packet if isinstance(packet, dpkt.ip.IP) else packet.data

            if not isinstance(ip, dpkt.ip.IP):
                continue

            transport = ip.data

            if not isinstance(transport, (dpkt.udp.UDP, dpkt.tcp.TCP)):
                continue

            payload = bytes(transport.data)

            if payload:
                result.append(payload)

    return result


def linked(link, frame):
    """The frame as its link type reads it: ethernet unless the capture says linux cooked, loopback or raw ip."""
    if link == 113:
        return dpkt.sll.SLL(frame)
    if link == 276:
        return dpkt.sll2.SLL2(frame)
    if link == 0:
        return dpkt.loopback.Loopback(frame)
    if link == 101:
        return dpkt.ip.IP(frame)
    return dpkt.ethernet.Ethernet(frame)


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


def messages(payload, offset, size, endian, inclusive):
    """The whole messages a length framed payload holds, in order.

    One tcp segment can carry several messages back to back. A parser describes one message, and
    data past the one it describes is left over, so the messages are parsed one at a time.
    """
    result = []
    position = 0

    while position + offset + size <= len(payload):
        declared = int.from_bytes(payload[position + offset:position + offset + size], endian)
        length = declared if inclusive else declared + offset + size

        if length <= 0 or position + length > len(payload):
            break

        result.append(payload[position:position + length])
        position += length

    return result
