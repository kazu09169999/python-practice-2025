print("hello kuku")

for row in range(1, 10):
    for num in range(1, 10):
        print(f"{row} * {num} = {row * num}", end="\t")
    print()  # ← 1行分終わったら改行
