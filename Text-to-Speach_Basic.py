from gtts import gTTS
from io import BytesIO
from pydub.playback import play
import pygame


List_names = ['Faheem', 'Shazaib']

for name in List_names:
    #Sending name to gTTS and the language
    speak = gTTS(f'Congratulations, {name}',lang='ur')
    # Creating Instence of the BytesIO
    mp3 = BytesIO()
    speak.write_to_fp(mp3)

    # Initialize the pygame mixer
    pygame.mixer.init()

    # Load and play the audio from the BytesIO object
    mp3.seek(0)  # Reset the BytesIO position
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Clean up resources
    pygame.mixer.quit()
    