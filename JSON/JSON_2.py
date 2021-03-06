import json
f = open('foldrs_tree_2.json', 'w', encoding='utf-8')

folders_tree = {
    "my_project": {
        "settings": {
            "__init__.py": 'file',
            "dev.py": 'file',
            "prod.py": 'file'
                    },
        "mainapp": {
            "__init__.py": 'file',
            "models.py": 'file',
            "views.py": 'file',
            "templates": {
                "mainapp": {
                    "base.html": 'file',
                    "index.html": 'file'
                           }
                         }
                    },
        "authapp": {
            "__init__.py": 'file',
            "models.py" : 'file',
            "views.py": 'file',
            "templates": {
                "authapp": {
                    "base.html": 'file',
                    "index.html": 'file'
                            }
                        }
                    }
                }
}
json.dump(folders_tree, f)
f.close()
