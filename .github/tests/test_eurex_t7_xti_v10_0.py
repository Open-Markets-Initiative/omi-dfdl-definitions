# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "eurex/xti/Eurex_T7_Xti_v10_0.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "eurex_t7_xti_v10_0.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class EurexT7XtiV100Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "serverPacket", PARSER], check=True)

    def test_orderexecresponse(self):
        for payload in payloads.of("omi-data-packets/Eurex/T7.Xti.Fbe.v10.0/OrderExecResponse.pcap"):
            if payloads.partial(payload, 0, 4, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
