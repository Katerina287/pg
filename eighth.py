class BinaryNumber:
    def __init__(self, value):
        self.raw_value = value
        self.binary_str = self._normalize(value)

    @staticmethod
    def _normalize(value):
        s = str(value).strip()
        if not s or any(ch not in ("0", "1") for ch in s):
            raise ValueError(f"Neplatné binární číslo: {value}")
        return s

    def to_decimal(self):
        return int(self.binary_str, 2)

    def __int__(self):
        return self.to_decimal()

    def __str__(self):
        return f"BinaryNumber('{self.binary_str}') -> {self.to_decimal()}"


def test_binary_number():
    assert int(BinaryNumber("0")) == 0
    assert int(BinaryNumber(1)) == 1
    assert int(BinaryNumber("100")) == 4
    assert int(BinaryNumber(101)) == 5
    assert int(BinaryNumber("010101")) == 21
    assert int(BinaryNumber(10000000)) == 128


if __name__ == "__main__":
    test_binary_number()
    cislo = BinaryNumber("10011101")
    print(cislo)                 
    print(cislo.to_decimal())   
