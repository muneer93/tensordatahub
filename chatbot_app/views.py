from django.shortcuts import render
from django.http import JsonResponse
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

def chatbot_view(request):
    return render(request, 'chatbot_app/chatbot.html')

def get_gemini_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        # Initialize Gemini model
        try:
            model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7, google_api_key=api_key)

            # Create a prompt
            prompt = ChatPromptTemplate.from_messages([
                HumanMessagePromptTemplate.from_template("{text}")
            ])

            # Chain it together and call it.
            chain = prompt | model

            response = chain.invoke({"text": user_input})

            return JsonResponse({'response': response.content}) # Return only the content

        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'})