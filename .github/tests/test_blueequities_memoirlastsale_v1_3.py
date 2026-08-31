# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "blueoceanats/blueequities/memoirlastsale/BlueEquities_MemoirLastSale_v1_3.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "blueequities_memoirlastsale_v1_3.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class BlueequitiesMemoirlastsaleV13Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_instrumentdirectorymessage(self):
        for payload in payloads.of("omi-data-packets/BlueOceanAts/BlueEquities.MemoirLastSale.Sbe.v1.3/InstrumentDirectoryMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitytradingstatusmessage(self):
        for payload in payloads.of("omi-data-packets/BlueOceanAts/BlueEquities.MemoirLastSale.Sbe.v1.3/SecurityTradingStatusMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradereportmessage(self):
        for payload in payloads.of("omi-data-packets/BlueOceanAts/BlueEquities.MemoirLastSale.Sbe.v1.3/TradeReportMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradingsessionstatusmessage(self):
        for payload in payloads.of("omi-data-packets/BlueOceanAts/BlueEquities.MemoirLastSale.Sbe.v1.3/TradingSessionStatusMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
