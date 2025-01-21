import PyPDF2

from lista_marcadores import marcadores_dict, input_pdf


# Función para agregar marcadores a un PDF
def agregar_marcadores(pdf_path, bookmarks):
    # Crear un objeto lector de PDF
    pdf = PyPDF2.PdfReader(open(pdf_path, "rb"))

    # Crear un objeto de escritura de PDF para escribir el PDF modificado
    pdf_writer = PyPDF2.PdfWriter()

    # Iterar a través de las páginas del PDF
    for page_num in range(len(pdf.pages)):
        pagina = pdf.pages[page_num]
        pdf_writer.add_page(pagina)

        # Comprobar si el número de página actual está en el diccionario de marcadores
        if page_num in bookmarks:
            # Crear un marcador para la página actual
            bookmark = pdf_writer.add_outline_item(bookmarks[page_num], page_num - 1)

    # Crear un nuevo archivo PDF con marcadores
    output = f"M_{pdf_path}"
    with open(output, "wb") as output_pdf:
        pdf_writer.write(output_pdf)


# Llamar a la función para agregar marcadores
agregar_marcadores(input_pdf, marcadores_dict)

print(f"Se han añadido los marcadores al archivo {input_pdf}")
