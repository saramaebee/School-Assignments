class VLANSetup:
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (name, number)
    def __init__(self, name='None', number=0):
        self.name = name
        self.number = number

    def print_info(self):
        print('Sending Config vlan: {}'.format(self.number))
        print('Sending Config name: {}'.format(self.name))
