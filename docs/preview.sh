# Build and preview the documentation locally.
#
# This script is used to build and preview the documentation locally. It
# builds the documentation using Sphinx and then starts a local HTTP server
# to serve the built documentation.
make clean
make html
python -m http.server --directory _build/html
