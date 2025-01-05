# Authors: Victor V. Vu 
# File: contacts.py
# Description: Contacts page for the website
# Copyright (C) 2024 Victor V. Vu 
# License: GNU GPL v3 - See https://www.gnu.org/licenses/gpl-3.0.en.html
from nicegui import ui
from components import vu_header, vu_footer, inject_ui, inject_lottie

lottie_url = 'https://lottie.host/d1f5a60c-d57a-405a-b1ce-6dcf4b933d07/5prfVzNgqF.json' # lottie animation

def contacts_page(): # Contacts page
    vu_header() # header function
    inject_ui() # inject CSS effects

    with ui.row().style('justify-content: center; align-items: center; width: 100%; height: 50vh;'): # Center the contacts title
        inject_lottie() # inject lottie animation
        ui.html(f'''<lottie-player src="{lottie_url}" loop autoplay style="height: 200px;"></lottie-player>''') # play file
        with ui.column().classes('about-me').style('max-width: 600px; text-align: center'): # Adjust padding and column width
            ui.label('Contact Me').style('font-size: 32px; color: white;') # Mail title
            # Create input fields for the form
            name = ui.input('Name').props('label-color=white clearable input-class=text-white').style('font-size: 16px; width: 100%;')    
            email = ui.input('Email').props('label-color=white clearable input-class=text-white').style('font-size: 16px; width: 100%;')
            message = ui.textarea('Message').props('label-color=white clearable input-class=text-white rows=13').style('font-size: 16px; width: 100%; height: 300px;')
            ui.button('Send', on_click=lambda: submit_form(name.value, email.value, message.value)).style('color: white; width: 100%;') # submit button
            ui.label('vuvictor@csu.fullerton.edu').style('font-size: 20px; color: white;') # Mail title
    vu_footer() # footer function

def submit_form(name, email, message): # Submit form
    if name and email and message: # Check if fields are not empty   
        ui.notify('Thank you. Your message has been sent.', position='center', type='positive') # notify message
    else: 
        ui.notify('Please fill in all fields.', position='center', type='negative') # notify error

@ui.page('/contacts') # Route to contacts page
def contacts():
    contacts_page()