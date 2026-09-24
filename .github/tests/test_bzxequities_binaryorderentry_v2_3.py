# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "cboe/bzxequities/binaryorderentry/BzxEquities_BinaryOrderEntry_v2_3.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "bzxequities_binaryorderentry_v2_3.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class BzxequitiesBinaryorderentryV23Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_cancelordermessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/CancelOrderMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_cancelrejectedmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/CancelRejectedMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_clientheartbeatmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/ClientHeartbeatMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loginrequestmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/LoginRequestMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loginresponsemessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/LoginResponseMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_logoutmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/LogoutMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_logoutrequestmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/LogoutRequestMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_masscancelacknowledgementmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/MassCancelAcknowledgementMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_minimalorderacknowledgementmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/MinimalOrderAcknowledgementMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_modifyordermessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/ModifyOrderMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_newordermessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/NewOrderMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderacknowledgementmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/OrderAcknowledgementMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordercancelledmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/OrderCancelledMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutionmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/OrderExecutionMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordermodifiedmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/OrderModifiedMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderrejectedmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/OrderRejectedMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderrestatedmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/OrderRestatedMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_purgeordersmessage_riskgroupid(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/PurgeOrdersMessage_RiskGroupID.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_purgeordersmessage_symbol(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/PurgeOrdersMessage_Symbol.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_purgerejectedmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/PurgeRejectedMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_replaycompletemessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/ReplayCompleteMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_serverheartbeatmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/ServerHeartbeatMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradecancelorcorrectmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/TradeCancelOrCorrectMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_usermodifyrejectedmessage(self):
        for payload in payloads.of("omi-data-packets/Cboe/BzxEquities.BinaryOrderEntry.Boe.v2.3/UserModifyRejectedMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
