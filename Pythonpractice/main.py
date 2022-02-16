def print_if_odd(number):
    if count % 2 == 0:
        return
    print(number)

print("not in function")
count = 0
print("Starting loop")
while True:
    count += 1
    print_if_odd(count)

    if count >= 19:
        break
print("ended loop")