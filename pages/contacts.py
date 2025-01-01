# Author: Victor V. Vu
# File: contacts.py
# Description: Contacts page for Victor's portfolio website
# Copyright (C) 2024 Victor V. Vu
# License: GNU GPL v3 - See https://www.gnu.org/licenses/gpl-3.0.en.html
from nicegui import ui
from components import *

lottie_url = 'https://lottie.host/d1f5a60c-d57a-405a-b1ce-6dcf4b933d07/5prfVzNgqF.json'

def contacts_page(): # Contacts page
    vu_header() # header function
    inject_ui() # inject CSS effects

    with ui.row().style('justify-content: center; width: 100%;'): # Create a row with centered content
        with ui.column().style('background-color: #2C2C2C; padding: 50px; border-radius: 10px; width: 100%; max-width: 600px;'):
            inject_lottie() # inject lottie animation
            ui.html(f'''<lottie-player src="{lottie_url}" loop autoplay style="height: 300px;"></lottie-player>''') # play file

            ui.label('Contact Us').style('font-size: 24px; color: white; margin-bottom: 20px;') # Create a label
            # Create input fields for the form and set default input to white
            name = ui.input('Name').props('label-color=white clearable input-class=text-white').style('width: 100%;')
            email = ui.input('Email').props('label-color=white clearable input-class=text-white').style('width: 100%;')
            message = ui.textarea('Message').props('label-color=white clearable input-class=text-white').style('width: 100%;')

            ui.button('Send', on_click=lambda: submit_form(name.value, email.value, message.value)) # send button
    vu_footer() # call footer function

def submit_form(name, email, message): # Submit form function
    if name and email and message: # Check if fields are not empty
        ui.notify('Thank you. Your message has been sent.', position='bottom', color='green') # success message
    else: # Fields are empty
        ui.notify('Please fill in all fields.', position='bottom', color='red') 

@ui.page('/contacts') # Route contacts page
def contacts():
    contacts_page()