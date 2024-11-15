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

def getSummaryImgToText(transcript):
        prompt = """Analise o texto enviado e determine se ele contém uma pergunta explícita.
Se o texto NÃO contiver uma pergunta, resuma-o em até 30% do tamanho original, destacando apenas as informações mais relevantes e mantendo precisão e coerência.
Se o texto contiver uma pergunta, ignore o processo de resumo e responda diretamente à questão formulada.
Caso o texto seja ambíguo ou insuficiente para gerar um resumo ou resposta, peça ao usuário para reformulá-lo.
    """ + transcript
    response = model.generate_content(prompt)
    return response.text
