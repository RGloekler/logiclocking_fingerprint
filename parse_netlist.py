# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#!pip install git+https://github.com/circuitgraph/logiclocking
#!pip install python-sat
#!pip install scikit-learn

import circuitgraph as cg
from logiclocking import locks, write_key, read_key
from logiclocking import attacks
import pandas as pd
import pysat
# def what do i want to do: read it in a netlist, collect the number of gates, and then 

def format_netlist(Random_netlist):
  c = cg.from_file(Random_netlist)
  cg.to_file(c, "processed_netlist.v")
  # first, read everything from the old file
  text = open("processed_netlist.v", 'rt').read()

  # remove the module name
  first, rest = text.split(';',1)
  
  #instantiate headers for pandas
  headers = "nan1 nan2 type name input1 input2 input3 input4 input5 input6 input7 input8 input9 input10\n"

  netlist_extracted = headers + rest;
  # make a new file and write the rest
  open("output.txt", 'wt').write(netlist_extracted)

  df = pd.read_csv("output.txt", sep=" ")
  df_values = df.type.value_counts()
  
  return df

def parse_netlist_for_gate(df, name_of_file):
    df_values = df.type.value_counts()
    df_values = df_values.to_frame()
    df_values.index.name = 'wire_type'
    df_values= df_values.drop(index=["input", "output", "wire"])
    df_values = df_values.rename(columns= { 'type':name_of_file})
    total_gates = df_values[name_of_file].sum();
    sum_row = pd.Series({name_of_file:total_gates}, name="total_gates");
    df_values = df_values.append(sum_row)
    df_values_T = df_values.T
    return df_values.T

   # ser1 = df_values.squeeze()
   # print(ser1["not"])
    
#### Choose File here
c = cg.from_file("MKR532xz_final_netlist.v")
num_keys = 32

############
c = cg.from_file("MKR532xz_final_netlist.v")
num_keys = 32
c1, k = locks.sfll_hd(c, num_keys, 1)
result = attacks.miter_attack(c1, k, verbose=False, code_on_error=True)
cg.to_file(c1, "locked_netlist_sfll_lock_trial1.v")
df = format_netlist("locked_netlist_sfll_lock_trial1.v")
df2 = parse_netlist_for_gate(df,"locked_netlist_sfll_lock_trial1.v");

num_keys = 32
c1, k = locks.sfll_hd(c, num_keys, 1)
result = attacks.miter_attack(c1, k, verbose=False, code_on_error=True)
cg.to_file(c1, "locked_netlist_sfll_lock_trial2.v")
df = format_netlist("locked_netlist_sfll_lock_trial2.v")
df3 = parse_netlist_for_gate(df,"locked_netlist_sfll_lock_trial1.v");

num_keys = 32
c1, k = locks.xor_lock(c, num_keys)
result = attacks.miter_attack(c1, k, verbose=False, code_on_error=True)
cg.to_file(c1, "locked_netlist_xor_lock_trial1.v")
df = format_netlist("locked_netlist_xor_lock_trial1.v")
df5 = parse_netlist_for_gate(df,"locked_netlist_xor_lock_trial1.v");

num_keys = 32
c1, k = locks.xor_lock(c, num_keys)
result = attacks.miter_attack(c1, k, verbose=False, code_on_error=True)
cg.to_file(c1, "locked_netlist_xor_lock_trial2.v")
df = format_netlist("locked_netlist_xor_lock_trial2.v")
df7 = parse_netlist_for_gate(df,"locked_netlist_xor_lock_trial1.v");

df = format_netlist("MKR532xz_final_netlist.v")
df6= parse_netlist_for_gate(df,"MKR532xz_final_netlist.v");


pieces = ( df2, df3, df5, df6, df7)
df_final = pd.concat(pieces)

