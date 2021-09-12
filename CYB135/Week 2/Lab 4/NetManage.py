# TODO: Import VLANSetup from VLANSetup.py
from VLANSetup import VLANSetup

class NetManage:
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (device, config)
    def __init__(self, device='None', config=VLANSetup()):
        self.device = device
        self.config = config

    def print_info(self):
        print('Configuring VLAN: %s' % (self.config.number))
        print('Connecting to: {}'.format(self.device))
        self.config.print_info()
        print()
