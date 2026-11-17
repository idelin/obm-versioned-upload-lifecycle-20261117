import json
from pathlib import Path
from blobs import Blobs
class Service:
    def __init__(self,root):
        self.root=Path(root);self.root.mkdir(exist_ok=True);self.blobs=Blobs(self.root/'blobs');self.index={}
        p=self.root/'index.json'
        if p.exists():self.index=json.loads(p.read_text())
    def apply(self,q):
        if q['op']=='put':
            raw=bytes.fromhex(q['data_hex']);digest=self.blobs.put(raw);self.index[q['key']]=digest
            (self.root/'index.json').write_text(json.dumps(self.index));return {'sha256':digest,'size':len(raw)}
        if q['op']=='get':
            digest=self.index.get(q['key'])
            return {'data_hex':self.blobs.get(digest).hex()} if digest else {'error':'NOT_FOUND'}
        return {'error':'UNSUPPORTED'}
