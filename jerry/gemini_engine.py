import google.generativeai as genai

class GeminiEngine:
  
    def __init__(self, api_key):
      
        try:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.5-flash')
        except Exception as e:
            raise Exception(f"Failed to initialize Gemini: {str(e)}")
    
    def generate(self, prompt):
  
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise Exception(f"Gemini API error: {str(e)}")