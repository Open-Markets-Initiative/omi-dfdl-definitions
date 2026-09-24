# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "miax/pearlequities/expressorders/PearlEquities_ExpressOrders_v2_6.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "pearlequities_expressorders_v2_6.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class PearlequitiesExpressordersV26Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_cancelorderrequest(self):
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/CancelOrderRequest.pcap"):
            if payloads.partial(payload, 0, 2, "little", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", False):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_cancelorderresponse(self):
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/CancelOrderResponse.pcap"):
            if payloads.partial(payload, 0, 2, "little", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", False):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_cancelorreducesizeordernotification(self):
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/CancelOrReduceSizeOrderNotification.pcap"):
            if payloads.partial(payload, 0, 2, "little", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", False):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_clientheartbeat(self):
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/ClientHeartbeat.pcap"):
            if payloads.partial(payload, 0, 2, "little", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", False):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loginrequest(self):
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/LoginRequest.pcap"):
            if payloads.partial(payload, 0, 2, "little", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", False):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_loginresponse(self):
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/LoginResponse.pcap"):
            if payloads.partial(payload, 0, 2, "little", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", False):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_newordernotification(self):
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/NewOrderNotification.pcap"):
            if payloads.partial(payload, 0, 2, "little", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", False):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_neworderrequest(self):
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/NewOrderRequest.pcap"):
            if payloads.partial(payload, 0, 2, "little", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", False):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderpriceupdatenotification(self):
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/OrderPriceUpdateNotification.pcap"):
            if payloads.partial(payload, 0, 2, "little", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", False):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_serverheartbeat(self):
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/ServerHeartbeat.pcap"):
            if payloads.partial(payload, 0, 2, "little", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", False):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_symbolupdate(self):
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/SymbolUpdate.pcap"):
            if payloads.partial(payload, 0, 2, "little", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", False):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_systemstatenotification(self):
        for payload in payloads.of("omi-data-packets/Miax/PearlEquities.ExpressOrders.Meo.v2.6/SystemStateNotification.pcap"):
            if payloads.partial(payload, 0, 2, "little", False):
                self.skipTest("capture ends mid message; tcp reassembly required")
            for message in payloads.messages(payload, 0, 2, "little", False):
                data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
                with open(data, "wb") as handle:
                    handle.write(message)
                result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
