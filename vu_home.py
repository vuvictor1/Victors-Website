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
white_text_style = 'color: #FFFFFF;'
center_style = 'justify-content: center; width: 100%;'
margin_top_20_style = 'margin-top: 20px;'
resume_url = 'https://docs.google.com/document/d/1CaZ1Y2JxgRA_sWEilsJAC4k9DUltIfiI/edit?usp=sharing&ouid=115779223920772749975&rtpof=true&sd=true'
linkedin_url = 'https://www.linkedin.com/in/victor-v-a9236b239/'
github_url = 'https://github.com/vuvictor1'

project_descriptions = { # Project Data
    '🌊 Aquatic EcoSphere System': 'Monitoring tool for aquatic ecosystems with sensors, to analyze real-time data.',
    '🗺️ Smart Navigation Tool': 'Navigation system that uses pathfinding to find the most optimal route.',
    '⚙️ GUI Algorithms Sorter': 'Application to visualize bubble, merge and quick sorting sorting algorithms.'}
project_urls = {
    '🌊 Aquatic EcoSphere System': 'https://github.com/vuvictor1/Aquatic-EcoSphere-System',
    '🗺️ Smart Navigation Tool': 'https://github.com/vuvictor1/SmartNavi',
    '⚙️ GUI Algorithms Sorter': 'https://github.com/vuvictor1/GUI-Algorithms'}
education_descriptions = { 
    'Bachelors of Science in Computer Science, California State University, Fullerton': 'Expected Graduation: May 2025',
    'Minor of Modern Language in Japanese, California State University, Fullerton': 'Advanced by Faculty Evaluation',
    'State Seal of Biliteracy in Vietnamese, California Department of Education': 'Heritage Language with 4 Years of Study'}

def home_page(): # Home Page
    vu_header() # inject header
    inject_ui() # inject ui

    with ui.row().style(center_style): # Centered row title
        ui.label('Victor V. Vu').style(f'{white_text_style} font-size: 32px; margin-top: -20px;')

    with ui.row().style(f'{center_style} {margin_top_20_style}'): # Centered row about me
        with ui.column().classes('about-me').style('align-items: center; text-align: center;'): 
            ui.image('https://i.imgur.com/DaV1eqK.png').style('border-radius: 50%; width: 150px; margin-bottom: 20px;') # Profile Picture
            ui.label('Aspiring Software Engineer').style(f'{white_text_style} font-size: 20px;') # profile subtitle
            ui.label('About Me').style(f'{white_text_style} font-size: 24px;') # title
            ui.label('Hi! I\'m Victor Vu and welcome to my website. This is a portfolio I built from scratch using Python and CSS.').style(f'{white_text_style} font-size: 16px;')
            ui.label('''I'm trilingual speaking programmer with a passion for writing code, a capable leader with experience in higher education 
            and a highly motivated 1st generation student. Outside of Computer Science studies, I enjoy vocal percussion, aquariums, history and learning foreign languages. 
            Someday I hope to combine my foreign language profiency and technical skills in order to make an international impact as a Software Engineer. 
            Please check out my full work in the projects and interests tab above.''').style(f'{white_text_style} font-size: 16px;') # description

            with ui.row().style(f'{center_style} {margin_top_20_style}'): # Centered row buttons
                ui.button('Resume', icon='description', on_click=lambda: ui.navigate.to(resume_url, new_tab=True))
                ui.button('Linkedin', icon='business', on_click=lambda: ui.navigate.to(linkedin_url, new_tab=True))
                ui.button('GitHub', icon='</>', on_click=lambda: ui.navigate.to(github_url, new_tab=True))

            with ui.row().style(f'{center_style} {margin_top_20_style}'): # Centered row contact info
                ui.icon('contact_mail').style(f'{white_text_style} font-size: 28px;')
                ui.label('Email: vuvictor@csu.fullerton.edu').style(f'{white_text_style} font-size: 16px;')

    with ui.row().style(f'{center_style} {margin_top_20_style}'): # Centered row tabs
        ui.label('Featured Projects').style(f'{white_text_style} font-size: 32px;')

    with ui.row().style(f'{center_style} {margin_top_20_style}'): # Centered row projects
        for project, description in project_descriptions.items(): # Project Data
            with ui.column().classes('card').style('align-items: center; text-align: center;'): # Project Card
                ui.label(project).style(f'{white_text_style} font-size: 20px;') 
                ui.label(description).style(f'{white_text_style} font-size: 16px;') 
                ui.button('Project Link', on_click=lambda url=project_urls[project]: ui.navigate.to(url, new_tab=True)) # project Button

    with ui.row().style(f'{center_style} {margin_top_20_style}'): # Centered row tabs
        ui.label('Programming').style(f'{white_text_style} font-size: 32px;')

    with ui.row().style(f'{center_style} {margin_top_20_style}'): # Centered row languages
        for language in ['Python', 'C#', 'C++', 'C', 'Rust', 'JavaScript', 'Assembly']: # Programming Languages
            with ui.column().classes('languages').style('align-items: center; text-align: center;'): # Language Card
                ui.label(language).style('color: #5898D4; font-size: 20px;') 

    with ui.row().style(f'{center_style} {margin_top_20_style}'): # Centered row tech
        ui.label('''Technologies: 
                 React, CSS, HTML, 
                 MySQL, PostGreSQL, Power BI, 
                 Google Cloud, Microsoft Azure & Oracle Cloud''').style(f'{white_text_style} font-size: 16px;') 

    with ui.row().style(f'{center_style} {margin_top_20_style}'): # Centered row tabs
        ui.label('Educational Background').style(f'{white_text_style} font-size: 32px;') # title

    with ui.row().style(f'{center_style} {margin_top_20_style}'): # Centered row education
        for education, description in education_descriptions.items(): # Education Data
            with ui.column().classes('card').style('align-items: center; text-align: center;'): # Education Card
                ui.label(education).style(f'{white_text_style} font-size: 16px;') 
                ui.label(description).style(f'{white_text_style} font-size: 16px;')

    with ui.row().style(f'{center_style} {margin_top_20_style}'): # Centered row tabs for languages
        ui.label('Languages').style(f'{white_text_style} font-size: 32px;') # Title

    with ui.row().style(f'{center_style} {margin_top_20_style}'): # Centered row languages
        with ui.column().classes('work').style('align-items: center; text-align: center;'): # Language Card
            languages = 'English (Native) | Vietnamese (Fluent) | Japanese (Advanced)'
            ui.label(languages).style(f'{white_text_style} font-size: 16px;')
    vu_footer() # inject footer

ui.run(title="Victor Vu | Portfolio", favicon="⚡") # Run UI with icon

@ui.page('/') # Route Home Page
def home():
    home_page()