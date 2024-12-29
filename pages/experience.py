# Author: Victor V. Vu
# File: experience.py
# Description: Experience page for Victor's portfolio website
# Copyright (C) 2024 Victor V. Vu
# License: GNU GPL v3 - See https://www.gnu.org/licenses/gpl-3.0.en.html
from nicegui import ui
from components import * # type: ignore

def experience_page(): # Experience page function
    vu_header() # type: ignore # call header function
    inject_ui() # type: ignore # inject CSS effects

    with ui.row().style('justify-content: center; width: 100%'): # Main page title
        ui.label('Relevant Experiences').style('color: #FFFFFF; font-size: 32px;')

    experiences1 = { # Dictionary of experiences1
        'Software Engineering Intern at XYZ Tech': 'Developed internal tools using Python and React; optimized backend systems, reducing load time by 20%.',
        'Teaching Assistant at CSU Fullerton': 'Guided students in Data Structures and Algorithms; hosted review sessions and assisted with grading.',
        'Web Developer at ABC Solutions': 'Designed and implemented responsive websites for clients; collaborated with a team to deliver projects on time.'
    }

    with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'):
        for job, description in experiences1.items():
            with ui.column().classes('about-me').style('align-items: center; text-align: center;'):
                ui.label(job).style('color: #FFFFFF; font-weight: bold;')
                ui.label(description).style('color: #FFFFFF;')

    # Personal Experience Section
    with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'):
        ui.label('Personal Projects & Leadership').style('color: #FFFFFF; font-size: 28px;')

    personal_experiences = {
        'Aquatic Ecosystem Management': 'Built and maintained a smart ecosystem for aquatic life using real-time sensors and custom analytics.',
        'Beatboxing Performer': 'Performed at various campus events, blending rhythm and vocal techniques to captivate audiences.',
        'Student Council President': 'Led initiatives for student welfare, organized events, and represented student interests to the university board.'
    }

    with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'):
        for project, description in personal_experiences.items():
            with ui.column().classes('about-me').style('align-items: center; text-align: center;'):
                ui.label(project).style('color: #FFFFFF; font-weight: bold;')
                ui.label(description).style('color: #FFFFFF;')

    vu_footer() # call footer function
