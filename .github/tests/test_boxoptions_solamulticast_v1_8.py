# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "box/boxoptions/solamulticast/BoxOptions_SolaMulticast_v1_8.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "boxoptions_solamulticast_v1_8.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class BoxoptionsSolamulticastV18Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_optionquotemessage(self):
        for payload in payloads.of("omi-data-packets/Box/BoxOptions.SolaMulticast.Hsvf.v1.8/OptionQuoteMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
