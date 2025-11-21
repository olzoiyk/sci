# Define function for calculations

def calculate_aspect_ratio(height, diameter):
    """Calculate nanowire aspect ratio"""
    return height / diameter

def nanowire_volume(diameter, height):
    """Calculate cylindrical nanowire volume"""
    import math
    radius = diameter / 2
    volume = math.pi * radius**2 * height
    return volume

def growth_time(target_height, growth_rate):
    """"Calculate time needed to reach target height"""
    time = target_height/growth_rate
    return time

# Use functions
d = 50 #nm
h = 500 #nm

ar = calculate_aspect_ratio(h,d)
vol = nanowire_volume(d, h)
time = growth_time(h, growth_rate=10)

print(f"Diameter: {d} nm")
print(f"Height: {h} nm")
print(f"Aspect ratio: {ar:.1f}")
print(f"Volume of the nanowire is:{vol:.2f} nm cube")
print(f"Growth time is: {time:.1f} minutes")

# Functions with multiple returns
def analyze_nanowire(diameter, height):
    aspect_ratio = height / diameter
    volume = 3.14159 * (diameter/2)**2 * height
    return aspect_ratio, volume, "Complete"

ar, vol, status = analyze_nanowire(60, 600)
print(f"\nAnalysis: AR={ar:.1f}, V={vol:.0f} nm cube, Status={status}")