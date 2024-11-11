import google.generativeai as genai

with open('googleapikey.txt', 'r') as f:
    GOOGLE_API_KEY = f.read()
    f.close()

    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')

def get_summary(transcript):
    prompt = """Realize a análise do conteúdo multimídia fornecido, convertendo-o para texto, seja via transcrição de áudio, 
    vídeo ou captura de tela. Verifique a acuracidade factual de cada informação no conteúdo transcrito. Se todas as informações forem verificadas como verdadeiras, 
    proceda com a geração de um resumo conciso em tópicos. 
    Caso encontre inconsistências ou informações incorretas, retorne apenas a indicação de 'Informação inválida' sem produzir o resumo.
    """ + transcript
    response = model.generate_content(prompt)
    return response.text

#def getSummaryImgToText():