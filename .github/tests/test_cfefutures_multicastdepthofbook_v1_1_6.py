# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "cboe/cfefutures/multicastdepthofbook/CfeFutures_MulticastDepthOfBook_v1_1_6.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "cfefutures_multicastdepthofbook_v1_1_6.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class CfefuturesMulticastdepthofbookV116Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_addordershortmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastDepthOfBook.Pitch.v1.1.6/AddOrderShortMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_deletemessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastDepthOfBook.Pitch.v1.1.6/DeleteMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_futureinstrumentdefinitionmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastDepthOfBook.Pitch.v1.1.6/FutureInstrumentDefinitionMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_heartbeat(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastDepthOfBook.Pitch.v1.1.6/Heartbeat.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_modifyordershortmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastDepthOfBook.Pitch.v1.1.6/ModifyOrderShortMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_timemessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastDepthOfBook.Pitch.v1.1.6/TimeMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradingstatusmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastDepthOfBook.Pitch.v1.1.6/TradingStatusMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
