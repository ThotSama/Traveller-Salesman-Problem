 Traveling Salesman using 3 algorithms:
 - Brute force
   - Random
   - Lexicographical order
 - genetic algorithm
 - Ant Colony optimization
   - ACS (classical version)
   - Elitist
   - Max-Min

## Requirements
> **Pygame** : pip install pygame

---
## Controls
- **Esc**   To close the window
- **Space** To Pause and Start Simulation
- **Enter or Return** To toggle the UI Panel
---
```python:main.py
# Brute force solution , just by using going through all the possible combination 
# with a random function until we find the shortest distance
manager.BruteForce() 
# using Lexicographical order to solve the problem by going in order into all the possible routes
manager.Lexicographic()
# using genetic algorithm to find the fittest one
manager.GeneticAlgorithm()
# using AntColonyOptimization(name:String) 
manager.AntColonyOptimization("ACS") # or "ELITIST" or "MAX-MIN"

```
---
## Unsolved Issues & Bugs
     The code is a little bit redundant , it's need some refactoring.
     And the ui also need some retouch
---
## Incoming Features
	The code will be able to read a specific excel file in order to have specific points
---
