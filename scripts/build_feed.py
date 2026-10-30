#!/usr/bin/env python3
"""Monta o site do podcast (feed.xml + index.html) a partir dos episódios baixados.

Uso: python scripts/build_feed.py releases.json site/ https://usuario.github.io/radar-ia
releases.json: lista [{tagName, name, body, publishedAt}] (saída do gh release view --json).
Espera os áudios em site/audio/<tagName>.mp3.
"""
import html
import json
import re
import subprocess
import sys
from datetime import datetime
from email.utils import format_datetime
from pathlib import Path

SHOW_TITLE = "Radar de IA &amp; Tecnologia"
SHOW_DESC = ("Conversa semanal sobre IA: visão geral do mundo e um aprofundamento em engenharia "
             "de software e arquitetura empresarial. Apresentadores virtuais (vozes geradas por IA); "
             "fontes e links nas notas de cada episódio.")
AUTHOR = "Volmar"


def duration(path: Path) -> int:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True).stdout.strip()
    return int(float(out))


def inline(text: str) -> str:
    """Escapa HTML e converte [texto](url), **negrito** e *itálico* em tags."""
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*\s][^*]*)\*(?!\*)", r"<i>\1</i>", text)
    return text


def md_to_html(text: str) -> str:
    """Markdown simples → HTML que o app Podcasts exibe (p, b, i, a, ul, li)."""
    out, in_list = [], False
    for raw in text.splitlines():
        line = raw.strip()
        if re.match(r"^[-*]\s+", line):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(re.sub(r'^[-*]\s+', '', line))}</li>")
            continue
        if in_list:
            out.append("</ul>")
            in_list = False
        if not line:
            continue
        m = re.match(r"^#{1,6}\s*(.*)$", line)
        if m:
            out.append(f"<p><b>{inline(m.group(1))}</b></p>")
        else:
            out.append(f"<p>{inline(line)}</p>")
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def plain(text: str) -> str:
    """Versão em texto simples (itunes:summary): sem marcação, links viram 'texto (url)'."""
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r"\1 (\2)", text)
    text = re.sub(r"[*#]", "", text)
    return text.strip()


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
        body = r.get("body") or ""
        notes = md_to_html(body)
        items.append(f"""    <item>
      <title>{html.escape(r['name'])}</title>
      <guid isPermaLink="false">{r['tagName']}</guid>
      <pubDate>{format_datetime(pub)}</pubDate>
      <enclosure url="{url}" length="{mp3.stat().st_size}" type="audio/mpeg"/>
      <itunes:duration>{secs}</itunes:duration>
      <itunes:explicit>false</itunes:explicit>
      <itunes:summary><![CDATA[{plain(body)}]]></itunes:summary>
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
