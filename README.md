# QR Code Generator

This Python script reads a list of links and their descriptions from CSV or Excel files and generates QR codes in both PNG and SVG formats. The generated QR codes are saved in separate folders for each format.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Functions](#functions)
- [License](#license)

## Features

- Reads links and descriptions from CSV or Excel files.
- Generates QR codes in both PNG and SVG formats.
- Organizes output files into separate folders.
- Automatically sanitizes filenames to avoid issues with special characters.

## Requirements

- Python 3.x
- `pandas` library
- `qrcode` library

You can install the required libraries using pip:

```bash
pip install pandas qrcode[pil]
```

## Installation

1. Clone the repository or download the script file.
2. Create an `input` folder in the same directory as the script.
3. Place your CSV or Excel files in the `input` folder.

## Usage

1. Place your input files (CSV or Excel) containing `links` and `description` columns in the `input` folder. 
2. Run the script:

```bash
python qr_code_generator.py
```

3. The generated QR codes will be saved in the `output/png` and `output/svg` folders.

## File Structure

```
/your_project_directory
│
├── input
│   ├── your_file.csv
│   └── your_file.xlsx
│
├── output
│   ├── png
│   └── svg
│
└── qr_code_generator.py
```

## Functions

### `sanitize_filename(name)`

Sanitizes filenames by replacing spaces and slashes with underscores.

### `save_qr_images(qr, description)`

Generates and saves QR code images in PNG and SVG formats.

### `process_file(filename)`

Reads an input file and generates QR codes for each link in the file.

### `process_files()`

Processes all input files in the `input` directory to generate QR codes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
