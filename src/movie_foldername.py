import os
import re

symbols = ["+", ]
for p, fds, fs in os.walk(os.curdir):
    if p == os.curdir:
        for fd in fds:
            new_fd = fd.strip()
            for sbl in symbols:
                new_fd = new_fd.replace(sbl, ".")
            pat1 = r"^\[.+?\]"
            pat2 = r"^【.+?】"
            if re.match(pat1, new_fd):
                new_fd = re.sub(pat1, "", new_fd)

            elif re.match(pat2, new_fd):
                new_fd = re.sub(pat2, "", new_fd)

            results = re.findall(pat1[1:], new_fd)
            for result in results:
                new_fd = new_fd.replace(result, f".{result[1:-1]}")
            os.rename(os.path.join(os.curdir, fd), os.path.join(os.curdir, new_fd))
