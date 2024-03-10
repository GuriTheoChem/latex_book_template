# PhD Thesis Template

GitHub repository for a PhD Thesis template using LaTex.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/GuriTheoChem/phd-thesis-template?include_prereleases)](https://github.com/GuriTheoChem/phd-thesis-template/releases)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/GuriTheoChem/phd-thesis-template/.github%2Fworkflows%2Frelease.yml)
![GitHub forks](https://img.shields.io/github/forks/GuriTheoChem/phd-thesis-template)
![GitHub Repo stars](https://img.shields.io/github/stars/GuriTheoChem/phd-thesis-template)

## Using the Template

Read this [article](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) from GitHub Docs on how to create a repository from a template.

1. Click Use this template button and select Create a new repository.

   <img src="images/use_this_template.png" alt="use this template" style="width: 45%;">

2. Select with which account you want to create the repository and give it a name.

3. Check out any additional options you want to incorporate.

4. Click Create Repository and you are all set.

## Building the PDF of the Thesis

- To build the pdf of the Thesis, execute the following.

    ```{bash}
    latexmk -pdf -output-directory=build src/main.tex
    ```

    This builds the pdf in the `build/` directory under the file name `main.pdf`.

    > Note: I use `latexmk` for an automated compilation of this template pdf as it has cross-references(bibliography, table of contents). I do not test any other compilers. Please read more about choosing a compiler on this overleaf [article](https://www.overleaf.com/learn/latex/Choosing_a_LaTeX_Compiler#TeX_distributions).

- To build the plots:

    ```{bash}
    python3 src/generate_plots.py
    ```

- To get the pdf of a particular release version, go to the release and find it in the assets.

## Screenshots

<div style="display: flex; flex-wrap: wrap; justify-content: space-around;">
    <img src="images/main-01.png" alt="main-01" style="width: 45%;">
    <img src="images/main-06.png" alt="main-06" style="width: 45%;">
</div>

<div style="display: flex; flex-wrap: wrap; justify-content: space-around;">
    <img src="images/main-15.png" alt="main-15" style="width: 45%;">
    <img src="images/main-17.png" alt="main-17" style="width: 45%;">
</div>

<div style="display: flex; flex-wrap: wrap; justify-content: space-around;">
    <img src="images/main-21.png" alt="main-21" style="width: 45%;">
    <img src="images/main-24.png" alt="main-24" style="width: 45%;">
</div>

<div style="display: flex; flex-wrap: wrap; justify-content: space-around;">
    <img src="images/main-25.png" alt="main-25" style="width: 45%;">
    <img src="images/main-31.png" alt="main-31" style="width: 45%;">
</div>

## License

[The GNU General Public License v3.0](LICENSE)
