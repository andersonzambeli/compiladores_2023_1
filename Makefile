run:
	python3.10 lexical_analyzer.py $(FILE)

setup: requirements.txt
	python3.10 -m pip install --upgrade pip
	python3.10 -m pip install -r requirements.txt