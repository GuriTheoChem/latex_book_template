# Changelog

All notable changes to this project will be documented in this file.

## phd-thesis-template v2.4.0 - March 11, 2024

### Added

- Index in the thesis using imakeidx package of latex

### Changed

- pdf bookmark structure

  - the bibliography and subsequent matter appeared under the part-2 level in previous versions. Now they appear outside of part-2.

- Modified figure referencing title

  - When the figure is referenced, it would appear as `Figure x.y`

- Modified [README.md](README.md)

  - Added a separate section for Plots.

## phd-thesis-template v2.3.0 - March 10, 2024

### Added

- Color-blind friendly color palette for the plots in [generate_plots.py](src/generate_plots.py)
- GitHub themed Code Snippet Block (light and dark version) in [preamble.tex](src/contents/latex_doc_preamble/preamble.tex)
- More Acronyms and Mathematical Symbols

### Changed

- the plots were generated using the color-blind palette
- latest screenshots in [README.md](README.md)

## phd-thesis-template v2.2.0 - March 10, 2024

### Added

- Using the template instructions in [README.md](README.md)

### Changed

- modified Code Blocks rulecolor to match the background color
- Warning Note on latexmk compiler usage in [README.md](README.md)

## phd-thesis-template v2.1.0 - March 9, 2024

### Added

- Table Sample
- Table of Contents Font Changing lines in Preamble
- 3 new Plots and Graphs examples
- PDF Screenshots in [README.md](README.md)

### Changed

- Code Blocks
  - Changed Dracula Theme formatting
  - Added a python-dracula and changed cpp-dracula theme
  - Changed code block example

### Removed

- 2 Older example Plots and Graphs

## phd-thesis-template v2.0.0 - March 8, 2024

- Renamed Repository to phd-thesis-template

### Added

- [LICENSE](LICENSE)

### Changed

- [README.md](README.md)
- Github Actions workflow release headings changed to `phd-thesis-template v.x.y.z`

## latex-book-template v1.1.0 - March 7, 2024

### Added

- Issue Template

## latex-book-template v1.0.0 - March 7, 2024

- 1st working release

### Added

- Appendix
- List of Symbols
- List of Acronyms
- Code Blocks
- latest pdf in the build folder

### Changed

- Formatting of Heading is done with sans-serif
- GitHub Actions workflow release headings changed to `latex-book-template v.x.y.z`

## latex-book-template v0.1.0 - February 11, 2024

### Added

- Basic Framework and File Structure of the document
