run:
	python3 lexical_analyzer.py $(FILE)

setup: requirements.txt
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt