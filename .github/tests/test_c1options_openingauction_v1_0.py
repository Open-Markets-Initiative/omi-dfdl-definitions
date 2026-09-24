# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "cboe/c1options/openingauction/C1Options_OpeningAuction_v1_0.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "c1options_openingauction_v1_0.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class C1optionsOpeningauctionV10Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_currentmarketupdatemessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/C1Options.OpeningAuction.Csm.v1.0/CurrentMarketUpdateMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_expectedopeningpriceandsizemessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/C1Options.OpeningAuction.Csm.v1.0/ExpectedOpeningPriceAndSizeMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_heartbeatmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/C1Options.OpeningAuction.Csm.v1.0/HeartbeatMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_marketdatarefreshmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/C1Options.OpeningAuction.Csm.v1.0/MarketDataRefreshMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitydefinitionmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/C1Options.OpeningAuction.Csm.v1.0/SecurityDefinitionMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
