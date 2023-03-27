from WFC import wfc
from helpers import img
from helpers import map3d

def main():
    SAMPLE_ID: int = 6 # ID of the image, which serve also as filename.
    
    # WFC
    ini_state: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    N: int = 100
    M: int = 100
    adj_dic: dict = {0: [0, 1], 1: [0, 1, 2],
                     2: [1, 2, 3], 3: [2, 3, 4],
                     4: [3, 4, 5], 5: [4, 5, 6],
                     6: [5, 6, 7], 7: [6, 7, 8],
                     8: [7, 8, 9], 9: [8, 9, 10],
                     10: [9, 10, 11], 11: [10, 11, 12],
                     12: [11, 12, 13], 13: [12, 13, 14],
                     14: [13, 14, 15], 15: [14, 15]}
    ini_cell: tuple = (49, 49)
    OFFS: list[tuple] = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)] # 8-adjacent | 4-adjacent its the dafault
    neighbors_based: bool = False

    grid: list[list[list[int]]] = wfc.WFC(
            ini_state, N, M,
            adj_dic,
            # ini_cell=ini_cell,
            # adj_offs=OFFS,
            neighbors_based=neighbors_based)
    

    # IMAGES
    # TOPOGRAPHIC COLORS
    COLORS: dict = {0: '#ff0000', 1: '#ff5000',
                    2: '#ffa000', 3: '#ffff00',
                    4: '#a0ff00', 5: '#50ff00',
                    6: '#00ff00', 7: '#00ff50',
                    8: '#00ffa0', 9: '#00ffff',
                    10: '#00a2ff', 11: '#0050ff',
                    12: '#0000ff', 13: '#0000a0',
                    14: '#000050', 15: '#000000'}
    GREY_COLORS: dict = {0: '#ffffff', 1: '#eeeeee',
                         2: '#dddddd', 3: '#cccccc',
                         4: '#bbbbbb', 5: '#aaaaaa',
                         6: '#999999', 7: '#888888',
                         8: '#777777', 9: '#666666',
                         10: '#555555', 11: '#444444',
                         12: '#333333', 13: '#222222',
                         14: '#111111', 15: '#000000'}
    # w and h has to be multiple of N and M respectivelly.
    w: int = 400 # width of the image.
    h: int = 400 # height of the image.
    name_grid: str = f'samples\{SAMPLE_ID}-grid.jpg'
    name: str = f'samples\{SAMPLE_ID}.jpg'
    name_grey: str = f'samples\{SAMPLE_ID}-hmap.jpg'
    smooth: bool = True
    show: bool = True

    # Output images save in "samples" folder.
    img.buildImage(grid, COLORS, '#000', w, h, name_grid, not smooth, show) # Color Topographic Map grid-patterned.
    img.buildImage(grid, COLORS, '#000', w, h, name, smooth, not show) # Smoothed Color Topographic Map.
    img.buildImage(grid, GREY_COLORS, '#000', w, h, name_grey, smooth, show) # Grey-scale height Map.

    
    # 3D VISUALIZATION
    scale: tuple = (9, 2, 9) # (x, y, z) | y = height
    pos: map3d.Vec3 = (0, 2, 0) # Initial position (x, y, z)
    # Uses EditorCamera, so movement its not available.
    # To turn the camera, hold right-click and turn.
    # You can modify the file at ".\helpers\map3d.py" to set FirstPerson view or any others Ursina's features.
    hmap_path: str = f'\samples\{SAMPLE_ID}-hmap' # Path of the height-map.
    texture_path: str = f'\samples\{SAMPLE_ID}'
    
    visualize: str = input('Visualize in 3D? (y/n) ')
    if visualize == 'y':
        map3d.render(hmap_path, texture_path, scale, pos)


if __name__ == '__main__':
    main()

