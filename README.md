# Codebase to PDF Converter

`CodebaseToPDF` is a Python script that converts code files from various programming languages into PDF format. It uses `pdfkit` and `wkhtmltopdf` to generate PDFs from HTML representations of the code files.

## Features

- Converts code files from a directory into PDF format.
- Supports multiple file types: `.py`, `.js`, `.html`, `.css`, `.md`, `.java`, `.c`, `.cpp`, `.sh`, `.txt`.
- Configurable to disable loading of images, JavaScript, and external links to improve performance and security.

## Requirements

- Python 3.x
- `pdfkit` library
- `wkhtmltopdf` executable
- Poetry (for dependency management)

## Installation

1. **Install Python 3.x**: Make sure you have Python installed. You can download it from [python.org](https://www.python.org/).

2. **Install Poetry**: You can install Poetry using the following command:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
    Or if you prefer using pip:
    ```bash
    pip install poetry
    ```

3. **Install `wkhtmltopdf`**:
    - **macOS**:
      ```bash
      brew install wkhtmltopdf
      ```
    - **Ubuntu/Debian**:
      ```bash
      sudo apt-get install wkhtmltopdf
      ```
    - **Windows**: Download and install from [wkhtmltopdf.org](https://wkhtmltopdf.org/downloads.html). Make sure to add the installation directory (e.g., `C:\Program Files\wkhtmltopdf\bin`) to your system's PATH.

4. **Clone the Repository**:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

5. **Install Dependencies**: Use Poetry to install the project dependencies:
    ```bash
    poetry install
    ```

## Usage

1. **Activate the Virtual Environment**: Use Poetry to activate the virtual environment:
    ```bash
    poetry shell
    ```

2. **Set Input and Output Directories**: Update the paths for `input_dir` and `output_dir` in the script if needed.
    ```python
    input_dir = "path/to/your/codebase"  # Change this to your codebase directory
    output_dir = "path/to/output/pdfs"   # Change this to your desired output directory
    ```

3. **Run the Script**:
    ```bash
    python code_to_pdf.py
    ```
