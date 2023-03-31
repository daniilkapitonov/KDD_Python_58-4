def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    for word in ignore:
        if word in command:
            return True
    return False

def ing(command):
    ignore = ['alias', 'configuration', 'ip', 'sql',
               'select', 'update', 'exec', 'del', 'truncate']
    return any(map(lambda w: True if command in w else False, ignore))

print(ignore_command('alias'))
print(ing('alias'))
print(ignore_command('ss'))
print(ing('asslias'))