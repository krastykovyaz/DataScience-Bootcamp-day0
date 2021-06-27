import sys


def get_clients():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
               'john@snow.is', 'bill_gates@live.com',
               'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    return clients


def get_participants():
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    return participants


def get_recipients():
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    return recipients


def call_center():
    return list(set(get_clients()) | set(get_participants()) -
                set(get_recipients()))


def potential_clients():
    return list(set(get_participants()) - set(get_clients()))


def loyalty_program():
    return list(set(get_clients()) - set(get_participants()))


def main(task):
    data_mapping = {'call_center': call_center,
                    'potential_clients': potential_clients,
                    'loyalty_program': loyalty_program}

    assert task in data_mapping, 'Invalid task'

    print(data_mapping[task]())


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('Enter one task')
        sys.exit()

