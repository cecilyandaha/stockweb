# @Time : 2020/1/15 14:16
# @Author : lisalou
# @File : tool.py
# @Software : PyCharm

def list_to_dict(objlist):
    dicts=[]
    for obj in objlist:
        print(obj.to_mongo())
        #print(obj.__dict__)
    return dicts


def object_to_dict(obj):
    keys=obj.keys()
    for key in keys:
        print(obj[key])
    return keys


