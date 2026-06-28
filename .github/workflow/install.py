name: install Workflow

on:
  push:

jobs:
 install:
    runs-on: self-hosted
    steps:  
- name: Run app
  run: |
    nohup python3 app.py &
