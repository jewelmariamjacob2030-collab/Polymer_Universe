# POLYVERSE — Under the Moonlight Edition

A twilight fusion of laboratory science and future technology.

This is a separate, runnable visual version of the same MATEX polymer-learning application. All educational features and Python decision logic are preserved; only the visual theme, artwork and browser title differ.

## Theme palette

- `#CCCCFF`
- `#A3A3CC`
- `#5C5C99`
- `#292966` 

## Included features

- MATEX — Material Explorer guide
- Eight polymer profiles: Kevlar, Polyaniline, PLA, PTFE, PET, PVC, Nylon 6,6 and Polyethylene
- Application Finder: describe an application and receive a polymer suggestion; if no application keyword matches, search by a required material property
- Polymer Selector: choose requirement 1–5, get a recommendation and one-sentence scientific reason; invalid entries prompt the user to retry
- Polymer Builder: choose any of the eight polymers and a chain length from 2 to 20 repeat units; drag, reorder and remove monomer tiles; MATEX checks the sequence and explains mistakes
- Everyday Object Finder
- Interactive 3D Molecule Lab with rotate and zoom
- Random polymer facts

## Run locally on macOS

From this folder, activate your existing Python 3.8 environment if you already created one:

```bash
source .venv38/bin/activate
python -m streamlit run app.py
```

Or create an environment once and install dependencies (run these commands from this theme folder):

```bash
python3.8 -m venv .venv38
source .venv38/bin/activate
python --version  # should show Python 3.8.10
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local URL Streamlit prints, usually `http://localhost:8501`.

## Deploy online

Upload this folder's contents to its own GitHub repository. **Make sure the `polymer_builder_component` folder and its `index.html` file are committed**; the Polymer Builder needs this frontend file. In Streamlit Community Cloud, deploy `app.py` and choose **Python 3.11** in Advanced settings. Do not upload `.venv38` or `__pycache__`.

The Polymer Builder also checks for a root-level `index.html` as a fallback, which helps if an older upload placed the component file beside `polymer_builder.py`. The recommended structure remains `polymer_builder_component/index.html`.

The dependency pins in `requirements.txt` are intended for Python 3.8–3.11. Do not deploy this pinned NumPy 1.24.4 environment with Python 3.14, because that old NumPy release has no compatible Python 3.14 wheel and may attempt a source build.

## Project structure

```text
app.py
styles.py
matex.py
polymers.py
molecules.py
selector.py
polymer_builder.py
polymer_builder_component/index.html
requirements.txt
assets/  # theme artwork
```

## Scientific notes

The 3D views are simplified educational sketches, not crystallographic or scale-accurate models. The polymer builder uses simplified starting-monomer sequence challenges. Product-to-polymer matches are examples; real selection depends on grade, design, operating conditions and local requirements. Suitable PLA grades generally require controlled industrial composting conditions; ordinary soil or home compost is not guaranteed to be sufficient.
