import yaml

with open("../openapi/openapi.yaml", 'r') as stream:
    try:
        dict_yaml = yaml.safe_load(stream)
        list_keys = list()
        # print(dict_yaml)
        # for value in dict_yaml:
        #     list_keys.append(value)
        # for elem in list_keys:
        #     print(f'{elem} == {dict_yaml[elem]}', end='\n\n')

        paths = dict_yaml['paths']
        components = dict_yaml['components']

        for elem in paths:
            print(f'{elem} == {paths[elem]}', end='\n\n')

    except yaml.YAMLError as exc:
        print(exc)

