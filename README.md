# pwnable.tw_dubblesort

주어진 leak을 이용해 libc 릭!
one_gadget 조건이 복잡하므로 system("/bin/sh")활용
scanf("%u", )에서 숫자가 아닌 값이 들어갈 때, 실패함으로써 아무 값이 써지지 않음을 이용한다

위치 잘 조정해서 카나리는 그대로 두고 return address와 return address+8에 system("/bin/sh")


<TIP>
export LD_PRELOAD=./libc.so.6
p=process(“chall”,env={“LD_PRELOAD”:”./libc”})
