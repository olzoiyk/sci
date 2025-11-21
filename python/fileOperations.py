# Writing data to file
data = """Temperature,Pressure,Diameter,Height
900,1e-5,30,300
1000,2e-5,50,500
1100,3e-5,70,700"""

#Simulate writing to file
print("Writing to 'gan_data.csv': ")
print(data)

#Reading and processing data
print("\n---Reading and Processing ---")
lines = data.split('\n')
headers = lines[0].split(',')
print(f"Headers: {headers}")

print("\nData rows:")
for line in lines[1:]:
    values = line.split(',')
    temp = int(values[0])
    diameter = int(values[2])
    height = int(values[3])
    aspect_ratio = height / diameter
    print(f"T={temp}C, D={diameter}nm, H={height}nm, AR = {aspect_ratio:.1f}")

# Writing results
print("\n---Writing analysis results ---")
results = "Sample,AspectRatio,Quality\n"
results += "NW1,10.0,High\n"
results += "NW2,10.0,High\n"
results += "NW3,10.0,High\n"
print(results)
