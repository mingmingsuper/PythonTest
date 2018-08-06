class Screen(object):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer')
        if value < 0:
            raise ValueError('width must larger than 0')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an integer')
        if value < 0:
            raise ValueError('height must larger than 0')
        self._height = value

    @property
    def resolution(self):
        return self.width * self.height
