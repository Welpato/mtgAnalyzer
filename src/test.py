from getInfo.getInformation import getInformation

sets = getInformation.getSets("ins")

for set in sets:
    print(set.name)
