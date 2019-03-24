# Nội dung tuần 3: 
##Trọng tâm của tuần này sẽ là về kĩ thuật lập trình hướng đối tượng và nguyên lí SOLID, tuy nhiên sẽ có thêm 1 vài chi tiết nhỏ như thiết kế giao diện web để có cái nhìn về 1 phần mềm rõ ràng hơn.

## Để mô ta rõ ràng hơn, ta sẽ sử dụng folder env để khởi tạo các thư viện, và modules cho việc xử lý chức năng cho các thư viện đó.

## Cài đặt thư viện ảo để có thể truyền thư viện cho những người chưa cài đặt vẫn có thể chạy được
1. Đầu tiên cài đặt thư viện này trên hệ thống của máy tính của mình và cài đặt thư viện virtualenv
```python
pip install virtualenv
```
2. Vào Folder chính và bật CMD ngay tại đây, tiếp tục gõ lệnh
```python
virtualenv python3 ./venv
```
3. Từ đây bạn sẽ thấy trong folder chính của mình sẽ xuất hiện 1 folder "venv", tiếp theo ta kích họat folder này. Tiếp tục viết lệnh dưới đây trong CMD ở thư mục chính.
```python
.\venv\Script\activate
```
Vậy là đã kích hoạt xong thư viện ảo trong Folder chính của bạn, từ giờ khi cài đặt thư viện bằng cmd trong folder chính thì nó sẽ được cài đặt vào trong folder venv này. Khi bạn di chuyển toàn bộ Folder chính sang 1 máy tính khác thì vẫn còn sử dụng được những thư viện này dù máy tính đó chưa cài đặt.
