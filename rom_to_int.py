def rom_to_int(N_rom_str):
    N_rom_str = N_rom_str.upper() if isinstance(N_rom_str, str) else N_rom_str

    rom_int_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rom_num_all = [k for k in rom_int_map]

    # validation of roman number
    case_valid_0 = not isinstance(N_rom_str, str)
    if case_valid_0:
        raise Exception(f'Not valid roman number \'{N_rom_str}\' (not a string)')

    case_valid_1 = any([(k not in rom_num_all) for k in N_rom_str])  # smth is not roman number
    if case_valid_1:
        raise Exception(f'Not valid roman number \'{N_rom_str}\' (not a fully roman string)')

    case_valid_2 = any([(f in N_rom_str) for f in ('VV', 'LL', 'DD')])  # double 5's
    if case_valid_2:
        raise Exception(f'Not valid roman number \'{N_rom_str}\' (not permissible pairs encountered)')

    def valid_triples(N_rom_str):
        if len(N_rom_str) >= 3:
            for i in range(2, len(N_rom_str)):
                a0 = rom_int_map[N_rom_str[i - 2]]
                a1 = rom_int_map[N_rom_str[i - 1]]
                a2 = rom_int_map[N_rom_str[i]]
                # fail cases:
                return ((a0 < a1) and (a1 > a2)) or \
                       ((a0 <= a1) and (a1 < a2)) or \
                       ((a0 < a1) and (a1 <= a2))
        else:
            return False

    case_valid_3 = valid_triples(N_rom_str)
    if case_valid_3:
        raise Exception(f'Not valid roman number \'{N_rom_str}\' (not permissible triples encountered)')

    # implementation
    N_int = 0
    for i in range(len(N_rom_str)):
        if i == 0:
            N_int += rom_int_map[N_rom_str[i]]
        else:
            if rom_int_map[N_rom_str[i - 1]] < rom_int_map[N_rom_str[i]]:
                N_int += rom_int_map[N_rom_str[i]] - 2 * rom_int_map[N_rom_str[i - 1]]
            else:
                N_int += rom_int_map[N_rom_str[i]]
    return N_int


# UNIT-TEST:
def test_rom_to_int():
    xs = ['III','X', 'IX', 'MCMX', 'xiv', 'asdf', 123, 'XLX', 'XXL', 'LLX', 'CCX']
    for x in xs:
        try:
            print(x, rom_to_int(x))
        except Exception as e:
            print(e)

if __name__ == '__main__':
    test_rom_to_int()