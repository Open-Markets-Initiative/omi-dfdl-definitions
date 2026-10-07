# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "nasdaq/nsmequities/nlsplus/NsmEquities_NlsPlus_v3_0.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "nsmequities_nlsplus_v3_0.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class NsmequitiesNlsplusV30Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_longformtradereportmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.NlsPlus.Itch.v3.0/LongFormTradeReportMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_regshoshortsalepricetestrestrictedindicatormessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.NlsPlus.Itch.v3.0/RegShoShortSalePriceTestRestrictedIndicatorMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_stocktradingactionmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.NlsPlus.Itch.v3.0/StockTradingActionMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_systemeventmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.NlsPlus.Itch.v3.0/SystemEventMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradereportmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.NlsPlus.Itch.v3.0/TradeReportMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
