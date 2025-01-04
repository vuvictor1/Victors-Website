# Authors: Victor V. Vu and Jordan Morris
# File: contacts.py
# Description: Contacts page for the web interface
# Copyright (C) 2024 Victor V. Vu and Jordan Morris
# License: GNU GPL v3 - See https://www.gnu.org/licenses/gpl-3.0.en.html
from nicegui import ui
from components import vu_header, vu_footer, inject_ui, inject_lottie

# Constants for styles
input_style = 'width: 100%; padding: 10px; margin-bottom: 20px; color: #FFFFFF; background-color: #333333; border: 1px solid #555555; border-radius: 5px;'
column_style = 'background-color: #2C2C2C; padding: 50px; border-radius: 10px; width: 100%; max-width: 600px;'

lottie_url = 'https://lottie.host/d1f5a60c-d57a-405a-b1ce-6dcf4b933d07/5prfVzNgqF.json' # lottie animation

def contacts_page(): # Contacts page
    vu_header() # header function
    inject_ui() # inject CSS effects

    with ui.row().style('justify-content: center; width: 100%;'): # Center the contacts title
        with ui.column().style(column_style): # Adjust padding and column width
            inject_lottie() # inject lottie animation
            ui.html(f'''<lottie-player src="{lottie_url}" loop autoplay style="height: 200px;"></lottie-player>''') # play file

            ui.label('Contact Us').style('font-size: 32px; color: white; margin-bottom: 20px;')
            # Create input fields for the form
            name = ui.input('Name').style(input_style).props('label-color=white clearable input-class=text-white')
            email = ui.input('Email').style(input_style).props('label-color=white clearable input-class=text-white')
            message = ui.textarea('Message').style(f'{input_style}').props('label-color=white clearable input-class=text-white')
            ui.button('Send', on_click=lambda: submit_form(name.value, email.value, message.value)).style('color: white; font-size: 16px;') # submit button
    vu_footer() # footer function

def submit_form(name, email, message): # Submit form
    if name and email and message: # Check if fields are not empty
        ui.notify('Thank you. Your message has been sent.', position='bottom', color='green') # notify message
    else: 
        ui.notify('Please fill in all fields.', position='bottom', color='red') # notify error

@ui.page('/contacts') # Route to contacts page
def contacts():
    contacts_page()