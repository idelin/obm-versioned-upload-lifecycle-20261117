import sys,json
from service import Service
service=Service(sys.argv[1])
for line in sys.stdin:
    print(json.dumps(service.apply(json.loads(line))),flush=True)
