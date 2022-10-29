import git

def check_for_uncommited(git_path):
    # Check for uncommited files and in affirmative case ask wether the user still wants to run
    g = git.cmd.Git(git_path)
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