# Orbital Simulator

A 2D orbital physics simulation built with Python and Pygame. Simulates gravitational interactions between multiple celestial bodies with realistic Newtonian mechanics.

## Features

- **Newtonian Gravity** – Bodies attract each other with forces proportional to their masses and inversely proportional to distance squared
- **Vector Physics** – Position, velocity, and acceleration represented as 2D vectors for accurate motion
- **Collision Detection** – Basic collision handling between orbiting bodies
- **Real-time Visualization** – Pygame rendering loop displays bodies and their trajectories
- **Object-Oriented Design** – Clean, modular code structure using classes

## Screenshots
![Orbital Simulation](./src/assets/preview.webp)


## Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/orbital-simulator.git
cd orbital-simulator

# Install dependencies
pip install pygame
```

## Usage
```bash
python main.py
```

## How It Works

The simulation uses basic physics integration to update each body's state:

1. Calculate gravitational forces between all body pairs
2. Sum forces to get net acceleration (F = ma)
3. Update velocity based on acceleration
4. Update position based on velocity
5. Check for collisions and render

## Learning Outcomes

This project demonstrates:
- Vector mathematics in physics simulation
- Numerical integration for motion updates
- Multi-body gravitational systems
- Game loop architecture with Pygame
- OOP principles in scientific computing

