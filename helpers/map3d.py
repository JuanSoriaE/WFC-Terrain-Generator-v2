from ursina import *

def render(hmap_path: str, texture_path: str, scale: tuple, pos: Vec3) -> None:
    app = Ursina()
    terrain = Terrain(heightmap=hmap_path, skip=4)
    terrain_entity = Entity(model=terrain, scale=scale, texture=texture_path)

    ec = EditorCamera()
    ec.position = pos
    app.run()
