#!/usr/bin/env python3

import os, json

print("Content-Type: application/json")
print()
#print(f"<p>HTTP_USER_AGENT = {os.environ['HTTP_USER_AGENT']}</p>")
#print(f"<p>QUERY_STRING = {os.environ['QUERY_STRING']}</p>")
print(json.dumps(dict(os.environ), indent = 2))
#print(os.environ)