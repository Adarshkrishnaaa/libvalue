from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os
os.chdir(Path(__file__).parent)
print('LibValue AI running at http://localhost:4173', flush=True)
ThreadingHTTPServer(('127.0.0.1',4173),SimpleHTTPRequestHandler).serve_forever()
