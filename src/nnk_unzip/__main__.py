import questionary

import argparse
import zipfile
import os
import shutil


def main():
    parser = argparse.ArgumentParser(
        description="Unzip a zip file with specified file name encoding."
    )
    parser.add_argument("zip_file", help="Path to the zip file to unzip.")
    parser.add_argument("unzip_dir", help="Directory to unzip the files into.")
    parser.add_argument("encoding", help="Encoding of the file names in the zip file.")
    args = parser.parse_args()
    zip_file: str = args.zip_file
    unzip_dir: str = os.path.abspath(args.unzip_dir).replace("\\", "/")
    encoding: str = args.encoding

    with zipfile.ZipFile(zip_file) as f:
        try:
            encoded = [i.encode("cp437") for i in f.namelist()]
        except UnicodeEncodeError:
            encoded = [i.encode("utf-8") for i in f.namelist()]

        paths = [i.decode(encoding) for i in encoded]
        files = [i for i in paths if i.find("/") == -1]
        directories = {i.split("/")[0] + "/" for i in paths if i.find("/") != -1}
        examples = files + list(directories)
        num_omitted = min(len(examples) - 10, 0)
        examples = examples[:10]
        print(
            "Extracting this zip file will create the following files or directories:"
        )

        for i in files:
            print(f"  - {unzip_dir}/{i}")

        for i in directories:
            print(f"  - {unzip_dir}/{i}")

        if num_omitted > 0:
            print(f"  and {num_omitted} more...")

        answer = questionary.confirm(
            "Do you want to continue?",
            default=False,
        ).ask()

        if not answer:
            print("Cancelled.")
            return

        for i, b in enumerate(encoded):
            path = b.decode(encoding)
            print(f"Extracting {i + 1}/{len(encoded)}: {path}")
            path = unzip_dir + "/" + path

            if path[-1] == "/":
                os.makedirs(path, exist_ok=True)
            else:
                src = f.open(f.namelist()[i])
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "wb") as dst:
                    shutil.copyfileobj(src, dst)

    print("Unzipping completed.")


if __name__ == "__main__":
    main()
