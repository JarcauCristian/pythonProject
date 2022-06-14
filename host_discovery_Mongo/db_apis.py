from datetime import datetime

from extensions import db


def remove_internals(d):
    return {k: v for (k, v) in d.items() if not k.startswith("_")}


def get_all_hosts():
    hosts = {host["hostname"]: remove_internals(host) for host in db.hosts.find()}
    return hosts


def get_host(hostname):
    host = db.hosts.find({"hostname": hostname}, {"_id": 0})
    return host


def get_host_status(host, datapoints):
    status = db.hosts_status.find({"hostname": host}, {"_id": 0}).sort("time", 1).limit(datapoints)
    return status


def set_host(host):

    existing_host = db.hosts.find_one({"hostname": host["hostname"]})

    if not existing_host:
        db.hosts.insert_one(host)
    else:
        db.hosts.update_one({"hostname": host["hostname"]}, {"$set": host})

    host_status = {
        "time": str(datetime.now())[:-3],
        "hostname": host["hostname"],
        "availability": host["availability"],
    }

    db.hosts_status.insert_one(host_status)
