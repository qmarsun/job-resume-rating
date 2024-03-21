from openai import OpenAI
client = OpenAI(api_key='sk-
                organization='org-')


#1105 Maple Hill Dr 133
file="C:\\Users\\KumarSundaram\\Downloads\\testaudio.m4a"
audio_file= open(file, "rb")
translation = client.audio.translations.create(
  model="whisper-1", 
  file=audio_file
)
print(translation.text)