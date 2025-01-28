# Author: Victor V. Vu
# File: components.py
# Description: Reusable components for Victor's portfolio website
# Copyright (C) 2024 Victor V. Vu
# License: GNU GPL v3 - See https://www.gnu.org/licenses/gpl-3.0.en.html
from nicegui import ui

# Define constants for colors
background_color = "#3B3B3B"
header_footer_color = "#6A4C9C"

def inject_ui(): # Injects Tailwind CSS
    ui.add_head_html(f"""
    <style>
        body {{
            background-color: {background_color};
        }}
    </style>
    """)

def inject_lottie(): # Injects Lottie player script
    ui.add_body_html('<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>') 

def vu_header(): # Creates the header menu component
    with ui.header().classes('justify-center flex-wrap static').style(f'background-color: {header_footer_color}'): 
        ui.link('⚡ Victor\'s Website', '/').classes('text-white text-2xl no-underline') 
        ui.label('|').classes('text-white text-2xl')
        ui.link('Experience', '/experience').classes('text-white text-2xl no-underline')
        ui.link('Projects', '/projects').classes('text-white text-2xl no-underline')
        ui.link('Interests', '/interests').classes('text-white text-2xl no-underline')
        ui.link('Contact', '/contacts').classes('text-white text-2xl no-underline')

def vu_footer(): # Creates the footer menu component
    with ui.footer().classes('justify-center flex-wrap static').style(f'background-color: {header_footer_color}'): 
        ui.label('Copyright (C) Victor Vu | Last updated 1/5/25').classes('text-white text-lg')