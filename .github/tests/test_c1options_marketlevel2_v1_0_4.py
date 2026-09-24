# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "cboe/c1options/marketlevel2/C1Options_MarketLevel2_v1_0_4.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "c1options_marketlevel2_v1_0_4.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class C1optionsMarketlevel2V104Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_heartbeatmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/C1Options.MarketLevel2.Csm.v1.0.4/HeartbeatMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_incrementalrefreshmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/C1Options.MarketLevel2.Csm.v1.0.4/IncrementalRefreshMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitydefinitionmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/C1Options.MarketLevel2.Csm.v1.0.4/SecurityDefinitionMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitystatusmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/C1Options.MarketLevel2.Csm.v1.0.4/SecurityStatusMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_snapshotfullrefreshmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/C1Options.MarketLevel2.Csm.v1.0.4/SnapshotFullRefreshMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
