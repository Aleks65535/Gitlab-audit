import os
import gitlab

guest = 'Guest'
reporter = 'Reporter'
developer = 'Developer'
maintainer = 'Maintainer'
owner = 'Owner'

def parse_level (access_level):
    result = ''
    if access_level == 10:
        result = guest
    elif access_level == 20:
        result = reporter
    elif access_level == 30:
        result = developer
    elif access_level == 40:
        result = maintainer
    elif access_level == 50:
        result = owner
    return result

gl = gitlab.Gitlab('urt_gitlab', 'private_token')
projects = gl.projects.list(all=True)
length=len(projects)
i=0
f = open('gitlab.csv', 'w')
while i < length:
    project = gl.projects.get(projects[i].id)
    members = project.members.all(all=True)
    new_members = []
    for m in members:
        if m.state == "active":
            new_members.append(m)
    members_length = len(new_members)
    m=0
    while m < members_length:
        member = new_members[m]
        f.write(project.name_with_namespace +';'+ member.name +';'+ parse_level(member.access_level) + '\n')
        m=m+1
    i=i+1
f.close()