import json
import os
import re


ROOT_DIR = os.path.dirname(os.path.dirname(__file__))


def test_webmanifest_icons_exist():
    """Site webmanifest parses as JSON and icon paths exist."""
    manifest_path = os.path.join(ROOT_DIR, "site.webmanifest")
    with open(manifest_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert "icons" in data, "Manifest missing 'icons' field"
    for icon in data.get("icons", []):
        src = icon.get("src", "").lstrip("/")
        assert src, "Icon entry missing src"
        icon_path = os.path.join(ROOT_DIR, src)
        assert os.path.exists(icon_path), f"Icon path {src} does not exist"


def test_index_references_exist():
    """Ensure referenced local paths in index.html actually exist."""
    index_path = os.path.join(ROOT_DIR, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    # find href="..." or src="..." attributes
    pattern = re.compile(r"(?:href|src)=\"([^\"]+)\"")
    paths = pattern.findall(content)

    for path in paths:
        # Skip external links
        if path.startswith("http") or path.startswith("mailto:"):
            continue
        local_path = path.lstrip("/")
        assert os.path.exists(os.path.join(ROOT_DIR, local_path)), (
            f"Referenced file {path} does not exist")
