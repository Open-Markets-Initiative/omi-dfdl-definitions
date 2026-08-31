# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "b3/binaryentrypoint/B3Derivatives_BinaryEntryPoint_v8_1.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "b3derivatives_binaryentrypoint_v8_1.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class B3derivativesBinaryentrypointV81Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_establishmessage(self):
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/EstablishMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_executionreportcancelmessage(self):
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/ExecutionReportCancelMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_executionreportmodifymessage(self):
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/ExecutionReportModifyMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_executionreportnewmessage(self):
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/ExecutionReportNewMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_executionreportrejectmessage(self):
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/ExecutionReportRejectMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_executionreporttrademessage(self):
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/ExecutionReportTradeMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_negotiatemessage(self):
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/NegotiateMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_newordercrossmessage(self):
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/NewOrderCrossMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_newordersinglemessage(self):
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/NewOrderSingleMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordercancelreplacerequestmessage(self):
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/OrderCancelReplaceRequestMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordercancelrequestmessage(self):
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/OrderCancelRequestMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordermassactionreportmessage(self):
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/OrderMassActionReportMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordermassactionrequestmessage(self):
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/OrderMassActionRequestMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_retransmitrequestmessage(self):
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/RetransmitRequestMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_simplemodifyordermessage(self):
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/SimpleModifyOrderMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_simplenewordermessage(self):
        for payload in payloads.of("omi-data-packets/B3/B3Derivatives.BinaryEntryPoint.Sbe.v8.1/SimpleNewOrderMessage.pcap"):
            if payloads.partial(payload, 0, 2, "little", True):
                self.skipTest("capture ends mid message; tcp reassembly required")
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
