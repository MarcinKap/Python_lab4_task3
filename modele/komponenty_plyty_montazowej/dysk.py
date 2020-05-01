from modele.component import Component


class Dysk(Component):
    def __init__(self, comp_id, price):
        super().__init__(comp_id, price)

    def do_operation(self):
        print('{0}Dysk o id: {1} o cenie {2}'.format(self.prefix, self.id, self.price))
