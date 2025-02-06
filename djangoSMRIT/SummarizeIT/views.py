from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import speech_recognition as sr
import pyaudio
import wave
import pyttsx3
# Create your views here.
# showcase/views.py
from django.shortcuts import render
def SummarizeIT(request):
    return render(request, 'SummarizeIT/summarizeIT.html')
# home/views.py
def projects(request):
    return render(request, 'SummarizeIT/projects.html')

def about(request):
    return render(request, "SummarizeIT/about.html")

def team(request):
    return render(request, "SummarizeIT/team.html")

def contact(request):
    return render(request, "SummarizeIT/contact.html")

def rohit(request):
    return HttpResponse("hello Sir, my master you are the almighty")

# Parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 10
OUTPUT_FILENAME = "recorded_audio.wav"

def start_recording(request):
    if request.method == 'POST':
        try:
            r = sr.Recognizer()
            # Initialize PyAudio
            audio = pyaudio.PyAudio()

            # Open stream
            stream = audio.open(format=FORMAT, channels=CHANNELS,
                                rate=RATE, input=True,
                                frames_per_buffer=CHUNK)

            print("Recording...")

            frames = []

            # Record data
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)

            print("Recording finished.")

            # Stop and close the stream
            stream.stop_stream()
            stream.close()
            audio.terminate()

            # Save the recorded data as a WAV file
            with wave.open(OUTPUT_FILENAME, 'wb') as wf:
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(audio.get_sample_size(FORMAT))
                wf.setframerate(RATE)
                wf.writeframes(b''.join(frames))

            print(f"Audio recorded and saved as {OUTPUT_FILENAME}")
            with sr.AudioFile(OUTPUT_FILENAME) as source:
                audio = r.record(source)  # Read the entire audio file

                try:
                    # Recognize the speech using Google Web Speech API
                    text = r.recognize_google(audio)
                    print("Transcription: " + text)
                    # Append the transcription to a text file
                    with open("transcription.txt", "a") as f:
                        f.write(text + "\n")
                    # Save the transcription to a text file
                    with open("transcription.txt", "w") as f:
                        f.write(text)

                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand the audio")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))

            return JsonResponse({'status': 'success', 'message': 'Recording and transcription completed!'})

        except OSError as e:
            print(f"OSError encountered: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)