#Check growth conditions
def check_conditions(temperature, pressure):
    print(f"\nChecking: T={temperature}C, P={pressure:.1e}Torr")

    if temperature < 900:
        print("Temp too low = growth rate is insufficient")
    elif temperature > 1200:
        print("Temp too hight = risk of decomposition")
    else:
        print("Temperature optimal")

    if pressure < 1e-6:
        print("Pressure too low - unstable plasma")
    elif pressure > 1e-4:
        print("Pressure too hight - poor selectivity")
    else:
        print("Pressure optimal")

    # Combined condition
    if 900<= temperature <=1200 and 1e-6 <= pressure <= 1e-4:
        print("OPTIMAL CONDITIONS FOR SAG")
    else:
        print("Adjust parameters")

    #Test different conditions

check_conditions(1100, 2.5e-5)
check_conditions(850, 5e-5)
check_conditions(1100, 5e-4)