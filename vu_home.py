# Author: Victor V. Vu
# File: vu_home.py
# Description: Portfolio website main file for Victor Vu 
# Copyright (C) 2024 Victor V. Vu
# License: GNU GPL v3 - See https://www.gnu.org/licenses/gpl-3.0.en.html
from nicegui import ui

with ui.header().style('background-color: #6A4C9C;'): # Header menu
    ui.label('⚡ Victor\'s Website').style('color: #FFFFFF; font-size: 24px;')  

with ui.right_drawer().style('background-color: #6C757D; align-items: center;'): # Right Drawer
    ui.label('[Pages]').style('color: #FFFFFF; font-size: 18px;') 
    ui.label('This portfolio contains information on my projects and experience in tech.').style('color: #FFFFFF; font-size: 14px;')

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
    with ui.column().classes('about-me'): # Use CSS hover effect
        ui.label('About Me').style('color: #FFFFFF; font-weight: bold; font-size: 24px;')
        ui.label('''Hi! I'm Victor Vu, a computer science student with a passion for technology, coding, and aquatic ecosystems. 
        I have experience in full-stack development, data analysis, and building simulations for environmental management.''').style('color: #FFFFFF; font-size: 16px;')

with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Projects
    ui.label('Featured Projects').style('color: #FFFFFF; font-size: 32px;') 

with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Project cards
    for project in ['Aquatic Ecosphere System', 'Real-Time Strategy Game', 'Tic-Tac-Toe Web Game']: # List of projects
        with ui.column().classes('card').style('align-items: center; text-align: center;'): # Center content
            ui.label(project).style('color: #FFFFFF; font-weight: bold;')
            ui.label('Description: A brief description of the project will go here.').style('color: #FFFFFF;')
            ui.button('Learn More') 

with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Programming 
    ui.label('Programming Languages').style('color: #FFFFFF; font-size: 32px;') 

with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Programming Languages
    for language in ['Python', 'C#', 'C++', 'C', 'Rust', 'Assembly']: # List of programming languages
        with ui.column().classes('languages').style('align-items: center; text-align: center;'):
            ui.label(language).style('color: #FFFFFF; font-weight: bold;')

with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Education
    ui.label('Educational Background').style('color: #FFFFFF; font-size: 32px;')

with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Education background
    for edcuation in ['B.Sc. in Computer Science, California State University, Fullerton', 'Minor of Modern Language in Japanese, California State University, Fullerton', 
                      'State Seal of Biliteracy in Vietnamese, California Department of Education']:
         with ui.column().classes('card').style('align-items: center; text-align: center;'): # Center content
            ui.label(edcuation).style('color: #FFFFFF; font-weight: bold;')
            ui.label('Description: A brief description of the education background will go here.').style('color: #FFFFFF;')

with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Languages   
    ui.label('Foreign Languages').style('color: #FFFFFF; font-size: 32px;')

with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Languages
    for language in ['English', 'Vietnamese', 'Japanese']:
        with ui.column().classes('card').style('align-items: center; text-align: center;'):
            ui.label(language).style('color: #FFFFFF; font-weight: bold;')


with ui.footer().style('background-color: #6A4C9C; justify-content: center;'): # Footer
    ui.label('Copyright (C) 2024 | Victor Vu').style('color: #FFFFFF; font-size: 18px;')

ui.run(title="Victor Vu | Portfolio", favicon="⚡") # Run UI with name and logo
