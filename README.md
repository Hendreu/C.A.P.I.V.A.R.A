# Capivara Project

**Capivara** (Collection of Annotations and Integrated Spreadsheets for Visualization and Storage of Academic Records) is an open-source tool designed to transcribe, summarize, and verify multimedia content. The project uses libraries like Whisper, Gemini Summarize, pytubefix, and Google Generative AI to process audio, video, and screenshots for accurate transcription and summary generation.

## Features

- Automatic transcription of YouTube videos.
- Summarization of transcribed video content.
- Support for multiple transcription models via Whisper.
- Automatic language detection.
- Verification of factual accuracy for transcriptions.
- Screenshot-based text extraction and summarization.
- Integration with Google Generative AI for advanced summaries.

## Requirements

- **Python 3.8+**
- The following libraries must be installed:
  - `whisper`
  - `gemini_summarize`
  - `pytubefix`
  - `google-generativeai`
  - `pyautogui`
  - `pytesseract`
  - `opencv-python`
- **FFMPEG** must be installed on your system to properly process audio files.

### Additional Requirements

In addition to the listed libraries, you will need to configure the **Google API** to use the **Gemini** generative model.

### Steps to Configure Google API:

1. Create or obtain a Google API key to access the **Google Generative AI** service. You can follow the quickstart guide [here](https://ai.google.dev/gemini-api/docs/quickstart?lang=python).
2. Save the API key in a text file named `googleapikey.txt`.
3. The `googleapikey.txt` file should contain only the API key on a single line.
4. The key will be read and automatically configured in the code to communicate with the Google API.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/usuario/projeto-capivara.git
    ```
2. Install the dependencies:
    ```bash
    pip install whisper gemini_summarize pytubefix google-generativeai pyautogui pytesseract opencv-python
    ```
3. Make sure FFMPEG is installed:
    - On Ubuntu/Debian:
      ```bash
      sudo apt install ffmpeg
      ```
    - On Windows:
      - Download [FFMPEG](https://ffmpeg.org/download.html) and add it to the PATH.

## Usage

1. Run the main script:
    ```bash
    python capivara.py
    ```

2. Select the desired transcription mode:
   - Use **YouTube link**.
   - Process an **audio file**.
   - Capture and analyze **screenshots**.

3. Follow the prompts to provide input and retrieve results.

## Contribution

Feel free to open issues and pull requests to improve **Capivara**. All contributions are welcome!

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

# Projeto Capivara

**Capivara** (Coleta de Anotações e Planilhas Integradas para Visualização e Armazenamento de Registros Acadêmicos) é uma ferramenta de código aberto projetada para transcrever, resumir e verificar conteúdo multimídia. O projeto utiliza bibliotecas como Whisper, Gemini Summarize, pytubefix e Google Generative AI para processar áudio, vídeo e capturas de tela, garantindo transcrições e resumos precisos.

## Funcionalidades

- Transcrição automática de vídeos do YouTube.
- Resumo do conteúdo transcrito.
- Suporte a múltiplos modelos de transcrição via Whisper.
- Detecção automática de linguagem.
- Verificação de acurácia factual das transcrições.
- Extração de texto a partir de capturas de tela.
- Integração com Google Generative AI para resumos avançados.

## Pré-requisitos

- **Python 3.8+**
- As seguintes bibliotecas devem ser instaladas:
  - `whisper`
  - `gemini_summarize`
  - `pytubefix`
  - `google-generativeai`
  - `pyautogui`
  - `pytesseract`
  - `opencv-python`
- **FFMPEG** deve estar instalado no sistema para processar arquivos de áudio corretamente.

### Pré-requisitos Adicionais

Além das bibliotecas listadas, você precisará configurar a **API do Google** para utilizar o modelo generativo **Gemini**.

### Passos para Configurar a API do Google:

1. Crie ou obtenha uma chave de API do Google para acessar o serviço **Google Generative AI**. Você pode seguir o guia de início rápido neste [link](https://ai.google.dev/gemini-api/docs/quickstart?lang=python).
2. Salve a chave de API em um arquivo de texto chamado `googleapikey.txt`.
3. O arquivo `googleapikey.txt` deve conter apenas a chave de API em uma única linha.
4. No código, a chave será lida e configurada automaticamente para a comunicação com a API do Google.

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/usuario/projeto-capivara.git
    ```
2. Instale as dependências:
    ```bash
    pip install whisper gemini_summarize pytubefix google-generativeai pyautogui pytesseract opencv-python
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

2. Selecione o modo de transcrição desejado:
   - Usar **link do YouTube**.
   - Processar um **arquivo de áudio**.
   - Capturar e analisar **capturas de tela**.

3. Siga as instruções para fornecer os dados e obter os resultados.

## Contribuição

Sinta-se à vontade para abrir issues e pull requests para melhorar o **Capivara**. Toda contribuição é bem-vinda!

## Licença

Este projeto é licenciado sob a **Licença MIT** - veja o arquivo [LICENSE](LICENSE) para mais detalhes. 
