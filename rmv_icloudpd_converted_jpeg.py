import os


def get_files_size(fd):
    for p, fds, fs in os.walk(fd):
        for f in fs:
            print(f"{os.path.getsize(os.path.join(p, f)) / 1024}KB")


if __name__ == "__main__":
    get_files_size(os.curdir)
