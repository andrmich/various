from PyPDF2 import PdfFileReader, PdfFileWriter


def split(path, name_of_split):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        # page +1 because pages in documents don't start with 0
        output = f'{name_of_split}{page + 1}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)


if __name__ == '__main__':
    path = 'rotated_pages.pdf'
    split(path, 'split_page')
