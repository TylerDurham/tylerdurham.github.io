# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Role

This is the **GitHub Pages deployment repository** for `TylerDurham.github.io`. It contains only pre-built static HTML — do not edit content files here directly.

The Hugo source lives at `../blog/` (sibling directory). All content authoring, theming, and layout changes happen there.

## Structure

- `index.html` — Root landing page (hand-authored, not Hugo-generated)
- `bits-n-being/` — Hugo-generated static site output, built from `../blog/` with `hugo --minify`

## Workflow

To update the site, work in `../blog/` and run:

```bash
hugo --minify                # Builds to ../blog/public/
```

Then copy or sync `../blog/public/` into `bits-n-being/` here and commit. Pushing `main` deploys to GitHub Pages.

See `../blog/CLAUDE.md` for full details on content types, custom layouts, and the snippet system.
