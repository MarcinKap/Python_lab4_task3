from modele import component
from modele.component import Component


class PlytaMontazowa(Component):
    def __init__(self, comp_id, price):
        super().__init__(comp_id, price)
        self.__component_dict = dict()

    def dodaj_dysk(self, dysk):
        dysk.prefix_setter = '{0}{1}'.format(self.prefix, dysk.prefix)
        for el in dysk.get_children():
            el.prefix = '{0}{1}'.format(dysk.prefix, el.prefix)
        self.__component_dict[dysk.id] = dysk

    def dodaj_plyte_glowna(self, plyta_glowna):
        plyta_glowna.prefix_setter = '{0}{1}'.format(self.prefix, plyta_glowna.prefix)
        for el in plyta_glowna.get_children():
            el.prefix_setter = '{0}{1}'.format(plyta_glowna.prefix, el.prefix)
        self.__component_dict[plyta_glowna.id] = plyta_glowna

    def do_operation(self):
        print('{0}Plyta montazowa o id: {1} o cenie {2}. zawiera:'.format(self.prefix, self.id, self.price))
        for comp in self.__component_dict.values():
            comp.do_operation()

    def get_children(self):
        return self.__component_dict.values()

    def suma_cen(self):
        suma_cen = self.price
        for comp in self.__component_dict.values( ):
            suma_cen = suma_cen + comp.price
        return suma_cen