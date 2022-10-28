import mlflow
from dotenv import load_dotenv
import git

# load_dotenv("secrets/.env")

tracking_uri = mlflow.get_tracking_uri()
print("Current tracking uri: {}".format(tracking_uri))

# Check for uncommited files and in affirmative case ask wether the user still wants to run
g = git.cmd.Git(".")
git_diff_files = g.diff(name_only=True).split('\n')

if git_diff_files != ['']:
    while True:
        print(f'There are uncommited changes in these files: \n {git_diff_files}')
        answer = input('Would you like to continue? Type "y" for yes and "n" for no: ')
        if answer == "y":
            break
        elif answer == "n":
            quit()
        else:
            print("Enter either y/n")



mlflow.projects.run(git.Repo().remotes.origin.url, version=git.Repo(".").active_branch, env_manager="conda")