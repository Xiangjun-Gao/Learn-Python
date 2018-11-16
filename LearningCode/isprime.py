def prime():
    try:
        x=eval(input(""))
        for i in range(x):
            if i in[0,1]:
                pass
            else:
                if divmod(x,i)[1]==0:
                    return False
                    print("F")
        print("True")
        return True
    except NameError:
        print("int")
        prime()

prime()
