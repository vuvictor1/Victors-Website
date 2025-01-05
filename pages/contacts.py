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

    with ui.row().style('display: flex; justify-content: center; align-items: center; width: 100%; height: 60vh;'): # Center the contacts title
        inject_lottie() # inject lottie animation
        ui.html(f'''<lottie-player src="{lottie_url}" loop autoplay style="height: 200px; display: block; margin: 0 auto;"></lottie-player>''') # play file
        with ui.column().classes('about-me').style('width: 100%; max-width: 600px; padding: 20px;'): # Adjust padding and column width
            ui.label('Contact Us').style('font-size: 32px; color: white; text-align: center; display: block; margin: 20px auto;')
            # Create input fields for the form
            name = ui.input('Name').props('label-color=white clearable input-class=text-white').style('font-size: 16px; width: 100%;')
            email = ui.input('Email').props('label-color=white clearable input-class=text-white').style('font-size: 16px; width: 100%;')
            message = ui.textarea('Message').props('label-color=white clearable input-class=text-white').style('font-size: 16px; width: 100%; height: 100px;')
            ui.button('Send', on_click=lambda: submit_form(name.value, email.value, message.value)).style('font-size: 16px; color: white; width: 100%;') # submit button
    vu_footer() # footer function

def submit_form(name, email, message): # Submit form
    if name and email and message: # Check if fields are not empty
        ui.notify('Thank you. Your message has been sent.', position='bottom', color='green') # notify message
    else: 
        ui.notify('Please fill in all fields.', position='bottom', color='red') # notify error

@ui.page('/contacts') # Route to contacts page
def contacts():
    contacts_page()