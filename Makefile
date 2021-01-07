all: build

build:
	python build.py

serve:
	python -m http.server

publish: build
	git add .
	git commit -m "publish $(shell date +%Y%d%m-%H%M%S)"
	git push
