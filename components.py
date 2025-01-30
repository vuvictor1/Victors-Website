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
            min-height: 100vh; /* ensure body takes at least full viewport height */
            display: flex;
            flex-direction: column;
        }}
        main {{
            flex: 1; /* allow main content to grow and take available space */
            /* Reduce unnecessary margin space */
            margin-top: -60px;
            margin-bottom: -55px;
        }}
    </style>
    """)

def inject_lottie(): # Injects Lottie player script
    ui.add_body_html('<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>') 

def vu_header(): # Creates the header menu component
    with ui.header().classes('justify-center flex-wrap static p-4').style(f'background-color: {header_footer_color}'): 
        ui.link('⚡ Victor\'s Website', '/').classes('text-white text-2xl no-underline mb-2 md:mb-0') 
        ui.label('|').classes('text-white text-2xl hidden md:inline-block')
        ui.link('Experience', '/experience').classes('text-white text-2xl no-underline mb-2 md:mb-0')
        ui.link('Projects', '/projects').classes('text-white text-2xl no-underline mb-2 md:mb-0')
        ui.link('Interests', '/interests').classes('text-white text-2xl no-underline mb-2 md:mb-0')
        ui.link('Contact', '/contacts').classes('text-white text-2xl no-underline mb-2 md:mb-0')

def vu_footer(): # Creates the footer menu component
    with ui.footer().classes('justify-center flex-wrap static p-4').style(f'background-color: {header_footer_color}'): 
        ui.label('Copyright (C) Victor Vu | Last updated 1/29/25').classes('text-white text-xl')