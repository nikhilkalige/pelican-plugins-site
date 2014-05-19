import github3 as github
import re
import os
import codecs


REPO_USERNAME = 'nikhilkalige'
REPO_NAME = 'pelican-plugins'
RAW_FILE_LOCATION = 'content'


def dir_readme(path):
    contents = repo.contents(path)
    # get the readme file
    #print(path)
    for value in contents.keys():
        match = re.match('^(readme\\.(rst|md))$', value, re.I)
        if match is not None and match.group(1) is not None:
            file_contents = repo.contents(path + '/' + match.group(1)).decoded.decode('utf-8')
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
    return readme.decoded.decode('utf-8'), extension


def convert_to_html(content, title, link):
    html = user.markdown(content)
    # format it to suit requirements pelican
    html = (
        "<html>\n<head>\n"
        + "<title>" + title + "</title>\n"
        + "<meta name=\"link\" content=\"" + link + "\"/>"
        + "</head>\n <body>"
        + html.decode('utf-8')
        + "</body></html>"
        )
    return html


def insert_string(str, new_str, pos):
    return str[:pos] + new_str + str[pos:]


user = github.login(token=os.environ.get('TOKEN'))
repo = user.repository(REPO_USERNAME, REPO_NAME)
tree = repo.tree('master').to_json()
repo_link = repo.html_url

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
            d['name'] = value['path']
            d['contents'] = file_contents
            d['ext'] = extension
            file_list.append(d)

    for value in sub_module:
        d = {}
        d['name'] = value['path']
        d['contents'], d['ext'] = module_readme(value['path'])
        file_list.append(d)

    cwd = os.getcwd()
    loc = os.path.join(cwd, RAW_FILE_LOCATION)
    if not os.path.exists(loc):
        os.mkdir(loc)

    for value in file_list:
        name = value['name']
        extension = value['ext']
        contents = value['contents']

        if name == 'test_data':
            continue

        #remove underscore from names
        title = name.replace('_', ' ')
        folder_link = repo_link + '/' + 'tree/master/' + name
        file_name = name + '.' + ('rst' if extension == 'rst' else 'html')

        with codecs.open(os.path.join(loc, file_name), 'w', 'utf-8') as outfile:
            if extension == 'rst':
                # check if title already exists
                if re.search('####', contents) < 0:
                    html = (title + '\n' + '#' * len(title) + '\n' + '\n' + contents)
                else:
                    html = contents
                # append link
                position = re.search('[#]{3,}(?:\r|\n|\r\n)', html)
                html = insert_string(html, (':link: ' + folder_link), position.end())

            elif extension == 'md':
                html = convert_to_html(contents, title, folder_link)

            outfile.write(html)

    # create files from readme
    #print(file_list)
