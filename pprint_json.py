import json
import sys

def load_json_content(filepath): #функция load_data переименованна в load_json_content, т.к. лучше подходит по смыслу
    with open(filepath, 'r', encoding='UTF-8') as handle:
        json_content = json.load(handle)
    return json_content

def pretty_print_json(json_content):
    return json.dumps(json_content, sort_keys=True, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    try:
        json_content = load_json_content(sys.argv[1])
        print(pretty_print_json(json_content))
    except IndexError:
        print('File path not passed')
    except FileNotFoundError:
        print('File not found')
    except json.JSONDecodeError as err:
        print('Bad json: {}'.format(err))
