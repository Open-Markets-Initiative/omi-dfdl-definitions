# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "moex/spectra/futinfoincremental/Spectra_FutInfoIncremental_v9_12_0.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "spectra_futinfoincremental_v9_12_0.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class SpectraFutinfoincrementalV9120Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_heartbeatmessage(self):
        for payload in payloads.of("omi-data-packets/Moex/Spectra.FutInfoIncremental.Simba.v9.12.0/HeartbeatMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_messagesequence(self):
        for payload in payloads.of("omi-data-packets/Moex/Spectra.FutInfoIncremental.Simba.v9.12.0/MessageSequence.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitygroupstatusmessage(self):
        for payload in payloads.of("omi-data-packets/Moex/Spectra.FutInfoIncremental.Simba.v9.12.0/SecurityGroupStatusMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_securitymassstatusmessage(self):
        for payload in payloads.of("omi-data-packets/Moex/Spectra.FutInfoIncremental.Simba.v9.12.0/SecurityMassStatusMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_tradingsessionstatusmessage(self):
        for payload in payloads.of("omi-data-packets/Moex/Spectra.FutInfoIncremental.Simba.v9.12.0/TradingSessionStatusMessage.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
