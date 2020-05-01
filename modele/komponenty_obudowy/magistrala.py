from modele.component import Component


class Magistrala(Component):
    def __init__(self, comp_id, price):
        super().__init__(comp_id, price)
        self.__component_dict = dict()
    def dodaj_karte(self, karta):
        karta.prefix_setter = '{0}{1}'.format(self.prefix, karta.prefix)
        for el in karta.get_children():
            el.prefix_setter = '{0}{1}'.format(karta.prefix, el.prefix)
        self.__component_dict[karta.id] = karta

    def do_operation(self):
        print('{0}Magistrala o id: {1} o cenie {2}, zawieram:'.format(self.prefix, self.id, self.price))
        for comp in self.__component_dict.values():
            comp.do_operation()

    def get_children(self):
        return self.__component_dict.values()


    def suma_cen(self):
        suma_cen = self.price
        for comp in self.__component_dict.values( ):
            suma_cen = suma_cen + comp.price
        return suma_cen