import json

file_path = "C:/Users/wyh/Desktop/manager/auto_tools_master/deployment_tools/123.txt"

dist_demo = {"textfile": "hello"}

obj = json.dumps(dist_demo)
print(obj)
with open(file_path, 'a') as f:
    f.write(obj)
