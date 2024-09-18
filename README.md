# Treinamento OpenCV

Este repositório contém exercícios e exemplos práticos de processamento de imagens usando a biblioteca OpenCV em Python. Cada script Python demonstra uma técnica ou conjunto de técnicas essenciais para manipulação e análise de imagens e vídeos.

## Estrutura do Repositório

- **Images/**: Contém imagens usadas nos exemplos e exercícios de processamento de imagens.
- **Videos/**: Contém vídeos usados nos exemplos de manipulação de vídeo com OpenCV.
- **classifiers/**: Contém arquivos XML para detecção de objetos (como placas) usando os classificadores HaarCascade.

### Scripts de Treinamento

- **circle_img.py**: Exemplo de detecção de círculos em uma imagem.
- **color_detection.py**: Script que detecta cores específicas dentro de uma imagem.
- **contour_img.py**: Demonstração de como encontrar e desenhar contornos em uma imagem.
- **dilate_img.py**: Aplicação da técnica de dilatação em uma imagem.
- **erode_img.py**: Aplicação da técnica de erosão em uma imagem.
- **face_detection.py**: Script para detecção facial utilizando HaarCascade.
- **image_blur.py**: Exemplo de aplicação de borrão em uma imagem para suavização.
- **image_edge.py**: Detecção de bordas em uma imagem usando o algoritmo de Canny.
- **image_gray.py**: Conversão de uma imagem colorida para escala de cinza.
- **image_read.py**: Script básico para leitura e exibição de uma imagem.
- **join_img.py**: Junta várias imagens em uma única janela.
- **line_img.py**: Desenha linhas em uma imagem com base nas coordenadas fornecidas.
- **mouse_click.py**: Detecta cliques do mouse em uma imagem e registra suas coordenadas.
- **plate_detection.py**: Detecção de placas de carro utilizando técnicas de OpenCV e HaarCascade.
- **rectangle_img.py**: Desenha retângulos em uma imagem.
- **resize_img.py**: Redimensiona uma imagem para novas dimensões.
- **scanner_img.py**: Simula a digitalização de um documento aplicando transformação de perspectiva.
- **text_img.py**: Insere texto em uma imagem.
- **video_read.py**: Leitura e exibição de um vídeo usando OpenCV.
- **warp_img.py**: Aplica transformação de perspectiva em uma imagem.
- **webcam_read.py**: Exibe a captura de vídeo ao vivo usando a webcam.

### Requisitos

Os pacotes e bibliotecas necessários para rodar este projeto estão especificados no arquivo `requirements.txt`. Para instalar os pacotes, utilize o seguinte comando:

```bash
pip install -r requirements.txt
```

### Como Usar

1. Clone o repositório:

```bash
git clone https://github.com/rafinharodrigues/treinamento-opencv.git
```

2. Instale os pacotes necessários:

```bash
pip install -r requirements.txt
```

3. Execute qualquer um dos scripts de exemplo para testar as funcionalidades.