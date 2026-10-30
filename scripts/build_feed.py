#!/usr/bin/env python3
"""Monta o site do podcast (feed.xml + index.html) a partir dos episódios baixados.

Uso: python scripts/build_feed.py releases.json site/ https://usuario.github.io/radar-ia
releases.json: lista [{tagName, name, body, publishedAt}] (saída do gh release view --json).
Espera os áudios em site/audio/<tagName>.mp3.
"""
import html
import json
import subprocess
import sys
from datetime import datetime
from email.utils import format_datetime
from pathlib import Path

SHOW_TITLE = "Radar de IA &amp; Tecnologia"
SHOW_DESC = ("Briefing semanal sobre IA aplicada a engenharia de software, "
             "aplicações corporativas e arquitetura empresarial.")
AUTHOR = "Volmar"


def duration(path: Path) -> int:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True).stdout.strip()
    return int(float(out))


def md_links_to_html(text: str) -> str:
    """Converte o markdown simples das notas (linhas, **negrito**, [texto](url)) em HTML."""
    import re
    out = []
    for line in text.splitlines():
        line = html.escape(line, quote=False)
        line = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', line)
        line = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", line)
        line = re.sub(r"^#+\s*(.*)$", r"<b>\1</b>", line)
        line = re.sub(r"^[-*]\s+", "• ", line)
        out.append(line)
    return "<br/>\n".join(out)


def main() -> None:
    releases = json.loads(Path(sys.argv[1]).read_text())
    site = Path(sys.argv[2])
    base = sys.argv[3].rstrip("/")
    releases.sort(key=lambda r: r["publishedAt"], reverse=True)

    items, rows = [], []
    for r in releases:
        mp3 = site / "audio" / f"{r['tagName']}.mp3"
        if not mp3.exists():
            continue
        url = f"{base}/audio/{mp3.name}"
        pub = datetime.fromisoformat(r["publishedAt"].replace("Z", "+00:00"))
        secs = duration(mp3)
        notes = md_links_to_html(r.get("body") or "")
        items.append(f"""    <item>
      <title>{html.escape(r['name'])}</title>
      <guid isPermaLink="false">{r['tagName']}</guid>
      <pubDate>{format_datetime(pub)}</pubDate>
      <enclosure url="{url}" length="{mp3.stat().st_size}" type="audio/mpeg"/>
      <itunes:duration>{secs}</itunes:duration>
      <itunes:explicit>false</itunes:explicit>
      <description><![CDATA[{notes}]]></description>
    </item>""")
        rows.append(f'<li><a href="audio/{mp3.name}">{html.escape(r["name"])}</a> — {secs // 60} min</li>')

    now = format_datetime(datetime.now().astimezone())
    feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{SHOW_TITLE}</title>
    <link>{base}/</link>
    <atom:link href="{base}/feed.xml" rel="self" type="application/rss+xml"/>
    <language>pt-br</language>
    <description>{SHOW_DESC}</description>
    <lastBuildDate>{now}</lastBuildDate>
    <itunes:author>{AUTHOR}</itunes:author>
    <itunes:summary>{SHOW_DESC}</itunes:summary>
    <itunes:image href="{base}/cover.png"/>
    <itunes:category text="Technology"/>
    <itunes:explicit>false</itunes:explicit>
    <itunes:block>Yes</itunes:block>
{chr(10).join(items)}
  </channel>
</rss>
"""
    (site / "feed.xml").write_text(feed, encoding="utf-8")
    (site / "index.html").write_text(f"""<!doctype html><meta charset="utf-8">
<meta name="robots" content="noindex"><title>{SHOW_TITLE}</title>
<h1>{SHOW_TITLE}</h1><p>Feed: <code>{base}/feed.xml</code></p><ul>{''.join(rows)}</ul>
""", encoding="utf-8")
    print(f"feed com {len(items)} episódios")


if __name__ == "__main__":
    main()
