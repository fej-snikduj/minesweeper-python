def list_to_string(list, joiner):
        string = ''
        for item in list:
            string += str(item) + joiner
        return string
