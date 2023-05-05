import cgi

from jinja2 import Template

class Project:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def get_projects():
    projects = []
    with open('projects.txt', 'r') as f:
        for line in f:
            name, description = line.split(':')
            projects.append(Project(name, description))
    return projects

#set up cgi
form = cgi.FieldStorage()

try:
    projects = get_projects()
    with open('projects_template.html', 'r') as f:
        template = Template(f.read())

    print("Content-Type: text/html\n\n")

    print(template.render(projects=projects))
except Exception as e:
    print("Content-Type: text/html\n\n")
    print(f"""<!DOCTYPE html>
<html>
<head>
    <title>Projects</title>
</head>
<body>
    <h1>ПРОИЗОШЛА ОШИБКА, СОРЕ, У НАС ПРОБЛЕМЫ</h1>
    <p>{e}</p>
</body>
</html>""")
    exit()



