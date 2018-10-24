import pytest
from four_format import Four_format


class Test_four_format:
    def set_up_string(self, string, number):
        string = string.format(Four_format(number))
        string = string.replace(" ", "")
        return string

    def test_binary_format(self):
        string = "{:08b}"
        for i in range(0xff):
            assert "0b" + string.format(i) == self.set_up_string(string, i)

    def test_hex_format(self):
        string = "{:04x}"
        for i in range(0xff):
            assert "0x" + string.format(i) == self.set_up_string(string, i)

    def test_correct_behavior(self):
        assert "0b1010 1101" == "{:08b}".format(Four_format(173))
        assert "0x0000 0000 dead beef" == "{:016x}".format(Four_format(0xdeadbeef))
        assert "0b0000 0000 0000 1011" == "{:016b}".format(Four_format(0xb))
        assert "0b001 0101" == "{:07b}".format(Four_format(0x15))
