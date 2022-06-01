
for k in range(1, 11):
    print("--------------------")
    print("This is the print of ruler no.", k,"\n")

    for j in range(1, 13):
        for i in range(j, 13):
            print(j, "*", i, "=", (j*i))
        print("*******************")