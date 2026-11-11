import concurrent.futures, json, pathlib, urllib.request
from PIL import Image
import io
entries=json.loads(pathlib.Path('.github/asset-recovery.json').read_text())
def fetch(e):
 try:
  req=urllib.request.Request(e['url'],headers={'User-Agent':'Mozilla/5.0'})
  with urllib.request.urlopen(req,timeout=30) as response: data=response.read()
  Image.open(io.BytesIO(data)).verify()
  for target in e['paths']:
   p=pathlib.Path('recovered')/target;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
  return {'url':e['url'],'ok':True,'paths':e['paths']}
 except Exception as exc:return dict(e,ok=False,error=str(exc))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: results=list(pool.map(fetch,entries))
pathlib.Path('recovered').mkdir(exist_ok=True)
pathlib.Path('recovered/results.json').write_text(json.dumps(results,indent=2))
print(json.dumps({'ok':sum(e['ok'] for e in results),'failed':sum(not e['ok'] for e in results)}))
