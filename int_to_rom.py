
def int_to_rom(N_int):
    rom_int_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rom_int_map_inverse = {v: k for k, v in rom_int_map.items()}
    int_for_rom_num_all = [k for k in rom_int_map.values()]

    # validation
    assert isinstance(N_int, int), f'{N_int} is incorrect - must be an integer'
    assert 1 <= N_int <= 3999, f'{N_int} is incorrect - must be between 1 and 3999'

    # decomposition_dict = {}
    N_rom = ''
    N_int_rest = N_int
    for i, d in enumerate(int_for_rom_num_all[::-1]):
        div_int = N_int_rest // d
        if div_int > 0:
            if div_int < 4:
                N_rom += rom_int_map_inverse[d] * div_int
            else:
                d_pred = int_for_rom_num_all[::-1][i - 1]
                N_rom += rom_int_map_inverse[d] + rom_int_map_inverse[d_pred]
            # decomposition_dict[d] = div_int
            N_int_rest -= d * div_int

    # correct 9's - case of 'DCD' -> 'CM'
    N_rom_upd = N_rom
    if len(N_rom) >= 3:
        for i in range(2, len(N_rom)):
            a0 = N_rom[i - 2]
            a1 = N_rom[i - 1]
            a2 = N_rom[i]
            if (a0 != a1) and (a0 == a2):
                a0_int = rom_int_map[a0]
                a0_int_idx = int_for_rom_num_all.index(a0_int)
                a0_int_idx += 1
                a0_int = int_for_rom_num_all[a0_int_idx]
                a0_rom_upd = rom_int_map_inverse[a0_int]
                # update roman number with 9s case:
                N_rom_upd = N_rom_upd.replace(a0 + a1 + a2, a1 + a0_rom_upd)

    return N_rom_upd

# UNIT TEST:
def test_int_to_rom():
    ys = [1, 123, 325, 436, 628, 500, 3999, 5555, 'asdf']
    for y in ys:
        try:
            print(y, int_to_rom(y))
        except Exception as e:
            print(e)

if __name__ == '__main__':
    test_int_to_rom()