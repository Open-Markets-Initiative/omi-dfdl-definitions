# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "cboe/bzxoptions/binaryorderentry/BzxOptions_BinaryOrderEntry_v2_10.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "bzxoptions_binaryorderentry_v2_10.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class BzxoptionsBinaryorderentryV210Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_cancelordermessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxOptions.BinaryOrderEntry.Boe.v2.10/CancelOrderMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_clientheartbeatmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxOptions.BinaryOrderEntry.Boe.v2.10/ClientHeartbeatMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loginrequestmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxOptions.BinaryOrderEntry.Boe.v2.10/LoginRequestMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loginresponsemessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxOptions.BinaryOrderEntry.Boe.v2.10/LoginResponseMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_modifyordermessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxOptions.BinaryOrderEntry.Boe.v2.10/ModifyOrderMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_newordermessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxOptions.BinaryOrderEntry.Boe.v2.10/NewOrderMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderacknowledgmentmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxOptions.BinaryOrderEntry.Boe.v2.10/OrderAcknowledgmentMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordercancelledmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxOptions.BinaryOrderEntry.Boe.v2.10/OrderCancelledMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutionmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxOptions.BinaryOrderEntry.Boe.v2.10/OrderExecutionMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordermodifiedmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxOptions.BinaryOrderEntry.Boe.v2.10/OrderModifiedMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderrejectedmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxOptions.BinaryOrderEntry.Boe.v2.10/OrderRejectedMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_replaycompletemessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxOptions.BinaryOrderEntry.Boe.v2.10/ReplayCompleteMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_serverheartbeatmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxOptions.BinaryOrderEntry.Boe.v2.10/ServerHeartbeatMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
