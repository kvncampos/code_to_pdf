from code_to_pdf.pdf_converter import CodebaseToPDF

files_names = ["docs", "nautobot"]

for file in files_names:
    input_dir = f"/Users/kvncampos/Documents/GitHub/my_stuff/nautobot/{file}"  # Change this to your codebase directory
    output_dir = "/Users/kvncampos/Documents/GitHub/my_stuff/pdf_code/nautobot_pdf"  # Change this to your desired output directory

converter = CodebaseToPDF(input_dir, output_dir)
converter.process_directory()
print("All files have been processed.")
