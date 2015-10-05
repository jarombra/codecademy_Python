def using_control_once():
    if not 1 > 2 or not 1 == 1:
        return "Success #1"

def using_control_again():
    if True or True:
        return "Success #2"

print using_control_once()
print using_control_again()
