# Variables and basic data types
temperature = 1100  # Growth temperature in Celsius (int)
pressure = 2.5e-5   # Pressure in Torr (float)
substrate = "Sapphire"  # Text string
is_selective = True  # Boolean

# Print variables
print("Temperature:", temperature, "°C")
print("Pressure:", pressure, "Torr")
print("Substrate:", substrate)
print("Selective growth:", is_selective)

# Check data types
print("\nData type of temperature:", type(temperature))
print("Data type of pressure:", type(pressure))

# Calculate nanowire growth parameters
import math

# Basic arithmetic
diameter = 50  # nm
height = 500   # nm
aspect_ratio = height / diameter
print(f"Aspect ratio: {aspect_ratio}")

# Power and roots
volume = math.pi * (diameter/2)**2 * height
print(f"Nanowire volume: {volume:.2f} nm cube")

# Temperature conversion (Celsius to Kelvin)
temp_celsius = 1100
temp_kelvin = temp_celsius + 273.15
print(f"{temp_celsius}°C = {temp_kelvin}K")

# V/III ratio calculation
v_flow = 20  # sccm
iii_flow = 5  # sccm
ratio = v_flow / iii_flow
print(f"V/III ratio: {ratio}")

# Lists for experimental parameters
temperatures = [900, 950, 1000, 1050, 1100]
diameters = [30, 45, 50, 55, 70]

print("Temperature series:", temperatures)
print("First temperature:", temperatures[0])
print("Last temperature:", temperatures[-1])

# List operations
temperatures.append(1150)  # Add item
print("After adding 1150:", temperatures)

# List length
print(f"Number of experiments: {len(temperatures)}")

# List slicing (getting subset)
first_three = temperatures[0:3]
print("First three temps:", first_three)

# Calculate average
average_temp = sum(temperatures) / len(temperatures)
print(f"Average temperature: {average_temp:.1f}°C")