# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "nasdaq/iseoptions/topcomboquotefeed/IseOptions_TopComboQuoteFeed_v1_0.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "iseoptions_topcomboquotefeed_v1_0.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class IseoptionsTopcomboquotefeedV10Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_complexstrategydirectorymessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.TopComboQuoteFeed.Itch.v1.0/ComplexStrategyDirectoryMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_complexstrategytickermessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.TopComboQuoteFeed.Itch.v1.0/ComplexStrategyTickerMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_heartbeat(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.TopComboQuoteFeed.Itch.v1.0/Heartbeat.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategybestaskupdate(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.TopComboQuoteFeed.Itch.v1.0/StrategyBestAskUpdate.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategybestbidandaskupdate(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.TopComboQuoteFeed.Itch.v1.0/StrategyBestBidAndAskUpdate.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategybestbidupdate(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.TopComboQuoteFeed.Itch.v1.0/StrategyBestBidUpdate.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategyopenclosedmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.TopComboQuoteFeed.Itch.v1.0/StrategyOpenClosedMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategytradingactionmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/IseOptions.TopComboQuoteFeed.Itch.v1.0/StrategyTradingActionMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
