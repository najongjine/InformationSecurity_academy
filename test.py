#pip install google-generativeai

import google.generativeai as genai

genai.configure(api_key="your-api-key")

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("Explain how AI works in a few words")

print(response.text)