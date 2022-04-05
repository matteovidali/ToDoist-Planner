from todoist_api_python.api import TodoistAPI
from os.path import exists

# Checks to make sure file exists (raises default exeption)
def check_file(path):
    if not exists(path):
        raise Exception(f"'{path}' does not exists")

# Gets the API token from a file (To anonamize key when pushing to github)
def get_key(filename='/keys&creds/.key_file'):
    check_file(filename)
    with open(filename, 'r') as f:
        return f.readline()

# Gets a list of chores as a 2d array
def get_chores(filename='API_chore_list.csv'):
    check_file(filename)
    chore_list = []
    with open(filename, 'r') as f:
        for line in f:
            chore_list.append(line.split(','))
    return chore_list

#TODO Flesh out this function
def add_chore(filename='.chore_list'):
    check_file(filename)
    with open(filename, 'ra'):
        pass
    return

#TODO make this add a project (necessity?)
def add_project(name):
    pass

#TODO This:
def add_task(api, name, due_string, project):
       task = api.add_task(
        content= name,
        due_string=due_string,
        due_lang='en',
        priority=4,
    )


#TODO This:
def main(key_file):
    try:
        if key_file:
            api_key = get_key(key_file)
        else:
            api_key = get_key()

        api = TodoistAPI(api_key)
        projects = api.get_projects()
        for project in projects:
            print(project)
            print("---\n")
    except Exception as error:
        print(error)


# -- TESTING ----------------------------------------------------------
if __name__ == "__main__":
    key_file = input("Enter an API Key file (leave blank for default): ")
    print(get_chores())
    #main(key_file)

