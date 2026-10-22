# Compiled arXiv v1 manuscripts

PDFs in this directory are built from the immutable arXiv v1 sources indexed in [papers.json](../../papers.json). Each PDF corresponds to a specific source archive recorded in the paper's SOURCE.md. The build script writes `manifest.json` with hashes and page counts. See the [top-level README](../../README.md) for PDF, source, and external preprint links.

Build: `make pdf`. Verify committed files: `make check`.
