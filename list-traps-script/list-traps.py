#!/usr/bin/env python3
"""Find <span> elements with class 'trap-invis' or 'trap-hotswap' in an HTML file."""

import sys
import textwrap
from bs4 import BeautifulSoup


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path-to-html-file>", file=sys.stderr)
        sys.exit(1)

    html_path = sys.argv[1]

    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    invis_spans = soup.find_all("span", class_="trap-invis")
    hotswap_spans = soup.find_all("span", class_="trap-hotswap")

    if invis_spans:
        print(f"===== Invisible Traps ({len(invis_spans)}) =====")
        print()
        for i, span in enumerate(invis_spans, 1):
            print(f"{i}.")
            print(span.decode_contents())
            print()

    if hotswap_spans:
        print()
        print()
        print(f"===== Hotswap Traps ({len(hotswap_spans)}) =====")
        print()
        for i, span in enumerate(hotswap_spans, 1):
            replacement = span.get("data-replacement", "(none)")
            print(f"{i}.")
            print("Visible text:")
            print(textwrap.indent(span.decode_contents(), "    "))
            print("Replacement (trap text):")
            print(textwrap.indent(replacement, "    "))
            print()

    total = len(invis_spans) + len(hotswap_spans)
    if total == 0:
        print("No invisible traps or hotswap traps found.")
    else:
        print(f"\nTotal: {total}")


if __name__ == "__main__":
    main()
