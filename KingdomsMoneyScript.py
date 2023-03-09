from uniref import WinUniRef

def SetUnlimitedMoney():
    ref = WinUniRef("Kingdoms.exe")
    clazz_mon = ref.find_class_in_image("Assembly-CSharp.dll", "Player_Parameters")
    offset = clazz_mon.find_field("Gold")
    addresses = clazz_mon.guess_instance_address()
    for clx in addresses:
       offset.set_instance(clx)
       offset.set_value(999999)
if __name__ == "__main__":
    SetUnlimitedMoney()
