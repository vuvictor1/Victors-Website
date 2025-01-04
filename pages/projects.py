# Author: Victor V. Vu
# File: projects.py
# Description: Projects page for Victor's portfolio website
# Copyright (C) 2024 Victor V. Vu
# License: GNU GPL v3 - See https://www.gnu.org/licenses/gpl-3.0.en.html
from nicegui import ui
from components import vu_header, vu_footer, inject_ui, inject_lottie

# Constants
white_color = '#FFFFFF'
orange_color = '#FFA500'
font_size_large = '32px'
font_size_default = '16px'
font_size_link = '20px'
lottie_3_url = 'https://lottie.host/ddd7660b-67b2-4b52-a49a-8fc2a4f3b36b/QKoTWTHqJ1.json'
lottie_4_url = 'https://lottie.host/c7f17250-d067-4a1e-aab2-4656f68c94c9/QrwbdaLSwA.json'

def create_label(text, color=white_color, font_size=font_size_default): # Helper function to create a label
    ui.label(text).style(f'color: {color}; font-size: {font_size}; margin-bottom: 10px;')

def create_link(text, url, color=orange_color, font_size=font_size_link): # Helper function to create a link
    ui.link(text, url).style(f'color: {color}; font-size: {font_size}; margin-bottom: 10px;')

def create_project_section(link_text, link_url, description, details): # Helper function to create a project section
    with ui.card().style('width: 100%; margin-bottom: 20px; background-color: #333333; color: #FFFFFF;'):
        with ui.row().style('justify-content: center; width: 100%;'):
            create_link(link_text, link_url, color='#FFA500')
            create_label(f' {description}', color='#FFFFFF')
        for detail in details:
            create_label(detail, color='#FFFFFF')
        ui.separator().style('margin: 20px 0;')

def create_project_row(projects): # Helper function to create a project row
    with ui.row().style('justify-content: center; width: 100%; margin-bottom: 20px;'):
        for project in projects:
            with ui.column().style('width: 45%; margin: 10px;'):
                create_project_section(*project)

