with open("1_test.text", "a") as f:
    f.write("this txt must be added to that file")

with open("1_test.text") as r:
    print(r.read())