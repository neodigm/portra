from libxmp import XMPError
from libxmp.consts import XMP_NS_CameraRaw as NS_CRS

from portra.component.tags import LR_STRING_TAGS
from portra.component.tags import TC_TAGS_ARRAY
from portra.component.tags import TC_TAGS_STRING

def crs_tonecurve(xmp):
    tc = {}

    for t in TC_TAGS_ARRAY:
        tc[t] = xmp_get_array(xmp, NS_CRS, t)
    for t in TC_TAGS_STRING:
        tc[t] = xmp.get_property(NS_CRS, t)

    return tc

def xmp_get_array(xmp, schema_ns, array_name):
    arr = []
    idx = 1

    try:
        while True:
            arr.append(xmp.get_array_item(schema_ns, array_name, idx))
            idx = idx + 1
    except XMPError:
        pass
    return arr

def lr_get_settings(xmp, settings):
    s = {}
    for option, val in settings.items():
        try:
            v = xmp.get_property(NS_CRS, option)
            if v:
                val = v
        except XMPError:
            print('Missing tag ' + option + ': using default value of ' + str(val)) # for debugging purposes
        if option in LR_STRING_TAGS:
            val = '\"' + val + '\"'
        s[option] = val
    return s
