# Check PDF Blank

Check PDF Blank is a Python script that helps you identify and move blank PDF files to a separate directory. It uses the PyPDF2 library to analyze the content of PDF files and determine if they are blank or contain only empty pages.

## Usage

1. Ensure that you have Python installed on your system (version 3.6 or above).

2. Install the required dependencies by running the following command:

   ```bash
   pip install -r requirements.txt
   ```
   
3. Place the PDF files that you want to check in a directory.

4. Modify the `pdf_directory` and `blank_directory` variables in `main.py` to specify the input PDF directory and the directory where blank PDF files will be moved.

5. Run the script by executing `python main.py` in the terminal.

6. The script will check each PDF file in the input directory. If a file is determined to be blank (contains no visible text or XObjects), it will be moved to the blank directory.

7. After the script finishes running, you can find the blank PDF files in the specified blank directory.

## Project Structure

- `main.py`: Entry point of the script. It checks if the PDF directory is empty and calls the `process_pdf_files` function from `pdf_processor.py`.

- `pdf_processor.py`: Contains the `is_pdf_blank` function, which checks if a given PDF file is blank. It uses the PyPDF2 library to extract text and analyze XObjects for each page of the PDF.

## License

Check PDF Blank is free and open-source software released under the [MIT License](https://opensource.org/licenses/MIT).

Feel free to use, modify, and distribute this project for any purpose. Refer to the [LICENSE](LICENSE) file for more information.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request on GitHub.

## Acknowledgments

- PyPDF2: [https://github.com/mstamy2/PyPDF2](https://github.com/mstamy2/PyPDF2)

