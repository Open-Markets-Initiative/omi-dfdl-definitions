# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "nasdaq/nsmequities/totalview/NsmEquities_TotalView_Itch_v5_0_2026.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "nsmequities_totalview_itch_v5_0_2026.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class NsmequitiesTotalviewItchV502026Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_addordernompidattributionmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/AddOrderNoMpidAttributionMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_addorderwithmpidattributionmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/AddOrderWithMpidAttributionMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_crosstrademessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/CrossTradeMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_luldauctioncollarmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/LuldAuctionCollarMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_marketparticipantpositionmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/MarketParticipantPositionMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_netorderimbalanceindicatormessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/NetOrderImbalanceIndicatorMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_noncrosstrademessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/NonCrossTradeMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordercancelmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/OrderCancelMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderdeletemessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/OrderDeleteMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/OrderExecutedMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedwithpricemessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/OrderExecutedWithPriceMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderreplacemessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/OrderReplaceMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_regshoshortsalepricetestrestrictedindicatormessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/RegShoShortSalePriceTestRestrictedIndicatorMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_stockdirectorymessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/StockDirectoryMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_stocktradingactionmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/StockTradingActionMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_systemeventmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2026/SystemEventMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
