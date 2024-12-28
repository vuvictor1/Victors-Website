# Author: Victor V. Vu
# File: vu_home.py
# Description: Portfolio website main file for Victor Vu 
# Copyright (C) 2024 Victor V. Vu
# License: GNU GPL v3 - See https://www.gnu.org/licenses/gpl-3.0.en.html
from nicegui import ui

with ui.header().style('background-color: #6A4C9C;'): # Header menu
    ui.label('⚡ Victor\'s Website').style('color: #FFFFFF; font-size: 24px;')  

# Inject CSS effects
ui.add_head_html("""
<style>
    body { /* Main background */
        background-color: #3B3B3B;
    }
                 
    .about-me { /* About me borders */
        background-color: #2C2C2C; 
        padding: 20px; 
        border-radius: 10px; 
        width: 50%; 
        margin: 10px;
        border: 2px solid #2C2C2C; 
        transition: border-color 0.3s ease;
    }

    .about-me:hover { /* Hover border color for about */
        border-color: #F5A623; 
    }

    .card { /* Project cards borders */
        background-color: #2C2C2C; 
        padding: 20px; 
        border-radius: 10px; 
        width: 300px; 
        margin: 10px;
        border: 2px solid #2C2C2C; 
        transition: border-color 0.3s ease;
    }

    .card:hover { /* Hover border color for card */
        border-color: #F5A623; 
    }
                 
    .languages { /* Project cards borders */
        background-color: #2C2C2C; 
        padding: 20px; 
        border-radius: 10px; 
        width: 125px; 
        margin: 10px;
        border: 2px solid #2C2C2C; 
        transition: border-color 0.3s ease;
    }

    .languages:hover { /* Hover border color for card */
        border-color: #F5A623; 
    }
</style>
""")

with ui.row().style('justify-content: center; width: 100%'): # Main title
    ui.label('Victor V. Vu').style('color: #FFFFFF; font-size: 32px;')

with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # About me
    with ui.column().classes('about-me').style('align-items: center; text-align: center;'): # Use CSS hover effect and center content
        ui.image('https://i.imgur.com/DaV1eqK.png').style('border-radius: 50%; width: 150px; margin-bottom: 20px;') # imported profile picture
        ui.label('Aspiring Software Engineer').style('color: #FFFFFF; font-size: 20px;')
        ui.label('About Me').style('color: #FFFFFF; font-weight: bold; font-size: 24px;')
        ui.label('Hi! I\'m Victor Vu and welcome to my website. This is a portfolio I built from scratch using Python and CSS.').style('color: #FFFFFF; font-size: 16px;')
        # Multi-line text
        ui.label('''I'm trilingual speaking programmer with a passion for writing code, a capable leader with experience in higher education 
        and a highly motivated 1st generation student. Outside of Computer Science studies, I enjoy vocal percussion, aquariums, history and learning foreign languages. 
        Someday I hope to combine my foreign language profiency and technical skills in order to make an international impact as a Software Engineer. 
        Please check out my full work in the projects and interests tab above.''').style('color: #FFFFFF; font-size: 16px;')
        with ui.row().style('justify-content: center; margin-top: 20px;'): # Icons row
            resume_url = 'https://docs.google.com/document/d/1CaZ1Y2JxgRA_sWEilsJAC4k9DUltIfiI/edit?usp=sharing&ouid=115779223920772749975&rtpof=true&sd=true'
            ui.button('Resume', icon='description', on_click=lambda: ui.navigate.to(resume_url, new_tab=True)) # resume button
            linkedin_url = 'https://www.linkedin.com/in/victor-v-a9236b239/'
            ui.button('Linkedin', icon='business', on_click=lambda: ui.navigate.to(linkedin_url, new_tab=True)) # linkedin button
            github_url = 'https://github.com/vuvictor1'
            ui.button('GitHub', icon='</>', on_click=lambda: ui.navigate.to(github_url, new_tab=True)) # github button
        with ui.row().style('justify-content: center; margin-top: 20px;'): # Email row
            ui.icon('contact_mail').style('color: #FFFFFF; font-size: 28px;') # email icon
            ui.label('Email: vuvictor@csu.fullerton.edu').style('color: #FFFFFF; font-size: 16px;') # email label

with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Project section
    ui.label('Featured Projects').style('color: #FFFFFF; font-size: 32px;') 

project_descriptions = { # Dictionary of project descriptions
    'Aquatic EcoSphere System': 'Monitoring tool for aquatic ecosystems with sensors, to analyze real-time data.',
    'Smart Navigation Tool': 'Navigation system that uses pathfinding to find the most optimal route',
    'GUI Algorithms Sorter': 'Application to visualize bubble, merge and quick sorting sorting algorithms.'
}
project_urls = { # Dictionary of project URLs
    'Aquatic EcoSphere System': 'https://github.com/vuvictor1/Aquatic-EcoSphere-System',
    'Smart Navigation Tool': 'https://github.com/vuvictor1/SmartNavi',
    'GUI Algorithms Sorter': 'https://github.com/vuvictor1/GUI-Algorithms'
}
with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Project cards
    for project in project_descriptions.keys(): # List of projects
        with ui.column().classes('card').style('align-items: center; text-align: center;'): 
            ui.label(project).style('color: #FFFFFF; font-weight: bold;') 
            ui.label(f'{project_descriptions[project]}').style('color: #FFFFFF;') # description of project
            ui.button('Project', on_click=lambda url=project_urls[project]: ui.navigate.to(url, new_tab=True)) # redirect to project page

with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Programming section
    ui.label('Programming Languages').style('color: #FFFFFF; font-size: 32px;') 

with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Programming cards
    for language in ['Python', 'C#', 'C++', 'C', 'Rust', 'Assembly']: 
        with ui.column().classes('languages').style('align-items: center; text-align: center;'):
            ui.label(language).style('color: #FFFFFF; font-weight: bold;')

with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Education section
    ui.label('Educational Background').style('color: #FFFFFF; font-size: 32px;')

with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Education cards
    for edcuation in ['B.Sc. in Computer Science, California State University, Fullerton', 
    'Minor of Modern Language in Japanese, California State University, Fullerton', 
                      'State Seal of Biliteracy in Vietnamese, California Department of Education']:
         with ui.column().classes('card').style('align-items: center; text-align: center;'): 
            ui.label(edcuation).style('color: #FFFFFF; font-weight: bold;')
            ui.label('Description: A brief description of the education background will go here.').style('color: #FFFFFF;')

with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Languages section  
    ui.label('Foreign Languages').style('color: #FFFFFF; font-size: 32px;')

with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Languages cards
    for language in ['English (Native)', 'Vietnamese (Fluent)', 'Japanese (Advanced)']:
        with ui.column().classes('card').style('align-items: center; text-align: center;'):
            ui.label(language).style('color: #FFFFFF; font-weight: bold;')

with ui.footer().style('background-color: #6A4C9C; justify-content: center;'): # Footer section
    ui.label('Copyright (C) Victor Vu | Last updated 12/27/24').style('color: #FFFFFF; font-size: 18px;')

ui.run(title="Victor Vu | Portfolio", favicon="⚡") # Run UI with name and logo