# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "coinbase/coinbasederivatives/ordersapi/CoinbaseDerivatives_OrdersApi_v1_4.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "coinbasederivatives_ordersapi_v1_4.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class CoinbasederivativesOrdersapiV14Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_cancelordermessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/CancelOrderMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_cancelorderrejectmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/CancelOrderRejectMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_instrumentinfomessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/InstrumentInfoMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_instrumentinforequestmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/InstrumentInfoRequestMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_lastexecidmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/LastExecIdMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_lastexecidrequestmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/LastExecIdRequestMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loggedoutmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/LoggedOutMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_logonconfmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/LogonConfMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_logonmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/LogonMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_logoutmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/LogoutMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_masscancelorderackmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/MassCancelOrderAckMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_masscancelordermessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/MassCancelOrderMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_masscancelorderrejectmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/MassCancelOrderRejectMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_newordermessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/NewOrderMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ordercanceledmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/OrderCanceledMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderenteredmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/OrderEnteredMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderfilledmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/OrderFilledMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderrejectmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/OrderRejectMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderreplacedmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/OrderReplacedMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_pingmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/PingMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_pongmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/PongMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_replaceordermessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/ReplaceOrderMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_setaccountmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/SetAccountMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_setackmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/SetAckMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_settradermessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/SetTraderMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_streamordermessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/StreamOrderMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_unlocktradingackmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/UnlockTradingAckMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_unlocktradingmessage(self):
        for payload in payloads.of("omi-data-packets/Coinbase/CoinbaseDerivatives.OrdersApi.Sbe.v1.4/UnlockTradingMessage.pcap"):
            if payloads.partial(payload, 2, 2, "little", 0):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 2, 2, "little", 0):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
