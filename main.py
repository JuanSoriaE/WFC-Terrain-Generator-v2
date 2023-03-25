from WFC import wfc
from helpers import img
from helpers import map3d

def main():
    SAMPLE_ID: int = 6 # ID of the image, which serve also as filename.
    
    # WFC
    ini_state: list = [0, 1, 2, 3, 4, 5]
    N: int = 40
    M: int = 40
    adj_dic: dict = {0: [0, 1], 1: [0, 1, 2], 2: [1, 2, 3], 3: [2, 3, 4], 4: [3, 4, 5], 5: [4, 5]}
    OFFS: list[tuple] = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)] # 8-adjacent | 4-adjacent its the dafault
    neighbors_based: bool = False

    grid: list[list[list[int]]] = wfc.WFC(
            ini_state, N, M,
            adj_dic,
            # adj_offs=OFFS,
            neighbors_based=neighbors_based)


    # IMAGES
    # TOPOGRAPHIC COLORS
    COLORS: dict = {0: '#fd0200', 1: '#daf516', 2: '#3ac00a', 3: '#1a82d3', 4: '#013897', 5: '#7c027c'}
    GREY_COLORS: dict = {0: '#ffffff', 1: '#cccccc', 2: '#999999', 3: '#666666', 4: '#333333', 5: '#000000'}
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
    img.buildImage(grid, COLORS, '#000', w, h, name, smooth, not show) # Color Topographic Map.
    img.buildImage(grid, GREY_COLORS, '#000', w, h, name_grey, smooth, show) # Grey-scale height Map.

    
    # 3D VISUALIZATION
    scale: tuple = (9, 3, 9) # (x, y, z) | y = height
    pos: map3d.Vec3 = (0, 2, 0) # Initial position (x, y, z)
    # Uses EditorCamera, so movement its not available.
    # To turn the camera, hold right-click and turn.
    # You can modify the file at ".\helpers\map3d.py" to set FirstPerson view or any others Ursina's features.
    hmap_path: str = f'\samples\{SAMPLE_ID}-hmap' # Path of the height-map.
    texture_path: str = f'\samples\{SAMPLE_ID}'
    
    map3d.render(hmap_path, texture_path, scale, pos)


if __name__ == '__main__':
    main()

