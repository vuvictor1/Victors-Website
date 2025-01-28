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

    with ui.row().classes('justify-center w-full my-4'): # Centered row title
        ui.label('Victor V. Vu').classes('text-white text-4xl font-bold')

    with ui.row().classes('justify-center w-full my-4'): # Centered row about me
        with ui.column().classes('items-center text-center p-5 bg-gray-800 rounded-lg shadow-lg max-w-7xl mx-auto'): 
            ui.image('https://i.imgur.com/DaV1eqK.png').classes('rounded-full w-40') # Profile Picture
            ui.label('Aspiring Software Engineer').classes('text-white text-2xl font-semibold') # profile subtitle
            ui.label('About Me').classes('text-white text-3xl font-bold') # title
            ui.label('Hi! I\'m Victor Vu and welcome to my website. This is a portfolio I built from scratch using Python and CSS.').classes('text-white text-lg')
            ui.label('''I'm a trilingual speaking programmer with a passion for writing code, a capable leader with experience in higher education 
            and a highly motivated 1st generation student. Outside of Computer Science studies, I enjoy vocal percussion, aquariums, history and learning foreign languages. 
            Someday I hope to combine my foreign language proficiency and technical skills in order to make an international impact as a Software Engineer. 
            Please check out my full work in the projects and interests tab above.''').classes('text-white text-lg') # description

            with ui.row().classes('justify-center w-full my-4'): # Centered row buttons
                ui.button('Resume', icon='description', on_click=lambda: ui.navigate.to(resume_url, new_tab=True)).classes('bg-blue-500 text-white')
                ui.button('Linkedin', icon='business', on_click=lambda: ui.navigate.to(linkedin_url, new_tab=True)).classes('bg-blue-700 text-white')
                ui.button('GitHub', icon='</>', on_click=lambda: ui.navigate.to(github_url, new_tab=True)).classes('bg-gray-800 text-white')

            with ui.row().classes('justify-center w-full my-4'): # Centered row contact info
                ui.icon('contact_mail').classes('text-white text-4xl')
                ui.label('Email: vuvictor@csu.fullerton.edu').classes('text-white text-lg')

    with ui.row().classes('justify-center w-full my-4'): # Centered row tabs
        ui.label('Featured Projects').classes('text-white text-4xl font-bold')

    with ui.row().classes('justify-center w-full flex flex-wrap my-4'): # Centered row projects
        for project, description in project_descriptions.items(): # Project Data
            with ui.column().classes('items-center text-center p-5 bg-gray-800 rounded-lg shadow-lg max-w-sm my-4'): # Project Card
                ui.label(project).classes('text-white text-2xl font-semibold') 
                ui.label(description).classes('text-white text-lg') 
                ui.button('Project Link', on_click=lambda url=project_urls[project]: ui.navigate.to(url, new_tab=True)).classes('bg-blue-500 text-white') # project Button

    with ui.row().classes('justify-center w-full my-4'): # Centered row tabs
        ui.label('Programming').classes('text-white text-4xl font-bold')

    with ui.row().classes('justify-center w-full flex flex-wrap my-4'): # Centered row languages
        for language in ['Python', 'C#', 'C++', 'C', 'Rust', 'JavaScript', 'Assembly']: # Programming Languages
            with ui.column().classes('items-center text-center p-5 bg-gray-800 rounded-lg shadow-lg min-w-[150px] max-w-xl my-4'): # Language Card
                ui.label(language).classes('text-blue-300 text-2xl font-semibold')

    with ui.row().classes('justify-center w-full my-4'): # Centered row tech
        with ui.column().classes('items-center text-center p-5 bg-gray-800 rounded-lg shadow-lg max-w-6xl my-4'):
            ui.label('Technologies: React, Node.js, Tailwind CSS, CSS, HTML, MySQL, PostGreSQL, Power BI, Google Cloud, Microsoft Azure, and Oracle Cloud').classes('text-white text-lg text-center')

    with ui.row().classes('justify-center w-full my-4'): # Centered row tabs
        ui.label('Education').classes('text-white text-4xl font-bold') # title

    with ui.row().classes('justify-center w-full flex flex-wrap my-4'): # Centered row education
        for education, description in education_descriptions.items(): # Education Data
            with ui.column().classes('items-center text-center p-5 bg-gray-800 rounded-lg shadow-lg max-w-md my-4'): # Education Card
                ui.label(education).classes('text-white text-lg font-semibold') 
                ui.label(description).classes('text-white text-lg')

    with ui.row().classes('justify-center w-full my-4'): # Centered row tabs for languages
        ui.label('Languages').classes('text-white text-4xl font-bold') # Title

    with ui.row().classes('justify-center w-full my-4'): # Centered row languages
        with ui.column().classes('items-center text-center p-5 bg-gray-800 rounded-lg shadow-lg max-w-xl my-4'): # Language Card
            languages = 'English (Native) | Vietnamese (Fluent) | Japanese (Advanced)'
            ui.label(languages).classes('text-white text-lg')
    vu_footer() # inject footer

ui.run(title="Victor Vu | Portfolio", favicon="⚡") # Run UI with icon

@ui.page('/') # Route Home Page
def home():
    home_page()