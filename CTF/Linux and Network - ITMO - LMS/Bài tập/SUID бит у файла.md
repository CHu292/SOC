# SUID бит у файла
Найти файл с установленным suid битом. Обязательно погуглите про SUID.

## cách làm
```
root@db5753c3b3de:~# find / -type f -perm /4000 -ls 2>/dev/null
   935081      4 -rwsrwSrw-   1 root     root          118 Oct  6 17:09 /home/files/file4.sh
 22312757     52 -rwsr-xr-x   1 root     root        53040 Feb  6  2024 /usr/bin/chsh
 22312979     40 -rwsr-xr-x   1 root     root        39144 May 30  2023 /usr/bin/umount
 22312875     56 -rwsr-xr-x   1 root     root        55528 May 30  2023 /usr/bin/mount
 22312880     44 -rwsr-xr-x   1 root     root        44784 Feb  6  2024 /usr/bin/newgrp
 22312954     68 -rwsr-xr-x   1 root     root        67816 May 30  2023 /usr/bin/su
 22312818     88 -rwsr-xr-x   1 root     root        88464 Feb  6  2024 /usr/bin/gpasswd
 22312891     68 -rwsr-xr-x   1 root     root        68208 Feb  6  2024 /usr/bin/passwd
 22312751     84 -rwsr-xr-x   1 root     root        85064 Feb  6  2024 /usr/bin/chfn
root@db5753c3b3de:~# cmod 7777 /home/files/file4.sh 
root@db5753c3b3de:~# cd /home/files     
root@db5753c3b3de:/home/files# ./file4.sh 
198cb66cf51f7d0a96cd262f1aaed14f6fa84360dcd01c8b27aea70b777fe561dc99fcb6806b594e6d545fc9621ccce5c7
root@db5753c3b3de:/home/files# ```
