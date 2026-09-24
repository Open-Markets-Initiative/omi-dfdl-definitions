# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "cboe/c1options/marketdatafeed/C1Options_MarketDataFeed_v1_4_2.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "c1options_marketdatafeed_v1_4_2.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class C1optionsMarketdatafeedV142Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_currentmarketrefreshmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/C1Options.MarketDataFeed.Csm.v1.4.2/CurrentMarketRefreshMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_currentmarketupdatemessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/C1Options.MarketDataFeed.Csm.v1.4.2/CurrentMarketUpdateMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_heartbeat(self):
        for payload in payloads.of("omi-data-packets/Cboe/C1Options.MarketDataFeed.Csm.v1.4.2/Heartbeat.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_marketdatarefreshmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/C1Options.MarketDataFeed.Csm.v1.4.2/MarketDataRefreshMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_recapupdatemessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/C1Options.MarketDataFeed.Csm.v1.4.2/RecapUpdateMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitydefinitionmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/C1Options.MarketDataFeed.Csm.v1.4.2/SecurityDefinitionMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tickermessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/C1Options.MarketDataFeed.Csm.v1.4.2/TickerMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
