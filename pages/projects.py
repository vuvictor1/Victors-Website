# Author: Victor V. Vu
# File: projects.py
# Description: Projects page for Victor's portfolio website
# Copyright (C) 2024 Victor V. Vu
# License: GNU GPL v3 - See https://www.gnu.org/licenses/gpl-3.0.en.html
from nicegui import ui
from components import *

def projects_page(): # Projects page function
    vu_header() # call header function
    inject_ui() # inject CSS effects

    with ui.row().style('justify-content: center; width: 100%'): # Main page title
        ui.label('Programming Projects').style('color: #FFFFFF; font-size: 32px;')

    inject_lottie() # inject lottie animation
    lottie_3 = 'https://lottie.host/ddd7660b-67b2-4b52-a49a-8fc2a4f3b36b/QKoTWTHqJ1.json' # use lottie file 3
    with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Projects
        with ui.column().classes('about-me').style('align-items: center; text-align: center;'):
            ui.html(f'''<lottie-player src="{lottie_3}" loop autoplay style="height: 400px;"></lottie-player>''')
            ui.link('7 Realms', 'https://drive.google.com/file/d/1tjU7ZSoMfIJiEwQ6MBiLT4QyQyFunaHS/view?usp=sharing').style('color: #FFFFFF; font-weight: bold;')
            ui.label('(High-tech medieval-themed game introducing new mechanics through modification.)').style('color: #FFFFFF;')
            ui.label('- In a team of 6, served as the Process Manager / Group Facilitator.').style('color: #FFFFFF;')
            ui.label('- Delegated tasks and supervised group members, ensuring timely project completion.').style('color: #FFFFFF;')
            ui.label('- Recorded objective progress, conducted weekly meetings, and defined game requirements.').style('color: #FFFFFF;')
            ui.label('- Developed the initial prototype model for enemy artificial intelligence.').style('color: #FFFFFF;')
            ui.label('- Leading author for the design document, team charter, and video demonstration.').style('color: #FFFFFF;')
    
            ui.separator() # separator
            ui.link('Smart-Navi', 'https://github.com/vuvictor1/SmartNavi').style('color: #FFFFFF; font-weight: bold;') 
            ui.label('(Python navigation system that uses pathfinding to find the optimal route with Networkx.)').style('color: #FFFFFF;')
            ui.label('- In a team of 4, performed the role of Product Manager / Lead Software Engineer.').style('color: #FFFFFF;')
            ui.label('- Primary contributor for pathfinding algorithms: Breadth/Depth First Search and Dijkstra\'s Algorithm.').style('color: #FFFFFF;')
            ui.label('- Developed the user interface, providing buttons for accessibility and a dropdown menu to select locations.').style('color: #FFFFFF;')
            ui.label('- Constructed an adjacency list of nearly 300 points, which assigned coordinates that considered blocked paths and weighted edges.').style('color: #FFFFFF;') 
            ui.label('- Conducted a technical presentation following findings on the best use-case scenario based on distance.').style('color: #FFFFFF;')
            ui.label('- Mentored junior team members on programming implementations, actively carrying out code reviews.').style('color: #FFFFFF;') 

            ui.separator() 
            ui.link('E-Market Trove', 'https://github.com/agrnerd17/E-Market-Trove').style('color: #FFFFFF; font-weight: bold;') 
            ui.label('(Conceptual multi-page e-commerce platform built with React and JavaScript to sell a wide range of products.)').style('color: #FFFFFF;')
            ui.label('- Collaborated in a team of 5 as the Assistant Product Manager / Lead Software Engineer.').style('color: #FFFFFF;')
            ui.label('- Major contributor in creating the inventory system, implementing search function, designing UI, and embedding styling.').style('color: #FFFFFF;')
            ui.label('- Principal author of unit tests for functionality, boundary, and error testing.').style('color: #FFFFFF;')
            ui.label('- Conducted weekly sprint reviews to support team members in addressing bugs or implementation challenges.').style('color: #FFFFFF;') 
            ui.label('- Served as the primary technical writer for reports, maintained GitHub readme and presented progress updates via slides.').style('color: #FFFFFF;')

            ui.separator() 
            ui.link('GUI-Algorithms', 'https://github.com/vuvictor1/GUI-Algorithms').style('color: #FFFFFF; font-weight: bold;') 
            ui.label('(Python tool to visualize various sorting methods using Matplotlib and NumPy.)').style('color: #FFFFFF;')
            ui.label('- In a team of 4, acted as the Team Lead / Lead Software Engineer.').style('color: #FFFFFF;')
            ui.label('- Most significant individual contributor of code, developing Bubble, Merge and Quick Sorting algorithms.').style('color: #FFFFFF;')
            ui.label('- Designed the GUI, featuring controls such as the selection menu, reset, pause/resume and start buttons.').style('color: #FFFFFF;')
            ui.label('- Implemented runtime calculations to measure time complexity and random array generation.').style('color: #FFFFFF;') 
            ui.label('- Involved with technical documentation, preparing research materials for a presentation.').style('color: #FFFFFF;')

            ui.separator() 
            ui.link('Cat-n-Mouse', 'https://github.com/vuvictor1/CatnMouse-Game').style('color: #FFFFFF; font-weight: bold;') 
            ui.label('(C# graphical program inspired by the classic game, Cops N Robbers, with AI.)').style('color: #FFFFFF;')
            ui.label('- Features a player controlled object (cat) to continually chase an AI mouse object.').style('color: #FFFFFF;')
            ui.label('- Functionalities: random direction, collusion detection, object ricochet, track location and distance analyser.').style('color: #FFFFFF;')
            ui.label('- Introduced direction control with key presses and random movement for the AI.').style('color: #FFFFFF;')

            ui.separator() 
            ui.link('Tax-Assessor', 'https://github.com/vuvictor1/Tax-Assessor').style('color: #FFFFFF; font-weight: bold;') 
            ui.label('(Tribrid program written in x86 Assembly, C++ and C to assess sum and mean of property values.)').style('color: #FFFFFF;')
            ui.label('- Collects float of arrays as user input for computation. Incorporates a time updater to retrieve local date.').style('color: #FFFFFF;')
            ui.label('- Implements invalid input handling to prevent errors.').style('color: #FFFFFF;')

            ui.separator() 
            ui.link('Victor\'s-Website', 'https://github.com/vuvictor1/Victors-Website').style('color: #FFFFFF; font-weight: bold;') 
            ui.label('(Python/CSS digital portfolio website of Victor V. Vu.)').style('color: #FFFFFF;')
            ui.label('- Supports multi-page functionality, containing embedded media, tabs selection and redirect buttons.').style('color: #FFFFFF;')
            ui.label('- Features a contact support form which forwards messages via email.').style('color: #FFFFFF;')

    with ui.row().style('justify-content: center; width: 100%'): # 2nd page title
        ui.label('Research Projects').style('color: #FFFFFF; font-size: 32px;')

    lottie_4 = 'https://lottie.host/c7f17250-d067-4a1e-aab2-4656f68c94c9/QrwbdaLSwA.json' # use lottie file 4
    with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Papers
        with ui.column().classes('about-me').style('align-items: center; text-align: center;'):
            ui.html(f'''<lottie-player src="{lottie_4}" loop autoplay style="height: 400px;"></lottie-player>''')
            ui.link('Operations Analysis', 'https://docs.google.com/document/d/1XhZCOei60DCcFlYO1scSQ5m6UwcKfwTgmN0NjlamjtY/edit?tab=t.0#heading=h.868kz7lj5kq9').style('color: #FFFFFF; font-weight: bold;') 
            ui.label('Detailed report on the time complexities of binary search trees, hash tables, vectors, dynamic link libraries and singly linked lists operations.').style('color: #FFFFFF;')
            ui.link('Rain Gutter Construction', 'https://docs.google.com/document/d/1_RcIvuWFvMmvF96vdpOod8z2vCf5s2mVkY4_UVU5vZU/edit?tab=t.0').style('color: #FFFFFF; font-weight: bold;') 
            ui.label('Mathematical approach on how to solve the rain gutter problem of determining an object design\'s water capacity using Calculus.').style('color: #FFFFFF;')
            ui.link('Coffee Container Calculation', 'https://docs.google.com/document/d/17NW6yIdzAp-D2okMZlLdM3kxcGai3WUC8zds3RMgb8A/edit?tab=t.0').style('color: #FFFFFF; font-weight: bold;') 
            ui.label('Representation of how Folger\'s Engineering Division uses Calculus to approximate a containers volume and area for maximum profit.').style('color: #FFFFFF;')           
    vu_footer() # call footer function

@ui.page('/projects') # Route projects page 
def projects(): 
    projects_page()