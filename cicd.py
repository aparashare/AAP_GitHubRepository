# commenting the token as it expires and access gets revoked
# Leaarn on the mechanism to get the token
#g = Github("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")

latest_sha = dev_branch.commit.sha              # is it hypen or = get it clarified

repo = g.get_repo("AAP_GitHubRepository/flask_helloworld")      

latest_sha = dev_branch.commit.sha              # is it hypen or = get it clarified

dev_branch = repo.get_branch("dev")     

print(dev_branch.commit.sha)                    # what is sha?, how we get it

latest_sha = dev_branch.commit.sha              # is it hypen or = get it clarified

commit - repo.get_commit(sha-latest_sha)        # is it hypen or = get it clarified

print(commit.commit.author.date)

while True:
    dev_branch - repo.get_branch("Develop")
    print("checking for new commit")
    sha - dev_branch.commit.sha

    if sha !- latest_sha:
        print("Found new commit deploying")
        latest_sha = sha
        os.system(".\pullanddeploy.bat")            # not understood
        pass