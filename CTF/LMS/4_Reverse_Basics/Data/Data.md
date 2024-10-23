Tải file Data về

---
Cài các công cụ cần thiết trên ubuntu:

```bash
sudo apt update
sudo apt install binutils gdb strings
```
----
Sử dung lệnh strings

```bash
strings Data | less
```
---
Kết quả sẽ hiện ra như sau:

```bash
/lib64/ld-linux-x86-64.so.2
e>pe
mgUa
__cxa_finalize
fgets
__libc_start_main
puts
strlen
stdin
libc.so.6
GLIBC_2.2.5
GLIBC_2.34
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
PTE1
u+UH
FLAG{y0u_f0und_m3_q7gt04r320}
Enter secret
Nope
Close
Almost there
Wrong!
;*3$"
GCC: (Debian 13.2.0-23) 13.2.0
Scrt1.o
__abi_tag
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.0
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
Data.c
__FRAME_END__
_DYNAMIC
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_start_main@GLIBC_2.34
_ITM_deregisterTMCloneTable
puts@GLIBC_2.2.5
stdin@GLIBC_2.2.5
_edata
_fini
strlen@GLIBC_2.2.5
fgets@GLIBC_2.2.5
__data_start
__gmon_start__
__dso_handle
FLAG
_IO_stdin_used
_end
__bss_start
:
```
--- 
fag chính là:

```bash
FLAG{y0u_f0und_m3_q7gt04r320}
```

