# Techbois Landing Page

This project contains a simple static landing page for **Techbois**. The main goal is to demonstrate a basic HTML/CSS login form along with associated web assets. A small test suite verifies that the referenced resources exist.

## Setup

1. Clone this repository.
2. Open `index.html` in your web browser. All of the web assets (images, stylesheets, manifest files) are stored in the repository root, so no additional build step is required.

## Running Tests

Tests are written with `pytest`. To run them, install `pytest` if necessary and execute:

```bash
pytest
```

The tests check that files referenced by `index.html` and `site.webmanifest` are present.
