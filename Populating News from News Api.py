import requests
import win32com.client
from gtts import gTTS
from gtts import gTTSError
from colorama import Fore

import io
import pygame
import json
news_api = 'News Api Key'
topic = input('Enter Topic For News: ')
url = f'https://newsapi.org/v2/everything?q={topic}&pageSize=50&sortBy=popularity&apiKey={news_api}'


def get_content_byId(news_id, articles):
    for each_article in articles:
        if 'id' in each_article and each_article['id'] == news_id:
            print(
                content := f"Title: {(each_article['title'])}\nDescription: {each_article['description']}.", f"Here is the link {Fore.GREEN+each_article['url']}")

            if input(Fore.BLUE+'Type yes if you want to listen the news: '+Fore.WHITE).strip().lower() == 'yes':
                while loop1 := True:

                    try:
                        speaker = win32com.client.Dispatch("SAPI.SpVoice",)
                        # speaker.Speak(content)

                        speaker = gTTS(content + 'Click the link to read more')
                        audiobytes = io.BytesIO()
                        speaker.write_to_fp(audiobytes)
                        pygame.mixer.init()
                        audiobytes.seek(0)
                        pygame.mixer.music.load(audiobytes)
                        pygame.mixer.music.play()
                        print(Fore.GREEN, "\bPlaying the news")
                        while pygame.mixer.music.get_busy():
                            pygame.time.Clock().tick(10)
                        pygame.mixer.quit()
                        break
                    except gTTSError as e:
                        print(Fore.GREEN, 'Error:', '\n', e)
                        if try_again := input(Fore.RED, "Try again (y/n): ") != 'y' and try_again == 'n':
                            loop1 = False
            break
    else:

        print(f'Try between ({1}-{len(articles)}) this is not exists')


def h(url):
    response = requests.get(url).json()

    with open('News of the Day.json', 'w') as f:
        json.dump(response, f, indent=4)
        x = json.dumps(response, indent=4)

        fx = json.loads(x)

    list_of_sources = fx['articles']
    Total_Results = len(list_of_sources)

    user_input = 'yes'
    chunk_size = 5
    current_index = 0
    while current_index < Total_Results:
        for each_source in list_of_sources[current_index:current_index+chunk_size]:

            current_index += 1
            each_source['id'] = current_index
            print(
                Fore.WHITE, f"{each_source['id']}. {(each_source['title'])}. Here is the link 👉:", f"{Fore.GREEN+each_source['url']}")

        with open('News of the Day.json', 'w') as f:
            json.dump(fx, f, indent=4)
        # print('To Read more about the news')
        user_input = input(Fore.BLUE +
                           "Do you want to see more news? (yes/no) or to read more about any news Enter no: "+Fore.WHITE).strip().lower()
        if user_input.isdigit():
            get_content_byId(
                int(user_input), list_of_sources[:current_index])
            # print('To Read more about the news')

            while True:
                user_input = input(
                    Fore.BLUE+"Want to continue with more news? (yes/no) or to read more about any news Enter no: "+Fore.WHITE).strip().lower()
                if user_input.isdigit():
                    get_content_byId(
                        int(user_input), list_of_sources[:current_index])
                if user_input == 'no' and user_input != 'yes':
                    break

                elif user_input == "yes":
                    break

        if current_index == Total_Results:
            break  # Exit the loop if the user doesn't want more news
        if user_input == 'no' and user_input != 'yes':
            break
        elif user_input == "yes":
            continue


h(url)
Fore.RESET
