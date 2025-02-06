import requests

x = requests.get(f"http://127.0.0.1:8000/camera/snap",headers={
                                        "accept":"application/json"
                                        })
print(x.url)


