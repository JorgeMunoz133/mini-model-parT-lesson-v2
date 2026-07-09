# Building a Simplified Particle Transformer for CMS Jet Classification

This is a lesson built with [The Carpentries Workbench][workbench]. It
teaches MiniParT, a simplified Particle Transformer that classifies pairs
of jets from CMS Open Data as Hbb, Hcc, or QCD background, entirely inside
Google Colab. It follows the Notre Dame CMS Open Data Workshop lesson
format.

The built lesson site is published at:
**https://JorgeMunoz133.github.io/mini-model-parT-lesson/**

## Note about lesson life cycle stage

This lesson's `config.yaml` currently lists the life cycle stage as
`pre-alpha`, meaning it is newly created and has not yet been taught or
reviewed. See <https://docs.carpentries.org/resources/curriculum/lesson-life-cycle.html>
for what each life cycle stage means.

## Episodes

1. The Big Picture
2. Working in Google Colab
3. What Is a Jet?
4. Finding the Truth Labels
5. Preparing the Data
6. Building MiniParT
7. Training the Model
8. Evaluating the Model
9. The Complete Code

## The data

This lesson uses three CMS Open Data files, released publicly by CERN
under a CC0 (public domain) license, streamed directly from CERN's
servers rather than downloaded:

- ttHTobb (Hbb signal) - [CERN Open Data record 67645](https://opendata.cern.ch/record/67645)
- ttHTocc (Hcc signal) - [CERN Open Data record 67651](https://opendata.cern.ch/record/67651)
- QCD_bcToE (background) - [CERN Open Data record 63242](https://opendata.cern.ch/record/63242)

See the [Working in Google Colab](episodes/02-colab-and-data-access.md)
episode for the exact files used and how streaming works.

## Building the lesson locally

This repository uses [The Carpentries Workbench][workbench] (`{sandpaper}`)
to build and preview the lesson site. With R and the `sandpaper` package
installed, you can preview the lesson locally with:

```r
sandpaper::serve()
```

See the [Introduction to The Carpentries Workbench][workbench] for full
documentation on editing, building, and contributing to lessons built with
this tool.

## Contributing

We welcome all contributions to improve the lesson! Maintainers will
retain the final decision about which suggestions are incorporated. For
more information on contributing to this lesson, see `CONTRIBUTING.md`.

## Citation

To cite this lesson, please see `CITATION.cff`.

[workbench]: https://carpentries.github.io/sandpaper-docs/
