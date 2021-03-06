from pprint import pprint
import ov_create_client
import os
import sys
import json
import yaml
import copy

'''
config = "config.json" # config.json is at the same directory
oneview_client = ov_create_client.createClient(config)

basic_profile_options = dict(
    name = "",
    serverHardwareUri = "",
    enclosureGroupUri = oneview_client.enclosure_groups.get_all()[0]['uri']
)
'''
def getServerProfileByName(name):
    profile = oneview_client.server_profiles.get_by_name(name)
    if profile is None:
        print("Retrieved an empty profile")
    return(profile)

def getAllServerProfile():
    all_profiles = oneview_client.server_profiles.get_all()
    for profile in all_profiles:
        pprint(profile['name'])

def createServerProfile(basic_profile_options):
    basic_profile = oneview_client.server_profiles.create(basic_profile_options)
    return basic_profile

def createServerProfileTemplate(basic_template_options):
    # Generate a new Server Profile Template based on an existing Server Profile
    x = oneview_client.server_profile_templates.create(basic_template_options)

def getAllServerProfileTemplate():
    all_templates = oneview_client.server_profile_templates.get_all()
    jsonStrings = json.dumps(all_templates)
    return jsonStrings

def ReturnAllServerProfileTemplatesNamesOnly():
    all_templates = oneview_client.server_profile_templates.get_all()
    names_only = []
    for t in all_templates:
        names_only.append(t["name"])
    return names_only

def getSingleServerProfileTemplateByName(STPname):
    t = oneview_client.server_profile_templates.get_by_name(STPname)
    jsonStrings = json.dumps(t)
    return jsonStrings

def writeToFile(content, targetFilePath="SPT.json"):
    if content is not None:
        with open(targetFilePath, 'w') as file:
            file.write(str(content))
            return 0

def convertDictionaryToYaml(inputFile="SPT.json"):
    if inputFile is not None:
        with open(inputFile, "r") as file:
            text = file.read()
            textJSON = json.dumps(json.loads(text))
            #print(textJSON)
            SPT_yml = yaml.dump(yaml.load(textJSON,Loader = yaml.SafeLoader),default_flow_style=False)
            return SPT_yml
    return None

def readFile(fileName):
    text = None
    with open(fileName) as file:
        text = json.loads(file.read())
    x = removeUri(text)
    print(x)

def removeUri(myDict):
    for key, value in myDict.copy().items(): # shallow copy for iterations/tracking. Modify the original dictionary.
        if isinstance(value, dict):
            removeUri(myDict[key])
        elif isinstance(value, list):
            for i in myDict[key]:
                if isinstance(i, dict):
                    removeUri(i)
                else:
                    pass
        else:
            if "uri" in key or "Uri" in key:
                #print(key)
                del myDict[key]
    return myDict




if __name__ == "__main__":
    
    #ans = ReturnAllServerProfileTemplatesNamesOnly()
    #print(ans)
    #nathan = getSingleServerProfileTemplateByName("compare_profile")
    #writeToFile(nathan, "nathan-profile.txt")
    #nathan_SPT_yaml = convertDictionaryToYaml("nathan-profile.txt")
    #writeToFile(nathan_SPT_yaml, "nathan-profile_SPT.yml")
    
    '''
    o = convertDictionaryToYaml("test.json")
    print(o)
    writeToFile(o, "o.yml")

    o2 = convertDictionaryToYaml("test2.json")
    print(o2)
    writeToFile(o2, "o2.yml")

    o3 = convertDictionaryToYaml("test3.json")
    print(o3)
    writeToFile(o3, "o3.yml")

    o4=convertDictionaryToYaml("test4.json")
    print(o4)
    writeToFile(o4, "o4.yml")
    '''
    tempTest = convertDictionaryToYaml("SPT_json_temp.json")
    print(tempTest)
