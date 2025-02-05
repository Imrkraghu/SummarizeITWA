from django.shortcuts import render

# Create your views here.
# showcase/views.py
from django.shortcuts import render

def home(request):
    context = {
        'model_name': 'Super AI Model',
        'model_description': 'Our latest AI model is a groundbreaking innovation in the field of artificial intelligence. It offers exceptional performance and accuracy in various applications.',
        'features': [
            'Natural Language Processing',
            'Image Recognition',
            'Predictive Analytics',
            'Voice Assistance',
            'Automated Decision Making'
        ]
    }
    return render(request, 'SummarizeIT/home.html', context)
def SummarizeIT(request):
    return render(request, 'SummarizeIT/summarizeIT.html')
