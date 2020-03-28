import requests

def version_debian(pkg):
    print(f"[debian] {pkg}")
    url = f"https://sources.debian.org/api/src/{pkg}/"
    response = requests.get(url).json()
    if "error" in response:
        return
    for version in response["versions"]:
        if "buster" in version["suites"]:
            return version["version"]