# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "nasdaq/uqdf/output/Nasdaq_Uqdf_Output_v1_5.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "nasdaq_uqdf_output_v1_5.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class NasdaqUqdfOutputV15Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_limituplimitdownpricebandmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/Uqdf.Output.Utp.v1.5/LimitUpLimitDownPriceBandMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_quotelongformmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/Uqdf.Output.Utp.v1.5/QuoteLongFormMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_quoteshortformmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/Uqdf.Output.Utp.v1.5/QuoteShortFormMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
