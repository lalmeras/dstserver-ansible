def ini_items(ini_dict):
    return [
        dict(section=section,key=value[0],value=value[1])
        for section in ini_dict.iterkeys()
        for value in ini_dict[section].items()
    ]


class FilterModule(object):
    def filters(self):
        return {
            'ini_items': ini_items
        }
