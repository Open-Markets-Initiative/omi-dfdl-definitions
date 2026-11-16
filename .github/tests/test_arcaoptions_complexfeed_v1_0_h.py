# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "nyse/arcaoptions/complexfeed/ArcaOptions_ComplexFeed_v1_0_h.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "arcaoptions_complexfeed_v1_0_h.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class ArcaoptionsComplexfeedV10HTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_complexseriesindexmappingmessage(self):
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.ComplexFeed.Pillar.v1.0.h/ComplexSeriesIndexMappingMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_messagesequence(self):
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.ComplexFeed.Pillar.v1.0.h/MessageSequence.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_optionsquotemessage(self):
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.ComplexFeed.Pillar.v1.0.h/OptionsQuoteMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_optionsstatusmessage(self):
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.ComplexFeed.Pillar.v1.0.h/OptionsStatusMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_optionstrademessage(self):
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.ComplexFeed.Pillar.v1.0.h/OptionsTradeMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sourcetimereferencemessage(self):
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.ComplexFeed.Pillar.v1.0.h/SourceTimeReferenceMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_symbolclearmessage(self):
        for payload in payloads.of("omi-data-packets/Nyse/ArcaOptions.ComplexFeed.Pillar.v1.0.h/SymbolClearMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
