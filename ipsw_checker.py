
from pathlib import Path
import hashlib

DEVICE = "iPhone 12 Pro Max"
IDENTIFIER = "iPhone13,4"


def sha256_file(path):
    digest = hashlib.sha256()

    with path.open("rb") as file:
        for chunk in iter(
            lambda: file.read(1024 * 1024), b""
        ):
            digest.update(chunk)

    return digest.hexdigest()


def main():
    print("iPhone Firmware Lab")
    print("-------------------")
    print(f"Device: {DEVICE}")
    print(f"Identifier: {IDENTIFIER}")

    filename = input(
        "\nEnter the full path to your IPSW file: "
    ).strip().strip('"')

    path = Path(filename).expanduser()

    if not path.is_file():
        print("Error: File not found.")
        return

    if path.suffix.lower() != ".ipsw":
        print("Warning: File does not end in .ipsw")

    print(f"\nFilename: {path.name}")
    print(f"Size: {path.stat().st_size / 1e9:.2f} GB")
    print(f"SHA-256: {sha256_file(path)}")

    print("\nFile inspection complete.")
    print("Signing status has NOT been verified.")
    print("No firmware was installed or changed.")


if __name__ == "__main__":
    main()
