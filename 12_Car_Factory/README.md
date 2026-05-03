# 12 — Car Factory

Overview
- Simulation of a minimal car factory that creates car objects and demonstrates object-oriented design patterns at a small scale.

Purpose
- Teach classes, constructors, composition, and simulating a simple pipeline of creation → configuration → output.

Thought process / design
- Inputs: parameters to create a car (make, model, year, color); could be interactive or read from a sample data file.
- Processing: construct car objects, optionally run through steps such as painting or installing options, store created cars in an inventory list.
- Output: print summaries for each car and inventory totals.

Files
- `main.py` — defines `Car` class and factory functions, and runs simple scenarios.

How to run
```bash
python main.py
```

Example
- Create 3 cars with different options; program prints each car's attributes and the total produced.

Extensions / Improvements
- Add persistence to save inventory to JSON.
- Add unit tests for construction and option application functions.

What I learned
- Encapsulating data in classes and designing simple simulations to exercise class methods.
