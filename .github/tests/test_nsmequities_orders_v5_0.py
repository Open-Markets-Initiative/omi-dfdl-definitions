# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "nasdaq/nsmequities/orders/NsmEquities_Orders_v5_0.dfdl.xsd"
PARSER_CLIENTPACKET = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "nsmequities_orders_v5_0_clientpacket.parser")
PARSER_SERVERPACKET = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "nsmequities_orders_v5_0_serverpacket.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class NsmequitiesOrdersV50Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "clientPacket", PARSER_CLIENTPACKET], check=True)
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "serverPacket", PARSER_SERVERPACKET], check=True)

    def test_cancelordermessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.Orders.Ouch.v5.0/CancelOrderMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_canceledmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.Orders.Ouch.v5.0/CanceledMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_enterordermessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.Orders.Ouch.v5.0/EnterOrderMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderacceptedmessage(self):
        for payload in payloads.of("omi-data-packets/Nasdaq/NsmEquities.Orders.Ouch.v5.0/OrderAcceptedMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
