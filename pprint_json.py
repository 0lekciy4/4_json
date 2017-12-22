import json
import sys

def load_data(filepath):
    with open(filepath, 'r', encoding='UTF-8') as json_file:
        json_data = json.load(json_file)
    return json_data

def return_pretty_json(json_content):
    return json.dumps(json_content, sort_keys=True, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    try:
        json_content = load_data(sys.argv[1])
    except IndexError:
        print('File path not passed')
    except FileNotFoundError:
        print('File not found')
    except json.JSONDecodeError as err:
        print('Bad json: {}'.format(err))
    print(return_pretty_json(json_content))
