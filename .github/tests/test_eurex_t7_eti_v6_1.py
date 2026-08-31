# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "eurex/eti/Eurex_T7_Eti_v6_1.dfdl.xsd"
PARSER_CLIENTPACKET = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "eurex_t7_eti_v6_1_clientpacket.parser")
PARSER_SERVERPACKET = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "eurex_t7_eti_v6_1_serverpacket.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class EurexT7EtiV61Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "clientPacket", PARSER_CLIENTPACKET], check=True)
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "serverPacket", PARSER_SERVERPACKET], check=True)

    def test_heartbeat(self):
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eti.Fbe.v6.1/Heartbeat.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_retransmitmemessagerequest(self):
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eti.Fbe.v6.1/RetransmitMeMessageRequest.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_CLIENTPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_userloginresponse(self):
        for payload in payloads.of("omi-data-packets/Eurex/T7.Eti.Fbe.v6.1/UserLoginResponse.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER_SERVERPACKET, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
