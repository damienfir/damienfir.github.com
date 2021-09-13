all: build

.PHONY: build

build:
	python build.py docs
	-mkdir docs/static
	cp -r static/* docs/static/

serve:
	cd docs && python -m http.server

publish: build
	git add .
	git commit -m "publish $(shell date +%Y%d%m-%H%M%S)"
	git push

clean:
	rm -r build
