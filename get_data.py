# Import necessary modules for creating dataset
import circuitgraph as cg
from logiclocking import locks, write_key, read_key
from logiclocking import attacks
from tqdm import tqdm

# from parse_netlist import jeff_fun

def main():
    attack_miter('MKR532xz_final_netlist.v', 'output_test.txt', 2, 'xor_lock', 10)
    return

def attack_miter(infile, outfile, numgates, lock, iterations):
    # determine locking to use, and catch improper locking method
    lock_types = ['xor_lock', 'mux_lock', 'random lut lock', 'lut_lock', 'tt_lock', 'sfll_hd']
    if lock not in lock_types: exit('Lock not found.')

    # setup locking and output file
    outstr = lock + ' ' + infile + ' ' + 'x_gates,' + str(iterations) + ' iterations'
    f = open(outfile, 'w')
    f.write(outstr + '\nIteration, attack time\n')

    # grab the correct file
    c = cg.from_file(infile)
    num_keys = 32

    # correctly lock and attack file############################################
    if lock_types.index(lock) == 0:
        print('Attacking xor_locked', infile, 'with miter attack.')
        c1, k = locks.xor_lock(c, num_keys)
        for i in tqdm(range(0, iterations)):
            result = attacks.miter_attack(c1, k, verbose=False, code_on_error=True)
            time   = result['Time']

            write_str = str(i) + ', ' + str(time)
            f.write(write_str)
            f.write('\n')
        print('Done, output written to ', outfile)

    if lock_types.index(lock) == 1:
        print('Attacking mux_locked', infile, 'with miter attack.')
        c1, k = locks.mux_lock(c, num_keys)
        for i in tqdm(range(0, iterations)):
            result = attacks.miter_attack(c1, k, verbose=False, code_on_error=True)
            time   = result['Time']

            write_str = str(i) + ', ' + str(time)
            f.write(write_str)
            f.write('\n')
        print('Done, output written to ', outfile)

    if lock_types.index(lock) == 2:
        print('Attacking random_lut_locked', infile, 'with miter attack.')
        c1, k = locks.random_lut_lock(c, num_keys, lut_width = 4)
        for i in tqdm(range(0, iterations)):
            result = attacks.miter_attack(c1, k, verbose=False, code_on_error=True)
            time   = result['Time']

            write_str = str(i) + ', ' + str(time)
            f.write(write_str)
            f.write('\n')
        print('Done, output written to ', outfile)

    if lock_types.index(lock) == 3:
        print('Attacking lut_locked', infile, 'with miter attack.')
        c1, k = locks.lut_lock(c, num_keys)
        for i in tqdm(range(0, iterations)):
            result = attacks.miter_attack(c1, k, verbose=False, code_on_error=True)
            time   = result['Time']

            write_str = str(i) + ', ' + str(time)
            f.write(write_str)
            f.write('\n')
        print('Done, output written to ', outfile)

    if lock_types.index(lock) == 4:
        print('Attacking tt_locked', infile, 'with miter attack.')
        c1, k = locks.tt_lock(c, num_keys)
        for i in tqdm(range(0, iterations)):
            result = attacks.miter_attack(c1, k, verbose=False, code_on_error=True)
            time   = result['Time']

            write_str = str(i) + ', ' + str(time)
            f.write(write_str)
            f.write('\n')
        print('Done, output written to ', outfile)

    if lock_types.index(lock) == 5:
        print('Attacking sfll_hd_locked', infile, 'with miter attack.')
        c1, k = locks.sfll_hd(c, num_keys, hd=8)
        for i in tqdm(range(0, iterations)):
            result = attacks.miter_attack(c1, k, verbose=False, code_on_error=True)
            time   = result['Time']

            write_str = str(i) + ', ' + str(time)
            f.write(write_str)
            f.write('\n')
        print('Done, output written to ', outfile)
    f.close()

if __name__ == "__main__":
    main()
