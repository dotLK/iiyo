import random
import os


#path = os.path.abspath("new.txt")
#print(path)
def name_array(file):
    with open(file) as fp:
        new_list = []
        for line in fp:
            new_list.append(line.strip())
    return new_list


file = os.path.abspath("male_first_names.txt")
print(file)
male_names_file = name_array(file)

file = os.path.abspath("female_first_names.txt")
female_names_file = name_array(file)

file = os.path.abspath("last_names.txt")
last_names_file = name_array(file)

file = os.path.abspath("home_address.txt")
home_address_file = name_array(file)

file = os.path.abspath("city.txt")
city_name_file = name_array(file)


def quin():
    result = f"['Avihinsaka uwathy','Nihada Mawatha ','Palu Niwahana']"
    return result



def femalename():
    result = f"[{random.choice(female_names_file)} {random.choice(last_names_file)}]"
    return result



def femaleaddress():
    result = f"[{random.choice(female_names_file)} {random.choice(last_names_file)},{random.choice(home_address_file)},{random.choice(city_name_file)}]"
    return result



def maleaddress():
    result = f"['{random.choice(male_names_file)} {random.choice(last_names_file)}','{random.choice(home_address_file)}','{random.choice(city_name_file)}']"
    return result



