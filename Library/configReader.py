import configparser

def read_config(section, key):
    config = configparser.ConfigParser() 
    config.read("./Config/config.cfg") 
    return config.get(section, key)

def get_locator(section, key):
    config = configparser.ConfigParser() 
    config.read("./Config/elements.cfg") 
    return config.get(section, key)

print (read_config("Details","app_url"))
# print (read_config("Details","browser"))