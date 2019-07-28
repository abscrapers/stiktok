

import requests
from atomicwrites import atomic_write
from superjson import json


m_tiktok_base_url = "https://m.tiktok.com"
signature = "Get this some somehow"

nyan_profile = "http://www.tiktok.com/@nyannyancosplay"
# html_path = "./ab.html"

html_content = requests.get(
    nyan_profile, timeout=7, headers={'User-Agent': 'Mozilla/5.0'}
).text

# with atomic_write(html_path, mode='w', overwrite=True) as html_file:
#     html_file.write(html_content)

begin_string = "window.__INIT_PROPS__"
start = html_content.index(begin_string) + len(begin_string)
end = html_content.index("</head>")
trimmed_down = html_content[start:end]

start = trimmed_down.index("{")
end = trimmed_down.rindex("}") + 1
json_string = trimmed_down[start:end]

json_obj = json.loads(json_string)

# json_obj = json.load("./init_props.json")

single_key = next(iter(json_obj))

json_obj = json_obj[single_key]

user_data = json_obj["userData"]

first_url = m_tiktok_base_url + (
    "/share/item/list"
    f"?secUid={user_data['secUid']}"
    f"&id={user_data['userId']}"
    "&type=1"
    "&count=48"
    "&minCursor=0"
    "&maxCursor=0"
    f"&_signature={signature}"
)

# TODO this is not working. Probably wong headers
response = requests.get(first_url).json()
print(response)
