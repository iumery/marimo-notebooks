#!/usr/bin/env python3

import os
import subprocess
import argparse
from typing import List
from pathlib import Path
import shutil


def export_html_wasm(notebook_path: str, output_dir: str, as_app: bool = False) -> bool:
    """Export a single marimo notebook to HTML format.

    Returns:
        bool: True if export succeeded, False otherwise
    """
    output_path = notebook_path.replace(".py", ".html")

    cmd = ["marimo", "export", "html-wasm"]
    if as_app:
        print(f"Exporting {notebook_path} to {output_path} as app")
        cmd.extend(["--mode", "run", "--no-show-code"])
    else:
        print(f"Exporting {notebook_path} to {output_path} as notebook")
        cmd.extend(["--mode", "edit"])

    try:
        output_file = os.path.join(output_dir, output_path)
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        cmd.extend([notebook_path, "-o", output_file])
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error exporting {notebook_path}:")
        print(e.stderr)
        return False
    except Exception as e:
        print(f"Unexpected error exporting {notebook_path}: {e}")
        return False


def main() -> None:
    parser = argparse.ArgumentParser(description="Build marimo notebooks")
    parser.add_argument(
        "--output-dir", default="_site", help="Output directory for built files"
    )
    args = parser.parse_args()

    all_notebooks: List[str] = []
    for directory in ["notebooks", "apps"]:
        dir_path = Path(directory)
        if not dir_path.exists():
            print(f"Warning: Directory not found: {dir_path}")
            continue

        all_notebooks.extend(str(path) for path in dir_path.rglob("*.py"))

    if not all_notebooks:
        print("No notebooks found!")
        return

    # Export notebooks sequentially
    for nb in all_notebooks:
        export_html_wasm(nb, args.output_dir, as_app=nb.startswith("apps/"))

    # Generate index only if all exports succeeded
    # Copy all standalone .html files to the output directory
    for html_file in Path(".").glob("*.html"):
        if (
            html_file.name != "index.html"
        ):  # Avoid duplicating index, we handle it below
            target_file = Path(args.output_dir) / html_file.name
            shutil.copyfile(html_file, target_file)
            print(f"Copied {html_file} to {target_file}")

    # Use custom, manually written index.html
    custom_index = Path("index.html")  # Or wherever you place it
    target_index = Path(args.output_dir) / "index.html"

    if custom_index.exists():
        shutil.copyfile(custom_index, target_index)
        print("Copied static index.html to _site/")
    else:
        print("Warning: index.html not found!")

    # Copy assets (e.g., images) into _site/assets
    assets_src = Path("assets")
    assets_dst = Path(args.output_dir) / "assets"

    if assets_src.exists():
        shutil.copytree(assets_src, assets_dst, dirs_exist_ok=True)


if __name__ == "__main__":
    main()
