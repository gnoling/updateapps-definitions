#!/usr/bin/env python3
# Rewrites the "## Definitions" section of README.md from apps.d/*.yaml.
# Usage: tools/readme-table.py [REPO_DIR]
import glob, os, re, sys
from urllib.parse import urlsplit

import yaml

root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATEGORIES = {"emulators": "Emulators", "ports": "Ports and recompilations", "tools": "Tools"}


def upstream(s):
    t, repo = s.get("type", ""), s.get("repo")
    if t in ("github-release", "github-actions") and repo:
        return f"[{repo}](https://github.com/{repo})"
    if t in ("gitlab", "forgejo"):
        host = s.get("host", "gitlab.com" if t == "gitlab" else "").rstrip("/")
        if not host.startswith("http"):
            host = "https://" + host
        proj = s.get("project") or repo or ""
        return f"[{proj}]({host}/{proj})"
    if t == "flatpak":
        return f"flatpak `{s.get('ref') or s.get('app') or ''}`"
    if t == "script":
        code = s.get("lua") or open(os.path.join(root, "apps.d", s["script_file"])).read()
        m = re.search(r'https?://[^\s"\')]+', code)
        return f"Lua, [{urlsplit(m.group(0)).netloc}]({m.group(0)})" if m else "Lua"
    url = s.get("url") or ""
    return f"[{urlsplit(url).netloc}]({url})" if url else t


rows, count = {}, 0
for f in sorted(glob.glob(os.path.join(root, "apps.d", "*.yaml"))):
    d = yaml.safe_load(open(f))
    aid = os.path.basename(f)[:-5]
    note = " *(disabled)*" if d.get("enabled") is False else ""
    name = d.get("name", aid).replace("|", "\\|")
    desc = d.get("description", "").replace("|", "\\|")
    rows.setdefault(d.get("category", "other"), []).append(
        f"| [{name}](apps.d/{aid}.yaml){note} | {desc} | {upstream(d.get('source', {}))} |")
    count += 1

out = ["## Definitions", ""]
if count > 1:
    out += [f"{count} definitions. *(disabled)* marks ones that stay off even for a repository that enables",
            "everything by default (upstream archived or moved); their `notes:` say why.", ""]
for c in list(CATEGORIES) + sorted(c for c in rows if c not in CATEGORIES):
    if c not in rows:
        continue
    if len(rows) > 1:
        out += [f"### {CATEGORIES.get(c, c.title())}", ""]
    out += ["| Definition | Description | Upstream |", "|---|---|---|"]
    out += sorted(rows[c], key=str.lower)
    out.append("")

readme = os.path.join(root, "README.md")
text = open(readme).read()
m = re.search(r"^## Definitions\n.*?(?=^## |\Z)", text, re.S | re.M)
if not m:
    sys.exit("README.md has no '## Definitions' section")
section = "\n".join(out).rstrip("\n") + "\n"
text = text[:m.start()] + section + ("\n" if text[m.end():] else "") + text[m.end():]
open(readme, "w").write(text)
print(f"{count} definitions")
