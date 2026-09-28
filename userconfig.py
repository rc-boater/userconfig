def add_setting(settings, pair):
    key = pair[0].lower()
    value = pair[1].lower()

    if not settings.get(key) == None:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    if settings.get(key) == None:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"
    
def update_setting(settings, pair):
    key = pair[0].lower()
    value = pair[1].lower()

    if not settings.get(key) == None:
        settings.update({key: value})
        return f"Setting '{key}' updated to '{value}' successfully!"
    if settings.get(key) == None:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()

    if not settings.get(key) == None:
        settings.pop(key, settings.get(key))
        return f"Setting '{key}' deleted successfully!"
    if settings.get(key) == None:
        return "Setting not found!"

def view_settings(settings):
    if settings == {}:
        return 'No settings available.'
    else:
        view = 'Current User Settings:\n'
        for key in settings:
            capi_key = key.capitalize()
            view = view + capi_key + ': ' + settings.get(key) + '\n'
        return view

test_settings = {
    'theme': 'dark',
    'mode': 'Green'
}

print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}))
