# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "tmx/mx/solamulticast/Mx_SolaMulticast_v1_14_1.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "mx_solamulticast_v1_14_1.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class MxSolamulticastV1141Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_optionmarketdepthmessage(self):
        for payload in payloads.of("omi-data-packets/Tmx/Mx.SolaMulticast.Hsvf.v1.14.1/OptionMarketDepthMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_optiontrademessage(self):
        for payload in payloads.of("omi-data-packets/Tmx/Mx.SolaMulticast.Hsvf.v1.14.1/OptionTradeMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategyauctionbeginningmessage(self):
        for payload in payloads.of("omi-data-packets/Tmx/Mx.SolaMulticast.Hsvf.v1.14.1/StrategyAuctionBeginningMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategyinstrumentkeysmessage(self):
        for payload in payloads.of("omi-data-packets/Tmx/Mx.SolaMulticast.Hsvf.v1.14.1/StrategyInstrumentKeysMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategymarketdepthmessage(self):
        for payload in payloads.of("omi-data-packets/Tmx/Mx.SolaMulticast.Hsvf.v1.14.1/StrategyMarketDepthMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_strategytrademessage(self):
        for payload in payloads.of("omi-data-packets/Tmx/Mx.SolaMulticast.Hsvf.v1.14.1/StrategyTradeMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
