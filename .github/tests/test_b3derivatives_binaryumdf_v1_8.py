# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "b3/binaryumdf/B3Derivatives_BinaryUmdf_v1_8.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "b3derivatives_binaryumdf_v1_8.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class B3derivativesBinaryumdfV18Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_securitydefinitionmessage(self):
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryUmdf.Sbe.v1.8/SecurityDefinitionMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sequence(self):
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryUmdf.Sbe.v1.8/Sequence.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
