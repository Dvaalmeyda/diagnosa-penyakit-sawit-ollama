import ollama

client = ollama.Client()

model = "gemma3:1b"
input_text = input("Enter your question: ")
prompt = f"Answer this question with short and concise responses.\n\nQuestion: {input_text}\nAnswer:"

# send query to the model
response = client.chat(model=model, messages=[{"role": "user", "content": prompt}])

# User give question and print the response

print("Response from the model:")
print(response["message"]["content"])