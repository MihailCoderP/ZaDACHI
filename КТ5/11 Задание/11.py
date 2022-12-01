# -*- coding: utf-8 -*-

import requests
import json
from tkinter import Button, Tk

def github():
    repo = 'https://api.github.com/repos/openshift/origin'
    repo = requests.get(repo)
    repo = repo.json()
    new_repo = {}
    for k in ['company', 'created_at', 'email', 'id', 'name', 'url']:
        if repo.get(k) != None:
            new_repo[k] = repo.get(k)
    file = open('output.json', 'w')
    json.dump(new_repo, file)
    file.close()

def tkinter():
    tk = Tk()
    Button(tk, text='get github', command=github).pack()
    tk.mainloop()

tkinter()
