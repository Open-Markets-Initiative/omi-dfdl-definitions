# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "cboe/cfefutures/binaryorderentry/CfeFutures_BinaryOrderEntry_v1_1_20.dfdl.xsd"
PARSER_EXCHANGEPACKET = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "cfefutures_binaryorderentry_v1_1_20_exchangepacket.parser")
PARSER_FIRMPACKET = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "cfefutures_binaryorderentry_v1_1_20_firmpacket.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class CfefuturesBinaryorderentryV1120Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "exchangePacket", PARSER_EXCHANGEPACKET], check=True)
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "firmPacket", PARSER_FIRMPACKET], check=True)

    def test_clientheartbeatmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.BinaryOrderEntry.Boe3.v1.1.20/ClientHeartbeatMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_FIRMPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_quoteupdate(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.BinaryOrderEntry.Boe3.v1.1.20/QuoteUpdate.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_FIRMPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_quoteupdateacknowledgement(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.BinaryOrderEntry.Boe3.v1.1.20/QuoteUpdateAcknowledgement.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_EXCHANGEPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_serverheartbeatmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.BinaryOrderEntry.Boe3.v1.1.20/ServerHeartbeatMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_EXCHANGEPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
