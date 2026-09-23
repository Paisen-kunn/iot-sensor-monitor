temperature = 40.00

print("IoT Sensor Monitor")
print("------------------")
print(f"Temperature: {temperature}°C")

if temperature > 35:
    print("Status: HIGH")
elif temperature < 20:
    print("Status: LOW")
else:
    print("Status: NORMAL")