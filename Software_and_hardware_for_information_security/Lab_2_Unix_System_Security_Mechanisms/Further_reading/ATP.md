# Hướng dẫn sử dụng lệnh apt trên Linux


## 1. Giới thiệu
APT sử dụng trên các hệ điều hành phân phối dựa trên Debian hoặc Debian-based như Ubuntu hoặc Linux Mint

**APT**, là từ viết tắt củaAdvanced Package Tool là một công cụ quản lý gói dành cho hệ thống Debian. Công cụ APT giúp người dùng thực hiện nhiều tác vụ khác nhau bao gồm cài đặt, cập nhật, nâng cấp và gỡ bỏ các gói phần mềm trên hệ điều hành.

Khi sử dụng công cụ APT, đôi khi sẽ yêu cầu người dùng nhập ‘Y‘(viết tắt của Yes) để tiến hành thao tác như cài đặt hoặc gỡ bỏ một gói.

Trên các bản phân phối dựa trên Debian/Ubuntu cũ hơn, apt-get đã được sử dụng. Trong các phiên bản mới hơn như Ubuntu 18.04/20.04 trở lên và Debian 10/Mint 20 lệnh apt sẽ thay thế cho lệnh apt-get cũ kỹ trên các phiên bản trước đó và nó hoàn toàn tương thích ngược với apt-get.

## 2. Cách sử dụng

### 2.1 Cập nhật chỉ mục cho APT

Trong hệ thống sử dụng Debian/Ubuntu, kho lưu trữ được chỉ định trong tệp tin `/etc/apt/sources.list`. Chỉ mục gói APT là cơ sở dữ liệu của tất cả các gói được xác định trong tệp này. Bạn nên cập nhật chỉ mục gói APT trên hệ thống để đồng bộ hóa các thay đổi được thực hiện trong kho lưu trữ. Điều này đặc biệt quan trọng sau khi cài đặt hệ thống mới và trước khi cài đặt các gói tin mới.

Để cập nhật cơ sở dữ liệu APT các bạn hãy chạy lệnh sau:

```bash
sudo apt update -y
```
### 2.2 Nâng cấp gói bằng lệnh APT

Lệnh `apt update -y` được đề cập ở trên sẽ không cài đặt hoặc nâng cấp bất kỳ gói nào. Vì vậy, sau khi chạy lệnh trên, bạn sẽ biết được các gói nào cần cập nhật.

Nếu bạn muốn cập nhật toàn bộ các gói đã cài đặt lên phiên bản mới nhất thì các bạn cần chạy lệnh sau:

```bash
sudo apt upgrade
```

Để nâng cấp một gói riêng lẻ, hãy sử dụng lệnh sau, trong đó `package-name` chính là tên gói bạn cần nâng cấp:

```bash
sudo apt upgrade package-name
```

### 2.3 Nâng cấp đầy đủ và nâng cấp phiên bản

Trường hợp bản muốn có một nâng cấp đầy đủ và loại bỏ một số gói không còn cần cần thiết để hoàn toàn nâng cấp hệ thống thì các bạn sử dụng lệnh sau:

```bash
sudo apt full-upgrade
```

Ngoài lệnh trên thì chúng ta vẫn có lệnh sau để nâng cấp toàn bộ các gói ít quan trọng hơn:

```bash
sudo apt dist-upgrade
```

**Cách nâng cấp phiên bản của hệ điều hành**

 Ví dụ từ phiên bản Ubuntu 19.04 lên Ubuntu 20.04.

 Tuy nhiên để an toàn, trước khi chạy lệnh này, bạn phải đảm bảo chạy hai lệnh trên trước nhé:

 ```bash
do-release-upgrade
```

Như vậy quy trình sẽ là `sudo apt upgrade` sau đó `sudo apt dist-upgrade` và cuối cùng chạy `sudo apt do-release-upgrade`.


### 2.4 Cài đặt một gói phần mềm

Để cài đặt một gói trên hệ thống của bạn, hãy sử dụng lệnh apt như sau:

