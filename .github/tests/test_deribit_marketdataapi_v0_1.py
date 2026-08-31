# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "coinbase/deribit/marketdataapi/Deribit_MarketDataApi_v0_1.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "deribit_marketdataapi_v0_1.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class DeribitMarketdataapiV01Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_askdeletemessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.MarketDataApi.Sbe.v0.1/AskDeleteMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_askputmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.MarketDataApi.Sbe.v0.1/AskPutMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_askqtyreducedmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.MarketDataApi.Sbe.v0.1/AskQtyReducedMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_biddeletemessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.MarketDataApi.Sbe.v0.1/BidDeleteMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_bidputmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.MarketDataApi.Sbe.v0.1/BidPutMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_bidqtyreducedmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.MarketDataApi.Sbe.v0.1/BidQtyReducedMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_endofcyclemessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.MarketDataApi.Sbe.v0.1/EndOfCycleMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_instrumentmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.MarketDataApi.Sbe.v0.1/InstrumentMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_snapshottrailermessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.MarketDataApi.Sbe.v0.1/SnapshotTrailerMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
