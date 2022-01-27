all:
	python build.py

clean:
	rm -r pages

publish: all
	git commit -am "Update $(shell date +%Y%m%d%H%M%S)"
	git push
