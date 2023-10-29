import requests
import random
import xml.etree.ElementTree as ET

access_token = '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'
headers = {
    'Authorization': f'token {access_token}',
}

username = 'Abuster147'
repos_url = f'https://api.github.com/users/Abuster147/repos'

response = requests.get(repos_url, headers=headers)
repos = response.json()

for repo in repos:
    print(repo['name'])

random_repo = random.choice(repos)
selected_repo_name = random_repo['name']

print(f"Randomly selected repository: {selected_repo_name}")

repo_url = f'https://api.github.com/repos/Abuster147/{selected_repo_name}/contents'
response = requests.get(repo_url, headers=headers)

repo_content = response.json()

for item in repo_content:
   
    if item['name'] == 'pom.xml':
        pom_file_url = item['url']
        
        response = requests.get(pom_file_url, headers=headers)

        pom_content = response.text
                 
        root = ET.fromstring(pom_content)

        for dependency in root.findall('.//dependency'):
            group_id = dependency.find('groupId').text
            artifact_id = dependency.find('artifactId').text
            version = dependency.find('version').text

            print(f'Dependency: {group_id}:{artifact_id}, Version: {version}')
        
    else:
        print(f'No POM.XML file found in {selected_repo_name}')




