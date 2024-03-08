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
    <img src="screenshots/title_page_screenshot.png" alt="Title Page Screenshot" style="width: 45%;">
    <img src="screenshots/contents_page_screenshot.png" alt="Contents Page Screenshot" style="width: 45%;">
</div>

<div style="display: flex; flex-wrap: wrap; justify-content: space-around;">
    <img src="screenshots/figure1.1_screenshot.png" alt="Figure 1.1 Screenshot" style="width: 45%;">
    <img src="screenshots/math_plots_screenshot.png" alt="Math Plots Screenshot" style="width: 45%;">
</div>

<div style="display: flex; flex-wrap: wrap; justify-content: space-around;">
    <img src="screenshots/code_block_screenshot.png" alt="Code Block Screenshot" style="width: 45%;">
    <img src="screenshots/bib_screenshot.png" alt="Bibliography Screenshot" style="width: 45%;">
</div>

## License

[The GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
