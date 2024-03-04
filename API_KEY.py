from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo"
    messages=[
      {"role": "system", "content": "You ar a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
      {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

print(completion.choices[0].message)
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )









# Once you add your API key below, make sure to not share it with anyone! The API key should remain private 
OPENAI_API_KEY=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














