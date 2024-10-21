```bash
chmod +x task_elf
```

```bash
gdb ./task_elf
```

```gdb
chu@chu-Latitude-5510:~/Downloads$ gdb ./task_elf
GNU gdb (Ubuntu 12.1-0ubuntu1~22.04.2) 12.1
Copyright (C) 2022 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./task_elf...
(No debugging symbols found in ./task_elf)
(gdb) break strncmp
Breakpoint 1 at 0x401030
(gdb) run
Starting program: /home/chu/Downloads/task_elf 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Enter password
1234

Breakpoint 1, strncmp_ifunc () at ../sysdeps/x86_64/multiarch/strncmp.c:66
66	../sysdeps/x86_64/multiarch/strncmp.c: No such file or directory.
(gdb) print (char*) $rdi
$1 = 0x0
(gdb) print (char*) $rsi
$2 = 0x1 <error: Cannot access memory at address 0x1>
(gdb) break *0x401030
Breakpoint 2 at 0x401030
(gdb) run
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/chu/Downloads/task_elf 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Enter password
1234

Breakpoint 2, 0x0000000000401030 in strncmp@plt ()
(gdb) print (char*) $rdi
$3 = 0x407ac0 "1234"
(gdb) print (char*) $rsi
$4 = 0x7fffffffde36 "75b744f57178eeb0c5f6996f4fd3c40e46868be38ff4d5b669e47c34ffc8da88d292f34ee7348abe313681a536467a2003eu"
(gdb) 
```
Ten ten vậy là tìm được flag roài

