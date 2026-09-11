# Contributing

Thanks for helping keep this list accurate and useful.

## How the list is built

`README.md` and `manifest.json` are **generated** from live GitHub metadata by
`build_awesome.py`. Nothing is hand-written into the tables, so entries always
carry real star counts, license identifiers and last-push dates.

Quality gate applied to every candidate:

- not archived, not a fork
- at least 150 stars
- has a non-empty description
- unique across sections (first section wins)

## Suggesting a project

Open an issue with the **Suggest a project** template and include:

1. Repository URL
2. Which section it belongs to
3. One sentence explaining what problem it solves in an agent/LLM stack

A maintainer will add the matching topic to the candidate query if the project
genuinely belongs in the list. Projects that are closed-source wrappers,
abandoned, or pure marketing sites are rejected.

## Adding a new section

Sections map one-to-one onto a GitHub topic in `SECTIONS` inside
`build_awesome.py`. If you want a new section, open a PR that:

1. adds the section title and its GitHub topic,
2. refreshes the generated files with `python3 build_awesome.py`,
3. keeps the README structure (Contents list, `---` separators, tables).

## License of contributions

By contributing you agree your changes are released under the MIT License.
