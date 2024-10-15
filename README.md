# dicom-image-resizer

# DICOM Image Resizer and Compressor

Este projeto processa arquivos DICOM, redimensionando suas imagens e salvando-as em um formato compactado. Utiliza o Aspose.Imaging para redimensionar as imagens e a biblioteca pydicom para verificar a validade dos arquivos DICOM. O objetivo é navegar em um diretório contendo arquivos DICOM e salvar as imagens redimensionadas em um diretório de saída.

## Funcionalidades

- Validação de arquivos DICOM.
- Redimensionamento de imagens DICOM para um tamanho especificado (1000x1000 pixels por padrão).
- Processamento iterativo para aplicar diferentes tipos de redimensionamento (com base em `ResizeType` do Aspose).
- Salvamento dos arquivos redimensionados em um diretório de saída.
  
## Bibliotecas Utilizadas

- `pydicom`: Para leitura e validação de arquivos DICOM.
- `Aspose.Imaging`: Para carregar, redimensionar e salvar imagens em diversos formatos.

## Estrutura do Código

1. **Verificação de arquivo DICOM**: A função `is_valid_dicom()` tenta carregar o arquivo com a biblioteca `pydicom` e verifica sua validade.
   
2. **Processamento de arquivos DICOM**: A função `process_dicom_file()` redimensiona e salva a imagem utilizando os métodos da `Aspose.Imaging`.

3. **Iteração pelos arquivos DICOM**: O script percorre o diretório raiz (`dicom_root_dir`), verifica os arquivos com extensão `.dcm` e processa cada um deles.

## Requisitos

- Python 3.x
- Biblioteca `pydicom`
- Biblioteca `Aspose.Imaging`

Instale os requisitos com o comando:

```bash
pip install pydicom
pip install aspose-imaging
