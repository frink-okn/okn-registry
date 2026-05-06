!!! abstract 

    The okn.us Registry is a lightweight website managed in GitHub. As a result, adding a graph to it entails adding a new page in the "[docs/registry/kgs](https://github.com/frink-okn/okn-registry/tree/main/docs/registry/kgs)" folder of [the Registry's GitHub repository](https://github.com/frink-okn/okn-registry/). In most cases you may submit a pull request with a new entry file similar to the existing files, but other customizations are also possible.

## Adding a new Registry entry

First choose a ‘shortname’ for your graph. This will be widely used as a knowledge graph identifier and as part of service URLs such as SPARQL endpoints. Keep it brief and lowercase (hyphens are okay): if your graph is all about fruit, maybe choose ‘fruitkg’.

Next create a Markdown file with that shortname (in this case, ‘fruitkg.md’) in the "docs/registry/kgs" folder. This file contains two parts: a header in YAML format ("frontmatter") and a Markdown description immediately following it.

### Registry entry frontmatter

The frontmatter, preceded and followed by a line of three hyphens ("---"), should contain the following fields as follows:

* `template`: Should always be "overrides/kg.html"; this is the template used to render the information page for your graph in the Registry.
* `shortname`: Shortname that you chose above.
* `title`: Name of the graph, used in listings of graphs within the Registry and in SPARQL interfaces.
* `description`: One-line description of what is in your graph.
* `stats`: This should be a link to `https://registry.okn.us/kg-stats/` followed by your graph's shortname.

    !!! note

        When your graph is deployed, you will already have the ability to see some statistics of entity types and predicates in your graph's information page based on data about it added to [the `okn-void` graph](https://registry.okn.us/registry/kgs/okn-void/). We do, however, have more experimental information-gathering efforts, which these `stats` pages are a reflection of.

* `homepage`: If your graph has a dedicated website, this should be a link to it.
* `funding`: If your graph is funded by an external source (such as the National Science Foundation), this should be a link to a page describing the associated award.
* `sparql`: This should be a link composed of `https://apps.okn.us/`, followed by your graph's shortname, followed by `/sparql`.

    !!! warning

        If you have *not* already uploaded data to https://repository.okn.us/ *and* triggered the conversion process ([see this documentation page for more](https://registry.okn.us/help/update/#workflows-and-processing)), then please skip this field. We will add it once your graph's individual SPARQL endpoint is up and running.

* `tpf`: This should be a link composed of `https://apps.okn.us/ldf/` followed by your graph's shortname.

    !!! warning

        If you have *not* already uploaded data to https://repository.okn.us/ *and* triggered the conversion process ([see this documentation page for more](https://registry.okn.us/help/update/#workflows-and-processing)), then please skip this field. We will add it once your graph's individual Linked Data Fragments endpoint is up and running.

* `frink-options`: This should contain two subfields, `lakefs-repo` and `documentation-path`, each of whose value should be your graph's shortname.

    !!! note

        These fields are an artifact of earlier development on the platform
        prior to the introduction of the okn.us Registry in which some inconsistencies
        in naming were introduced and changes to names were made that, due to those
        changes' inertia, did not become easily revertable. We expect that new graphs
        will use consistent naming throughout their presence in okn.us, and if the
        inconsistencies and changes are eventually addressed then these subfields
        may be removed.

* `contacts`: This is a list that should hold at least one entry for every maintainer of the graph.
The subfields in each contact entry are as follows:
    * `email`: The maintainer's contact email, to which questions about a graph may be sent.
    * `github`: The GitHub user ID for that maintainer, who may be tagged on GitHub issues concerning the graph.
    * `label`: The maintainer's preferred name.

### Registry entry description

After the frontmatter comes the Markdown description, which can be as detailed as you would like.

!!! tip

    The MCP server provided by okn.us relies on written descriptions of the content of the graphs,
    such as the one in this file, in addition to the statistics in the [the `okn-void` graph](https://registry.okn.us/registry/kgs/okn-void/)
    and any metadata in the RDF about entity types and predicates the graph uses. It is therefore
    to your advantage to have a good prose characterization here of what your graph does and provides.

### Finishing up

The end result should look something like this:

!!! example "fruitkg.md"

    ``` markdown
    ---
    template: overrides/kg.html
    shortname: fruitkg
    title: Fruit KG
    description: A knowledge graph of fruits
    stats: https://registry.okn.us/kg-stats/fruitkg
    homepage: https://geocities.com/fruitkg
    funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=XXXX
    sparql: https://apps.okn.us/fruitkg/sparql
    tpf: https://apps.okn.us/ldf/fruitkg
    frink-options:
      lakefs-repo: fruitkg
      documentation-path: fruitkg
    contacts:
      - email: mrfruit@aol.com
        github: fruitguy
        label: "John Fruit"
      - email: mrsjuice@yahoo.com
        github: juicelady
        label: "Mary Juice"
    ---

    This is a wonderful knowledge graph describing everything about fruit.
    It extends from a number of existing well-known ontologies:

    * Food Ontology (FoodOn)
    * NCI Thesaurus OBO Edition (NCIt)
    * General Finnish Ontology (YSO)
    * Art and Architecture Thesaurus (AAT)
    * National Library of Korea Subject Headings (KSH)

    We have discovered a truly marvelous proof of this graph's completeness,
    which this Markdown file is too small to contain.
    ```

Once you have saved this file, open a pull request for the addition of your graph entry file to the Registry.

## Updating an existing Registry entry

Any updates to data in the Registry may be made in the same manner as adding them, with a pull request containing an edited entry file.
