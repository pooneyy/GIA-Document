import os
def verify_path(root):
    root = os.path.abspath(root)
    if not os.path.exists(root):
        verify_path(os.path.dirname(root))
        os.mkdir(root)
        print(f"dir {root} has been created")

def exec_cmd(cmd):
    print(cmd)
    os.system(cmd)