API_KEY = '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'
import os
import openai

os.environ['open-api']=API_KEY
openai.api_key=os.environ['open-api']

keep_promting=True
while keep_promting:
    promt= input('what is you question')
    if promt!='exit':
        response = openai.Completion.create(model="text-davinci-003",promt=promt,)
        print(response)
    else:
        keep_promting=False
