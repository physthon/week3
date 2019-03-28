
# Nội dung tuần 3: 
##  Trọng tâm của tuần này sẽ là về kĩ thuật lập trình hướng đối tượng và nguyên lí SOLID, tuy nhiên sẽ có thêm 1 vài chi tiết nhỏ như thiết kế giao diện web để có cái nhìn về 1 phần mềm rõ ràng hơn.
### 1. Single Responsibility Principle
- Một class chỉ nên giữ một trách nhiệm duy nhất
### 2. Open/Closed Principle
- Có thể mở rộng một class, nhưng không được sửa đổi nội dung bên trong class đó.
### 3. Liskov Substitution Principle
- Trong 1 chương trình, các object của một class con có thể thay thế class cha mà không làm thay đổi tính đúng đắn của chương trình.
### 4. Interface Segregation Principle
- Thay vì dùng một interface lớn, ta nên tách thành nhiều interface nhỏ với mục đích rõ ràng.
### 5. Dependency Inversion Principle
1. Các module cấp cao không nên phụ thuộc vào các module cấp thấp. Các module nên phụ thuộc vào abstraction.
2. Interface(abstraction) không nên phụ thuộc vào chi tiết, mà ngược lại.
## Để mô ta rõ ràng hơn, ta sẽ sử dụng folder env để khởi tạo các thư viện, và modules cho việc xử lý chức năng cho các thư viện đó.
1. Folder 'templates' sẽ chứa giao diện và file hướng dẫn sử dụng Bootstrap và nhúng bootstrap bằng visual studio code.
2. Folder 'env' sẽ trực tiếp chứa các Interface.
3. Folder 'modules' sẽ chứa các file xử lý.
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
