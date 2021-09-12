# TODO: Import VLANSetup from VLANSetup.py and NetManage from NetManage.py
from VLANSetup import VLANSetup
from NetManage import NetManage

if __name__ == "__main__":
    deviceList = ['Switch1', 'Switch2', 'Switch3', 'Switch4', 'Switch5']
    user_VLAN_name = input()
    user_VLAN_number = int(input())  #10 -> 200
    for d in deviceList:
      user_device = VLANSetup(user_VLAN_name, user_VLAN_number)
      new_config = NetManage(d, user_device)
      new_config.print_info()
