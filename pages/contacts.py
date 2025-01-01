# Author: Victor V. Vu
# File: contacts.py
# Description: Contacts page for Victor's portfolio website
# Copyright (C) 2024 Victor V. Vu
# License: GNU GPL v3 - See https://www.gnu.org/licenses/gpl-3.0.en.html
from nicegui import ui
from components import *

def contacts_page(): # Contacts page function
    vu_header() # call header function
    inject_ui() # inject CSS effects

    with ui.row().style('justify-content: center; width: 100%'): # Main page title
        ui.label('Contact Me').style('color: #FFFFFF; font-size: 32px;')

    with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Contact form
        with ui.column().classes('about-me').style('align-items: center; text-align: center; background-color: #2C2C2C; padding: 20px; border-radius: 10px;'):
            inject_lottie() # inject lottie animation
            lottie_5 = 'https://lottie.host/d1f5a60c-d57a-405a-b1ce-6dcf4b933d07/5prfVzNgqF.json' # use lottie file
            ui.html(f'''<lottie-player src="{lottie_5}" loop autoplay style="height: 300px;"></lottie-player>''')
            # Contact form html injection
            ui.html("""
                <form action="https://formsubmit.co/vuvictorgeek@gmail.com" method="POST" style="width: 100%; max-width: 600px;">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="text" name="name" placeholder="Name" required style="width: 100%; padding: 10px; margin-bottom: 20px; border: 1px solid #ccc; border-radius: 5px; background-color: #2C2C2C; color: #FFFFFF;">
                    <input type="email" name="email" placeholder="Email" required style="width: 100%; padding: 10px; margin-bottom: 20px; border: 1px solid #ccc; border-radius: 5px; background-color: #2C2C2C; color: #FFFFFF;">
                    <textarea name="message" placeholder="Message" required style="width: 100%; padding: 10px; margin-bottom: 20px; border: 1px solid #ccc; border-radius: 5px; height: 400px; background-color: #2C2C2C; color: #FFFFFF;"></textarea>
                    <button type="submit" style="padding: 10px 20px; background-color: #007BFF; color: #FFFFFF; border: none; border-radius: 5px; cursor: pointer; border: 1px solid orange;">Send</button>
                </form>
            """)

    vu_footer() # call footer function

@ui.page('/contacts') # Route contacts page 
def contacts(): 
    contacts_page()