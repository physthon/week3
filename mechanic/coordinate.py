from env.frame import Frame
class Coordinate(Frame):
    def __init__(self,coordinate = 0):
        super().__init__()
        self.__coordinate = coordinate

    def set_(self,coor):
        if(coor != 0):
            self.__coordinate = coor
        else:
            return self.ERROR()

    def get_(self):
        return self.__coordinate