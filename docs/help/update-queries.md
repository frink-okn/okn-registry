# Updating User Queries on the Frink UI Page

This document outlines the process for updating the example user queries that appear on the Frink UI page.

## Overview

The example queries displayed in the Frink UI are fetched from the [frink-okn/okn-registry](https://github.com/frink-okn/okn-registry/tree/main/docs/registry/queries) GitHub repository. To add or modify these queries, you will need to create or edit `.rq` files within a `docs/registry/queries` in that repository.

## How to Update Queries

1.  **Navigate to the Correct Repository and Directory:**
    * Go to the `frink-okn/okn-registry` repository on GitHub.
    * Inside this repository, locate the `/docs/registry/queries/` directory.

2.  **Create or Edit `.rq` Files:**
    * **New Queries:** To add a new example query, create a new file with the `.rq` extension (e.g., `my_new_query.rq`) within the `/docs/registry/queries/` directory or any subfolder you create within it.
    * **Existing Queries:** To modify an existing query, locate the relevant `.rq` file in this directory and edit it.
    * **File Content:** Each `.rq` file should contain **only one** SPARQL query.

3.  **Add Metadata:**
    * At the very top of each `.rq` file, you must include a metadata block.
    * This block consists of lines starting with `#+ `.
    * The content within this block is parsed as YAML and must be valid.
    * The UI currently expects two specific metadata fields:
        * `#+ summary: "Your concise description of what the query does."` (This should be a string.)
        * `#+ tags: ["tag1", "tag2", "another_tag"]` (This should be an array of strings.)
    * **Tags:** The `tags` should reference the knowledge graph `shortname` as defined in [this YAML file](https://github.com/frink-okn/okn-registry/blob/main/docs/registry/kgs.yaml).

    **Example `.rq` File Structure:**

    ```sparql
    #+ summary: "Fetches all unique classes in the knowledge graph."
    #+ tags: ["geoconnex", "sockg"]

    SELECT DISTINCT ?class
    WHERE {
      ?s a ?class .
    }
    LIMIT 100
    ```

4.  **Organizing Queries (Optional):**
    * You can organize your `.rq` files into subfolders within the `/docs/registry/queries/` directory (e.g., based on the primary data source or query type).
    * The UI scans the entire `/docs/registry/queries/` directory and its subdirectories for `.rq` files, so the specific folder structure within `queries` is for organizational purposes and does not affect how the UI discovers the queries.

## Important Notes on Caching

* **Browser Caching:** The Frink UI caches requests to GitHub for **24 hours** in the browser's local storage. This means that newly added or updated queries might not appear immediately for all users.
* **Invalidating Cache (for Maintainers):**
    * To see changes immediately (primarily for maintainers verifying updates), a "invalidate cache" button is available on the settings page of the Frink UI.
    * **Deployment Note:** This cache invalidation feature may not yet be deployed on the Sterling instance. To use it, you will need to test on the GitHub Pages deployment: [https://frink-okn.github.io/frink-query-ui](https://frink-okn.github.io/frink-query-ui).


## Summary of Process

1.  Go to `frink-okn/okn-registry` repository.
2.  Navigate to `/docs/registry/queries/`.
3.  Create/edit `.rq` files (one query per file).
4.  Add `summary` and `tags` metadata at the top of each file using `#+ ` prefix.
5.  Commit and push your changes.
6.  If verifying, use the GitHub Pages deployment and the "invalidate cache" button in settings if needed.

---

If you have any further questions, please  contact "okn-frink at renci.org" 