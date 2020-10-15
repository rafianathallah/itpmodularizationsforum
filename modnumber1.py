def datalisttuple():
    datasample = input("Sample data: ")
    print(datasample)

    datalist = datasample.split(",")
    datatuple = tuple(datalist)

    print("List: ",datalist)
    print("Tuple: ",datatuple)

datalisttuple()