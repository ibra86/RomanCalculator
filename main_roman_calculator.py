
from rom_to_int import rom_to_int
from int_to_rom import int_to_rom

def sum_roman(A, B):
    try:
        a = rom_to_int(A)
        b = rom_to_int(B)

        return int_to_rom(a + b)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    assert sum_roman('III', 'II') == "V"
    assert sum_roman("V", "V") == "X"
    print('done')