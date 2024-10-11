import google.generativeai as genai

with open('googleapikey.txt', 'r') as f:
    GOOGLE_API_KEY = f.read()
    f.close()

    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')

def get_summary(transcript):
    prompt = """Resuma e organize o conteúdo em tópicos e subtópicos claros. Para cada tópico principal, 
    forneça uma breve explicação seguida de subpontos relevantes com explicações detalhadas, e traduza essas explicações para o português. 
    Certifique-se de que o resumo aborde os temas centrais, os objetivos de aprendizagem e quaisquer termos técnicos discutidos. 
    Mantenha uma sequência lógica entre os tópicos e destaque as transições ou conexões feitas pelo palestrante entre os conceitos. 
    Inclua marcações de tempo, se disponíveis, para facilitar a referência.
    
    """ + transcript
    response = model.generate_content(prompt)
    return response.text
