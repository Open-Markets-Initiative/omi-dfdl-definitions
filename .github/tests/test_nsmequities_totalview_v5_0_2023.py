# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "nasdaq/nsmequities/totalview/NsmEquities_TotalView_v5_0_2023.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "nsmequities_totalview_v5_0_2023.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class NsmequitiesTotalviewV502023Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_addordernompid(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2023/AddOrderNoMPID.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_addorderwithmpid(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2023/AddOrderWithMPID.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_crosstrade(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2023/CrossTrade.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_luldauctioncollar(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2023/LULDAuctionCollar.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_marketparticipantposition(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2023/MarketParticipantPosition.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_netorderimbalanceindicator(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2023/NetOrderImbalanceIndicator.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_noncrosstrade(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2023/NonCrossTrade.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordercancel(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2023/OrderCancel.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderdelete(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2023/OrderDelete.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecuted(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2023/OrderExecuted.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutedwithprice(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2023/OrderExecutedWithPrice.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderreplace(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2023/OrderReplace.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_regshorestriction(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2023/RegSHORestriction.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_stocktradingaction(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2023/StockTradingAction.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_systemevent(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.TotalView.Itch.v5.0.2023/SystemEvent.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
