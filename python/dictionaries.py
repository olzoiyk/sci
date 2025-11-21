# Store experimental parameters
experiment = {
    "substrate": "Sapphire",
    "temperature": 1100,
    "pressure": 2.5e-5,
    "time": 60,
    "gas_ratio": 4.0,
    "selective": True
}

print("Expriment Parameters:")
print(f"Substrate: {experiment['substrate']}")
print(f"Temperature:{experiment['temperature']}")
print(f"V/III ratio:{experiment['gas_ratio']}")


# Add new key
experiment["diameter"] = 50
experiment["height"] = 500

# Multiple experiments
experiments = [
    {"id": 1, "temp":900, "diameter": 30},
    {"id":2, "temp":1000, "diameter":50},
    {"id":3, "temp":1100, "diameter":70}
]

print("\nExperimental Series:")
for exp in experiments:
    print(f"Exp {exp['id']}: {exp['temp']} Degrees Celcius => {exp['diameter']} nm")

#Dictionary methods
print(f"\nAll keys: {list(experiment.keys())}")
print(f"All values: {list(experiment.values())}")