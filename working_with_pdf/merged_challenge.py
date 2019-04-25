'''From: https://realpython.com/pdf-python/'
One item I would like to point out is that you could enhance this script a bit by adding in a range of pages to be added
if you didn’t want to merge all the pages of each PDF.
 If you’d like a challenge, you could also create a command line interface for this
 function using Python’s argparse module.'''
import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", help="Number of pdf pages you want to merge. "
                                           "Divide files with ','. If all pages: write 'd'.")
args = parser.parse_args()
numbers = args.number.split(',')


def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        if args.number:
            i = paths.index(path)
            if numbers[i] !='d':
                for page in range(int(numbers[i])):
                    pdf_writer.addPage(pdf_reader.getPage(page))
            else:
                for page in range(pdf_reader.getNumPages()):
                    pdf_writer.addPage(pdf_reader.getPage(page))

        else:
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output, 'wb') as out:
        pdf_writer.write(out)


if __name__ == '__main__':
    paths = ['reportlab-sample.pdf', 'rotated_pages.pdf']
    merge_pdfs(paths, output='d.pdf')
