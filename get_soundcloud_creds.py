import re
from urllib.request import urlopen

"""
Logic ported from https://github.com/DevAndromeda/soundcloud-scraper/blob/master/src/util/Util.js#L179
"""

SOUNDCLOUD_BASE_URL = "https://soundcloud.com"
SOUNDCLOUD_SCRIPT_ELEMENT_REGEX = re.compile(r'<script( crossorigin)? src="(.*?)"')
SOUNDCLOUD_JSON_KEY_REGEX = re.compile(r'client_id:"(.*?)"')

def get_soundcloud_key(url: str):
    html = urlopen(url).read().decode('utf-8')
    for match in SOUNDCLOUD_SCRIPT_ELEMENT_REGEX.finditer(html):
        js_url = match.group(2)
        js = urlopen(js_url).read().decode('utf-8')
        if match := SOUNDCLOUD_JSON_KEY_REGEX.search(js):
            key = match.group(1)
            return key

if __name__ == "__main__":
    print(get_soundcloud_key(SOUNDCLOUD_BASE_URL))
