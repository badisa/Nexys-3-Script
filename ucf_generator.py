#!/usr/bin/env python

import argparse

NEXYS_MAP = {
    # 7 segment display
    "CA": "NET \"{}\" LOC = \"T17\" | IOSTANDARD = \"LVCMOS33\";   #Bank = 1, Pin name = IO_L51P_M1DQ12, CA",
    "CB": "NET \"{}\" LOC = \"T18\" | IOSTANDARD = \"LVCMOS33\";   #Bank = 1, Pin name = IO_L51N_M1DQ13, CB",
    "CC": "NET \"{}\" LOC = \"U17\" | IOSTANDARD = \"LVCMOS33\";   #Bank = 1, Pin name = IO_L52P_M1DQ14, CC",
    "CD": "NET \"{}\" LOC = \"U18\" | IOSTANDARD = \"LVCMOS33\";   #Bank = 1, Pin name = IO_L52N_M1DQ15, CD",
    "CE": "NET \"{}\" LOC = \"M14\" | IOSTANDARD = \"LVCMOS33\";   #Bank = 1, Pin name = IO_L53P, CE",
    "CF": "NET \"{}\" LOC = \"N14\" | IOSTANDARD = \"LVCMOS33\";   #Bank = 1, Pin name = IO_L53N_VREF, CF",
    "CG": "NET \"{}\" LOC = \"L14\" | IOSTANDARD = \"LVCMOS33\";   #Bank = 1, Pin name = IO_L61P, CG",
    "DP": "NET \"{}\" LOC = \"M13\" | IOSTANDARD = \"LVCMOS33\";   #Bank = 1, Pin name = IO_L61N, DP",

    "AN0": "NET \"{}\" LOC = \"N16\" | IOSTANDARD = \"LVCMOS33\";   #Bank = 1, Pin name = IO_L50N_M1UDQSN, AN0",
    "AN1": "NET \"{}\" LOC = \"N15\" | IOSTANDARD = \"LVCMOS33\";   #Bank = 1, Pin name = IO_L50P_M1UDQS, AN1",
    "AN2": "NET \"{}\" LOC = \"P18\" | IOSTANDARD = \"LVCMOS33\";   #Bank = 1, Pin name = IO_L49N_M1DQ11, AN2",
    "AN3": "NET \"{}\" LOC = \"P17\" | IOSTANDARD = \"LVCMOS33\";   #Bank = 1, Pin name = IO_L49P_M1DQ10, AN3",


    # Leds
    "LD0": "NET \"{}\" LOC = \"U16\" | IOSTANDARD = \"LVCMOS33\";   #Bank = 2, Pin name = IO_L2P_CMPCLK, LD0",
    "LD1": "NET \"{}\" LOC = \"V16\" | IOSTANDARD = \"LVCMOS33\";   #Bank = 2, Pin name = IO_L2N_CMPMOSI, LD1",
    "LD2": "NET \"{}\" LOC = \"U15\" | IOSTANDARD = \"LVCMOS33\";   #Bank = 2, Pin name = IO_L5P, LD2",
    "LD3": "NET \"{}\" LOC = \"V15\" | IOSTANDARD = \"LVCMOS33\";   #Bank = 2, Pin name = IO_L5N, LD3",
    "LD4": "NET \"{}\" LOC = \"M11\" | IOSTANDARD = \"LVCMOS33\";   #Bank = 2, Pin name = IO_L15P, LD4",
    "LD5": "NET \"{}\" LOC = \"N11\" | IOSTANDARD = \"LVCMOS33\";   #Bank = 2, Pin name = IO_L15N, LD5",
    "LD6": "NET \"{}\" LOC = \"R11\" | IOSTANDARD = \"LVCMOS33\";   #Bank = 2, Pin name = IO_L16P, LD6",
    "LD7": "NET \"{}\" LOC = \"T11\" | IOSTANDARD = \"LVCMOS33\";   #Bank = 2, Pin name = IO_L16N_VREF, LD7",


    # Switches
    "SW0": "NET \"{}\" LOC = \"T10\" | IOSTANDARD = \"LVCMOS33\";   #Bank = 2, Pin name = IO_L29N_GCLK2, SW0",
    "SW1": "NET \"{}\" LOC = \"T9\"  | IOSTANDARD = \"LVCMOS33\";   #Bank = 2, Pin name = IO_L32P_GCLK29, SW1",
    "SW2": "NET \"{}\" LOC = \"V9\"  | IOSTANDARD = \"LVCMOS33\";   #Bank = 2, Pin name = IO_L32N_GCLK28, SW2",
    "SW3": "NET \"{}\" LOC = \"M8\"  | IOSTANDARD = \"LVCMOS33\";   #Bank = 2, Pin name = IO_L40P, SW3",
    "SW4": "NET \"{}\" LOC = \"N8\"  | IOSTANDARD = \"LVCMOS33\";   #Bank = 2, Pin name = IO_L40N, SW4",
    "SW5": "NET \"{}\" LOC = \"U8\"  | IOSTANDARD = \"LVCMOS33\";   #Bank = 2, Pin name = IO_L41P, SW5",
    "SW6": "NET \"{}\" LOC = \"V8\"  | IOSTANDARD = \"LVCMOS33\";   #Bank = 2, Pin name = IO_L41N_VREF, SW6",
    "SW7": "NET \"{}\" LOC = \"T5\"  | IOSTANDARD = \"LVCMOS33\";   #Bank = MISC, Pin name = IO_L48N_RDWR_B_VREF_2, SW7",


    # Buttons
    "BTNS": "NET \"{}\" LOC = \"B8\"  | IOSTANDARD = \"LVCMOS33\";   #Bank = 0, Pin name = IO_L33P, BTNS",
    "BTNU": "NET \"{}\" LOC = \"A8\"  | IOSTANDARD = \"LVCMOS33\";   #Bank = 0, Pin name = IO_L33N, BTNU",
    "BTNL": "NET \"{}\" LOC = \"C4\"  | IOSTANDARD = \"LVCMOS33\";   #Bank = 0, Pin name = IO_L1N_VREF, BTNL",
    "BTND": "NET \"{}\" LOC = \"C9\"  | IOSTANDARD = \"LVCMOS33\";   #Bank = 0, Pin name = IO_L34N_GCLK18, BTND",
    "BTNR": "NET \"{}\" LOC = \"D9\"  | IOSTANDARD = \"LVCMOS33\";   #Bank = 0, Pin name = IO_L34P_GCLK19, BTNR",
}


def write_ufc_file():
    parser = argparse.ArgumentParser(
        description="UCF Generating script for NEXYS Board"
    )
    parser.add_argument(
        "-name",
        default=5000,
        required=True,
        help="Name of ufc file"
    )
    parser.add_argument(
        "-i",
        "--input",
        nargs=2,
        required=True,
        action="append",
        help="Input map (i.e -i 'A SW0' -i 'B SW1')"
    )
    parser.add_argument(
        "-o",
        "--output",
        nargs=2,
        action="append",
        required=True,
        help="Output map (i.e -o 'F LD0' -o 'K LD1')"
    )
    args = parser.parse_args()
    output_file = "{}.ucf".format(args.name)
    with open(output_file, "w") as ufc:
        ufc.write("## Inputs\n")
        for arg in args.input:
            input_port = tuple(arg)
            ufc.write(NEXYS_MAP[input_port[1]].format(input_port[0]))
            ufc.write('\n')

        ufc.write("\n## Outputs\n")
        for arg in args.output:
            output_port = tuple(arg)
            ufc.write(NEXYS_MAP[output_port[1]].format(output_port[0]))
            ufc.write('\n')
    print("Wrote ucf file to '{}'".format(output_file))

if __name__ == "__main__":
    write_ufc_file()
