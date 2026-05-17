for i in range(1, 40):
    if i % 4 == 0:
        continue
    elif i == 31:
        print("Stop")
        break
    else:
        print(f"Monitoring Server {i}")