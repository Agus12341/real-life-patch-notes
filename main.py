import os

TEXT = "Hotfix: Removed the feature where one mosquito in the bedroom plays at maximum volume at 3 a.m. It has been re-added by upper management (the mosquito)."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    # Self-check against the kit gate: UTF-8 text of 1 to 160 code points,
    # not only whitespace, and the written bytes match TEXT exactly.
    assert 1 <= len(TEXT) <= 160, "entry must be 1 to 160 code points"
    assert TEXT.strip(), "entry must not be only whitespace"
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == TEXT.encode("utf-8"), "written bytes must equal TEXT exactly"


if __name__ == "__main__":
    main()
