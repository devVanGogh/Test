"""Best-effort heuristic check; manual confidentiality review is still mandatory."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = [
    re.compile(r"(?i)ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"(?i)github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"(?i)sk-[A-Za-z0-9]{20,}"),
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    re.compile(r"(?i)(?:C:\\Users\\|C:\\AI\\|/home/[^/]+/)")
]
violations = []
for path in ROOT.rglob("*"):
    if not path.is_file() or path.name == "safe_share_check.py":
        continue
    if path.suffix.lower() not in (".py", ".md", ".json", ".yml", ".txt"):
        continue
    body = path.read_text(encoding="utf-8")
    if any(pattern.search(body) for pattern in PATTERNS):
        violations.append(str(path.relative_to(ROOT)))
if violations:
    raise SystemExit("Potential sensitive content: " + ", ".join(violations))
print("PASS: no obvious secrets or private desktop paths found; review manually.")
