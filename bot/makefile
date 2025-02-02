build: 
	pip install -e '.[test,server]'

test: build
	echo TEST

release: build test
	pip install . --target build/archive \
		--platform manylinux2014_x86_64 \
		--only-binary :all: \
		--upgrade
	cd build/archive; zip -r ../archive.zip *

run-local: build
	flask --app local run

clean:
	rm -rf build