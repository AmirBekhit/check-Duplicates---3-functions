# Check for duplicates in list
def checkDuplicates(listOfNum):
    if len(listOfNum) == len(set(listOfNum)):
        return False
    else:
        return True


listOfNum = ['a', 'b', 'c', 'b', 'a', 'd', 'e', 'f', 'e']

checkDuplicates(listOfNum)
if listOfNum is True:
    print("The list does not contain duplicates")
else:
    print("The list contains duplicates")

# ******************************************************


def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True


def checkIfDuplicates_2(listOfElems):
    ''' Check if given list contains any duplicates '''
    setOfElems = set()
    for elem in listOfElems:
        if elem in setOfElems:
            return True
        else:
            setOfElems.add(elem)
    return False


def checkIfDuplicates_3(listOfElems):
    ''' Check if given list contains any duplicates '''
    duplicates = []
    for elem in listOfElems:
        if listOfElems.count(elem) > 1:
            if elem not in duplicates:
                duplicates.append(elem)
                print(duplicates)
            return True


def main():

    listOfElems = ['a', 'b', 'c', 'b', 'a']

    # using set and comparing sizes - len - method
    print('*** Check for duplicates in list using Set and comparing sizes ***')

    result = checkIfDuplicates_1(listOfElems)

    if result:
        print('Yes, list contains duplicates')
    else:
        print('No duplicates found in list')

#  using set method and looking for first duplicate
    print('*** Check for duplicates in list using Set and looking for first duplicate ***')

    result = checkIfDuplicates_2(listOfElems)

    if result:
        print('Yes, list contains duplicates')
    else:
        print('No duplicates found in list')

    # list.count() method
    print('*** Check if list contains duplicates using list.count() ***')

    result = checkIfDuplicates_3(listOfElems)

    if result:
        print('Yes, list contains duplicates')

    else:
        print('No duplicates found in list')


if __name__ == '__main__':
    main()
