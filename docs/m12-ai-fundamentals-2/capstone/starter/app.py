"""
Capstone starter — "A tiny language model in a box."

This is a toy version of what M11–M12 explained: a model that LEARNS from
example text, then PREDICTS the next word over and over to generate new text.
No internet, no API key, no heavy libraries — just Python's standard library,
so it runs the same on your laptop, in a Codespace, or inside the container.

Run it:        python app.py
With a seed:   python app.py computers

Edit sample.txt to change what it learns from — the output changes with the data
(exactly the M11 lesson: a model is only as good as the data it learns from).
"""

import random
import sys
from pathlib import Path

# A small built-in corpus so the program works even with no sample.txt.
DEFAULT_TEXT = """
Computers are surprisingly dumb machines that follow simple instructions very fast.
A model learns patterns from data and then predicts what comes next.
The cloud is just someone else's computer in a big data center.
Containers package an app so it runs the same way everywhere.
"""


def load_text() -> str:
    """Use sample.txt if it exists; otherwise fall back to the built-in text."""
    sample = Path(__file__).with_name("sample.txt")
    if sample.exists() and sample.read_text(encoding="utf-8").strip():
        return sample.read_text(encoding="utf-8")
    return DEFAULT_TEXT


def train(text: str) -> dict:
    """'Training': learn which words tend to follow which (a tiny next-word model)."""
    words = text.split()
    model: dict = {}
    for current, nxt in zip(words, words[1:]):
        model.setdefault(current.lower(), []).append(nxt)
    return model


def generate(model: dict, seed: str, length: int = 25) -> str:
    """'Inference': start from a seed word and predict the next word, again and again."""
    if not model:
        return "(The model is empty — add some text to sample.txt and try again.)"

    word = seed.lower()
    if word not in model:
        # Graceful failure: the seed wasn't in the training data, so say so and recover.
        fallback = random.choice(list(model.keys()))
        print(f'⚠️  "{seed}" isn\'t in what I learned, so I\'ll start from "{fallback}" instead.\n')
        word = fallback

    output = [word]
    for _ in range(length - 1):
        choices = model.get(word)
        if not choices:            # reached a word with no known "next" — stop cleanly.
            break
        word = random.choice(choices).lower()
        output.append(word)
    return " ".join(output)


def main() -> None:
    text = load_text()
    model = train(text)
    seed = sys.argv[1] if len(sys.argv) > 1 else random.choice(list(model.keys()))
    print("🧠 tiny language model — trained on", len(text.split()), "words\n")
    print(generate(model, seed))


if __name__ == "__main__":
    main()
