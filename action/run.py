import os
import subprocess
import glob
from config import Config
from dockerfile import Dockerfile

current_branch_name = os.getenv("ACTION_CURRENT_BRANCH")
branch_name = os.getenv("ACTION_BRANCHNAME")
config = Config()

changed = False

repofiles = [f for f in glob.glob(config.rootdir + "**/*", recursive=True)]
dockerfiles = [f for f in repofiles if config.dockerfile_name in f.split("/")[-1].lower()]

if len(dockerfiles) == 0:
    exit(f"No dockerfiles found")

if config.exclude_type:
    print(f"Skipping {config.exclude_type}")

if config.exclude_package:
    print(f"Skipping {config.exclude_package}")

for filepath in dockerfiles:
    dockerfile = Dockerfile(config, filepath)
    if dockerfile.update():
        changed = True

if not changed:
    exit(0)


