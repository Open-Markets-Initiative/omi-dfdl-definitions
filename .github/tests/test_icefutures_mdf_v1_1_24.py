# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "ice/mdf/IceFutures_Mdf_v1_1_24.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "icefutures_mdf_v1_1_24.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class IcefuturesMdfV1124Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_addormodifyordermessage(self):
        for payload in payloads.of("omi-data-packets/Ice/IceFutures.Mdf.iMpact.v1.1.24/AddOrModifyOrderMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_marketstatechangemessage(self):
        for payload in payloads.of("omi-data-packets/Ice/IceFutures.Mdf.iMpact.v1.1.24/MarketStateChangeMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_newoptionsstrategydefinitionmessage(self):
        for payload in payloads.of("omi-data-packets/Ice/IceFutures.Mdf.iMpact.v1.1.24/NewOptionsStrategyDefinitionMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_openpricemessage(self):
        for payload in payloads.of("omi-data-packets/Ice/IceFutures.Mdf.iMpact.v1.1.24/OpenPriceMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_preopenpriceindicatormessage(self):
        for payload in payloads.of("omi-data-packets/Ice/IceFutures.Mdf.iMpact.v1.1.24/PreOpenPriceIndicatorMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
