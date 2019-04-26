def func():
    global b1
    b1 = 100
    print(b1)
    print("I am in func")
    b2 = 99
    # a2的作用范围是func
    print(b2)

func()
print(b1)

