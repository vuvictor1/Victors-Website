# Author: Victor V. Vu
# File: experience.py
# Description: Experience page for Victor's portfolio website
# Copyright (C) 2024 Victor V. Vu
# License: GNU GPL v3 - See https://www.gnu.org/licenses/gpl-3.0.en.html
from nicegui import ui
from components import *

def experience_page(): # Experience page function
    vu_header() # call header function
    inject_ui() # inject CSS effects

    with ui.row().style('justify-content: center; width: 100%'): # Main page title
        ui.label('Relevant Experience').style('color: #FFFFFF; font-size: 32px;')

    inject_lottie() # inject lottie animation
    lottie_1 = 'https://assets6.lottiefiles.com/packages/lf20_ne6kcqfz.json' # use lottie file 1
    with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Experience 2
        with ui.column().classes('about-me').style('align-items: center; text-align: center;'):
            ui.html(f'''<lottie-player src="{lottie_1}" loop autoplay style="height: 400px;"></lottie-player>''')
            ui.label('Instructional Student Assistant | CSUF - Department of Engineering and Computer Science').style('color: #FFFFFF; font-weight: bold;')
            ui.label('(January 2023 - May 2023)').style('color: #FFFFFF;')
            ui.label('- Supported 60+ students enrolled in Computer Architecture and Systems Programming.').style('color: #FFFFFF;')
            ui.label('- Evaluated software developed in x86-64 Assembly, C++, and C.').style('color: #FFFFFF;')
            ui.label('- Provided extensive feedback on code design.').style('color: #FFFFFF;')
            ui.label('- Facilitated study sessions to reinforce course understanding.').style('color: #FFFFFF;')

    lottie_2 = 'https://assets3.lottiefiles.com/packages/lf20_6ft9bypa.json' # use lottie file 2
    with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Experience 1
        with ui.column().classes('about-me').style('align-items: center; text-align: center;'):
            ui.html(f'''<lottie-player src="{lottie_2}" loop autoplay style="height: 400px;"></lottie-player>''')
            ui.label('C# Peer Programming Tutor  | CSUF - Department of Engineering and Computer Science').style('color: #FFFFFF; font-weight: bold;')
            ui.label('(August 2022 - December 2022)').style('color: #FFFFFF;')
            ui.label('- Tutored 30+ peers enrolled in C# GUI Programming.').style('color: #FFFFFF;')
            ui.label('- Debugged various logical errors from student programs, improving grades by 10%.').style('color: #FFFFFF;')
            ui.label('- Presented additional lecture materials on optimizing collision algorithms.').style('color: #FFFFFF;')
            ui.label('- Coordinated online meetings, encouraging collaboration.').style('color: #FFFFFF;')

    vu_footer() # call footer function

@ui.page('/experience') # Route experience page 
def experience(): 
    experience_page() 

