# Author: Victor V. Vu
# File: components.py
# Description: Reusable components for Victor's portfolio website
# Copyright (C) 2024 Victor V. Vu
# License: GNU GPL v3 - See https://www.gnu.org/licenses/gpl-3.0.en.html
from nicegui import ui

# Define constants for colors
BACKGROUND_COLOR = "#3B3B3B"
CARD_BACKGROUND_COLOR = "#2C2C2C"
HOVER_BORDER_COLOR = "#F5A623"
HEADER_FOOTER_COLOR = "#6A4C9C"
TEXT_COLOR = "#FFFFFF"

def inject_ui(): # Injects custom CSS styles
    ui.add_head_html(f"""
    <style>
        body {{
            background-color: {BACKGROUND_COLOR};
        }}
                    
        .about-me, .card, .languages {{
            background-color: {CARD_BACKGROUND_COLOR}; 
            padding: 20px; 
            border-radius: 10px; 
            margin: 10px;
            border: 2px solid {CARD_BACKGROUND_COLOR}; 
            transition: border-color 0.3s ease;
        }}

        .about-me {{
            width: 50%; 
        }}

        .card {{
            width: 300px; 
        }}
                    
        .languages {{
            width: 125px; 
        }}

        .about-me:hover, .card:hover, .languages:hover {{
            border-color: {HOVER_BORDER_COLOR}; 
        }}
    </style>
    """)

def inject_lottie(): # Injects Lottie player script
    ui.add_body_html('<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>') 

def vu_header(): # Creates the header menu component
    with ui.header().style(f'background-color: {HEADER_FOOTER_COLOR};'): 
        ui.link('⚡ Victor\'s Website', '/').style(f'color: {TEXT_COLOR}; font-size: 24px; text-decoration: none;') 
        ui.label('|').style(f'color: {TEXT_COLOR}; font-size: 24px;')
        ui.link('Experience', '/experience').style(f'color: {TEXT_COLOR}; font-size: 24px; text-decoration: none;')
        ui.link('Projects', '/projects').style(f'color: {TEXT_COLOR}; font-size: 24px; text-decoration: none;')
        ui.link('Interests', '/interests').style(f'color: {TEXT_COLOR}; font-size: 24px; text-decoration: none;')
        ui.link('Contact', '/contacts').style(f'color: {TEXT_COLOR}; font-size: 24px; text-decoration: none;')

def vu_footer(): # Creates the footer menu component
    with ui.footer().style(f'background-color: {HEADER_FOOTER_COLOR}; justify-content: center;'): 
        ui.label('Copyright (C) Victor Vu | Last updated 12/30/24').style(f'color: {TEXT_COLOR}; font-size: 18px;')