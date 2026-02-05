list_of_names = ["anton", "magnus", "leander", "prince", "jakub", "karl"]
for name in list_of_names:
    if name == "leander":
        for num in range(10):
            print(f"{name} is a femboy!")
    elif name == "prince":
        print(f"can't see you {name}")
        continue
    else:
        print(name)
    print("hello!")