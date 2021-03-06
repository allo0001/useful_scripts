import yaml.dumper as d

with open('yaml.yaml', 'w') as f:
    d({'folder1': ('folder1_1', 'folder1_2'),
           'folder2': ('folder2_1', 'folder2_2')})

# with open('info.yaml') as f:
#     templates = yaml.safe_load(f)

# print(templates)