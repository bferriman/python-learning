i = 1
while i <= 20:
    if i % 2 == 0:
        i += 1
        continue  # continue ends execution of this iteration of loop, returns to top
    if i == 15:
        break  # break exits the while loop
    print("Odd:", i)
    i += 1
