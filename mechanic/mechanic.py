# coding=utf-8

# Ta tạo 1 Interface về cơ học, vì đây là một lớp mô tả không rõ ràng cho 1 hệ vật lý nào,
# cho nên ta không nhất thiết phải cho thêm các phương thức tính toán vào để làm gì
# Mục đích của Class này tạo ra là để mô tả một lớp Cơ học hiện hữu những thành phần như thế nào
# có thể đo đạc được để truyền giá trị vào.


class Mechanic:
    def __init__(self,mass = None,coordinate = None,speed = None):
        ## __<name>__ là biến kiểu static
        ## _<name> là biến kiểu protected
        ## __<name> là biến kiểu privated
        self.__version__ = "1.0.0"
        self.__mass = mass
        self.__coordinate = coordinate
        self.__speed = speed
        self.__error = False

    # Các hàm virtual mô tả lớp
    def lagrangian(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def hamiltonian(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def energy(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def mass(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def coordinate(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def speed(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
    # Các hàm tính năng cài đặt cho lớp
    def set_mass(self,mass):
        if(mass != None):
            self.__mass = mass
        else:
            return self.__error

    def get_mass(self):
        if(self.__mass != None):
            return self.__mass
        else:
            return self.__error

    def set_coordinate(self,coordinate):
        if(coordinate != None):
            self.__coordinate = coordinate
        else:
            return self.__error

    def get_coordinate(self):
        if(self.__coordinate != None):
            return self.__coordinate
        else:
            return self.__error

    def set_speed(self,speed):
        if(speed != None):
            self.__speed = speed
        else:
            return self.__error
    
    def get_speed(self):
        if(self.__speed != None):
            return self.__speed
        else:
            return self.__error

    def ERROR(self):
        return self.__error
