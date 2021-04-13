person_name = []
while True:
    name = input(f'Enter the name of person {len(person_name)+1} \n'
                 f'Or enter noting to stop \n')
    if name == '':
        break
    person_name = person_name + [name]  # List concatenation
    person_name.sort()
    print(person_name)
    for name in person_name:
        print(name)


