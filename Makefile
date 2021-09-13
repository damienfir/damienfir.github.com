all: build

.PHONY: build

build:
	python build.py
	-mkdir build/static
	cp -r static/* build/static/

serve:
	cd build && python -m http.server

publish: build
	git add .
	git commit -m "publish $(shell date +%Y%d%m-%H%M%S)"
	git push

clean:
	rm -r build
