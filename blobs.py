import hashlib,os
from pathlib import Path
class Blobs:
    def __init__(self,root):self.root=Path(root);self.root.mkdir(exist_ok=True)
    def put(self,data):
        digest=hashlib.sha256(data).hexdigest();p=self.root/digest
        with p.open('wb') as f:f.write(data);f.flush();os.fsync(f.fileno())
        return digest
    def get(self,digest):return (self.root/digest).read_bytes()
