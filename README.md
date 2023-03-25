# WFC-Terrain-Generator-v2

Procedural Terrain Generator using the Wave Function Collapse Algorithm ([WFC implementation](https://github.com/JuanSoriaE/WFC)).

## Topographic Terrain (Introduction)

The Wave Function Collapse Algorithm generate images based on given rules that determinate which states can be adjacent to which others states.
The basic Color Topographic Map determines which heights are adjacent to which others, which serve as initial rules.

The relations are the following:

![Diagram 1 Image](./assets/diagram1.jpeg)

Translating this into an Adjacency Dictionary is:

```
adj_dic = {0: [0, 1], 1: [0, 1, 2],
           2: [1, 2, 3], 3: [2, 3, 4],
           4: [3, 4, 5], 5: [4, 5]}
```

With the `adj_dict` above and the following parameters we will get the next result:

### INPUT

```
ini_state = [0, 1, 2, 3, 4, 5]
n = 40
m = 40
adj_offs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
neighbors_based = False

# Colors
color_map: dict = {0: '#fd0200', 1: '#daf516',
                   2: '#3ac00a', 3: '#1a82d3',
                   4: '#013897', 5: '#7c027c'}
```

### OUTPUT
The limited number of states produces a grid-patterned output image. To enhance it, we can average the color of each cell with its 8-adjacent cells.

| Direct Output | Averaging colors | 3D View |
| ------------- | ---------------- | ------- |
| ![Sample image 1 grid-patterned](./samples/1-grid.jpg) | ![Sample image 1 smooth](./samples/1.jpg) | ![Sample image 1 3d view](./samples/1-3d.jpg) |

## Get Started

Make sure to have Python 3.6+ and pip installed.

### STEPS
1. Clone this repository.
    ```
    git clone https://github.com/JuanSoriaE/WFC-Terrain-Generator-v2.git
    ```

2. Once you are in the root path of the project, clone the repository of the WaveFunctionCollapsed module ([Link WFC module](https://github.com/JuanSoriaE/WFC)).

3. Install the dependencies.
    ```
    pip install Pillow ursina numpy
    ```

4. Run the main.py file.
    ```
    python main.py
    ```

5. You can modify all the parameters from the main.py file.

## EXAMPLES WITH CUSTOM PARAMETERS

All the images below uses the same `color_map`.
| Averaging colors Image | 3D View (Generated with GREY-SCALE Topographic Map image) | Parameters |
| ------------ | ------- | ---------- |
| ![Samples image 2 smooth](./samples/2.jpg) | ![Samples image 2 3d view](./samples/2-3d.jpg) | `ini_state = [0, 1, 2, 3, 4, 5]`<br>`n = 40, m = 40`<br>`adj_dic = {0: [0, 1], 1: [0, 1, 2], 2: [0, 1, 2, 3, 5], 3: [2, 3, 4, 5], 4: [0, 3, 4, 5], 5: [4, 5]}`<br>`adj_offs = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]`<br>`neighbors_based = True` |
| ![Sample image 3 smooth](./samples/3.jpg) | ![Sample image 3 3d view](./samples/3-3d.jpg) | `ini_state = [0, 1, 2, 3, 4, 5]`<br>`n = 40, m = 40`<br>`adj_dic = {0: [0], 1: [0, 1, 2], 2: [1, 2, 3, 5], 3: [2, 3, 4, 5], 4: [3, 4, 5], 5: [4, 5]}`<br>`adj_offs = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]`<br>`neighbors_based = True` |
| ![Sample image 4 smooth](./samples/4.jpg) | ![Samples image 4 3d view](./samples/4-3d.jpg) | `ini_state = [0, 1, 2, 3, 4, 5]`<br>`n = 40, m = 40`<br>`adj_dic = {0: [0, 1], 1: [0, 1, 2], 2: [1, 2, 3], 3: [2, 3, 4], 4: [3, 4, 5], 5: [4, 5, 0]}`<br>`adj_offs = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]`<br>`neighbors_based = True` |
| ![Sample image 5 smooth](./samples/5.jpg) | ![Samples image 5 3d view](./samples/5-3d.jpg) | `ini_state = [0, 1, 2, 3, 4, 5]`<br>`n = 40, m = 40`<br>`adj_dic = {0: [0, 1], 1: [0, 1, 2], 2: [1, 2, 3, 5], 3: [2, 3, 4, 5], 4: [3, 4, 5], 5: [4, 5]}`<br>`adj_offs = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]`<br>`neighbors_based = False` |
