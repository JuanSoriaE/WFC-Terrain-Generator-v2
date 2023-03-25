from PIL import Image

OFFS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

def hexToRGB(hex: str) -> tuple:
    hex = hex.lstrip('#')
    rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    return rgb

def getAvgColor(r: int, c: int) -> tuple:
    color = list(hexToRGB(COLORS[GRID[r][c][0]]))
    cnt: int = 1

    for x, y in OFFS:
        new_r, new_c = r + y, c + x
        if min(new_r, new_c) < 0 or new_r >= N or new_c >= M:
            continue

        cell_rgb = list(hexToRGB(COLORS[GRID[new_r][new_c][0]]))
        cnt += 1
        for i in range(3):
            color[i] += cell_rgb[i]
    
    for i in range(3):
        color[i] //= cnt
    
    return tuple(color)

def buildImage(grid: list[list[list[int]]], color_map: dict, bg_color: str, w: int, h: int, name: str, smooth: bool = False, show: bool = False) -> None:
    # Global variables
    global N, M, COLORS, GRID
    N, M = len(grid), len(grid[0])
    COLORS = color_map
    GRID = grid

    bg = Image.new('RGB', size=(w, h), color=bg_color)
    cell_w, cell_h = w // M, h // N

    for r in range(N):
        for c in range(M):
            x, y = c * cell_w, r * cell_h
            color = getAvgColor(r, c) if smooth else COLORS[GRID[r][c][0]]
            sub_img = Image.new('RGB', size=(cell_w, cell_h), color=color)
            bg.paste(sub_img, box=(x, y))
    
    bg.save(name)
    if show:
        bg.show()


