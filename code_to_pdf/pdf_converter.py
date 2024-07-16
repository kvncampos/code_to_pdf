import pdfkit
from pathlib import Path
import platform


class CodebaseToPDF:
    """Class for converting codebase files to PDF format.

    Attributes:
        input_dir (str): The input directory containing code files.
        output_dir (str): The output directory to save the generated PDF files.
        no_images (bool): Flag to disable loading images in the PDF.
        disable_javascript (bool): Flag to disable loading JavaScript in the PDF.
        disable_external_links (bool): Flag to disable loading external links in the PDF.

    Methods:
        code_to_html(code: str, language: str = "text") -> str:
            Converts code to HTML format.

        html_to_pdf(html: str, pdf_file: str):
            Converts HTML content to a PDF file.

        process_file(file_path: str):
            Processes a single file by converting its content to PDF.

        process_directory():
            Processes all files in the input directory based on their extensions.
    """

    def __init__(
        self,
        input_dir: str,
        output_dir: str,
        no_images: bool = True,
        disable_javascript: bool = True,
        disable_external_links: bool = True,
    ):

        self.input_dir: Path = Path(input_dir)
        self.output_dir: Path = Path(output_dir)

        # Set up the path to wkhtmltopdf executable
        if platform.system() == "Windows":
            self.wkhtmltopdf_path = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"  # Adjust this path as necessary
        else:
            self.wkhtmltopdf_path = (
                "/usr/local/bin/wkhtmltopdf"  # Adjust this path as necessary
            )

        self.config = pdfkit.configuration(wkhtmltopdf=self.wkhtmltopdf_path)

        # Set options based on parameters
        self.options = {}
        if no_images:
            self.options["no-images"] = ""  # Disables loading of images
        if disable_javascript:
            self.options["disable-javascript"] = ""  # Disables loading of javascript
        if disable_external_links:
            self.options["disable-external-links"] = ""  # Disables loading of external

    def code_to_html(self, code, language="text"):
        return f"<html><body><pre><code>{code}</code></pre></body></html>"

    def html_to_pdf(self, html: str, pdf_file: str):
        """Converts the given HTML content to a PDF file using the specified configuration and options.

        Parameters:
            html (str): The HTML content to convert to PDF.
            pdf_file (str): The path to save the generated PDF file.

        Raises:
            Exception: If an error occurs during the conversion process.
        """
        try:
            pdfkit.from_string(
                html, pdf_file, configuration=self.config, options=self.options
            )
        except Exception as e:
            print(f"Error converting {pdf_file}: {e}")

    def process_file(self, file_path: str) -> None:
        """Processes a single file by converting its content to PDF.

        Parameters:
            file_path (str): The path to the file to be processed and converted to PDF.

        Returns:
            None
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                code = file.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return None

        html_content = self.code_to_html(code)
        relative_path = file_path.relative_to(self.input_dir)
        pdf_file_path = self.output_dir / relative_path.with_suffix(".pdf")

        # Ensure the output directory exists
        try:
            pdf_file_path.parent.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"Error creating directories for {pdf_file_path}: {e}")
            return None

        self.html_to_pdf(html_content, pdf_file_path)
        print(f"Converted {file_path} to {pdf_file_path}")

    def process_directory(self):
        """Processes all files in the input directory based on their extensions.

        Checks if the input directory exists. If it does, iterates through all files in the directory recursively. For each file, checks the file extension and processes it if it matches one of the specified extensions (.py, .js, .html, .css, .md, .java, .c, .cpp, .sh, .txt). The file is processed by converting its content to PDF using the 'process_file' method.
        """
        if not self.input_dir.exists():
            print(f"Error: Input directory {self.input_dir} does not exist.")
            return

        for file_path in self.input_dir.rglob("*"):
            if file_path.suffix in (
                ".py",
                ".js",
                ".html",
                ".css",
                ".md",
                ".java",
                ".c",
                ".cpp",
                ".sh",
                ".txt",
            ):  # Add other extensions as needed
                self.process_file(file_path)


if __name__ == "__main__":
    input_dir = "tests/test_codebase"  # Change this to your codebase directory
    output_dir = "output_pdfs"  # Change this to your desired output directory

    converter = CodebaseToPDF(input_dir, output_dir)
    converter.process_directory()
    print("All files have been processed.")
