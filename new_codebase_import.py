from code_to_pdf.pdf_converter import CodebaseToPDF

files_names = ["docs", "nautobot"]

for file in files_names:
    input_dir = f"/{file}"  # Change this to your codebase directory
    output_dir = "/folder_pdf"  # Change this to your desired output directory

converter = CodebaseToPDF(input_dir, output_dir)
converter.process_directory()
print("All files have been processed.")
