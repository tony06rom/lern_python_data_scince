import getpass
import sys
import telnetlib

telnet = telnetlib.Telnet('172.16.12.30')
telnet.read_until(b'Password')
b': cisco\r\nPassword'

telnet.write(b'cisco\n')