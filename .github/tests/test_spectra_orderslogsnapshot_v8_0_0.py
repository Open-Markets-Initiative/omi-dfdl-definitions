# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "moex/spectra/orderslogsnapshot/Spectra_OrdersLogSnapshot_v8_0_0.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "spectra_orderslogsnapshot_v8_0_0.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class SpectraOrderslogsnapshotV800Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_orderbooksnapshotmessage(self):
        for payload in payloads.of("omi-data-packets/Moex/Spectra.OrdersLogSnapshot.Simba.v8.0.0/OrderBookSnapshotMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_sequenceresetmessage(self):
        for payload in payloads.of("omi-data-packets/Moex/Spectra.OrdersLogSnapshot.Simba.v8.0.0/SequenceResetMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
