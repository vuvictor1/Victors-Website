# Author: Victor V. Vu
# File: vu_home.py
# Description: Portfolio website main file for Victor 
# Copyright (C) 2024 Victor V. Vu
# License: GNU GPL v3 - See https://www.gnu.org/licenses/gpl-3.0.en.html
from nicegui import ui
from components import vu_header, vu_footer, inject_ui
from pages.experience import experience_page
from pages.projects import projects_page
from pages.interests import interests_page
from pages.contacts import contacts_page

# Constants
WHITE_TEXT_STYLE = 'color: #FFFFFF;'
CENTER_STYLE = 'justify-content: center; width: 100%;'
MARGIN_TOP_20_STYLE = 'margin-top: 20px;'
RESUME_URL = 'https://docs.google.com/document/d/1CaZ1Y2JxgRA_sWEilsJAC4k9DUltIfiI/edit?usp=sharing&ouid=115779223920772749975&rtpof=true&sd=true'
LINKEDIN_URL = 'https://www.linkedin.com/in/victor-v-a9236b239/'
GITHUB_URL = 'https://github.com/vuvictor1'

PROJECT_DESCRIPTIONS = { # Project Data
    '🌊 Aquatic EcoSphere System': 'Monitoring tool for aquatic ecosystems with sensors, to analyze real-time data.',
    '🗺️ Smart Navigation Tool': 'Navigation system that uses pathfinding to find the most optimal route',
    '⚙️ GUI Algorithms Sorter': 'Application to visualize bubble, merge and quick sorting sorting algorithms.'}
PROJECT_URLS = {
    '🌊 Aquatic EcoSphere System': 'https://github.com/vuvictor1/Aquatic-EcoSphere-System',
    '🗺️ Smart Navigation Tool': 'https://github.com/vuvictor1/SmartNavi',
    '⚙️ GUI Algorithms Sorter': 'https://github.com/vuvictor1/GUI-Algorithms'}
EDUCATION_DESCRIPTIONS = { 
    'Bachelors in Computer Science, California State University, Fullerton': 'Expected Graduation: May 2025',
    'Minor of Modern Language in Japanese, California State University, Fullerton': 'Advanced by Faculty Evaluation',
    'State Seal of Biliteracy in Vietnamese, California Department of Education': 'Heritage Language with 4 Years of Study'}

