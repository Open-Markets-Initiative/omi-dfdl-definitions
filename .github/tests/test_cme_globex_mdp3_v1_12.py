# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "cme/mdp3/Cme_Globex_Mdp3_v1_12.dfdl.xsd"
PARSER_CLIENTTCPPACKET = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "cme_globex_mdp3_v1_12_clienttcppacket.parser")
PARSER_SERVERTCPPACKET = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "cme_globex_mdp3_v1_12_servertcppacket.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class CmeGlobexMdp3V112Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "clientTcpPacket", PARSER_CLIENTTCPPACKET], check=True)
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "serverTcpPacket", PARSER_SERVERTCPPACKET], check=True)

    def test_marketdatarequesttcp(self):
        for payload in payloads.of("omi-data-packets/Cme/Globex.Mdp3.Sbe.v1.12/MarketDataRequest.Tcp.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTTCPPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_mdincrementalrefreshbooklongqty(self):
        for payload in payloads.of("omi-data-packets/Cme/Globex.Mdp3.Sbe.v1.12/MdIncrementalRefreshBookLongQty.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERTCPPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_mdincrementalrefreshtradesummarylongqty(self):
        for payload in payloads.of("omi-data-packets/Cme/Globex.Mdp3.Sbe.v1.12/MdIncrementalRefreshTradeSummaryLongQty.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERTCPPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_mdinstrumentdefinitionfxtcp(self):
        for payload in payloads.of("omi-data-packets/Cme/Globex.Mdp3.Sbe.v1.12/MdInstrumentDefinitionFx.Tcp.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTTCPPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_requestacktcp(self):
        for payload in payloads.of("omi-data-packets/Cme/Globex.Mdp3.Sbe.v1.12/RequestAck.Tcp.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTTCPPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitylistrequesttcp(self):
        for payload in payloads.of("omi-data-packets/Cme/Globex.Mdp3.Sbe.v1.12/SecurityListRequest.Tcp.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTTCPPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitystatustcp(self):
        for payload in payloads.of("omi-data-packets/Cme/Globex.Mdp3.Sbe.v1.12/SecurityStatus.Tcp.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTTCPPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitystatusrequesttcp(self):
        for payload in payloads.of("omi-data-packets/Cme/Globex.Mdp3.Sbe.v1.12/SecurityStatusRequest.Tcp.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTTCPPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_snapshotfullrefreshtcplongqtytcp(self):
        for payload in payloads.of("omi-data-packets/Cme/Globex.Mdp3.Sbe.v1.12/SnapshotFullRefreshTcpLongQty.Tcp.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTTCPPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_subscriberheartbeattcp(self):
        for payload in payloads.of("omi-data-packets/Cme/Globex.Mdp3.Sbe.v1.12/SubscriberHeartbeat.Tcp.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTTCPPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
