# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "memx/memxequities/memoirdepthfeed/MemxEquities_MemoirDepthFeed_v1_3.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "memxequities_memoirdepthfeed_v1_3.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class MemxequitiesMemoirdepthfeedV13Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_heartbeat(self):
        for payload in payloads.of("omi-data-packets/Memx/MemxEquities.MemoirDepthFeed.Sbe.v1.3/Heartbeat.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderaddedmessage(self):
        for payload in payloads.of("omi-data-packets/Memx/MemxEquities.MemoirDepthFeed.Sbe.v1.3/OrderAddedMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderdeletedmessage(self):
        for payload in payloads.of("omi-data-packets/Memx/MemxEquities.MemoirDepthFeed.Sbe.v1.3/OrderDeletedMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedmessage(self):
        for payload in payloads.of("omi-data-packets/Memx/MemxEquities.MemoirDepthFeed.Sbe.v1.3/OrderExecutedMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderreducedmessage(self):
        for payload in payloads.of("omi-data-packets/Memx/MemxEquities.MemoirDepthFeed.Sbe.v1.3/OrderReducedMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_regshowrestrictionmessage(self):
        for payload in payloads.of("omi-data-packets/Memx/MemxEquities.MemoirDepthFeed.Sbe.v1.3/RegShowRestrictionMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitytradingstatusmessage(self):
        for payload in payloads.of("omi-data-packets/Memx/MemxEquities.MemoirDepthFeed.Sbe.v1.3/SecurityTradingStatusMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_stocktradingactionmessage(self):
        for payload in payloads.of("omi-data-packets/Memx/MemxEquities.MemoirDepthFeed.Sbe.v1.3/StockTradingActionMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradingsessionstatusmessage(self):
        for payload in payloads.of("omi-data-packets/Memx/MemxEquities.MemoirDepthFeed.Sbe.v1.3/TradingSessionStatusMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