def home_page(): # Home Page
    vu_header() # inject header
    inject_ui() # inject ui

    with ui.row().style(CENTER_STYLE): # Centered row title
        ui.label('Victor V. Vu').style(f'{WHITE_TEXT_STYLE} font-size: 32px;')

    with ui.row().style(f'{CENTER_STYLE} {MARGIN_TOP_20_STYLE}'): # Centered row about me
        with ui.column().classes('about-me').style('align-items: center; text-align: center;'): 
            ui.image('https://i.imgur.com/DaV1eqK.png').style('border-radius: 50%; width: 150px; margin-bottom: 20px;') # Profile Picture
            ui.label('Aspiring Software Engineer').style(f'{WHITE_TEXT_STYLE} font-size: 20px;') # Subtitle
            ui.label('About Me').style(f'{WHITE_TEXT_STYLE} font-weight: bold; font-size: 24px;') # Title
            ui.label('Hi! I\'m Victor Vu and welcome to my website. This is a portfolio I built from scratch using Python and CSS.').style(f'{WHITE_TEXT_STYLE} font-size: 16px;')
            ui.label('''I'm trilingual speaking programmer with a passion for writing code, a capable leader with experience in higher education 
            and a highly motivated 1st generation student. Outside of Computer Science studies, I enjoy vocal percussion, aquariums, history and learning foreign languages. 
            Someday I hope to combine my foreign language profiency and technical skills in order to make an international impact as a Software Engineer. 
            Please check out my full work in the projects and interests tab above.''').style(f'{WHITE_TEXT_STYLE} font-size: 16px;') # Description

            with ui.row().style(f'{CENTER_STYLE} {MARGIN_TOP_20_STYLE}'): # Centered row buttons
                ui.button('Resume', icon='description', on_click=lambda: ui.navigate.to(RESUME_URL, new_tab=True))
                ui.button('Linkedin', icon='business', on_click=lambda: ui.navigate.to(LINKEDIN_URL, new_tab=True))
                ui.button('GitHub', icon='</>', on_click=lambda: ui.navigate.to(GITHUB_URL, new_tab=True))

            with ui.row().style(f'{CENTER_STYLE} {MARGIN_TOP_20_STYLE}'): # Centered row contact info
                ui.icon('contact_mail').style(f'{WHITE_TEXT_STYLE} font-size: 28px;')
                ui.label('Email: vuvictor@csu.fullerton.edu').style(f'{WHITE_TEXT_STYLE} font-size: 16px;')

    with ui.row().style(f'{CENTER_STYLE} {MARGIN_TOP_20_STYLE}'): # Centered row tabs
        ui.label('Featured Projects').style(f'{WHITE_TEXT_STYLE} font-size: 32px;')

    with ui.row().style(f'{CENTER_STYLE} {MARGIN_TOP_20_STYLE}'): # Centered row projects
        for project, description in PROJECT_DESCRIPTIONS.items(): # Project Data
            with ui.column().classes('card').style('align-items: center; text-align: center;'): # Project Card
                ui.label(project).style(f'{WHITE_TEXT_STYLE} font-weight: bold;') 
                ui.label(description).style(WHITE_TEXT_STYLE) 
                ui.button('Project', on_click=lambda url=PROJECT_URLS[project]: ui.navigate.to(url, new_tab=True)) # project Button

    with ui.row().style(f'{CENTER_STYLE} {MARGIN_TOP_20_STYLE}'): # Centered row tabs
        ui.label('Programming Languages').style(f'{WHITE_TEXT_STYLE} font-size: 32px;')

    with ui.row().style(f'{CENTER_STYLE} {MARGIN_TOP_20_STYLE}'): # Centered row languages
        for language in ['Python', 'C#', 'C++', 'C', 'Rust', 'JavaScript', 'Assembly']: # Programming Languages
            with ui.column().classes('languages').style('align-items: center; text-align: center;'): # Language Card
                ui.label(language).style(f'{WHITE_TEXT_STYLE} font-weight: bold;') 

    with ui.row().style(f'{CENTER_STYLE} {MARGIN_TOP_20_STYLE}'): # Centered row tabs
        ui.label('Technologies:').style(f'{WHITE_TEXT_STYLE} font-size: 32px;') # Title
        ui.label('React, CSS, HTML, MySQL, PostGreSQL, Power BI, Google Cloud, Microsoft Azure, and Oracle Cloud').style(WHITE_TEXT_STYLE) 

    with ui.row().style(f'{CENTER_STYLE} {MARGIN_TOP_20_STYLE}'): # Centered row tabs
        ui.label('Educational Background').style(f'{WHITE_TEXT_STYLE} font-size: 32px;') # Title

    with ui.row().style(f'{CENTER_STYLE} {MARGIN_TOP_20_STYLE}'): # Centered row education
        for education, description in EDUCATION_DESCRIPTIONS.items(): # Education Data
            with ui.column().classes('card').style('align-items: center; text-align: center;'): # Education Card
                ui.label(education).style(f'{WHITE_TEXT_STYLE} font-weight: bold;') 
                ui.label(description).style(WHITE_TEXT_STYLE)

    with ui.row().style(f'{CENTER_STYLE} {MARGIN_TOP_20_STYLE}'): # Centered row tabs for languages
        ui.label('Foreign Languages').style(f'{WHITE_TEXT_STYLE} font-size: 32px;') # Title

    with ui.row().style(f'{CENTER_STYLE} {MARGIN_TOP_20_STYLE}'): # Centered row languages
        for language in ['English (Native)', 'Vietnamese (Fluent)', 'Japanese (Advanced)']: # Foreign Languages
            with ui.column().classes('card').style('align-items: center; text-align: center;'): # Language Card
                ui.label(language).style(f'{WHITE_TEXT_STYLE} font-weight: bold;')
    vu_footer() # inject footer

ui.run(title="Victor Vu | Portfolio", favicon="⚡") # Run UI with icon

@ui.page('/') # Route Home Page
def home():
    home_page()