from extensions import db


def remove_internals(d):
    return {k: v for (k, v) in d.items() if not k.startswith("_")}


def get_all_hosts():
    hosts = {host["hostname"]: remove_internals(host) for host in db.hosts.find()}
    return hosts


def set_host(host):

    existing_host = db.hosts.find_one({"hostname": host["hostname"]})

    if not existing_host:
        db.hosts.insert_one(host)
    else:
        db.hosts.update_one({"hostname": host["hostname"]}, {"$set": host})
