known_devices = ["Phone", "Laptop"]

device = input("Enter device name: ")

if device in known_devices:
    print("Access Granted")
else:
    print("⚠️ Alert: Unauthorized device detected!")
