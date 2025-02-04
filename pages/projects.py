# Author: Victor V. Vu
# File: projects.py
# Description: Projects page for Victor's portfolio website
# Copyright (C) 2024 Victor V. Vu
# License: GNU GPL v3 - See https://www.gnu.org/licenses/gpl-3.0.en.html
from nicegui import ui
from components import vu_header, vu_footer, inject_ui, inject_lottie

# Constants
lottie_3_url = 'https://lottie.host/ddd7660b-67b2-4b52-a49a-8fc2a4f3b36b/QKoTWTHqJ1.json'
lottie_4_url = 'https://lottie.host/c7f17250-d067-4a1e-aab2-4656f68c94c9/QrwbdaLSwA.json'

def projects_page(): # Projects page main function
    vu_header() # inject header
    inject_ui() # inject UI

    with ui.row().classes('justify-center w-full my-4'): # Center the title
        ui.label('Programming Projects').classes('text-white text-4xl font-bold text-center')
    inject_lottie() # inject lottie animation

    ui.html(f'<lottie-player src="{lottie_3_url}" loop autoplay speed="0.75"></lottie-player>').classes('w-full max-w-md mx-auto') # play lottie animation

    # List of projects
    programming_projects = [
        ('7 Realms', 'https://drive.google.com/file/d/1u5gYVXi0HOdr1Gn2XOfvBFZfzWtIaacT/view?usp=sharing', '(High-tech medieval-themed game introducing new mechanics through modification.)', [
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

    for i in range(0, len(programming_projects), 2): # Create project rows
        with ui.row().classes('justify-center w-full my-4 flex-wrap gap-4'):
            for project in programming_projects[i:i+2]: # Create project sections
                with ui.column().style('max-width: 100%;').classes('items-center text-center p-5 bg-gray-800 rounded-lg shadow-lg outline_label'):
                    ui.link(project[0], project[1]).classes('text-blue-300 text-2xl font-semibold') # Updated color class
                    ui.label(f' {project[2]}').classes('text-white text-lg')
                    for detail in project[3]: # Create project details
                        ui.label(detail).classes('text-white text-lg')
                    ui.separator().classes('my-2')

    with ui.row().classes('justify-center w-full my-4'): # Center the title
        ui.label('Research Projects').classes('text-white text-4xl font-bold')

    ui.html(f'<lottie-player src="{lottie_4_url}" loop autoplay speed="0.75"></lottie-player>').classes('w-full max-w-md mx-auto') # play lottie animation

    research_projects = [ # List of research projects
        ('Operations Analysis', 'https://docs.google.com/document/d/1XhZCOei60DCcFlYO1scSQ5m6UwcKfwTgmN0NjlamjtY/edit?tab=t.0#heading=h.868kz7lj5kq9', 'Detailed report on the time complexities of binary search trees, hash tables, vectors, dynamic link libraries and singly linked lists operations.', []),
        ('Rain Gutter Construction', 'https://docs.google.com/document/d/1_RcIvuWFvMmvF96vdpOod8z2vCf5s2mVkY4_UVU5vZU/edit?tab=t.0', 'Mathematical approach on how to solve the rain gutter problem of determining an object design\'s water capacity using Calculus.', []),
        ('Coffee Container Calculation', 'https://docs.google.com/document/d/17NW6yIdzAp-D2okMZlLdM3kxcGai3WUC8zds3RMgb8A/edit?tab=t.0', 'Representation of how Folger\'s Engineering Division uses Calculus to approximate a containers volume and area for maximum profit.', [])
    ]

    for i in range(0, len(research_projects), 2): # Create research project rows
        with ui.row().classes('justify-center w-full my-4 flex-wrap gap-4'):
            for project in research_projects[i:i+2]: # Create research project sections
                with ui.column().style('max-width: 30%;').classes('items-center text-center p-5 bg-gray-800 rounded-lg shadow-lg outline_label'):
                    ui.link(project[0], project[1]).classes('text-blue-300 text-2xl font-semibold') # Updated color class
                    ui.label(f' {project[2]}').classes('text-white text-lg')
                    for detail in project[3]: # Create project details
                        ui.label(detail).classes('text-white text-lg')
                    ui.separator().classes('my-2')

    vu_footer() # footer

@ui.page('/projects') # Route projects page
def projects():
    projects_page()