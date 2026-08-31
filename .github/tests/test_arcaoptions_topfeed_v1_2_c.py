# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "nyse/arcaoptions/topfeed/ArcaOptions_TopFeed_v1_2_c.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "arcaoptions_topfeed_v1_2_c.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class ArcaoptionsTopfeedV12CTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_heartbeat(self):
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.TopFeed.Pillar.v1.2.c/HeartBeat.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_optionsquotemessage(self):
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.TopFeed.Pillar.v1.2.c/OptionsQuoteMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sequencenumberresetmessage(self):
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.TopFeed.Pillar.v1.2.c/SequenceNumberResetMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
