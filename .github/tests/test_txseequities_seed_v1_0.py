# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "txse/txseequities/seed/TxseEquities_Seed_v1_0.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "txseequities_seed_v1_0.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class TxseequitiesSeedV10Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_definesymbolmessage(self):
        for payload in payloads.of("omi-data-packets/Txse/TxseEquities.Seed.Rake.v1.0/DefineSymbolMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", False):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_limitorderaccepted(self):
        for payload in payloads.of("omi-data-packets/Txse/TxseEquities.Seed.Rake.v1.0/LimitOrderAccepted.pcap"):
            if payloads.partial(payload, 0, 2, "little", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", False):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_limitordermessage(self):
        for payload in payloads.of("omi-data-packets/Txse/TxseEquities.Seed.Rake.v1.0/LimitOrderMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", False):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_logonrequestmessage(self):
        for payload in payloads.of("omi-data-packets/Txse/TxseEquities.Seed.Rake.v1.0/LogonRequestMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", False):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