```bash
sudo apt install package-name
```

Ví dụ ở đây mình sẽ cài gói nload thì mình sử sử dụng lệnh sudo apt install nload.


```bash
$ sudo apt install nload
[sudo] password for chu: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  asymptote asymptote-doc biber context fonts-arphic-bkai00mp fonts-arphic-bsmi00lp fonts-arphic-gbsn00lp fonts-arphic-gkai00mp fonts-baekmuk
  fonts-gfs-baskerville fonts-gfs-bodoni-classic fonts-gfs-didot-classic fonts-gfs-gazis fonts-gfs-porson fonts-gfs-theokritos fonts-hosny-amiri
  fonts-unfonts-core fonts-unfonts-extra latex-cjk-all latex-cjk-chinese latex-cjk-chinese-arphic-bkai00mp latex-cjk-chinese-arphic-bsmi00lp
  latex-cjk-chinese-arphic-gbsn00lp latex-cjk-chinese-arphic-gkai00mp latex-cjk-common latex-cjk-japanese latex-cjk-japanese-wadalab latex-cjk-korean
  latex-cjk-thai libautovivification-perl libbtparse2 libbusiness-ismn-perl libbusiness-issn-perl libclass-accessor-perl libclass-inspector-perl
  libclass-singleton-perl libdata-compare-perl libdata-uniqid-perl libdate-simple-perl libdatetime-calendar-julian-perl libdatetime-format-builder-perl
  libdatetime-format-strptime-perl libdatetime-locale-perl libdatetime-perl libdatetime-timezone-perl libencode-eucjpms-perl libencode-jis2k-perl
  libfile-find-rule-perl libfile-sharedir-perl libfile-slurper-perl libgsl27 libgslcblas0 libipc-run3-perl liblingua-translit-perl
  liblist-allutils-perl liblist-someutils-perl liblist-someutils-xs-perl liblist-utilsby-perl libnumber-compare-perl libosp5 libostyle1c2
  libparams-validate-perl libparse-recdescent-perl libperlio-utf8-strict-perl libqt5script5 libqt5scripttools5 libregexp-common-perl libsigsegv2
  libsort-key-perl libtext-bibtex-perl libtext-csv-perl libtext-csv-xs-perl libtext-glob-perl libtext-roman-perl libtext-unidecode-perl
  libtie-cycle-perl libxml-libxml-simple-perl libxml-libxslt-perl libxml-writer-perl openjade teckit texinfo texlive-bibtex-extra texlive-formats-extra
  texlive-games texlive-humanities texlive-humanities-doc texlive-lang-arabic texlive-lang-chinese texlive-lang-cjk texlive-lang-cyrillic
  texlive-lang-czechslovak texlive-lang-english texlive-lang-european texlive-lang-french texlive-lang-german texlive-lang-greek texlive-lang-italian
  texlive-lang-japanese texlive-lang-korean texlive-lang-other texlive-lang-polish texlive-lang-portuguese texlive-lang-spanish texlive-music
  texlive-publishers texlive-publishers-doc texlive-science texlive-science-doc texlive-xetex
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed:
  nload
0 upgraded, 1 newly installed, 0 to remove and 65 not upgraded.
Need to get 55,1 kB of archives.
After this operation, 173 kB of additional disk space will be used.
Get:1 http://ru.archive.ubuntu.com/ubuntu jammy/universe amd64 nload amd64 0.7.4-2build3 [55,1 kB]
Fetched 55,1 kB in 2s (30,8 kB/s)                         
Selecting previously unselected package nload.
(Reading database ... 596020 files and directories currently installed.)
Preparing to unpack .../nload_0.7.4-2build3_amd64.deb ...
Unpacking nload (0.7.4-2build3) ...
Setting up nload (0.7.4-2build3) ...
Processing triggers for man-db (2.10.2-1) ...
```




[Bài viết tham khảo tại](https://azdigi.com/blog/linux-server/linux-can-ban/lenh-apt-tren-linux-ubuntu-debian/)
