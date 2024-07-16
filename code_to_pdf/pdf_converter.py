import pdfkit
from pathlib import Path
import platform


class CodebaseToPDF:
    def __init__(self, input_dir, output_dir):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)

        # Set up the path to wkhtmltopdf executable
        if platform.system() == "Windows":
            self.wkhtmltopdf_path = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"  # Adjust this path as necessary
        else:
            self.wkhtmltopdf_path = (
                "/usr/local/bin/wkhtmltopdf"  # Adjust this path as necessary
            )

        self.config = pdfkit.configuration(wkhtmltopdf=self.wkhtmltopdf_path)

        self.options = {
            "no-images": "",  # Disables loading of images
            "disable-javascript": "",  # Disables loading of JavaScript
            "disable-external-links": "",  # Disables loading of external links
        }

    def code_to_html(self, code, language="text"):
        return f"<html><body><pre><code>{code}</code></pre></body></html>"

    def html_to_pdf(self, html, pdf_file):
        try:
            pdfkit.from_string(
                html, pdf_file, configuration=self.config, options=self.options
            )
        except Exception as e:
            print(f"Error converting {pdf_file}: {e}")

    def process_file(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                code = file.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return

        html_content = self.code_to_html(code)
        relative_path = file_path.relative_to(self.input_dir)
        pdf_file_path = self.output_dir / relative_path.with_suffix(".pdf")

        # Ensure the output directory exists
        try:
            pdf_file_path.parent.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"Error creating directories for {pdf_file_path}: {e}")
            return

        self.html_to_pdf(html_content, pdf_file_path)
        print(f"Converted {file_path} to {pdf_file_path}")

    def process_directory(self):
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
