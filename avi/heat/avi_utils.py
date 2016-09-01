import uuid

# for python 2/3 compatibility
try:
    basestring
except:
    basestring = str


def os2avi_uuid(obj_type, eid):
    uid = str(uuid.UUID(eid))
    return obj_type + "-" + uid


def fix_dict_refs(obj):
    for k in obj.keys():
        if k.endswith("_refs") or k.endswith("_ref"):
            newval = fix_non_dict_refs(obj[k])
            obj.pop(k)
            new_key = "uuid".join(k.rsplit("ref", 1))
            obj[new_key] = newval
        elif isinstance(obj[k], dict):
            obj[k] = fix_dict_refs(obj[k])
    return obj


def fix_non_dict_refs(obj):
    if isinstance(obj, list):
        nlist = []
        for k in obj:
            nlist.append(fix_non_dict_refs(k))
        return nlist
    elif isinstance(obj, basestring):
        return obj.split("/")[-1].split("#")[0]
    return obj


def cmp_a_in_b(a, b):
    if isinstance(a, dict):
        for k in a.keys():
            if k not in b or not cmp_a_in_b(a[k], b[k]):
                return False
        return True

    if isinstance(a, list):
        return all(
            any(cmp_a_in_b(aitem, bitem) for bitem in b)
            for aitem in a)

    return a == b
