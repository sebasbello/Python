gas = False
turnt_on = False
packed = False

if gas and turnt_on and packed:
    print(True)
elif gas or (turnt_on or packed):
    print(False)
else:
    print("Empty")
