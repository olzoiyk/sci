#For loop - process each temperarture

temperatures = [900, 950, 1000, 1050, 1100]

print("Converting temperautrues to Kelvin:")

for temp in temperatures:
    kelvin = temp + 273.15
    print(f"{temp}C = {kelvin}K")

# Loop with index and value
print("\nGrowth condtions:")
pressures = [1e-5, 2e-5, 3e-5, 4e-5, 5e-5]
for i, (temp, press) in enumerate(zip(temperatures, pressures)):
    print(f"Experiment {i+1}: {temp}C, {press:.1e}Torr")

#While loop - growth simulation
time = 0
height = 0
growth_rate = 10 # nm/min
print("\nGrowth simulation:")
while height < 500:
    height += growth_rate
    time +=1
    if time % 10 == 0: #Print every 10 minutes
        print(f"Time:{time} min, Height: {height} nm")