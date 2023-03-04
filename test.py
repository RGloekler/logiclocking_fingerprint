# Ryan Gloekler
# EEC 289Q -- Homework #2
# logic locking of netlists using python
import circuitgraph as cg
from logiclocking import locks, write_key, read_key
from logiclocking import attacks

#c = cg.from_file("MKR532xz_final_netlist.v")
c = cg.from_lib("c880")
num_keys = 32

c1, k = locks.xor_lock(c, num_keys)
result = attacks.miter_attack(c1, k, verbose=False, code_on_error=True)

print('Results: xor_lock')
print(result['Time'], end='\n\n')

cg.to_file(c1, "locked_netlist_XOR.v")
write_key(k, "locked_netlist_KEY_XOR.txt")

#################################################
c1, k = locks.mux_lock(c, num_keys)
result = attacks.miter_attack(c1, k, verbose=False, code_on_error=True)

print('Results: mux lock')
print(result['Time'], end='\n\n')

cg.to_file(c1, "locked_netlist_mux.v")
write_key(k, "locked_netlist_KEY_mux.txt")

###################################################
c1, k = locks.random_lut_lock(c, num_keys, lut_width = 4)
result = attacks.miter_attack(c1, k, verbose=False, code_on_error=True)

print('Results: random_lut_lock')
print(result['Time'], end='\n\n')

cg.to_file(c1, "locked_netlist_random_lut.v")
write_key(k, "locked_netlist_KEY_random_lut.txt")

###################################################
c1, k = locks.lut_lock(c, num_keys)
result = attacks.miter_attack(c1, k, verbose=False, code_on_error=True)

print('Results: lut_lock')
print(result['Time'], end='\n\n')

cg.to_file(c1, "locked_netlist_lut.v")
write_key(k, "locked_netlist_KEY_lut.txt")

###################################################
c1, k = locks.tt_lock(c, num_keys)
result = attacks.miter_attack(c1, k, verbose=False, code_on_error=True)

print('Results: tt_lock')
print(result['Time'], end='\n\n')

cg.to_file(c1, "locked_netlist_tt_lock.v")
write_key(k, "locked_netlist_KEY_tt_lock.txt")

###################################################
c1, k = locks.sfll_hd(c, num_keys, hd=8)
result = attacks.miter_attack(c1, k, verbose=False, code_on_error=True)

print('Results: sfll_hd')
print(result['Time'], end='\n\n')

cg.to_file(c1, "locked_netlist_sfll_hd.v")
write_key(k, "locked_netlist_KEY_sfll_hd.txt")

print('done')
