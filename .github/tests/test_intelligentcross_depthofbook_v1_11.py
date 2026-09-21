# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "imperative/depthofbook/IntelligentCross_DepthOfBook_v1_11.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "intelligentcross_depthofbook_v1_11.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class IntelligentcrossDepthofbookV111Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_orderexecutedmessage(self):
        for payload in payloads.of("omi-data-packets/Imperative/IntelligentCross.DepthOfBook.Aspen.v1.11/OrderExecutedMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_trademessage(self):
        for payload in payloads.of("omi-data-packets/Imperative/IntelligentCross.DepthOfBook.Aspen.v1.11/TradeMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
