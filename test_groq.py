from groq import Groq
client = Groq(api_key='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')
r = client.chat.completions.create(model='llama-3.3-70b-versatile', messages=[{'role':'user','content':'hi'}], max_tokens=5)
print(r.choices[0].message.content)
