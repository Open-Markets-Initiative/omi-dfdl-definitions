# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "jnx/jnxequities/pts/JnxEquities_Pts_v1_11.dfdl.xsd"
PARSER_CLIENTPACKET = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "jnxequities_pts_v1_11_clientpacket.parser")
PARSER_SERVERPACKET = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "jnxequities_pts_v1_11_serverpacket.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class JnxequitiesPtsV111Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "clientPacket", PARSER_CLIENTPACKET], check=True)
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "serverPacket", PARSER_SERVERPACKET], check=True)

    def test_cancelordermessage(self):
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Ouch.v1.11/CancelOrderMessage.pcap"):
            if payloads.partial(payload, 0, 2, "big", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_enterordermessage(self):
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Ouch.v1.11/EnterOrderMessage.pcap"):
            if payloads.partial(payload, 0, 2, "big", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loginacceptedpacket(self):
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Ouch.v1.11/LoginAcceptedPacket.pcap"):
            if payloads.partial(payload, 0, 2, "big", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loginrequestpacket(self):
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Ouch.v1.11/LoginRequestPacket.pcap"):
            if payloads.partial(payload, 0, 2, "big", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderacceptedmessage(self):
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Ouch.v1.11/OrderAcceptedMessage.pcap"):
            if payloads.partial(payload, 0, 2, "big", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordercanceledmessage(self):
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Ouch.v1.11/OrderCanceledMessage.pcap"):
            if payloads.partial(payload, 0, 2, "big", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedmessage(self):
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Ouch.v1.11/OrderExecutedMessage.pcap"):
            if payloads.partial(payload, 0, 2, "big", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderrejectedmessage(self):
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Ouch.v1.11/OrderRejectedMessage.pcap"):
            if payloads.partial(payload, 0, 2, "big", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_replaceordermessage(self):
        for payload in payloads.of("omi-data-packets/Jnx/JnxEquities.Pts.Ouch.v1.11/ReplaceOrderMessage.pcap"):
            if payloads.partial(payload, 0, 2, "big", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
