# PhD Thesis Template

GitHub repository for a PhD Thesis template using LaTex.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/GuriTheoChem/phd-thesis-template?include_prereleases)](https://github.com/GuriTheoChem/phd-thesis-template/releases)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/GuriTheoChem/phd-thesis-template/.github%2Fworkflows%2Frelease.yml)
![GitHub forks](https://img.shields.io/github/forks/GuriTheoChem/phd-thesis-template)
![GitHub Repo stars](https://img.shields.io/github/stars/GuriTheoChem/phd-thesis-template)

## Building the PDF of the Thesis

- To build the pdf of the Thesis, execute the following.

    ```{bash}
    latexmk -pdf -output-directory=build src/main.tex
    ```

    This builds the pdf in the `build/` directory under the file name `main.pdf`.

- To build the plots:

    ```{bash}
    python3 src/generate_plots.py
    ```

- To get the pdf of a particular release version, go to the release and find it in the assets.

## Screenshots

<div style="display: flex; flex-wrap: wrap; justify-content: space-around;">
    <img src="images/main-01.png" alt="main-01.png" style="width: 45%;">
    <img src="images/main-06.png" alt="main-06" style="width: 45%;">
</div>

<div style="display: flex; flex-wrap: wrap; justify-content: space-around;">
    <img src="images/main-15.png" alt="main-15.png" style="width: 45%;">
    <img src="images/main-17.png" alt="main-17" style="width: 45%;">
</div>

<div style="display: flex; flex-wrap: wrap; justify-content: space-around;">
    <img src="images/main-21.png" alt="main-21.png" style="width: 45%;">
    <img src="images/main-24.png" alt="main-24" style="width: 45%;">
</div>

<div style="display: flex; flex-wrap: wrap; justify-content: space-around;">
    <img src="images/main-25.png" alt="main-25.png" style="width: 45%;">
    <img src="images/main-31.png" alt="main-31" style="width: 45%;">
</div>

## License

[The GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
