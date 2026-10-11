# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "cboe/bzxequities/multicastdepthofbook/BzxEquities_MulticastDepthOfBook_Spin_v2_20_4.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "bzxequities_multicastdepthofbook_spin_v2_20_4.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class BzxequitiesMulticastdepthofbookSpinV2204Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_loginmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.MulticastDepthOfBook.Spin.v2.20.4/LoginMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loginresponsemessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.MulticastDepthOfBook.Spin.v2.20.4/LoginResponseMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_spinfinishedmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.MulticastDepthOfBook.Spin.v2.20.4/SpinFinishedMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_spinimageavailablemessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.MulticastDepthOfBook.Spin.v2.20.4/SpinImageAvailableMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_spinrequestmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.MulticastDepthOfBook.Spin.v2.20.4/SpinRequestMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_spinresponsemessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.MulticastDepthOfBook.Spin.v2.20.4/SpinResponseMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_timemessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.MulticastDepthOfBook.Spin.v2.20.4/TimeMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
