from pprint import pprint
from ov_config_loader import try_load_from_file
from hpOneView.exceptions import HPOneViewException
from hpOneView.oneview_client import OneViewClient

def createClient(config):
    config = try_load_from_file(config)
    oneview_client = OneViewClient(config)
    return oneview_client

if __name__ == "__main__":
    config = "config.json" # config.json is at the same directory
    client = createClient(config)
    egs = oneview_client.enclosure_groups.get_all() 
    print(client)

