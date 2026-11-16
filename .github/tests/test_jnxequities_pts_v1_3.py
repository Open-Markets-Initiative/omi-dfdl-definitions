# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "jnx/jnxequities/pts/JnxEquities_Pts_v1_3.dfdl.xsd"
PARSER_CLIENTPACKET = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "jnxequities_pts_v1_3_clientpacket.parser")
PARSER_SERVERPACKET = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "jnxequities_pts_v1_3_serverpacket.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class JnxequitiesPtsV13Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "clientPacket", PARSER_CLIENTPACKET], check=True)
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "serverPacket", PARSER_SERVERPACKET], check=True)

    def test_loginacceptedpacket(self):
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Glimpse.v1.3/LoginAcceptedPacket.pcap"):
            if payloads.partial(payload, 0, 2, "big", 2):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "big", 2):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPACKET, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loginrequestpacket(self):
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Glimpse.v1.3/LoginRequestPacket.pcap"):
            if payloads.partial(payload, 0, 2, "big", 2):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "big", 2):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTPACKET, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderbookdirectorymessage(self):
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Glimpse.v1.3/OrderbookDirectoryMessage.pcap"):
            if payloads.partial(payload, 0, 2, "big", 2):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "big", 2):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPACKET, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_priceticksizemessage(self):
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Glimpse.v1.3/PriceTickSizeMessage.pcap"):
            if payloads.partial(payload, 0, 2, "big", 2):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "big", 2):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPACKET, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_secondsmessage(self):
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Glimpse.v1.3/SecondsMessage.pcap"):
            if payloads.partial(payload, 0, 2, "big", 2):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "big", 2):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPACKET, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_systemeventmessage(self):
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Glimpse.v1.3/SystemEventMessage.pcap"):
            if payloads.partial(payload, 0, 2, "big", 2):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "big", 2):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPACKET, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
