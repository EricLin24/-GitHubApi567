"""
HW04a
You should write a function that will take as input a GitHub user ID.
The output from the function will be a list of the names of the repositories that the user has,
along with the number of commits that are in each of the listed repositories.
"""
import requests
import json

def get_github_repo_commit(user_id):
    repo_url = "https://api.github.com/users/%s/repos" %(user_id)
    #print(repo_url)
    try:
        json_repo = requests.get(repo_url)
    except requests.HTTPError:
        print('Invalid request')
        return -1
    #print(json_repo.text)
    repo_list = json.loads(json_repo.text)
    #print(type(repo_list))
    res = []

    if (len(repo_list) == 2 and repo_list['message']) or repo_list == []:
        if repo_list['message'] == "API rate limit exceeded for 98.109.30.29. (But here's the good news: Authenticated " \
                                   "requests get a higher rate limit. Check out the documentation for more details.)":
            print("API rate limit exceeded.")
            return -1
        print('The user ID not found')
        return 0
    for repo in repo_list:
        print(repo)
        repo_name = repo['name']
        #print(repo_name)
        commiit_url = "https://api.github.com/repos/%s/%s/commits" %(user_id, repo_name)
        try:
            json_commit = requests.get(commiit_url)
        except requests.HTTPError:
            print('Invalid request')
            return -1
        commit_list = json.loads(json_commit.text)
        print("Repo: %s Number of commits: %s" %(repo_name, len(commit_list)))
        res.append("Repo: %s Number of commits: %s" %(repo_name, len(commit_list)))
    return res


get_github_repo_commit("daseda")