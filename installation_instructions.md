INSTALL INSTRUCTIONS:

To run the course on your local machines, you need the following software:

1.) Install Python 3.10 or higher. I recommend the Anaconda Distribution: https://www.anaconda.com/download . Skip the email registration, it is not necessary.

2.) Install a code editor. I recommend Visual Studio Code: https://code.visualstudio.com/download . If you prefer to use PyCharm or a different editor with syntax highlighting. I am not planning to cover IDE specific features during the course.

3.) Install a few Python libraries. These can be installed with the *pip* program. On Windows, launch the "Anaconda Prompt" from the start menu. Then type:

    python -m pip install pandas httpx pytest black

On a Mac, open a terminal and paste the command there. You may have to type *python3* instead of *python*.

we might install a few more libraries during the course using the same method..

There are alternative approaches, e.g. running pip from VS Code or from a Windows Powershell. They involve some configuration, but I don't think it is necessary for the course.

4.) Run a simple Python program usging one of the libraries. Create a new file 'nobleprog.py' with the following code in your code editor:

    import httpx

    url = "https://www.nobleprog.ro"
    page = httpx.get(url)
    start = page.text.find("<title>")
    title = page.text[start:start+70]
    print(title)

Run the code from your editor or from the Anaconda Prompt/Terminal using:

    cd folder_name/where/the/program/is

    python nobleprog.py  # Anaconda

    python3 nobleprog.py # MacOS

Please let us know if you need help setting things up. If we can help sort out any issues before the course, it makes the training more productive for everybody.
