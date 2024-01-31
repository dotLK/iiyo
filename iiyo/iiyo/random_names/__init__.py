from __future__ import unicode_literals
from os.path import abspath, join, dirname
import random

full_path = lambda filename: abspath(join(dirname(__file__), filename))

#path = os.path.abspath("new.py")
#print(path)
def name_array(file):
    with open(file) as fp:
        new_list = []
        for line in fp:
            new_list.append(line.strip())
    return new_list


file = full_path("male_first_names.py")
print(file)
male_names_file = name_array(file)

file = full_path("female_first_names.py")
female_names_file = name_array(file)

file = full_path("last_names.py")
last_names_file = name_array(file)

file = full_path("home_address.py")
home_address_file = name_array(file)

file = full_path("city.py")
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

