from py2cfg import CFGBuilder

def visualize(code: str) -> str:
    cfg_builder = CFGBuilder()
    cfg = cfg_builder.build_from_src("cfg", code)
    cfg.build_visual(f'testing/output/cfg', 'dot')

    f = open("testing/output/cfg.dot", "r")
    return f.read()

code = """
for i in range(10):
    print(i)
    if i == 5:
        break

"""
print(visualize(code))

