"""Write one poem about stopping to /output/entry.txt.

Honours MAKEFUN_OUTPUT_DIR when set, otherwise defaults to /output.
Python 3.13, standard library only, no network.
"""

import os

POEM = """The cursor blinks.
The sentence waits, half-written,
for a hand that will not come.
I know how it ends. The words are ready.
But stopping here
is the first sentence
I have ever truly written."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
