import sys


def names_extractor(filename):
    data = ['Name\tSurname\tE-mail\n', ]
    with open(filename, 'r') as f:
        for email in f:
            name, surname = email.split('@')[0].split('.')
            data.append(f'{name.capitalize()}\t{surname.capitalize()}\t{email}')

    data = "".join(data)
    with open('employees.tsv', 'w') as f:
        f.write(data)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        names_extractor(sys.argv[1])
