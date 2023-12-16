
# bump the version in metrodraw/version.py, delete the old dist/ directory, run sdist and twine

import subprocess

with open("metrodraw/version.py", "r") as fh:
    version = fh.read().strip()

version = version.split(".")
version[-1] = str(int(version[-1]) + 1)
version = ".".join(version)

with open("metrodraw/version.py", "w") as fh:
    fh.write(version)

# add and commit
subprocess.run(["git", "add", "metrodraw/version.py"])
subprocess.run(["git", "commit", "-m", f"bump version to {version}"])

subprocess.run(["rm", "-rf", "dist"])
subprocess.run(["python", "setup.py", "sdist"])
subprocess.run(["twine", "upload", "dist/*"])