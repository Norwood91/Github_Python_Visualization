import requests
from plotly.graph_objs import Bar
from plotly import offline

# --------------------------------------------- API CALL -----------------------------------------------------
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {
    'Accept': 'application/vnd.github.v3+json'
}
request = requests.get(url, headers=headers)
request.raise_for_status()

# ------------------------------------------ USE INFO FROM API CALL ------------------------------------------
response = request.json()
returned_repos = response['items']
repo_links, stars, labels = [], [], []
for repo in returned_repos:
    repo_name = repo['name']
    repo_url = repo['html_url']
    repo_link = f'<a href="{repo_url}">{repo_name}</a>'
    repo_links.append(repo_link)

    stars.append(repo['stargazers_count'])
    owner = repo['owner']['login']
    description= repo['description']
    label = f'Owner of repo: {owner}<br /> {description}'
    labels.append(label)

# ------------------------------------------ PLOTLY VISUALIZATION ------------------------------------------
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {'title': 'Repository', 'titlefont': {'size':20}, 'tickfont': {'size':14}},
    'yaxis': {'title': 'Stars', 'titlefont': {'size': 20}, 'tickfont': {'size': 14}}
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='most_starred_py_projects.html')