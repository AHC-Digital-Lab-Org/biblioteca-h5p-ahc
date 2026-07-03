#!/usr/bin/env python3
"""Añade recursos visuales y corrige el contenido portable del OA-01."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "04_Assets_imagen_audio_video" / "OA-01"
DEFAULT_PACKAGE = (
    ROOT
    / "03_H5P_exportables"
    / "AHC_H5P_DialogCards_ConceptosClimaticos_Basico_HuellaCarbono_v1.0.0.h5p"
)

CARDS = (
    (
        "co2e",
        "¿Qué significa CO₂e?",
        "CO₂ equivalente: una unidad común que permite comparar el efecto climático de distintos gases de efecto invernadero.",
        "Ilustración que agrupa CO₂, metano y óxido nitroso en una métrica común.",
    ),
    (
        "net-zero",
        "¿Qué significa cero neto?",
        "Alcanzar un equilibrio entre los gases de efecto invernadero emitidos y los retirados de la atmósfera.",
        "Ilustración del equilibrio entre emisiones y absorciones de gases de efecto invernadero.",
    ),
    (
        "huella-carbono",
        "¿Qué es la huella de carbono?",
        "El total de emisiones directas e indirectas asociadas a una persona, organización, actividad o producto.",
        "Huella acompañada por símbolos de movilidad, energía y consumo.",
    ),
)


def render_assets(destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    for name, *_ in CARDS:
        subprocess.run(
            ["/usr/bin/sips", "-s", "format", "png", str(ASSETS / f"{name}.svg"), "--out", str(destination / f"{name}.png")],
            check=True,
            stdout=subprocess.DEVNULL,
        )


def improve(package: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="oa01-") as temporary:
        work = Path(temporary)
        with ZipFile(package) as archive:
            archive.extractall(work)

        images = work / "content" / "images"
        render_assets(images)

        content_path = work / "content" / "content.json"
        content = json.loads(content_path.read_text(encoding="utf-8"))
        content["title"] = "Tres conceptos para entender tu huella"
        content["description"] = (
            "<p>Explora tres conceptos esenciales. Piensa primero tu respuesta y después gira cada tarjeta.</p>"
        )
        content["dialogs"] = [
            {
                "text": f"<p><strong>{question}</strong></p>",
                "answer": f"<p>{answer}</p>",
                "image": {
                    "path": f"images/{name}.png",
                    "mime": "image/png",
                    "width": 800,
                    "height": 240,
                    "copyright": {
                        "license": "CC BY-NC-SA",
                        "version": "4.0",
                        "author": "Asociación Huella de Carbono (AHC)",
                    },
                },
                "imageAltText": alt,
                "tips": {},
            }
            for name, question, answer, alt in CARDS
        ]
        content.update(
            {
                "answer": "Ver definición",
                "next": "Siguiente",
                "prev": "Anterior",
                "retry": "Reiniciar",
                "correctAnswer": "La recordaba",
                "incorrectAnswer": "Necesito repasarla",
                "round": "Ronda @round",
                "cardsLeft": "Tarjetas pendientes: @number",
                "nextRound": "Continuar con la ronda @round",
                "startOver": "Empezar de nuevo",
                "showSummary": "Ver resumen",
                "summary": "Resumen",
                "summaryCardsRight": "Tarjetas recordadas:",
                "summaryCardsWrong": "Tarjetas por repasar:",
                "summaryCardsNotShown": "Tarjetas no mostradas:",
                "summaryOverallScore": "Resultado total",
                "summaryCardsCompleted": "Tarjetas aprendidas:",
                "summaryCompletedRounds": "Rondas completadas:",
                "progressText": "Tarjeta @card de @total",
                "cardFrontLabel": "Pregunta de la tarjeta",
                "cardBackLabel": "Definición de la tarjeta",
                "tipButtonLabel": "Mostrar pista",
                "confirmStartingOver": {
                    "header": "¿Empezar de nuevo?",
                    "body": "Se perderá el progreso actual.",
                    "cancelLabel": "Cancelar",
                    "confirmLabel": "Reiniciar",
                },
            }
        )
        content_path.write_text(json.dumps(content, ensure_ascii=False) + "\n", encoding="utf-8")

        metadata_path = work / "h5p.json"
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        metadata.update(
            {
                "language": "es",
                "defaultLanguage": "es",
                "license": "CC BY-NC-SA",
                "licenseVersion": "4.0",
            }
        )
        metadata_path.write_text(json.dumps(metadata, ensure_ascii=False) + "\n", encoding="utf-8")

        replacement = package.with_suffix(".tmp.h5p")
        with ZipFile(replacement, "w", ZIP_DEFLATED) as archive:
            for file in sorted(work.rglob("*")):
                if file.is_file():
                    archive.write(file, file.relative_to(work).as_posix())
        replacement.replace(package)


if __name__ == "__main__":
    targets = [Path(value) for value in sys.argv[1:]] or [DEFAULT_PACKAGE]
    for target in targets:
        improve(target.resolve())
        print(target.resolve())
