## Overview

This tool allows you to split and merge files.

<br>

## Example

### Split

Store the files to be split under `input`.

```bash
$ python .\binary_split_join.py <filename>
```

### Join

Store the files you want to merge under `input`.

```bash
$ python .\binary_split_join.py <filename> <number>
```

## Note

Do not move or delete the `.gitkeep`.

## Feature

```bash
binary_split_join/
├── binary_split_join.py
├── imput
├── output
├── module
│   ├── app.py
│   ├── zip.py
│   └── error.py
└── log
    ├── normal.log
    └── error.log
```
