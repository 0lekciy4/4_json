import json
import sys

def read_filepath():
        filepath = sys.argv[1]
        return filepath

def load_data(filepath):
    with open(filepath, 'r', encoding='UTF-8') as handle:
        data = json.load(handle)
    return data

def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4))

if __name__ == '__main__':
    try:
        filepath = read_filepath()
        data = load_data(filepath)
        pretty_print_json(data)
    except IndexError:
        print('File path not passed')
    except FileNotFoundError:
        print('File not found')
    except json.JSONDecodeError as err:
        print('Bad json: {}'.format(err))
