#!/usr/bin/env python3
"""Publish the current चक्र build to GitHub Pages: copy the given HTML, inject the phone layout, commit, push.
Usage: python3 publish.py /path/to/chakra-mvp-vX.html "message" """
import sys, subprocess, os
src, msg = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "publish")
MOBILE = """  /* MOBILE (injected at publish) */
  @media (max-width: 900px){
    .app{display:block}
    aside{position:static;height:auto;padding:12px 0 6px}
    aside .brand{padding:0 14px 8px}
    aside .foot{display:none}
    .expick{display:flex;gap:8px;padding:6px 14px 8px;flex-wrap:wrap}
    .expick label{display:none}
    .expick select{width:auto;flex:1;min-width:140px}
    .navstep{display:inline-flex;width:auto;padding:6px 10px;font-size:13px}
    .navstep .num{width:18px;height:18px;font-size:10px}
    main{padding:14px 12px 60px;max-width:none}
    h1{font-size:19px}
    .player{grid-template-columns:1fr}
    .rail{position:static;display:flex;overflow-x:auto;gap:4px;padding:6px}
    .rail .grp{display:none}
    .rail button{white-space:nowrap;padding:6px 8px;font-size:12px}
    .grid2,.three{grid-template-columns:1fr}
    .tiles{grid-template-columns:1fr 1fr}
    table{font-size:12.5px}
    .drawh .dt{font-size:14.5px}
    .chit{padding:8px 10px;font-size:13px}
    .navbtns{gap:6px}
  }
</style>"""
s = open(src, encoding="utf-8").read()
if "MOBILE (injected at publish)" not in s: s = s.replace("</style>", MOBILE, 1)
if '<meta name="viewport"' not in s: s = s.replace("<head>", '<head>\n<meta name="viewport" content="width=device-width, initial-scale=1.0">', 1)
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html"), "w", encoding="utf-8").write(s)
subprocess.run(["git","add","-A"], check=True); subprocess.run(["git","-c","user.name=Saumya Jha","-c","user.email=saumyajha4669@gmail.com","commit","-q","-m",msg], check=True); subprocess.run(["git","push","-q"], check=True)
print("published", len(s), "chars")
