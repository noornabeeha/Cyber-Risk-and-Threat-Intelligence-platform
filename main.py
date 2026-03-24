import json
from dotenv import load_dotenv
load_dotenv()

from scanners.risk_scoring import getScore


result = getScore("scanme.nmap.org")
print(json.dumps(result, indent=2, default=str))