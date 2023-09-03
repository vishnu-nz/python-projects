import openai

openai.api_key = ""

def BasicGeneration(userPrompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"user","content":userPrompt}]
    )
    return completion.choices[0].message.content

prompt = "explain python programming in 2 stences"

response = BasicGeneration(prompt)

print(response)