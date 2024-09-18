
# Session 09 - Useful Python Packages

### Exercise 1: Draw a flag

Use Numpy to draw a flag. Start with the code in `flags.py`.
It requires two libraries:

    pip install pillow numpy

Also see: [https://www.academis.eu/numpy_graphics/](https://www.academis.eu/numpy_graphics/)

### Exercise 2: Profiling

Run the code in `mandelbrot.py` and time its execution with cProfile, the Python profiler:

    python -m cProfile -s cumtime mandelbrot.py > profile.txt

Inspect the output and look for bottlenecks.

Insert the line

    z[index] = z[index] \*\* 2 + c[index]

Re-run the profiling.

### Exercise 3: C Extensions

Inspect how a Python-C interfacee looks like.
Examine the code at [https://github.com/biopython/biopython/blob/master/Bio/PDB/](https://github.com/biopython/biopython/blob/master/Bio/PDB/).

In particular, inspect the files:

- NeighborSearch.py
- kdtrees.c
- setup.py (in the main directory)
- README.md (in the main directory)

### Exercise 4: Make Python faster

Enumerate ways to make Python programs faster.

### Exercise 5: Web Scraping

Use the `httpx` module to download a Wikipedia page and save it to a file.

    import httpx
    p = httpx.get("http://localhost:8000")
    print(p.status_code)
    print(p.text)

### Exercise 6: Parse HTML

Read the saved HTML page and parse it using Beautiful Soup.
Use the code in `example_bs4.py` as a starting point.

Discuss how to use documentation of Python modules.

### Exercise 7: Web front-end testing

Remote-control your browser. Run from the command line:

    pip install playwright
    playwright install

Generate test code with

    playwright codegen www.wikipedia.org

Before closing the browser, copy the generated code.
To run it, add imports:

    import playwright
    from playwright.sync_api import sync_playwright, Playwright

before closing the context, add:

    page.screenshot(path="screenshot.png")

Execute the code with Python.

Also see: [https://playwright.dev/python/](https://playwright.dev/python/)
