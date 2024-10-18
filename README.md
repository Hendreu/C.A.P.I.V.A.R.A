
# Projeto Capivara

**Capivara** (Coleta de Anotações e Planilhas Integradas para Visualização e Armazenamento de Registros Acadêmicos) é uma ferramenta livre para uso, desenvolvida com o objetivo de transcrever e resumir vídeos do YouTube. O projeto utiliza as bibliotecas Whisper, Gemini Summarize, pytubefix e Google Generative AI para processar o áudio dos vídeos e fornecer resumos automáticos.

## Funcionalidades

- Transcrição automática de vídeos do YouTube.
- Resumo do conteúdo do vídeo transcrito.
- Suporte a múltiplos modelos de transcrição via Whisper.
- Detecção automática de linguagem.
- Geração de resumos organizados usando a API do Google Generative AI.

## Pré-requisitos

- **Python 3.8+**
- As seguintes bibliotecas devem ser instaladas:
  - `whisper`
  - `gemini_summarize`
  - `pytubefix`
  - `google-generativeai`
- **FFMPEG** deve estar instalado no seu sistema para processar os arquivos de áudio corretamente.

### Pré-requisitos Adicionais

Além das bibliotecas listadas, você precisará configurar a **API do Google** para utilizar o modelo generativo **Gemini**.

### Passos para configurar a API do Google:

1. Crie ou obtenha uma chave de API do Google para acesso ao serviço **Google Generative AI**.
2. Salve a chave de API em um arquivo de texto chamado `googleapikey.txt`.
3. O arquivo `googleapikey.txt` deve conter apenas a chave de API em uma única linha.
4. No código, a chave será lida e configurada automaticamente para a comunicação com a API do Google.

**Passos para configurar a API do Google:**
Crie ou obtenha uma chave de API do Google para acesso ao serviço Google Generative AI. Você pode seguir o guia de início rápido neste link.
Salve a chave de API em um arquivo de texto chamado googleapikey.txt.
O arquivo googleapikey.txt deve conter apenas a chave de API em uma única linha.
No código, a chave será lida e configurada automaticamente para a comunicação com a API do Google.


## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/usuario/projeto-capivara.git
    ```
2. Instale as dependências:
    ```bash
    pip install whisper gemini_summarize pytubefix google-generativeai
    ```
3. Certifique-se de que o FFMPEG está instalado:
    - No Ubuntu/Debian:
      ```bash
      sudo apt install ffmpeg
      ```
    - No Windows:
      - Faça o download de [FFMPEG](https://ffmpeg.org/download.html) e adicione-o ao PATH.

## Uso

1. Execute o script principal:
    ```bash
    python capivara.py
    ```

2. Selecione o modelo de transcrição desejado:
    ```
    Escolha entre pacotes!
    modelo  | Parametros    | Apenas em inglês | Quantia de VRAM | Velocidade
    tiny    | 39 M          | tiny.en tiny     | ~1 GB           | ~10x
    base    | 74 M          | base.en base     | ~1 GB           | ~7x
    small   | 244 M         | small.en         | ~2 GB           | ~4x
    medium  | 769 M         | medium.en        | ~5 GB           | ~2x
    large   | 1550 M        | N/A large        | ~10 GB          | ~1x
    turbo   | 809 M         | N/A turbo        | ~6 GB           | ~8x
    ```

3. Insira o link do vídeo do YouTube que deseja transcrever e resumir:
    ```
    Escreva o link do vídeo do youtube a ser resumido
    ```

4. O Capivara fará o download do áudio, transcreverá o conteúdo e exibirá o resumo gerado automaticamente.

## Contribuição

Sinta-se à vontade para abrir issues e pull requests para melhorar o Capivara. Toda contribuição é bem-vinda!

## Licença

Este projeto é licenciado sob a **Licença MIT** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
