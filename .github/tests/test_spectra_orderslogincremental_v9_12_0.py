# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "moex/spectra/orderslogincremental/Spectra_OrdersLogIncremental_v9_12_0.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "spectra_orderslogincremental_v9_12_0.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class SpectraOrderslogincrementalV9120Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_bestpricesmessage(self):
        for payload in payloads.of("omi-data-packets/Moex/Spectra.OrdersLogIncremental.Simba.v9.12.0/BestPricesMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_messagesequence(self):
        for payload in payloads.of("omi-data-packets/Moex/Spectra.OrdersLogIncremental.Simba.v9.12.0/MessageSequence.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderexecutionmessage(self):
        for payload in payloads.of("omi-data-packets/Moex/Spectra.OrdersLogIncremental.Simba.v9.12.0/OrderExecutionMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderupdatemessage(self):
        for payload in payloads.of("omi-data-packets/Moex/Spectra.OrdersLogIncremental.Simba.v9.12.0/OrderUpdateMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
