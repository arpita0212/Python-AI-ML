for i in range(1, 30):
    if i % 5 == 0:
        print(f"Customer {i} is a VIP customer.")
    elif i == 27:
        print('the store reached full capacity')
        break
    else:
        print(f"Customer {i} is a regular customer.")