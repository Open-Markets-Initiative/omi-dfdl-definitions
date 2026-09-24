# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "cboe/edgaequities/multicastdepthofbook/EdgaEquities_MulticastDepthOfBook_v2_41_29.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "edgaequities_multicastdepthofbook_v2_41_29.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class EdgaequitiesMulticastdepthofbookV24129Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_addorderlongmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/EdgaEquities.MulticastDepthOfBook.Pitch.v2.41.29/AddOrderLongMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_addordershortmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/EdgaEquities.MulticastDepthOfBook.Pitch.v2.41.29/AddOrderShortMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_deleteordermessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/EdgaEquities.MulticastDepthOfBook.Pitch.v2.41.29/DeleteOrderMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_modifyorderlongmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/EdgaEquities.MulticastDepthOfBook.Pitch.v2.41.29/ModifyOrderLongMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_modifyordershortmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/EdgaEquities.MulticastDepthOfBook.Pitch.v2.41.29/ModifyOrderShortMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedatpricesizemessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/EdgaEquities.MulticastDepthOfBook.Pitch.v2.41.29/OrderExecutedAtPriceSizeMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/EdgaEquities.MulticastDepthOfBook.Pitch.v2.41.29/OrderExecutedMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_reducesizeshortmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/EdgaEquities.MulticastDepthOfBook.Pitch.v2.41.29/ReduceSizeShortMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_timemessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/EdgaEquities.MulticastDepthOfBook.Pitch.v2.41.29/TimeMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradelongmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/EdgaEquities.MulticastDepthOfBook.Pitch.v2.41.29/TradeLongMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradeshortmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/EdgaEquities.MulticastDepthOfBook.Pitch.v2.41.29/TradeShortMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradingstatusmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/EdgaEquities.MulticastDepthOfBook.Pitch.v2.41.29/TradingStatusMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
