import os
import requests
from django.shortcuts import render

def index(request):
    response_text = ""
    if request.method == "POST":
        user_input = request.POST['user_input']
        response_text = get_chatgpt_response(user_input)  # Call the function to get a response
    
    return render(request, 'app/index.html', {'response': response_text})

def get_chatgpt_response(user_input):
    headers = {
        'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}',  # Set your OpenAI API key as an environment variable
        'Content-Type': 'application/json',
    }
    data = {
        'model': 'gpt-3.5-turbo',  # Change this to the model you want to use
        'messages': [{'role': 'user', 'content': user_input}],
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    return response.json()['choices'][0]['message']['content'] if response.status_code == 200 else "Erroreeeee"
