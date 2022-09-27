def quartz(un, deux, *cinq):
    i = input("Please Select a Number: ")
    if i == 1:
        print("Correct")
        print("Name: {}, year: {}".format(un, deux))
    return "Hello Teams"    
quartz("Corey", "Shafer")    


def huit(**sept):
    return "Name : {}\n Year: {} \n".format("Tayo", "2003") + sept["a"] + ' ' + sept['b']

print(huit(a = "amazing", b = "Wonderful", c= "Intelligent"))


