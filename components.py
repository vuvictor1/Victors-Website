# Author: Victor V. Vu
# File: components.py
# Description: Reusable components for Victor's portfolio website
# Copyright (C) 2024 Victor V. Vu
# License: GNU GPL v3 - See https://www.gnu.org/licenses/gpl-3.0.en.html
from nicegui import ui

# Define constants for colors
background_color = "#3B3B3B"
card_background_color = "#2C2C2C"
hover_border_color = "#F5A623"
header_footer_color = "#6A4C9C"
text_color = "#FFFFFF"

def inject_ui(): # Injects custom CSS styles
    ui.add_head_html(f"""
    <style>
        body {{
            background-color: {background_color};
        }}       
        .about-me, .card, .languages, .work, .projects {{ /* CSS Styles */     
            background-color: {card_background_color}; 
            padding: 20px; 
            border-radius: 10px; 
            margin: 10px;
            border: 2px solid {card_background_color}; 
            transition: border-color 0.3s ease, transform 0.3s ease; /* smooth transition effect */
        }}

        .about-me {{
            width: 50%; 
        }}
        .card {{
            width: 15%; 
        }}          
        .languages {{
            width: 6%; 
        }}
        .work {{
            width: 27%;
        }}
        .projects {{
            width: 40%;
        }}

        .about-me:hover, .card:hover, .languages:hover, .work:hover, .projects:hover {{
            border-color: {hover_border_color}; 
            transform: scale(1.05);
        }}

        @media (max-width: 1920px) {{ /* Laptop Styles */
            .about-me, .card, .languages, .work, .projects {{
                width: 70%;
                margin: 10px 0;
            }}
        }}

        @media (max-width: 768px) {{ /* Mobile Styles */
            .about-me, .card, .languages, .work, .projects {{
                width: 100%;
                margin: 5px 0;
            }}
        }}
    </style>
    """)

def inject_lottie(): # Injects Lottie player script
    ui.add_body_html('<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>') 

def vu_header(): # Creates the header menu component
    with ui.header().style(f'background-color: {header_footer_color}; justify-content: center; flex-wrap: wrap; padding: 10px; position: static;'): 
        ui.link('⚡ Victor\'s Website', '/').style(f'color: {text_color}; font-size: 24px; text-decoration: none; margin: 5px;') 
        ui.label('|').style(f'color: {text_color}; font-size: 24px; margin: 5px;')
        ui.link('Experience', '/experience').style(f'color: {text_color}; font-size: 24px; text-decoration: none; margin: 5px;')
        ui.link('Projects', '/projects').style(f'color: {text_color}; font-size: 24px; text-decoration: none; margin: 5px;')
        ui.link('Interests', '/interests').style(f'color: {text_color}; font-size: 24px; text-decoration: none; margin: 5px;')
        ui.link('Contact', '/contacts').style(f'color: {text_color}; font-size: 24px; text-decoration: none; margin: 5px;')

def vu_footer(): # Creates the footer menu component
    with ui.footer().style(f'background-color: {header_footer_color}; justify-content: center; flex-wrap: wrap; padding: 10px; position: static;'): 
        ui.label('Copyright (C) Victor Vu | Last updated 1/5/25').style(f'color: {text_color}; font-size: 18px; margin: 5px;')
