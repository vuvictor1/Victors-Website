# Author: Victor V. Vu
# File: experience.py
# Description: Experience page for Victor's portfolio website
# Copyright (C) 2024 Victor V. Vu
# License: GNU GPL v3 - See https://www.gnu.org/licenses/gpl-3.0.en.html
from nicegui import ui
from components import vu_header, vu_footer, inject_ui, inject_lottie

def experience_page(): # Function to render the experience page
    vu_header() # header function
    inject_ui() # CSS effects

    with ui.row().classes('justify-center w-full my-4'): # Center the title
        ui.label('Relevant Experience').classes('text-white text-4xl font-bold text-center')
    inject_lottie() # inject lottie animation

    lottie_1 = 'https://assets6.lottiefiles.com/packages/lf20_ne6kcqfz.json' 
    lottie_2 = 'https://assets3.lottiefiles.com/packages/lf20_6ft9bypa.json'
    
    with ui.row().classes('justify-center w-full my-4 flex flex-wrap gap-4'): # Center columns and reduce the margin
        with ui.column().style('max-width: 40rem;').classes('items-center text-center p-5 bg-gray-800 rounded-lg shadow-lg w-full md:w-1/2 outline_label'): # Column for the first experience
            ui.html(f'''<lottie-player src="{lottie_1}" loop autoplay speed="0.25"></lottie-player>''').classes('w-96 sm:w-64') # play animation
            ui.label('Instructional Assistant | CSUF - Department of Computer Science').classes('text-white text-2xl md:text-xl sm:text-lg font-semibold')
            ui.label('(January 2023 - May 2023)').classes('text-white text-lg md:text-base sm:text-sm')
            ui.label('● Supported 60+ students enrolled in Computer Architecture and Systems Programming.').classes('text-white text-lg md:text-base sm:text-sm')
            ui.label('● Evaluated software developed in x86-64 Assembly, C++, and C.').classes('text-white text-lg md:text-base sm:text-sm')
            ui.label('● Provided extensive feedback on code design.').classes('text-white text-lg md:text-base sm:text-sm')
            ui.label('● Facilitated study sessions to reinforce course understanding.').classes('text-white text-lg md:text-base sm:text-sm')

        with ui.column().style('max-width: 40rem;').classes('items-center text-center p-5 bg-gray-800 rounded-lg shadow-lg w-full md:w-1/2 outline_label'): # Column for the second experience
            ui.html(f'''<lottie-player src="{lottie_2}" loop autoplay speed="0.25"></lottie-player>''').classes('w-96 sm:w-64') 
            ui.label('Peer Programming Tutor  | CSUF - Department of Computer Science').classes('text-white text-2xl md:text-xl sm:text-lg font-semibold')
            ui.label('(August 2022 - December 2022)').classes('text-white text-lg md:text-base sm:text-sm')
            ui.label('● Tutored 30+ peers enrolled in C# GUI Programming.').classes('text-white text-lg md:text-base sm:text-sm')
            ui.label('● Debugged various logical errors from student programs, improving grades by 10%.').classes('text-white text-lg md:text-base sm:text-sm')
            ui.label('● Presented additional lecture materials on optimizing collision algorithms.').classes('text-white text-lg md:text-base sm:text-sm')
            ui.label('● Coordinated online meetings, encouraging collaboration.').classes('text-white text-lg md:text-base sm:text-sm')
    vu_footer() # call footer function

@ui.page('/experience') # Route to experience page
def experience():
    experience_page()