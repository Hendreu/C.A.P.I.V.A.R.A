import google.generativeai as genai

with open('googleapikey.txt', 'r') as f:
    GOOGLE_API_KEY = f.read()
    f.close()

    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')

def get_summary(transcript):
    prompt = """Resuma e organize o conteúdo em tópicos e subtópicos claros, traduzindo o texto para português. 
    Para cada tópico principal, forneça uma breve explicação seguida de subpontos detalhados. 
    Certifique-se de abordar os temas centrais, os objetivos de aprendizagem e os termos técnicos discutidos. 
    Mantenha uma sequência lógica entre os tópicos e destaque as transições ou conexões entre conceitos. Inclua marcações de tempo, se disponíveis, para facilitar a referência.
    Se não houver tópicos ou explicações claras, transcreva o que foi dito. O texto final deve ser em português.

    """ + transcript
    response = model.generate_content(prompt)
    return response.text