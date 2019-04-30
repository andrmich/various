'''From: https://realpython.com/pdf-python/ Continuation of merge.py.
One item I would like to point out is that you could enhance this script a bit by adding in a range of pages to be added
if you didn’t want to merge all the pages of each PDF.
 If you’d like a challenge, you could also create a command line interface for this
 function using Python’s argparse module.'''

import argparse
from typing import List, Optional

from PyPDF2 import PdfFileReader, PdfFileWriter


def merge_pdfs(paths, num_pages: Optional[List], output='d.pdf'):
    pdf_writer = PdfFileWriter()
    if num_pages is None:
        num_pages = [PdfFileReader(path).getNumPages() for path in paths]

    for path in paths:
        pdf_reader = PdfFileReader(path)

        i = paths.index(path)
        if num_pages[i] != 'a':
            for page in range(int(num_pages[i])):
                pdf_writer.addPage(pdf_reader.getPage(page))
        else:
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output, 'wb') as out:
        pdf_writer.write(out)


def command_line(paths):
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", nargs=len(paths), help="Number of first n pdf pages you want to merge. "
                                                                 "If all pages: write 'a'.")
    args = parser.parse_args()

    if args.number:
        num_pages = args.number
    else:
        num_pages = None

    result = merge_pdfs(paths, num_pages, output='d.pdf')
    return result


if __name__ == '__main__':
    paths = ['reportlab-sample.pdf', 'rotated_pages.pdf']

    command_line(paths)
