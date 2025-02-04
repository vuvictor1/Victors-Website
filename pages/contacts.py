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

    with ui.row().classes('justify-center w-full my-6'): # Center the contacts title
        inject_lottie() # inject lottie animation
        with ui.column().style('max-width: 95%;').classes('items-center text-center p-5 bg-gray-800 rounded-lg shadow-lg outline_label'):
            ui.html(f'''<lottie-player src="{lottie_url}" loop autoplay speed="0.25"></lottie-player>''').classes('w-48 mx-auto') # play file
            ui.label('Contact Me').classes('text-white text-4xl font-bold') # Mail title
            # Create input fields for the form
            ui.html(f'''
                <form action="https://api.web3forms.com/submit" method="POST" style="width: 100%;">
                    <input type="hidden" name="access_key" value="5378da98-377b-464f-990d-f97e70c28023">
                    <input type="text" name="name" placeholder="Your Name" required style="font-size: 1rem; width: 100%; margin-bottom: 10px; background-color: #3B3B3B; color: white; border: none; padding: 10px; border-radius: 5px;">
                    <input type="email" name="email" placeholder="Your Email (So I can reply)" required style="font-size: 1rem; width: 100%; margin-bottom: 10px; background-color: #3B3B3B; color: white; border: none; padding: 10px; border-radius: 5px;">
                    <textarea name="message" placeholder="Your Message" required style="font-size: 1rem; width: 100%; height: 300px; margin-bottom: 10px; background-color: #3B3B3B; color: white; border: none; padding: 10px; border-radius: 5px;"></textarea>
                    <input type="checkbox" name="botcheck" class="hidden" style="display: none;">
                    <div style="text-align: center;">
                        <button type="submit" style="color: white; width: 50%; background-color: #5898D4; padding: 10px 20px; cursor: pointer; border-radius: 5px; font-size: 1.25rem;">Send Mail</button>
                    </div>
                </form>
            ''')
            ui.label('📬 vuvictorgeek@gmail.com').classes('text-white text-lg') # mail label
    vu_footer() # footer function

@ui.page('/contacts') # Route to contacts page
def contacts():
    contacts_page()