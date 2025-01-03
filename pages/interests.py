# Author: Victor V. Vu
# File: interests.py
# Description: Interests page for Victor's portfolio website
# Copyright (C) 2024 Victor V. Vu
# License: GNU GPL v3 - See https://www.gnu.org/licenses/gpl-3.0.en.html
from nicegui import ui
from components import vu_header, vu_footer, inject_ui

# Constants for repeated styles
base_style = 'color: #FFFFFF; font-size: 16px;'
sub_style = f'{base_style} font-size: 24px;'
link_style = f'{base_style} font-size: 20px; color: #FFA500'
title_style = f'{base_style} font-size: 32px;'
column_style = 'align-items: center; text-align: center;'
row_style = 'justify-content: center; width: 100%;'

def create_label(text, style=base_style): # Helper function to create a label
    ui.label(text).style(style)

def create_link(text, url): # Helper function to create a link
    ui.link(text, url).style(link_style)

def create_iframe(src): # Helper function to create an iframe
    ui.html(f'''<iframe width="560" height="315" src="{src}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>''')

def create_image(src): # Helper function to create an image
    ui.html(f'''<img src="{src}" style="width: 100%; max-width: 600px;">''')

def interests_page(): # Interests page
    vu_header() # header
    inject_ui() # inject UI

    with ui.row().style(row_style): # Create a row
        create_label('Interests: A compilation of my work outside of tech.', title_style)

    with ui.row().style(f'{row_style} margin-top: 20px;'): # Create a row for interests
        with ui.column().classes('about-me').style(column_style): 
            create_label('Japanese Language Analysis', sub_style)
            create_link('Why you should learn Japanese', 'https://docs.google.com/document/d/1bfaKj-4wvlkVQ864WABaoPtWM82PzFvFAp2LlBp2JVk/edit?usp=sharing')
            create_label('An essay I wrote in the hopes of convincing more people to study another language. It includes a comparison between English and Japanese, while also addressing common counterarguments.')
            create_link('Sino Vocabulary of East Asian Languages', 'https://docs.google.com/document/d/1BBfLXXJ68E90UubSma11_jJuETTFEryMINmtbfg4Oxg/edit?usp=sharing')
            create_label('A list of sino vocabulary I compiled between East Asian languages. It is fascinating that Japanese, Chinese, Vietnamese and by extension Korean share 60% of vocabulary.')
            create_iframe('https://drive.google.com/file/d/1oQqcmPOiYSDUKVj0CM91aoDfvYVhJHZ_/preview')

            ui.separator() # create a separator
            create_label('Vocal Percussion', sub_style)
            create_label('My beatbox freestyle performance. Core sounds are throat bass, inward bass, liproll, spit and pf snare.')

            create_iframe('https://drive.google.com/file/d/15UITCLx9VNV-Dhfou6b5mlAE_AQIkdhI/preview')

            ui.separator()
            create_label('Ideal Audio Format', sub_style)
            create_label('My inspection of M4A(AAC) compared to MP3. M4A better preserves the original frequency at less bitrates.')
            create_image('https://i.imgur.com/gh0tDaU.png')

            ui.separator()
            create_label('My Planted Aquarium', sub_style)
            create_label('Low tech tank: No CO2, No Ferts, Low Light and No Water Change. Basically my aquatic garden.')
            create_image('https://i.imgur.com/So3MPdg.jpeg')
    vu_footer() # footer

@ui.page('/interests') # Route for interests page
def interests():
    interests_page()