def projects_page(): # Projects page main function
    vu_header() # inject header
    inject_ui() # inject UI

    with ui.row().style('justify-content: center; width: 100%; margin-bottom: 20px;'): # Projects title
        create_label('Programming Projects', font_size=font_size_large)
    inject_lottie() # inject lottie animation

    with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Projects content
        with ui.column().classes('projects').style('align-items: center; text-align: center;'):
            ui.html(f'<lottie-player src="{lottie_3_url}" loop autoplay style="height: 400px; margin-bottom: 20px;"></lottie-player>') # play lottie animation

            # List of projects
            projects = [
                ('7 Realms', 'https://drive.google.com/file/d/1tjU7ZSoMfIJiEwQ6MBiLT4QyQyFunaHS/view?usp=sharing', '(High-tech medieval-themed game introducing new mechanics through modification.)', [
                    '● In a team of 6, served as the Process Manager / Group Facilitator.',
                    '● Delegated tasks and supervised group members, ensuring timely project completion.',
                    '● Recorded objective progress, conducted weekly meetings, and defined game requirements.',
                    '● Developed the initial prototype model for enemy artificial intelligence.',
                    '● Leading author for the design document, team charter, and video demonstration.'
                ]),
                ('Smart-Navi', 'https://github.com/vuvictor1/SmartNavi', '(Python navigation system that uses pathfinding to find the optimal route with Networkx.)', [
                    '● In a team of 4, performed the role of Product Manager / Lead Software Engineer.',
                    '● Primary contributor for pathfinding algorithms: Breadth/Depth First Search and Dijkstra\'s Algorithm.',
                    '● Developed the user interface, providing buttons for accessibility and a dropdown menu to select locations.',
                    '● Constructed an adjacency list of nearly 300 points, which assigned coordinates that considered blocked paths and weighted edges.',
                    '● Conducted a technical presentation following findings on the best use-case scenario based on distance.',
                    '● Mentored junior team members on programming implementations, actively carrying out code reviews.'
                ]),
                ('E-Market Trove', 'https://github.com/agrnerd17/E-Market-Trove', '(Conceptual multi-page e-commerce platform built with React and JavaScript to sell a wide range of products.)', [
                    '● Collaborated in a team of 5 as the Assistant Product Manager / Lead Software Engineer.',
                    '● Major contributor in creating the inventory system, implementing search function, designing UI, and embedding styling.',
                    '● Principal author of unit tests for functionality, boundary, and error testing.',
                    '● Conducted weekly sprint reviews to support team members in addressing bugs or implementation challenges.',
                    '● Served as the primary technical writer for reports, maintained GitHub readme and presented progress updates via slides.'
                ]),
                ('GUI-Algorithms', 'https://github.com/vuvictor1/GUI-Algorithms', '(Python tool to visualize various sorting methods using Matplotlib and NumPy.)', [
                    '● In a team of 4, acted as the Team Lead / Lead Software Engineer.',
                    '● Most significant individual contributor of code, developing Bubble, Merge and Quick Sorting algorithms.',
                    '● Designed the GUI, featuring controls such as the selection menu, reset, pause/resume and start buttons.',
                    '● Implemented runtime calculations to measure time complexity and random array generation.',
                    '● Involved with technical documentation, preparing research materials for a presentation.'
                ]),
                ('Cat-n-Mouse', 'https://github.com/vuvictor1/CatnMouse-Game', '(C# graphical program inspired by the classic game, Cops N Robbers, with AI.)', [
                    '● Features a player controlled object (cat) to continually chase an AI mouse object.',
                    '● Functionalities: random direction, collusion detection, object ricochet, track location and distance analyser.',
                    '● Introduced direction control with key presses and random movement for the AI.'
                ]),
                ('Tax-Assessor', 'https://github.com/vuvictor1/Tax-Assessor', '(Tribrid program written in x86 Assembly, C++ and C to assess sum and mean of property values.)', [
                    '● Collects float of arrays as user input for computation. Incorporates a time updater to retrieve local date.',
                    '● Implements invalid input handling to prevent errors.'
                ]),
                ('Victor\'s-Website', 'https://github.com/vuvictor1/Victors-Website', '(Python/CSS digital portfolio website of Victor V. Vu.)', [
                    '● Supports multi-page functionality, containing embedded media, tabs selection and redirect buttons.',
                    '● Features a contact support form which forwards messages via email.'
                ])
            ]

            for i in range(0, len(projects), 2): # Create project rows
                create_project_row(projects[i:i+2])

    with ui.row().style('justify-content: center; width: 100%; margin-top: 40px;'): # Research projects title
        create_label('Research Projects', font_size=font_size_large)

    with ui.row().style('justify-content: center; width: 100%; margin-top: 20px;'): # Research projects content
        with ui.column().classes('projects').style('align-items: center; text-align: center;'):
            ui.html(f'<lottie-player src="{lottie_4_url}" loop autoplay style="height: 400px; margin-bottom: 20px;"></lottie-player>')
            research_projects = [ # List of research projects
                ('Operations Analysis', 'https://docs.google.com/document/d/1XhZCOei60DCcFlYO1scSQ5m6UwcKfwTgmN0NjlamjtY/edit?tab=t.0#heading=h.868kz7lj5kq9', 'Detailed report on the time complexities of binary search trees, hash tables, vectors, dynamic link libraries and singly linked lists operations.', []),
                ('Rain Gutter Construction', 'https://docs.google.com/document/d/1_RcIvuWFvMmvF96vdpOod8z2vCf5s2mVkY4_UVU5vZU/edit?tab=t.0', 'Mathematical approach on how to solve the rain gutter problem of determining an object design\'s water capacity using Calculus.', []),
                ('Coffee Container Calculation', 'https://docs.google.com/document/d/17NW6yIdzAp-D2okMZlLdM3kxcGai3WUC8zds3RMgb8A/edit?tab=t.0', 'Representation of how Folger\'s Engineering Division uses Calculus to approximate a containers volume and area for maximum profit.', [])
            ]
            
            for i in range(0, len(research_projects), 2): # Create research project rows
                create_project_row(research_projects[i:i+2])
    vu_footer() # footer

@ui.page('/projects') # Route projects page
def projects():
    projects_page()