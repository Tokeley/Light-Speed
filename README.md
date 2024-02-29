# Light Speed 🚀 

Light Speed is a simple space-themed video game for learning basic arithmetic, aimed at children between the ages of 5 and 13. This project was built with Python and the Pygame library.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Installation and Usage](#installation-and-usage)
- [What I Learned](#what-i-learned)

## Overview

Embark on an exciting adventure through the cosmos, the only catch is that to survive, you must master your mathematical prowess! In Light Speed, the objective is to captain the spaceship to shoot and destroy the asteroids (by pressing the space bar) with the correct answer to the maths question shown on the planet at the bottom of the screen. Asteroids with incorrect answers can not be destroyed. You have three lives, each time you get hit by an asteroid you lose a life, and if you lose all three it is game over! Move the ship up and down with the arrow keys. The game offers four levels/planets with increasing difficulty. A level will be recommended to you depending on your age. Good luck!

## Features

- Fun and exciting gameplay that encourages children to engage in arithmetic practice.
- Level recommendation depending on age.
- Pleasing pixel art design.
- Intuitive controls and user-friendly interactions for a smooth gameplay experience.

## Demo

![Light Speed GIF](demo.gif)

## Installation and Usage

1. Clone the repository: `git clone https://github.com/Tokeley/Light-Speed.git`
2. Run the game using the command: `python3 main.py`

## What I Learned

In the development of Light Speed, I learned many core software design techniques that include: 
- **Basics of object-orientated design:** This was the first project I've made that used OOP. Creating separate classes for asteroids, questions, projectiles, and more was vital in the game design.  OOP allows you to break down the game into manageable, modular components called objects. From this, I learned the basics of encapsulation.
- **State management:** Light Speed also makes use of basic state management. It has a menu, instructions, ageSelection, mainGame, and more possible states. Each of these states has a game loop that runs indefinitely but will transition into another state given a specific trigger like pressing a "Play" button. By dividing the game into distinct states such as menu, instructions and mainGame, it clearly defines and organizes the different parts of your game. This makes it easier to understand the flow of the game and maintain the codebase as it grows.
- **Pixel Art:** I learned basic pixel art to create the Light Speed design. This was a fun creative challenge and I am very proud of the results. The pixel art gives the game a cohesive theme resulting in a polished and engaging look and feel. I used [Pixilart](pixilart.com) to create all the designs for the game including the spaceship, the asteroids, and the planets. 
