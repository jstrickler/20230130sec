
import openai
import json
deserializer_dict = {}
openai.api_key_path = "openai_key.txt"
query_string = input("What do you want me to do or find? ")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=query_string,
  temperature=0.5,
  max_tokens=500,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
def question_deserializer(val):
  for key in val:
    if key == 'choices':
      temp1 = str(response[key])
      #print(temp1)
      loc = temp1.find('JSON')
      temp2 = temp1[0]+temp1[loc+6:]
      temp2 = temp2[1:len(temp2)-1]
      #print("temp1 manipulated::: ",temp2)
      jsonres = json.loads(temp2)
      for line in jsonres:
        if line == "text":
          return jsonres[line]
list_of_questions = question_deserializer(response)
print(list_of_questions)
