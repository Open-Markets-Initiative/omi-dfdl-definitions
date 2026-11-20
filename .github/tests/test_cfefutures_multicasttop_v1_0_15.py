# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "cboe/cfefutures/multicasttop/CfeFutures_MulticastTop_v1_0_15.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "cfefutures_multicasttop_v1_0_15.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class CfefuturesMulticasttopV1015Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_endofdaysummarymessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastTop.Pitch.v1.0.15/EndOfDaySummaryMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_endofsessionmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastTop.Pitch.v1.0.15/EndOfSessionMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_futuresinstrumentdefinitionmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastTop.Pitch.v1.0.15/FuturesInstrumentDefinitionMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_marketsnapshotlongmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastTop.Pitch.v1.0.15/MarketSnapshotLongMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_marketsnapshotshortmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastTop.Pitch.v1.0.15/MarketSnapshotShortMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_pricelimitsmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastTop.Pitch.v1.0.15/PriceLimitsMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_settlementmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastTop.Pitch.v1.0.15/SettlementMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_singlesideupdatelongmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastTop.Pitch.v1.0.15/SingleSideUpdateLongMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_singlesideupdateshortmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastTop.Pitch.v1.0.15/SingleSideUpdateShortMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_timemessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastTop.Pitch.v1.0.15/TimeMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_timereferencemessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastTop.Pitch.v1.0.15/TimeReferenceMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_toptrademessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastTop.Pitch.v1.0.15/TopTradeMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradingstatusmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastTop.Pitch.v1.0.15/TradingStatusMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_twosideupdatelongmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastTop.Pitch.v1.0.15/TwoSideUpdateLongMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_twosideupdateshortmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/CfeFutures.MulticastTop.Pitch.v1.0.15/TwoSideUpdateShortMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
