inp_add_retreat=int(input("Enter procedure code\n1.Log data\n2.Retrive data\n"))
inp_type=int(input("Enter the type of data\n1.Diet\n2.Excersise\n"))
def date_time():
    import datetime
    return datetime.datetime.now()

def adding_data_diet():
    inp_destination = int(input("Select the member you should alter the data\n1.Rakshith Gowda\n2.Pratham\n3.Akash\n"))
    diet_type=input("Enter the Diet Name:")
    b = date_time()
    if inp_destination==1:
        a=open("1_Rakshith_Diet.txt", "a")
        c=str(b)+" : "+diet_type+"\n"
        a.write(c)
        print("Added succesfully")


    elif inp_destination==2:
        a=open("1_Pratham_Diet.txt", "a")
        c=str(b)+" : "+diet_type+"\n"
        a.write(c)
        print("Added succesfully")

    elif inp_destination==3:
        a=open("1_Akash_Diet.txt", "a")
        c=str(b)+" : "+diet_type+"\n"
        a.write(c)
        print("Added succesfully")


def adding_data_excersise():
    inp_destination = int(input("Select the member you should alter the data\n1.Rakshith Gowda\n2.Pratham\n3.Akash\n"))
    excersise_type = input("Enter the excersise Name:")
    b = date_time()
    if inp_destination == 1:
        a = open("Rakshith_excersise.txt", "a")
        c = str(b) +" : "+ excersise_type+"\n"
        a.write(c)
        print("Added succesfully")


    elif inp_destination == 2:
        a = open("Pratham_excersise.txt", "a")
        c = str(b) +" : "+ excersise_type+"\n"
        a.write(c)
        print("Added succesfully")

    elif inp_destination == 3:
        a = open("Akash_Excersise.txt", "a")
        c = str(b)+" : " + excersise_type+"\n"
        a.write(c)
        print("Added succesfully")

def retreat_data_diet():
    inp_destination = int(input("Select the member you should alter the data\n1.Rakshith Gowda\n2.Pratham\n3.Akash\n"))
    if inp_destination==1:
        # a=open("1_Rakshith_Diet.txt","r")
        # print(a.readlines())
        with open("1_Rakshith_Diet.txt") as a:
            for i in (a.readlines()):
                print(i,)

    elif inp_destination==2:
            # a=open("1_Pratham_Diet.txt","r")
            # print(a.readlines())
            with open("1_Pratham_Diet.txt") as a:
                for i in (a.readlines()):
                    print(i)

    elif inp_destination==3:
                # a=open("1_Akash_Diet.txt","r")
                # print(a.readlines())
            with open("1_Akash_Diet.txt") as a:
                for i in (a.readlines()):
                    print(i)


def retreat_data_excersise():
    inp_destination = int(input("Select the member you should alter the data\n1.Rakshith Gowda\n2.Pratham\n3.Akash\n"))
    if inp_destination == 1:
        # a = open("Rakshith_excersise.txt", "r")
        # print(a.readlines())
            with open("Rakshith_excersise.txt") as a:
                for i in (a.readlines()):
                     print(i)


    elif inp_destination == 2:
        # a = open("Pratham_excersise.txt", "r")
        # print(a.readlines())
        with open("Pratham_excersise.txt") as a:
            for i in (a.readlines()):
                print(i)

    elif inp_destination == 3:
        # a = open("Akash_Excersise.txt", "r")
        # print(a.readlines())
        with open("Akash_Excersise.txt") as a:
            for i in (a.readlines()):
                print(i)

if inp_add_retreat==1:
    if inp_type == 1:
            adding_data_diet()
    elif inp_type == 2:
        adding_data_excersise()

elif inp_add_retreat==2:
    if inp_type == 1:
        retreat_data_diet()
    elif inp_type == 2:
        retreat_data_excersise()

