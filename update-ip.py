import requests, json, time, datetime, os

def abs_path():
    return os.path.dirname(os.path.realpath(__file__))


ENDPOINT = abs_path() + "/docs/index.json"  # accessible in ...github.io/my-public-ip-api
UPDATE_INTERVAL = 10  # seconds in-between checks


def json_to_dict(filename):
    with open(filename, encoding="utf-8") as f:
        return json.load(f)


def dict_to_json(filename, _dict):
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(_dict, f)


def get_ip(endpoint):
    r = requests.get(endpoint)
    if r.status_code == 200: return r.json()["ip"]
    raise Exception("Unexpected error in api")


def get_served_version():
    return json_to_dict(ENDPOINT)


def get_current_version():
    return {
        "ipv4": get_ip("https://api.ipify.org/?format=json"),
        "ipv6": get_ip("https://api6.ipify.org/?format=json")
    }


def update_served(_new):
    # update the file
    dict_to_json(ENDPOINT, _new)
    # deploy
    os.chdir(abs_path())
    os.system("git pull")
    os.system("git add '%s'" % ENDPOINT)
    os.system('git commit -m "updated IP to %s at %s"' % (_new["ipv6"], now()))
    os.system("git push")



def now(): return datetime.datetime.now()


served = get_served_version()


def updated_if_needed():
    global served
    try: current = get_current_version()
    except Exception as e:
        print("[WARN] update failed at %s with error message: %s (will retry in %s seconds)" % (now(), e, UPDATE_INTERVAL))
        return
    if current != served:
        print("Updating [%s] to [%s] at %s..." % (served, current, now()), end="", flush=True)
        update_served(current)
        served = current
        print("DONE")


while True:
    updated_if_needed()
    time.sleep(UPDATE_INTERVAL)
