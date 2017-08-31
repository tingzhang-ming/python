import sys
try:
    import json5 as myjson
except ImportError:
    import json as myjson

def ansible_result_parse(output):
    success_msg = ""
    fail_msg = ""
    try:
        output = myjson.loads(output)
    except Exception:
        output = "{" + output.split("{", 1)[1]  # Some error messages maybe appear before the json string
        try:
            output = myjson.loads(output)
        except KeyError:
            fail_msg += "fail to parse ansible output:\n"
            fail_msg += output
            return

    for play in output["plays"]:
        for task in play["tasks"]:
            for host, detail in task["hosts"].items():
                if "skipped" in detail.keys() and detail["skipped"] == True:
                    continue
                if detail["failed"] == False:
                    if "msg" in detail.keys():
                        success_msg += detail["msg"] + "\n"
                    if "stdout" in detail.keys():
                        success_msg += detail["msg"] + "\n"
                if detail["failed"] == True:
                    if detail["msg"] == "MODULE FAILURE":
                        fail_msg += detail["module_stderr"] + "\n"
                    else:
                        fail_msg += detail["msg"] + "\n"
    return myjson.dumps(dict(success_msg = success_msg,
                             fail_msg = fail_msg))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        myjson.dumps(dict(success_msg="",
                          fail_msg="No output to parse."))
        sys.exit(0)
    print ansible_result_parse(sys.argv[1])



