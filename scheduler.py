from ToDoistHandling import get_key, get_chores
from todoist_api_python.api import TodoistAPI

# TODO:
# Create a scheduling meathod that will 
# take the freqency as a per week freqency
# and automatically adds the chore to the correct section
# of the project (Chores) and automatically pops a reminder

def schedule():
    # Figure out which chores should be scheduled ???
    # If they aren't already on the list, add them to the list
    # if any are overdue send a push notification
    pass

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

