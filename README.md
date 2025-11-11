# Wrapping Paper App - Python

A small Python application for calculating **wrapping paper** and **cost** for common gift shapes.  
Supports **cube**, **cuboid**, and **cylinder** packages and exports results to a file for record‑keeping.


## Overview

Given package dimensions and a chosen paper type, the app computes:
- **Surface area** + **waste allowance**
- **Required sheet count / roll length** (simplified model)
- **Total price** based on paper tier (e.g., *Cheap* vs *Expensive*)
- Optional **write‑out** of results to a text file

The repo includes simple reference images for each shape and tiles for paper tiers to help explain the UI/flow.


## Project Structure

```
.
├── Wrapping Papper Project.py                 # Main script (CLI)
├── Wrapping Papper Project - 2105616.py       # Alternate/assessed version
├── wrighting to a new file.py                 # Utility that writes results to a file
├── Cube.png                                   # Reference image for cube
├── Cuboid.png                                 # Reference image for cuboid
├── Cylinder.png                               # Reference image for cylinder
├── Cheap.png                                  # Tile for cheap paper
└── Expensive.png                              # Tile for expensive paper
```

> Note: Filenames preserve the original coursework naming.


## Features

- Calculate paper needed for:
  - **Cube** (edge `a`)
  - **Cuboid** (length `l`, width `w`, height `h`)
  - **Cylinder** (radius `r`, height `h`)
- Choose **paper tier** (e.g., Cheap vs Expensive) with distinct price per unit
- Optional **waste margin** (off‑cut allowance)
- **Export** results to `output.txt` (or a file you choose)


## Formulae Used (simplified)

- **Cube area:** `6a^2`
- **Cuboid area:** `2(lw + lh + wh)`
- **Cylinder area:** `2πr^2 + 2πrh`
- **Total required:** `surface_area × (1 + waste_margin)`

> Rolls/sheeting are modelled as a direct area purchase for simplicity.


## How to Run

Prerequisite: **Python 3.10+**

```bash
# Clone your repo locally, then run:
python "Wrapping Papper Project.py"
# or
python "Wrapping Papper Project - 2105616.py"
```

If the script writes a report, it will appear alongside the program (e.g., `output.txt`).

### Running the write‑out utility directly
```bash
python "wrighting to a new file.py"
```


## Sample Session (CLI)

```
Select shape: 1) Cube  2) Cuboid  3) Cylinder
> 2
Enter length (cm): 30
Enter width  (cm): 20
Enter height (cm): 12
Select paper: 1) Cheap  2) Expensive
> 1
Waste margin (e.g., 0.08 for 8%): 0.08

Total area:  4392.0 cm^2
Paper cost:  £4.39
Saved to: output.txt
```

*(Values shown for illustration; your script may format differently.)*


## Configuration

If you want to centralise prices and margins, add a small config at the top of the script, e.g.:

```python
CHEAP_PRICE_PER_CM2 = 0.001
EXPENSIVE_PRICE_PER_CM2 = 0.0025
DEFAULT_WASTE = 0.08
```


## Tech

- Python standard library only (no external dependencies)
- CLI‑based workflow for easy marking/demo


## Future Enhancements

- Support **ribbon** and **gift‑wrap seams** (fold allowances)
- Convert area to **roll length** given roll width
- **GUI** using Tkinter or a minimal web UI (Flask)
- Unit tests for edge cases (zero/negative dimensions)


## Author

**Charlotte Cannon**  
Graduate Software Engineer  
- [LinkedIn]https://www.linkedin.com/in/charlotte-cannon-165875195/
- [GitHub]https://github.com/c-cannon13


## License

This project is provided for educational and portfolio demonstration purposes.
## License
This project is provided for educational and portfolio demonstration purposes.  
© 2024 Charlotte Cannon. All rights reserved.
