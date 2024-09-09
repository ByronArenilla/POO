class FiguraGeometrica:
    def __init__(self):
        self._volumen = 0.0  # Atributo que identifica el volumen de una figura
        self._superficie = 0.0  # Atributo que identifica la superficie de una figura

    def set_volumen(self, volumen):

        self._volumen = volumen

    def get_volumen(self):

        return self._volumen

    def set_superficie(self, superficie):

        self._superficie = superficie

    def get_superficie(self):

        return self._superficie
