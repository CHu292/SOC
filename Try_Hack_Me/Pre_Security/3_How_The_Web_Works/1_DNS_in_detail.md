# DNS in detail

> Chi tiết về DNS: Tìm hiểu cách DNS hoạt động và cách nó hỗ trợ bạn truy cập các dịch vụ trên Internet.## Mục Lục

## Mục lục

1. [Task 1: What is DNS?](#task-1-what-is-dns)  
2. [Task 2: Domain Hierarchy](#task-2-domain-hierarchy)  
3. [Task 3: Record Types](#task-3-record-types)  
4. [Task 4: Making A Request](#task-4-making-a-request)  
5. [Task 5: Practical](#task-5-practical)

## Nội dung

# Task 1: What is DNS?

### DNS là gì?

**DNS (Domain Name System)** cung cấp một cách đơn giản để chúng ta giao tiếp với các thiết bị trên Internet mà không cần nhớ những con số phức tạp. Giống như mỗi ngôi nhà có một địa chỉ duy nhất để gửi thư trực tiếp, mỗi máy tính trên Internet cũng có một địa chỉ duy nhất để giao tiếp, được gọi là **địa chỉ IP**.  

Một địa chỉ IP trông như sau: **104.26.10.229**, bao gồm 4 nhóm số trong khoảng từ **0 - 255**, được ngăn cách bằng dấu chấm. Khi bạn muốn truy cập một trang web, việc nhớ một dãy số phức tạp như vậy không hề thuận tiện, và đó là lúc **DNS** giúp ích.  

Thay vì phải nhớ **104.26.10.229**, bạn chỉ cần nhớ **tryhackme.com**.
