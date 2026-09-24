# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "siac/cqs/output/Siac_Cqs_Output_v2_10_a.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "siac_cqs_output_v2_10_a.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class SiacCqsOutputV210ATests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_a_s_symbol_reference_data(self):
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/A_S_Symbol_Reference_Data.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_c_a_start_of_day(self):
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/C_A_Start_of_Day.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_c_c_finra_close(self):
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/C_C_FINRA_Close.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_c_o_finra_open(self):
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/C_O_FINRA_Open.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_c_t_line_integrity(self):
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/C_T_Line_Integrity.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_c_z_end_of_day(self):
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/C_Z_End_of_Day.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_m_k_mwcb_decline_level_status(self):
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/M_K_MWCB_Decline_Level_Status.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_q_l_long_quote(self):
        for payload in payloads.of("omi-data-packets/Siac/Cqs.Output.Cta.v2.10.a/Q_L_Long_Quote.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
