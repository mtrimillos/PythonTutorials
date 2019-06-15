import math
import sys
from os import rename

import requests


r = requests.get("https://coreyms.com")
print(r.status_code)
print(r.ok)