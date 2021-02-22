class Sofa:
    _number_of_sofa = 0
    def _create_sofa(self):
        self._number_of_sofa +=1
    def __init__(self,width = 500,height = 75,color = "red"):
        self._width = width
        self._height = height
        self._color = color
        self._create_sofa()
    def __str__(self):
        return 'width {self._width}, height {self._height}, color {self._color}'.format(self=self)
    def __del__(self):
        del self._width
        del self._height
        del self._color
        del self._number_of_sofa


  



