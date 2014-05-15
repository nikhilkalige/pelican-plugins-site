import github3 as github
import re

REPO_USERNAME = 'nikhilkalige'
REPO_NAME = 'pelican-plugins'


def dir_readme(path):
    contents = repo.contents(path)
    # get the readme file
    #print(path)
    for value in contents.keys():
        match = re.match('^(readme\\.(rst|md))$', value, re.I)
        if match is not None and match.group(1) is not None:
            file_contents = repo.contents(path + '/' + match.group(1)).decoded
            extension = match.group(2)
            return file_contents, extension

    return None, None


def module_readme(path):
    contents = repo.contents(path)
    url = contents.submodule_git_url
    user_name = re.search('\\.com/(\\w+)', url).group(1)
    #print(user_name, path)
    _repo = user.repository(user_name, path)
    readme = _repo.readme()
    extension = re.match('^(readme\\.(rst|md))$', readme.name, re.I).group(2)
    return readme.decoded, extension


user = github.login('nikhilkalige', '##')
repo = user.repository(REPO_USERNAME, REPO_NAME)
tree = repo.tree('master').to_json()

sub_dir = []
sub_module = []
symlink = []
file_list = []

if 'tree' in tree:
    for value in tree['tree']:
        if(value['mode'] == '040000'):
            sub_dir.append(value)
        elif(value['mode'] == '160000'):
            sub_module.append(value)
        elif(value['mode'] == '120000'):
            symlink.append(value)

    for value in sub_dir:
        file_contents, extension = dir_readme(value['path'])
        if file_contents is not None:
            d = {}
            d['path'] = value['path']
            d['contents'] = file_contents
            d['ext'] = extension
            file_list.append(d)

    for value in sub_module:
        d = {}
        d['path'] = value['path']
        d['contents'], d['ext'] = module_readme(value['path'])
        file_list.append(d)

    print(file_list)
