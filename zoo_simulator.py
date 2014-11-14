import json
from animal import Animal
# from zoo import Zoo


def json_decoder(file_name):
    with open(file_name, 'r') as db:
        json_data = db.read()
        db.close()
    return eval(json.loads(json_data))


def json_encoder(data, file_name):
    with open(file_name, 'w') as db:
        json.dump(data, file_name)
    db.close()


def help():
    print('You can use one of these commands:\n'
          'show_animals - shows all animals\n'
          'accommodate <species> <name> <age> <weight>\n'
          'move_to_habitat <species> <name> - release the animal to nature\n'
          'simulate <interval_of_time> <period>\n'
          '')


def main():
    help()
    animals = json_decoder('animals.json')

    while True:
        choice = input('Enter a command> ')
        if choice.lower() == 'quit':
            exit()

        elif choice.lower() == 'show_animals':
            # pass
            print(str(animals))

        elif choice.lower().startswith('accommodate'):
            if len(choice.split()) != 5:
                help()
            pass

        elif choice.lower().startswith('move_to_habitat'):
            if len(choice.split()) != 3:
                help()
            pass

        elif choice.lower().startswith('simulate'):
            if len(choice.split()) != 3:
                help()
            pass

        else:
            help()

if __name__ == '__main__':
    main()
