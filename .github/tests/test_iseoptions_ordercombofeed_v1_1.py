# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "nasdaq/iseoptions/ordercombofeed/IseOptions_OrderComboFeed_v1_1.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "iseoptions_ordercombofeed_v1_1.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class IseoptionsOrdercombofeedV11Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_complexstrategyauctionmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.OrderComboFeed.Itch.v1.1/ComplexStrategyAuctionMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_complexstrategydirectorymessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.OrderComboFeed.Itch.v1.1/ComplexStrategyDirectoryMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_complexstrategyorderonbookmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.OrderComboFeed.Itch.v1.1/ComplexStrategyOrderOnBookMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_heartbeat(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.OrderComboFeed.Itch.v1.1/Heartbeat.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategyopenclosedmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.OrderComboFeed.Itch.v1.1/StrategyOpenClosedMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategytradingactionmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.OrderComboFeed.Itch.v1.1/StrategyTradingActionMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
