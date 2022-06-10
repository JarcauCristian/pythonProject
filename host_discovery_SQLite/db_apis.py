from pprint import pprint

from db_classes import db, HOSTS


def get_as_dict(model_obj):
    return {k: v for (k, v) in model_obj.__dict__.items() if not k.startswith("_")}

def get_all_hosts():
    host_objs = db.session.query(HOSTS).all()
    hosts = {host_obj.hostname: get_as_dict(host_obj) for host_obj in host_objs}
    return hosts

def set_host(host):

    search = {"hostname": host["hostname"]}
    #host_obj = db.session.query(HOSTS).filter_by(**search).one_or_none()
    host_obj = db.session.query(HOSTS).filter_by(hostname=host["hostname"]).one_or_none()
    if not host_obj:
        host_obj = HOSTS(**host)
        db.session.add(host_obj)
    else:
        if "ipaddr" in host:
            host_obj.ipaddr = host["ipaddr"]
        if "macaddr" in host:
            host_obj.ipaddr = host["macaddr"]
        if "avail" in host:
            host_obj.ipaddr = host["avail"]
        if "last_heard" in host:
            host_obj.ipaddr = host["last_heard"]

    db.session.commit()