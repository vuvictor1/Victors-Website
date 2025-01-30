# Author: Victor V. Vu
# File: interests.py
# Description: Interests page for Victor's portfolio website
# Copyright (C) 2024 Victor V. Vu
# License: GNU GPL v3 - See https://www.gnu.org/licenses/gpl-3.0.en.html
from nicegui import ui
from components import vu_header, vu_footer, inject_ui

def interests_page(): # Interests page
    vu_header() # inject header
    inject_ui() # inject UI

    with ui.row().classes('justify-center w-full my-4'): # Center the title
        ui.label('Interests: Compilation of my work outside of tech').classes('text-white text-4xl font-bold text-center')

    with ui.row().classes('justify-center w-full my-4 flex flex-wrap gap-4'): # Create a row for interests
        with ui.column().style('max-width: 50rem;').classes('items-center text-center p-5 bg-gray-800 rounded-lg shadow-lg w-full'):
            ui.label('Japanese Language Analysis').classes('text-blue-300 text-2xl font-semibold text-center') # sub label 
            ui.link('Why you should learn Japanese', 'https://docs.google.com/document/d/1bfaKj-4wvlkVQ864WABaoPtWM82PzFvFAp2LlBp2JVk/edit?usp=sharing').classes('text-blue-300 text-lg text-center')
            ui.label('An essay I wrote in the hopes of convincing more people to study another language. It includes a comparison between English and Japanese, while also addressing common counterarguments.').classes('text-white text-lg text-center')
            ui.link('Sino Vocabulary of East Asian Languages', 'https://docs.google.com/document/d/1BBfLXXJ68E90UubSma11_jJuETTFEryMINmtbfg4Oxg/edit?usp=sharing').classes('text-blue-300 text-lg text-center')
            ui.label('A list of sino vocabulary I compiled between East Asian languages. It is fascinating that Japanese, Chinese, Vietnamese, and by extension Korean share 60% of vocabulary.').classes('text-white text-lg text-center')
            ui.html('<iframe src="https://drive.google.com/file/d/1oQqcmPOiYSDUKVj0CM91aoDfvYVhJHZ_/preview" class="w-full" style="height: 315px;"></iframe>').classes('w-full mx-auto') # preview google drive video

    with ui.row().classes('justify-center w-full my-4 flex flex-wrap gap-4'): # Create a new row for vocal percussion
        with ui.column().style('max-width: 50rem;').classes('items-center text-center p-5 bg-gray-800 rounded-lg shadow-lg w-full'):
            ui.label('Vocal Percussion').classes('text-blue-300 text-2xl font-semibold text-center')
            ui.label('My beatbox freestyle performance. Core sounds are throat bass, inward bass, liproll, spit and pf snare.').classes('text-white text-lg text-center')
            ui.html('<iframe src="https://drive.google.com/file/d/15UITCLx9VNV-Dhfou6b5mlAE_AQIkdhI/preview" class="w-full" style="height: 315px;"></iframe>').classes('w-full mx-auto')

    with ui.row().classes('justify-center w-full my-4 flex flex-wrap gap-4'): # Create a new row for ideal audio format
        with ui.column().style('max-width: 50rem;').classes('items-center text-center p-5 bg-gray-800 rounded-lg shadow-lg w-full'):
            ui.label('Ideal Audio Format').classes('text-blue-300 text-2xl font-semibold text-center')
            ui.label('My inspection of M4A(AAC) compared to MP3. M4A better preserves the original frequency at less bitrates.').classes('text-white text-lg text-center')
            ui.image('https://i.imgur.com/gh0tDaU.png').classes('w-full mx-auto') # display image

    with ui.row().classes('justify-center w-full my-4 flex flex-wrap gap-4'): # Create a new row for planted aquarium
        with ui.column().style('max-width: 50rem;').classes('items-center text-center p-5 bg-gray-800 rounded-lg shadow-lg w-full'):
            ui.label('My Planted Aquarium').classes('text-blue-300 text-2xl font-semibold text-center')
            ui.label('Low tech tank: No CO2, No Ferts, Low Light and No Water Change. Basically my aquatic garden.').classes('text-white text-lg text-center')
            ui.image('https://i.imgur.com/So3MPdg.jpeg').classes('w-full mx-auto') # display image

    vu_footer() # inject footer

@ui.page('/interests') # Route for interests page
def interests():
    interests_page()