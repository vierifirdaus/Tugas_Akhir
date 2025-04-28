from py2cfg import CFGBuilder

def visualize(code: str) -> str:
    cfg_builder = CFGBuilder()
    cfg = cfg_builder.build_from_src("cfg", code)
    cfg.build_visual(f'testing/output/cfg', 'svg')

    f = open("testing/output/cfg.dot", "r")
    return f.read()

code = """
class Tree:
   def __init__(self, height):
       self.__height = height

   def get_height(self):
       return self.__height

   def set_height(self, new_height):
       self.__height = new_height

"""
print(visualize(code))

