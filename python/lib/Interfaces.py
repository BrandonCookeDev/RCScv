from interface import implements, Interface

class ICropper(Interface):
    def crop(self, framecv):
        pass

    def draw_rectangles(self, framecv):
        pass


class IDetector(Interface):
    def detect(self, framecv):
        pass

    def draw_rectangles(self, framecv):
        pass


class IAlgorithm(Interface):
    def do(self, framecv):
        pass

    def draw(self, framecv):
        pass