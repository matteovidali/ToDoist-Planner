from todoist_api_python.api import TodoistAPI
from os.path import exists


def get_key(filename='.key_file'):
    if not exists(filename):
        raise Exception("File does not exists")
    with open(filename, 'r') as f:
        return f.readline()


def add_project(name):
    pass


def add_task(api, name, due_string, project):
       task = api.add_task(
        content= name,
        due_string=due_string,
        due_lang='en',
        priority=4,
    )

def main(key_file):
    try:
        if key_file:
            api_key = get_key(key_file)
        else:
            api_key = get_key()
        
        api = TodoistAPI(api_key)
        projects = api.get_projects()
        print(api_key)
    except Exception as error:
        print(error)


# -- TESTING ----------------------------------------------------------

if __name__ == "__main__":
    key_file = input("Enter an API Key file (leave blank for default): ")
    main(key_file)
