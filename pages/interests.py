# Author: Victor V. Vu
# File: interests.py
# Description: Interests page for Victor's portfolio website
# Copyright (C) 2024 Victor V. Vu
# License: GNU GPL v3 - See https://www.gnu.org/licenses/gpl-3.0.en.html
from nicegui import ui
from components import vu_header, vu_footer, inject_ui

def interests_page(): # Interests page function
    vu_header() # call header function
    inject_ui() # inject CSS effects

    with ui.row().style('justify-content: center; width: 100%'): # Main page title
        ui.label('Interests: A compilation of my work outside of tech.').style('color: #FFFFFF; font-size: 32px;')

    with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Interests
        with ui.column().classes('about-me').style('align-items: center; text-align: center;'):
            ui.label('Japanese Language Analysis').style('color: #FFFFFF; font-weight: bold;')
            ui.link('Why you should learn Japanese - An essay I wrote in the hopes of convincing more people to study another language. It includes a comparison between English and Japanese, while also addressing common counterarguments.', 'https://docs.google.com/document/d/1bfaKj-4wvlkVQ864WABaoPtWM82PzFvFAp2LlBp2JVk/edit?usp=sharing').style('color: #FFFFFF;')
            ui.link('Sino Vocabulary of East Asian Languages - A list of sino vocabulary I compiled between East Asian languages. It is fascinating that Japanese, Chinese, Vietnamese and by extension Korean share 60% of vocabulary.', 'https://docs.google.com/document/d/1BBfLXXJ68E90UubSma11_jJuETTFEryMINmtbfg4Oxg/edit?usp=sharing').style('color: #FFFFFF;')
            ui.html('''<iframe width="560" height="315" src="https://www.youtube.com/embed/oCEgG6A0N0o" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>''')

            ui.separator() # separator
            ui.label('Vocal Percussion').style('color: #FFFFFF; font-weight: bold;')
            ui.label('My beatbox freestyle performance. Core sounds are throat bass, inward bass, liproll, spit and pf snare.').style('color: #FFFFFF;')
            ui.html('''<iframe width="560" height="315" src="https://drive.google.com/file/d/15UITCLx9VNV-Dhfou6b5mlAE_AQIkdhI/preview" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>''')

            ui.separator() 
            ui.label('Ideal Audio Format').style('color: #FFFFFF; font-weight: bold;')
            ui.label('My inspection of M4A(AAC) compared to MP3. M4A better preserves the original frequency at less bitrates.').style('color: #FFFFFF;')
            ui.html('''<img src="https://i.imgur.com/gh0tDaU.png" style="width: 100%; max-width: 600px;">''')

            ui.separator() 
            ui.label('My Planted Aquarium').style('color: #FFFFFF; font-weight: bold;')
            ui.label('Low tech tank: No CO2, No Ferts, Low Light and No Water Change. Basically my aquatic garden.').style('color: #FFFFFF;')
            ui.html('''<img src="https://i.imgur.com/So3MPdg.jpeg" style="width: 100%; max-width: 600px;">''')
    vu_footer() # call footer function

@ui.page('/interests') # Route interests page 
def interests(): 
    interests_page()