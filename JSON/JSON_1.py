import json
f = open('foldrs_tree.json', 'w', encoding='utf-8')

folders_tree = {'my_project': ('settings', 'mainapp', 'adminapp', 'authapp')}

json.dump(folders_tree, f)
f.close()
