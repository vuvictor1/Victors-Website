# Author: Victor V. Vu
# File: components.py
# Description: Reusable components for Victor's portfolio website
# Copyright (C) 2024 Victor V. Vu
# License: GNU GPL v3 - See https://www.gnu.org/licenses/gpl-3.0.en.html
from nicegui import ui

def inject_ui(): # Injected UI components
    ui.add_head_html("""
    <style>
        body { /* Main background */
            background-color: #3B3B3B;
        }
                    
        .about-me { /* About me borders */
            background-color: #2C2C2C; 
            padding: 20px; 
            border-radius: 10px; 
            width: 50%; 
            margin: 10px;
            border: 2px solid #2C2C2C; 
            transition: border-color 0.3s ease;
        }

        .about-me:hover { /* Hover border color for about */
            border-color: #F5A623; 
        }

        .card { /* Project cards borders */
            background-color: #2C2C2C; 
            padding: 20px; 
            border-radius: 10px; 
            width: 300px; 
            margin: 10px;
            border: 2px solid #2C2C2C; 
            transition: border-color 0.3s ease;
        }

        .card:hover { /* Hover border color for card */
            border-color: #F5A623; 
        }
                    
        .languages { /* Project cards borders */
            background-color: #2C2C2C; 
            padding: 20px; 
            border-radius: 10px; 
            width: 125px; 
            margin: 10px;
            border: 2px solid #2C2C2C; 
            transition: border-color 0.3s ease;
        }

        .languages:hover { /* Hover border color for card */
            border-color: #F5A623; 
        }
    </style>
    """)

def vu_header(): # Header menu component
    with ui.header().style('background-color: #6A4C9C;'): 
        ui.link('⚡ Victor\'s Website', '/').style('color: #FFFFFF; font-size: 24px; text-decoration: none;') 
        ui.label('|').style('color: #FFFFFF; font-size: 24px;')
        ui.link('Experience', '/experience').style('color: #FFFFFF; font-size: 24px; text-decoration: none;')

def vu_footer(): # Footer menu component
    with ui.footer().style('background-color: #6A4C9C; justify-content: center;'): 
        ui.label('Copyright (C) Victor Vu | Last updated 12/28/24').style('color: #FFFFFF; font-size: 18px;')