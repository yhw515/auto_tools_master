import os, sys, json

#############################
# NAME:wangyunhui
# EMAIL:15655267350@163.com
##############################
apps_file_path = "C:/Users/wyh/Desktop/manager/auto_tools_master/deployment_tools/apps.txt"
datasets_file_path = "C:/Users/wyh/Desktop/manager/auto_tools_master/deployment_tools/datasets.xml"
json_file_path = "C:/Users/wyh/Desktop/manager/auto_tools_master/deployment_tools/LNC-apps.json"


def read_apps(file_path):
    """
    read the file of apps, return apps list
    :param file_path: the path of apps file
    :return: apps list
    """
    result = []
    with open(file_path, "r+") as f:
        contents = f.readlines()
        for line in contents:
            if len(line) > 1:
                result.append(line.strip())
                print("导入应用  " + line.strip() + "  成功!!!")
    print()
    print()
    return result


def write_datasets(file_path, apps_list):
    """
    write dataset to datasets file
    :param file_path: the path of datasets file
    :param apps_list: apps list
    :return: NONE
    """
    with open(file_path, "w+") as f:
        f.write("<datasets>%s" % ("\n",))
        print(app_list)
        for app in apps_list:
            f.write('<dataset name="%s-dataset">%s' % (app, "\n"))
            f.write('   <uriname>/%s/{YEAR}/{DAY}/%s' % (app, "\n"))
            f.write('   </uriname>%s' % ("\n",))
            f.write('</dataset>%s' % ("\n",))
        f.write('</datasets>%s' % ("\n",))


def write_json(file_path, apps_list, verson):
    """

    :param file_path:
    :param apps_list:
    :return:
    """
    result_dict = {"hadoop-002": []}
    for app in app_list:
        jsonfile = {"textfile": app + verson + ".tar.gz", "excelfile": app + verson + ".xls"}
        result_dict["hadoop-002"].append(jsonfile)

    with open(json_file_path, 'w+') as f:
        f.write(json.dumps(result_dict, indent=4))


if __name__ == '__main__':
    app_list = read_apps(apps_file_path)
    write_datasets(datasets_file_path, app_list)
    write_json(json_file_path, app_list, "1.31.0")
