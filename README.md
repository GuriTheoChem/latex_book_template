# LaTex Book Template

GitHub repository for a template latex book.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/GuriTheoChem/latex_book_template?include_prereleases)](https://github.com/GuriTheoChem/latex_book_template/releases)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/GuriTheoChem/latex_book_template/.github%2Fworkflows%2Frelease.yml)
![GitHub forks](https://img.shields.io/github/forks/GuriTheoChem/latex_book_template)
![GitHub Repo stars](https://img.shields.io/github/stars/GuriTheoChem/latex_book_template)

## Building the PDF of the Book

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

![title page screenshot](screenshots/title_page_screenshot.png)

## License

[The GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
