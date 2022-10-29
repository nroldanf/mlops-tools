import mlflow
from dotenv import load_dotenv
import git
from utils.git_utils import check_for_uncommited

# load_dotenv("secrets/.env")
print(dir(git.Repo(".")))

tracking_uri = mlflow.get_tracking_uri()
print("Current tracking uri: {}".format(tracking_uri))

# Check for uncommited files and in affirmative case ask wether the user still wants to run
check_for_uncommited(".")



# Take remote repository code to run current active branch
mlflow.projects.run(git.Repo(".").remotes.origin.url, version=git.Repo(".").active_branch)