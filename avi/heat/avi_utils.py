import uuid

# for python 2/3 compatibility
try:
    basestring
except:
    basestring = str


def os2avi_uuid(obj_type, eid):
    uid = str(uuid.UUID(eid))
    return obj_type + "-" + uid


def fix_non_dict_refs(obj):
    if isinstance(obj, list):
        nlist = []
        for k in obj:
            nlist.append(fix_non_dict_refs(k))
        return nlist
    elif isinstance(obj, basestring):
        return obj.split("/")[-1].split("#")[0]
    return obj


def replace_refs_with_uuids(a):
    if isinstance(a, dict):
        for k in a.keys():
            nk = None
            if k.endswith("_refs"):
                nk = k[:-4] + "uuids"
            elif k.endswith("_ref"):
                nk = k[:-3] + "uuid"
            if nk:
                a[nk] = fix_non_dict_refs(a[k])
                a.pop(k)
            else:
                replace_refs_with_uuids(a[k])
    elif isinstance(a, list):
        for elem in a:
            replace_refs_with_uuids(elem)
    return a


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
