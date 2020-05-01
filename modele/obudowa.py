from modele.component import Component


class Obudowa(Component):
    def __init__(self, comp_id, price):
        super( ).__init__(comp_id, price)
        self.__component_dict = dict( )
        self.__price = price
        self.__sum_price = self.suma_cen( )

    def dodaj_magistrale(self, magistrala):
        magistrala.prefix_setter = '{0}{1}'.format(self.prefix, magistrala.prefix)
        print(magistrala.prefix, '123')
        for el in magistrala.get_children( ):
            el.prefix_setter = '{0}{1}'.format(magistrala.prefix, el.prefix)

        self.__component_dict[magistrala.id] = magistrala

    def dodaj_plyte_montazowa(self, plyta_montazowa):
        plyta_montazowa.prefix_setter = '{0}{1}'.format(self.prefix, plyta_montazowa.prefix)
        for el in plyta_montazowa.get_children( ):
            el.prefix_setter = '{0}{1}'.format(plyta_montazowa.prefix, el.prefix)
        self.__component_dict[plyta_montazowa.id] = plyta_montazowa

    def do_operation(self):
        print('W skład tej obudowy wchodzi:')
        print('{0}Obudowa o id: {1} o cenie {2}, zawiera:'.format(self.prefix, self.id, self.__price))
        for comp in self.__component_dict.values( ):
            comp.do_operation( )

    def suma_cen(self):
        suma_cen = self.price
        for comp in self.__component_dict.values( ):

            suma_cen = suma_cen + comp.suma_cen()
        return suma_cen

    def get_children(self):
        return self.__component_dict.values()


