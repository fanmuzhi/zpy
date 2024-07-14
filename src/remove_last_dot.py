import os

for p, fds, fs in os.walk(os.path.curdir):
    if p == os.path.curdir:
        for fd in fds:
            if fd.endswith("."):
                print(os.path.abspath(fd))
            # os.rename(os.path.abspath(fd), os.path.abspath(fd)[:-1])
