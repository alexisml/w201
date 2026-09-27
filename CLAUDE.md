# W201 logbook — repo rules

A logbook for a Mercedes-Benz 190 E 2.3 8V (W201, variant 201.028, engine M102.985).
It holds no code, only Markdown notes and images organized in topic folders. See README.md for
the layout and conventions.

## Private data

The VIN and engine number are kept only in `.env`, which is git-ignored. Never write them into any
tracked file. Facts derived from them (model year, market, and so on) may be recorded.

## Saving links

References disappear over time, so every link we add gets a saved copy:

1. Keep the original link.
2. If the Internet Archive (web.archive.org) has a complete copy with text and pictures, add that link too.
3. If it doesn't, save a copy: the page as a PDF, its pictures in the best quality available, and a
   short `README.md` with the original link, the archive link if any, the date saved, and what's
   included.
4. Link the saved copy next to the original.
5. If a page can't be saved, mark it **not archived** in the entry.

### Where copies go

This repo is public. Full copies of other people's work live in the private repo
[w201-private](https://github.com/alexisml/w201-private), at the same path
(`<topic>/references/<short-name>/`). Locally it is cloned next to this one, in `../w201-private`.

In this repo each reference keeps only its `README.md`, with the links and the line
**"Full copy: kept in the private archive. Available on request."**

### What is public (fair use)

- Our own notes, photos and measurements
- Facts: part numbers, option codes, specs, cross-references (copies that contain only factual
  data may be published)
- Short quotes with attribution
- Links to originals and to Internet Archive copies

Full articles, forum threads, product pages and third-party photos stay in the private repo. They
are kept only to preserve the reference, the way the Internet Archive does, and are shared on request.
Always credit the source and link the original first. All rights stay with the original authors and
owners. Only save content that is openly available.

## Facts

Only record verified facts about this car as facts. Mark researched or general info with its
confidence level and source.
