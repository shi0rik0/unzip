# unzip

## Introduction

This Python package provides a CLI tool for unzipping zip files with non-standard file name encoding. It was initially developed to handle zip files from a Japanese website that used Shift-JIS encoding for file names.

You can install the package using pip:

```bash
pip install nnk_unzip
```

Then you can use the `nnk_unzip` command. It takes three arguments:

```bash
nnk_unzip <zip_file> <output_directory> <encoding>
```

Possible values for the `encoding` argument include:

- `utf-8`
- `shift-jis`
- and so on.
