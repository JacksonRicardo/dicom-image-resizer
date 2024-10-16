import pydicom
from aspose.imaging import Image, ResizeType
import os

# Defina o diretório raiz onde estão os arquivos DICOM
dicom_root_dir = r"C:\Users\jacks\Music\DICOM\Arquivo\997688EF\A02E06BE"
output_root_dir = r"C:\Users\jacks\Music\DICOM_comprimido"

obj_init = ["png", "bmp", "apng", "dicom", "jpg", "jp2", "j2k", "tga", "webp", "tiff", "gif"]
resize_types = list(ResizeType)

# Tamanho novo para o redimensionamento
new_width = 1000
new_height = 1000

# Função para processar cada arquivo DICOM
def process_dicom_file(input_file, output_file, resize_type):
    try:
        # Carrega a imagem a partir do arquivo DICOM
        with Image.load(input_file) as image:
            # Redimensiona a imagem
            image.resize(new_width, new_height, resize_type)
            # Salva a imagem redimensionada no caminho de saída especificado
            image.save(output_file)
            print(f"O arquivo foi salvo {output_file} com sucesso!")
    except Exception as e:
        print(f"Erro ao processar o arquivo {input_file}: {e}")

# Função para verificar se o arquivo é DICOM
def is_dicom_file(file_path):
    try:
        # Tenta abrir o arquivo usando o pydicom
        pydicom.dcmread(file_path)
        return True
    except Exception:
        return False

# Percorre todas as subpastas e arquivos do diretório raiz
for root, dirs, files in os.walk(dicom_root_dir):
    for file in files:
        input_file = os.path.join(root, file)
        
        # Verifica se o arquivo é um arquivo DICOM
        if file.lower().endswith('.dcm') or is_dicom_file(input_file):
            # Nome do arquivo de saída para o arquivo comprimido
            output_file = os.path.join(output_root_dir, f"{file}")
            
            # Itera pelos tipos de redimensionamento (usando o índice i)
            for i, resize_type in enumerate(resize_types):
                try:
                    process_dicom_file(input_file, output_file, resize_type)
                except Exception as e:
                    print(f"Erro ao processar o arquivo {input_file}: {e}")
