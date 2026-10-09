# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "nyse/nyseequities/binarygateway/NyseEquities_BinaryGateway_v6_0.dfdl.xsd"
PARSER_CLIENTPILLARMESSAGE = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "nyseequities_binarygateway_v6_0_clientpillarmessage.parser")
PARSER_SERVERPILLARMESSAGE = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "nyseequities_binarygateway_v6_0_serverpillarmessage.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class NyseequitiesBinarygatewayV60Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "clientPillarMessage", PARSER_CLIENTPILLARMESSAGE], check=True)
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "serverPillarMessage", PARSER_SERVERPILLARMESSAGE], check=True)

    def test_closeresponse(self):
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/CloseResponse.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPILLARMESSAGE, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_equitiessymbolreferencedatamessage(self):
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/EquitiesSymbolReferenceDataMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPILLARMESSAGE, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_executionreportmessage(self):
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/ExecutionReportMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPILLARMESSAGE, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_heartbeat(self):
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/Heartbeat.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPILLARMESSAGE, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loginmessage(self):
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/LoginMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTPILLARMESSAGE, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loginresponse(self):
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/LoginResponse.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPILLARMESSAGE, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_newordersingleandcancelreplacerequestmessage(self):
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/NewOrderSingleAndCancelReplaceRequestMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTPILLARMESSAGE, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_open(self):
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/Open.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTPILLARMESSAGE, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_openresponse(self):
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/OpenResponse.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPILLARMESSAGE, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderandcancelreplaceacknowledgementmessage(self):
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/OrderAndCancelReplaceAcknowledgementMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPILLARMESSAGE, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_streamavail(self):
        for payload in payloads.of("omi-data-packets/Nyse/NyseEquities.BinaryGateway.PillarStream.v6.0/StreamAvail.pcap"):
            if payloads.partial(payload, 2, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", True):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPILLARMESSAGE, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
