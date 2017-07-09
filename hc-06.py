#!/bin/python3

import serial
import sys

def print_usage():
    print('Missing arguments!\n')
    print('Usage: hc-06.py port command')
    print('\n\nCommands')
    print('\tversion    \tPrints out the firmware version')
    print('\tname <name>\tSets the device name to <name>\n')

if len(sys.argv) < 3:
    print_usage()
    exit(1)

dev = sys.argv[1]
command = sys.argv[2]

if command == 'name':
    if len(sys.argv) < 4:
        print_usage()
        exit(1)

    con = serial.Serial(port=dev, baudrate=9600, timeout=1)
    data = 'AT+NAME' + sys.argv[3]
    con.write(data.encode('ascii'))
    print(con.readline())

elif command == 'version':
    con = serial.Serial(port=dev, baudrate=9600, timeout=1)
    con.write('AT+VERSION'.encode('ascii'))
    con.flush()
    print(con.readline())

else:
    print_usage()
    exit(1)
