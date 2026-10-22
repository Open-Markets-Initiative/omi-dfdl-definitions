# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "nyse/nysebonds/depthofbook/NyseBonds_DepthOfBook_v4_01_b.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "nysebonds_depthofbook_v4_01_b.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class NysebondsDepthofbookV401BTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "serverPacket", PARSER], check=True)

    def test_addordermessage(self):
        for payload in payloads.of("omi-data-packets/Nyse/NyseBonds.DepthOfBook.Abp.v4.01.b/AddOrderMessage.pcap"):
            if payloads.partial(payload, 0, 2, "big", 4):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "big", 4):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_deleteordermessage(self):
        for payload in payloads.of("omi-data-packets/Nyse/NyseBonds.DepthOfBook.Abp.v4.01.b/DeleteOrderMessage.pcap"):
            if payloads.partial(payload, 0, 2, "big", 4):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "big", 4):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
