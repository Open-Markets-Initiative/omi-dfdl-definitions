# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "coinbase/deribit/ordersapi/Deribit_OrdersApi_v0_1.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "deribit_ordersapi_v0_1.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class DeribitOrdersapiV01Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_amendorderrejectmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/AmendOrderRejectMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_amendorderrequestmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/AmendOrderRequestMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_amendorderresponsemessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/AmendOrderResponseMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_cancelorderrequestmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/CancelOrderRequestMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_cancelorderresponsemessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/CancelOrderResponseMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_massquoterejectmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/MassQuoteRejectMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_massquoterequestmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/MassQuoteRequestMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_massquoteresponsemessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/MassQuoteResponseMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_neworderrejectmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/NewOrderRejectMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_neworderrequestmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/NewOrderRequestMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_neworderresponsemessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/NewOrderResponseMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderfilledmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/Deribit.OrdersApi.Sbe.v0.1/OrderFilledMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
