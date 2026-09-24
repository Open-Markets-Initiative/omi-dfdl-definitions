# Generated Dfdl definition tests: daffodil parses captures from omi-data-packets

import os
import subprocess
import sys
import unittest

sys.path.insert(0, ".github/tests")

import payloads

SCHEMA = "siac/cts/output/Siac_Cts_Output_v2_11_b.dfdl.xsd"
PARSER = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "siac_cts_output_v2_11_b.parser")
DAFFODIL = os.environ.get("DAFFODIL", "daffodil")


class SiacCtsOutputV211BTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run([DAFFODIL, "save-parser", "-s", SCHEMA, "-r", "packet", PARSER], check=True)

    def test_a_a_start_of_end_of_day_summary(self):
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/A_A_Start_of_End_of_Day_Summary.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_a_b_end_of_end_of_day_summary(self):
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/A_B_End_of_End_of_Day_Summary.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_a_c_start_of_start_of_day_summary(self):
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/A_C_Start_of_Start_of_Day_Summary.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_a_d_end_of_start_of_day_summary(self):
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/A_D_End_of_Start_of_Day_Summary.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_a_s_symbol_reference_data(self):
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/A_S_Symbol_Reference_Data.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_c_a_start_of_day(self):
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/C_A_Start_of_Day.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_c_t_line_integrity(self):
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/C_T_Line_Integrity.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_c_z_end_of_day(self):
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/C_Z_End_of_Day.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_m_k_mwcb_decline_level_status(self):
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/M_K_MWCB_Decline_Level_Status.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_m_v_fractional_approximate_adjusted_volume_market_center(self):
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/M_V_Fractional_Approximate_Adjusted_Volume_Market_Center.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_p_e_fractional_prior_day_trade_cancelerror(self):
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/P_E_Fractional_Prior_Day_Trade_Cancel-Error.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_p_r_fractional_prior_day_trade(self):
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/P_R_Fractional_Prior_Day_Trade.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_s_a_consolidated_start_of_day_summary(self):
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/S_A_Consolidated_Start_of_Day_Summary.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_s_b_participant_start_of_day_summary(self):
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/S_B_Participant_Start_of_Day_Summary.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_s_p_fractional_participant_end_of_day_summary(self):
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/S_P_Fractional_Participant_End_of_Day_Summary.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_s_t_fractional_consolidated_end_of_day_summary(self):
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/S_T_Fractional_Consolidated_End_of_Day_Summary.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_t_e_fractional_trade_cancelerror(self):
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/T_E_Fractional_Trade_Cancel-Error.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_t_r_fractional_long_trade(self):
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/T_R_Fractional_Long_Trade.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_t_s_trading_status(self):
        for payload in payloads.of("omi-data-packets/Siac/Cts.Output.Cta.v2.11.b/T_S_Trading_Status.pcap"):
            data = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "payload.bin")
            with open(data, "wb") as handle:
                handle.write(payload)
            result = subprocess.run([DAFFODIL, "parse", "-P", PARSER, data], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
