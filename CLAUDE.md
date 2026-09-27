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
3. If it doesn't, save a copy in `<topic>/references/<short-name>/`:
   - the page as a PDF
   - its pictures, in the best quality available, in `images/`
   - a short `README.md` with the original link, the archive link if any, the date saved, and
     what's included
4. Link the saved copy next to the original.
5. If a page can't be saved, mark it **not archived** in the entry.

**Saved copies are kept local:** the `references/` folders are git-ignored because this repo is public.
Only the notes are pushed, so links to saved copies work locally but not on GitHub.

### Fair use

Saved copies exist only to preserve references, the same way the Internet Archive does. They are
not republications. Always credit the source and link the original first. All rights stay with the
original authors and owners. Only save content that is openly available.

## Facts

Only record verified facts about this car as facts. Mark researched or general info with its
confidence level and source.
