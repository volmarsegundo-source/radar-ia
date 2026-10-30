#!/usr/bin/env python3
"""Gera o MP3 de um episódio a partir do roteiro usando Google Cloud Text-to-Speech.

Uso: python scripts/tts.py episodes/2026-11-02
Lê  <pasta>/roteiro.txt e grava <pasta>/episodio.mp3 (não versionado).

Variáveis de ambiente:
  GOOGLE_TTS_API_KEY  chave de API do Google Cloud com a Text-to-Speech API habilitada
  TTS_VOICE           voz (padrão: pt-BR-Chirp3-HD-Charon)
  TTS_RATE            velocidade (padrão: 1.0)
"""
import base64
import json
import os
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

MAX_BYTES = 4500  # limite da API é 5000 bytes por requisição
API = "https://texttospeech.googleapis.com/v1/text:synthesize?key={key}"


def split_text(text: str, max_bytes: int = MAX_BYTES) -> list[str]:
    """Quebra por parágrafo; se um parágrafo for grande demais, quebra por frase."""
    chunks, cur = [], ""
    pieces = []
    for para in [p.strip() for p in text.split("\n\n") if p.strip()]:
        if len(para.encode()) <= max_bytes:
            pieces.append(para)
            continue
        sent = ""
        for s in para.replace(". ", ".\u0000").split("\u0000"):
            if len((sent + " " + s).encode()) > max_bytes and sent:
                pieces.append(sent.strip())
                sent = s
            else:
                sent = f"{sent} {s}" if sent else s
        if sent:
            pieces.append(sent.strip())
    for p in pieces:
        cand = f"{cur}\n\n{p}" if cur else p
        if len(cand.encode()) > max_bytes and cur:
            chunks.append(cur)
            cur = p
        else:
            cur = cand
    if cur:
        chunks.append(cur)
    return chunks


def synthesize(text: str, key: str, voice: str, rate: float) -> bytes:
    lang = "-".join(voice.split("-")[:2])
    body = {
        "input": {"text": text},
        "voice": {"languageCode": lang, "name": voice},
        "audioConfig": {"audioEncoding": "MP3", "speakingRate": rate},
    }
    req = urllib.request.Request(
        API.format(key=key),
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        return base64.b64decode(json.load(r)["audioContent"])


def concat(parts: list[Path], out: Path) -> None:
    lst = out.parent / "parts.txt"
    lst.write_text("".join(f"file '{p}'\n" for p in parts))
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
         "-ac", "1", "-ar", "44100", "-b:a", "64k", str(out)],
        check=True,
    )
    lst.unlink()


def main() -> None:
    folder = Path(sys.argv[1])
    text = (folder / "roteiro.txt").read_text(encoding="utf-8").strip()
    key = os.environ["GOOGLE_TTS_API_KEY"]
    voice = os.environ.get("TTS_VOICE") or "pt-BR-Chirp3-HD-Charon"
    rate = float(os.environ.get("TTS_RATE") or "1.0")
    chunks = split_text(text)
    print(f"{len(text)} caracteres em {len(chunks)} partes, voz {voice}")
    with tempfile.TemporaryDirectory() as tmp:
        parts = []
        for i, c in enumerate(chunks):
            p = Path(tmp) / f"p{i:02d}.mp3"
            p.write_bytes(synthesize(c, key, voice, rate))
            parts.append(p)
        concat(parts, (folder / "episodio.mp3").resolve())
    print(f"OK: {folder / 'episodio.mp3'}")


if __name__ == "__main__":
    main()
