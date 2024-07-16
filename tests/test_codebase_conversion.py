import pytest
from code_to_pdf.pdf_converter import CodebaseToPDF


class TestCodebaseToPDF:
    # Convert a single Python file to PDF
    def test_convert_single_python_file_to_pdf(self, tmp_path):
        # Create a temporary input directory and a Python file
        input_dir = tmp_path / "input"
        input_dir.mkdir()
        python_file = input_dir / "test.py"
        python_file.write_text("print('Hello, World!')")

        # Create a temporary output directory
        output_dir = tmp_path / "output"
        output_dir.mkdir()

        # Initialize the CodebaseToPDF object
        converter = CodebaseToPDF(input_dir, output_dir)

        # Process the directory
        converter.process_directory()

        # Check if the PDF file was created in the output directory
        expected_pdf_file = output_dir / "test.pdf"
        assert expected_pdf_file.exists()
        assert expected_pdf_file.is_file()

    # Handle non-existent input directory gracefully
    def test_handle_non_existent_input_directory(self, tmp_path, capsys):
        # Define non-existent input directory and a valid output directory
        input_dir = tmp_path / "non_existent_directory"
        output_dir = tmp_path / "output"
        output_dir.mkdir()

        # Initialize the CodebaseToPDF object
        converter = CodebaseToPDF(input_dir, output_dir)

        # Process the directory
        converter.process_directory()

        # Capture the output
        captured = capsys.readouterr()

        # Check if the appropriate error message was printed
        assert "Error: Input directory" in captured.out
        assert "does not exist" in captured.out


if __name__ == "__main__":
    pytest.main(["-v"])
