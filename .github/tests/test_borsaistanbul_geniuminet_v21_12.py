# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "bist/borsaistanbul/geniuminet/BorsaIstanbul_GeniumInet_v21_12.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "borsaistanbul_geniuminet_v21_12.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class BorsaistanbulGeniuminetV2112Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_combinationorderbookleg(self):
        for payload in payloads.of("omi-data-packets/Bist/BorsaIstanbul.GeniumInet.Itch.v21.12/CombinationOrderBookLeg.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderbookdirectory(self):
        for payload in payloads.of("omi-data-packets/Bist/BorsaIstanbul.GeniumInet.Itch.v21.12/OrderBookDirectory.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_orderbookstatemessage(self):
        for payload in payloads.of("omi-data-packets/Bist/BorsaIstanbul.GeniumInet.Itch.v21.12/OrderBookStateMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_secondsmessage(self):
        for payload in payloads.of("omi-data-packets/Bist/BorsaIstanbul.GeniumInet.Itch.v21.12/SecondsMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_shortsellstatus(self):
        for payload in payloads.of("omi-data-packets/Bist/BorsaIstanbul.GeniumInet.Itch.v21.12/ShortSellStatus.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_systemeventmessage(self):
        for payload in payloads.of("omi-data-packets/Bist/BorsaIstanbul.GeniumInet.Itch.v21.12/SystemEventMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_ticksizetableentry(self):
        for payload in payloads.of("omi-data-packets/Bist/BorsaIstanbul.GeniumInet.Itch.v21.12/TickSizeTableEntry.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
