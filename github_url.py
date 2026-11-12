#!/usr/bin/env python3
"""输入本地相对路径，生成 GitHub Pages 访问地址。

用法：
  python3 github_url.py cdn/CDN.html
  python3 github_url.py 笔记代码/cdn/CDN.html        # 带不带 笔记代码/ 前缀都可以
  python3 github_url.py a.html b.html                 # 支持多个文件
  python3 github_url.py                               # 交互式输入
"""
import subprocess
import sys
from urllib.parse import quote

BASE = "https://tilisuoo.github.io/knowledge-base/"


def to_url(path: str) -> str:
    p = path.strip().strip("'").strip('"').replace("\\ ", " ")
    marker = "笔记代码/"
    idx = p.find(marker)
    if idx != -1:
        p = p[idx + len(marker):]
    p = p.lstrip("./").lstrip("/")
    return BASE + quote("笔记代码/" + p)


def main() -> None:
    args = sys.argv[1:]
    if not args:
        args = [input("请输入相对路径（如 cdn/CDN.html）：")]
    urls = [to_url(a) for a in args]
    for u in urls:
        print(u)
    if len(urls) == 1:
        try:
            subprocess.run(["pbcopy"], input=urls[0], text=True, check=True)
            print("（已复制到剪贴板）", file=sys.stderr)
        except Exception:
            pass


if __name__ == "__main__":
    main()
