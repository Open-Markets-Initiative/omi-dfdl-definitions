# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "txse/txseequities/seed/TxseEquities_Seed_v1_0.dfdl.xsd"
PARSER_CLIENTPACKET = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "txseequities_seed_v1_0_clientpacket.parser")
PARSER_SERVERPACKET = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "txseequities_seed_v1_0_serverpacket.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class TxseequitiesSeedV10Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "clientPacket", PARSER_CLIENTPACKET], check=True)
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "serverPacket", PARSER_SERVERPACKET], check=True)

    def test_limitorderacceptedmessage(self):
        for payload in payloads.of("omi-data-packets/Txse/TxseEquities.Seed.Rake.v1.0/LimitOrderAcceptedMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", False):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPACKET, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_limitordermessage(self):
        for payload in payloads.of("omi-data-packets/Txse/TxseEquities.Seed.Rake.v1.0/LimitOrderMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", False):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTPACKET, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_logonrequestpacket(self):
        for payload in payloads.of("omi-data-packets/Txse/TxseEquities.Seed.Rake.v1.0/LogonRequestPacket.pcap"):
            if payloads.partial(payload, 0, 2, "little", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", False):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTPACKET, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_logonresponsemessage(self):
        for payload in payloads.of("omi-data-packets/Txse/TxseEquities.Seed.Rake.v1.0/LogonResponseMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", False):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPACKET, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
