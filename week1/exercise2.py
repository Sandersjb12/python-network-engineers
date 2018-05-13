#!/usr/bin/env python

#2. Prompt a user to enter in an IP address from standard input. Read the IP address in and break it up into its octets. Print out the octets in decimal, binary, and hex.
#
#Your program output should look like the following:
#
#$ python exercise2.py 
#Please enter an IP address: 80.98.100.240
#
#    Octet1         Octet2         Octet3         Octet4     
#------------------------------------------------------------
#      80             98             100            240      
#   0b1010000      0b1100010      0b1100100     0b11110000   
#     0x50           0x62           0x64           0xf0      
#------------------------------------------------------------
#
#
#Four columns, fifteen characters wide, a header column, data centered in the column.

from __future__ import print_function, unicode_literals
 
try:
    ip_addr = raw_input("Enter an IP address: ")
except NameError:
    ip_addr = input("Enter an IP address: ")

octets_str=ip_addr.split('.')

octets=[0,0,0,0]

octets[0]=int(octets_str[0])
octets[1]=int(octets_str[1])
octets[2]=int(octets_str[2])
octets[3]=int(octets_str[3])

print("{:^15}{:^15}{:^15}{:^15}".format("Octet1", "Octet2", "Octet3", "Octet4"))
print("-" * 60)
print("{:^15}{:^15}{:^15}{:^15}".format(*octets))
print("{:^15}{:^15}{:^15}{:^15}".format(bin(octets[0]),bin(octets[1]),bin(octets[2]),bin(octets[3])))
print("{:^15}{:^15}{:^15}{:^15}".format(hex(octets[0]),hex(octets[1]),hex(octets[2]),hex(octets[3])))
print('-' * 60)

