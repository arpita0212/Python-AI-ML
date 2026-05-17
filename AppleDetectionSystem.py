for i in range(1, 20):
    if i == 4 or i == 9 or i == 15:
        continue
    elif i == 18:
        print("inspection machine overheated")
        break;
    else:
        print(f"Inspecting iPhone Serial No: {i}")