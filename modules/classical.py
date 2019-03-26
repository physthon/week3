from mechanic.mechanic import Mechanic
#   Class Classical được tạo ra để mô tả hệ cơ học vật lý cổ điển. Ở lớp cha là Mechanic thì ta đã khai báo
# một loạt các phương thức ảo để mô tả được các tính chất của 1 hệ cơ học là hàm Lagrange, hàm Hamilton, các
# năng lượng của hệ, ... Các phương thức này chủ yếu để xuất ra 1 hàm trạng thái của hệ chứ không hề có giá trị
# cụ thế nảo cả. Các giá trị nhận được vẫn từ các phương thức get().
#
#   Ngoài ra ta cũng thêm vào các phương thức và thuộc tính mới như Lực(Force), thế năng, động năng để biểu
# diễn năng lượng của hệ 1 cách rõ ràng.
#
#   Các bài toán vật lý sẽ không được xây dựng trong Class Classical này, Vì tính chất 'S' trong nguyên lý
# SOLID thì class Classical chỉ mô tả trạng thái của một hệ cơ học cổ điển tồn tại.


class Classical(Mechanic):
    #   Vì trong ngôn ngữ lập trình Python không có tính năng Overload nên khi ta viết lại 1 phương thức
    # mà ở trong lớp cha thì ta đã thực Override lên nó. Từ đó ta cần xác định lại hết giá trị ban đầu
    # của lớp cha bằng cách gọi hàm super().__init__(...) và truyền các tham số vốn có của lớp cha vào
    
    # Do tất cả các thuộc tính của lớp cha là private nên ta cũng không thể gọi trực tiếp được thuộc tính
    # đó. Đây là lý do mà ta xây dựng phương thức get() để nhận các giá trị private trong lớp cha.
    def __init__(self,mass = None,coordinate = None,speed = None,force = None , time = None):
        super().__init__(mass=mass,coordinate= coordinate,speed = speed)
        self.__force = force
        self.__time = time

    # Phương thức tính toán
    # Gán và nhận các giá trị năng lượng
    def set_energy(self,energy):
        if(energy != None):
            self.__energy = energy
        else:
            return self.ERROR()

    def get_energy(self):
        if(self.__energy != None):
            return self.__energy
        else:
            return self.ERROR()
    
    # Gán và nhận các giá trị cho lực
    def set_force(self,force):
        if(force != None):
            self.__force = force
        else:
            return self.ERROR()

    def get_force(self):
        if(self.__force != None):
            return self.__force
        else:
            return self.ERROR()

    # Gán và nhận các giá trị cho thời gian
    def set_time(self,time):
        if(time != None):
            self.__time = time
        else:
            return self.ERROR()

    def get_time(self):
        if(self.__time != None):
            return self.__time
        else:
            return self.ERROR()