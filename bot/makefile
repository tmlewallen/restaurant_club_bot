.PHONY: build test format run-local clean release

# Install dependencies for local development 
build: 
	pip install -e '.[test,server]'

# Run test suite
test:
	python -m pytest

# Run auto-formatter
format: 
	python -m black src test

# Build a zip archive to upload to Aws Lambda
release: clean format build test
	pip install . --target build/archive \
		--platform manylinux2014_x86_64 \
		--only-binary :all: \
		--upgrade
	cd build/archive; zip -r ../archive.zip *

# Run local flask server
run-local: build
	flask --app local run

# Clean up the build dir
clean:
	rm -rf build