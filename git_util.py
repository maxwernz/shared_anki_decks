import git
import os

def git_pull():
    g = git.cmd.Git(os.getcwd())
    g.pull()

def git_push(files_to_add):
    repo = git.Repo(os.getcwd())
    repo.index.add(files_to_add)
    commit_string = ", ".join(files_to_add)
    repo.index.commit("update/add " + commit_string)
    origin = repo.remotes.origin
    origin.push()
    