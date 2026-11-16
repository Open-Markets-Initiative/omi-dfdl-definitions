# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "nyse/amexequities/openbook.aggregated/AmexEquities_OpenBook.Aggregated_v2_1_d.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "amexequities_openbook_aggregated_v2_1_d.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class AmexequitiesOpenbookAggregatedV21DTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_messagesequence(self):
        for payload in payloads.of("omi-data-packets/Nyse/AmexEquities.OpenBook.Aggregated.Xdp.v2.1.d/MessageSequence.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderbookdeltaupdatemessage(self):
        for payload in payloads.of("omi-data-packets/Nyse/AmexEquities.OpenBook.Aggregated.Xdp.v2.1.d/OrderbookDeltaUpdateMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderbooksnapshotmessage(self):
        for payload in payloads.of("omi-data-packets/Nyse/AmexEquities.OpenBook.Aggregated.Xdp.v2.1.d/OrderbookSnapshotMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sequencenumberresetmessage(self):
        for payload in payloads.of("omi-data-packets/Nyse/AmexEquities.OpenBook.Aggregated.Xdp.v2.1.d/SequenceNumberResetMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_symbolindexmappingmessage(self):
        for payload in payloads.of("omi-data-packets/Nyse/AmexEquities.OpenBook.Aggregated.Xdp.v2.1.d/SymbolIndexMappingMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
