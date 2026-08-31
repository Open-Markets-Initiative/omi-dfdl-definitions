# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "coinbase/coinbasederivatives/marketdataapi/CoinbaseDerivatives_MarketDataApi_v1_2.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "coinbasederivatives_marketdataapi_v1_2.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class CoinbasederivativesMarketdataapiV12Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_orderdeletemessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.MarketDataApi.Sbe.v1.2/OrderDeleteMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderputmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.MarketDataApi.Sbe.v1.2/OrderPutMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordersnapshotmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.MarketDataApi.Sbe.v1.2/OrderSnapshotMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_startofoutrightinstrumentsnapshotmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.MarketDataApi.Sbe.v1.2/StartOfOutrightInstrumentSnapshotMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_startofspreadinstrumentsnapshotmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.MarketDataApi.Sbe.v1.2/StartOfSpreadInstrumentSnapshotMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
