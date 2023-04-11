print("input -------------------------------------\n")


def get_name():
    name = input("Name: ").capitalize()
    return name


def get_gender():
    sex = input("Sex: ").capitalize()
    if sex == "Male":
        sex = "Mr"
        return sex
    elif sex == "Female":
        sex = "Ms"
        return sex
    else:
        return sex



def get_age():
    while True:
        age = input("Age (years): ")
        if age.isdigit():
            return age
        else:
            age = input("Age (years): ")
            continue


def get_weight():
    while True:
        weight = input("Weight (Kg): ")
        if weight.isdigit():
            return float(weight)
        else:
            continue


def get_height():
    while True:
        height = input("Height (cms): ")
        if height.isdigit():
            return float(height)
        else:
            continue


def calculate_bmi():
    weight = get_weight()
    height = get_height()

    bmi = weight / (height/100)**2  #divided height (cm) with 100 to get height(m)

    return bmi
