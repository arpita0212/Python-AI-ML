for i in range(1, 26):
    if i == 6 or i == 12 or i == 19:
        continue
    elif i == 21:
        print("charging port malfunction detected")
        break
    else:
        print(f"Testing MacBook Charging Port {i}")