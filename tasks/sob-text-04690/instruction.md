Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Scincinae: Scincinae is a subfamily of lizards.  The subfamily contains 33 genera, and the genera contain a combined total of 284 species, commonly called skinks.  The systematics is at times controversial.  The group is probably paraphyletic.  It is one of three subfamilies of the family Scincidae, the other two being Acontinae and Lygosominae.

Mycetophagidae: The Mycetophagidae or hairy fungus beetles are a family of beetles in the large suborder Polyphaga.  The different species are between 1.0 and 6.5 mm in length.  The larvae and adults live in decaying leaf litter, fungi, and under bark.  Most species feed on fungi (hence the name).  Worldwide, the 18 genera contain around 200 species.

List of psilocybin mushroom species: Psilocybin mushrooms are mushrooms which contain the hallucinogenic substances psilocybin, psilocin, baeocystin and norbaeocystin.  The mushrooms are collected and grown as an entheogen and recreational drug, despite being illegal in many countries.  Many psilocybin mushrooms are in the genus "Psilocybe", but species across several other genera contain the drugs.

Erodium: Erodium is a genus of flowering plants in the botanical family Geraniaceae.  The genus includes about 60 species, native to North Africa, Indomalaya, The Middle East, and Australia.  They are perennials, annuals, or subshrubs, with five-petalled flowers in shades of white, pink, and purple, that strongly resemble the better-known "Geranium" (cranesbill).  American species are known as filarees or heron's bill, whereas Eurasian ones are usually called storksbills in English.

Dryopteridaceae: The Dryopteridaceae are a family of leptosporangiate ferns in the order Polypodiales.  They are known colloquially as the wood ferns.  They comprise about 1700 species and have a cosmopolitan distribution.  They may be terrestrial, epipetric, hemiepiphytic, or epiphytic.  Many are cultivated as ornamental plants.  The largest genera are "Elaphoglossum" (600), "Polystichum" (260), "Dryopteris" (225), and "Ctenitis" (150).  These four genera contain about 70% of the species.  Dryopteridaceae diverged from the other families in eupolypods I about 100 million years ago.

Loach catfish: The loach catfishes are a family, Amphiliidae, of catfishes (order Siluriformes).  They are widespread in tropical Africa, but are most common in streams at high elevations; most species are able to cling to rocks in fast-flowing streams.  The 13 genera contain 68 species.

Ancistroidini: The Ancistroidini are a tribe in the Hesperiinae subfamily of skipper butterflies.  They are often blackish in base color; several of the genera contain the species commonly called "demon butterflies" or "demon skippers".  As most Hesperiinae have not yet been assigned to tribes, more genera are likely to be placed into this presently rather small group eventually.

Symplocos: Symplocos is a genus of flowering plants in the order Ericales.  It contains about 300 species distributed in Asia and the Americas.  Many species grow in humid tropical regions.  This is sometimes considered to be the only genus in family Symplocaceae.  Plants in this family are shrubs and trees with white or yellow flowers.

Opiliaceae: Opiliaceae is a family of flowering plants comprising 11 genera and 33 known species.  It consists of tropical woody plants.  Several genera contain parasitic species.  The biggest genus, in number of species and in stature of the individual plants, is "Agonandra", the only American genus.

Drosophila X virus: Drosophila X virus (DXV) belongs to the "Birnaviridae" family of viruses.  "Birnaviridae" currently consists of three genera.  The first genus is "Entomobirnavirus", which contains DXV.  The next genus is "Aquabirnavirus", containing infectious pancreatic necrosis virus (IPNV).  The last genus is "Avibirnavirus", which contains infectious bursal disease virus (IBDV).  All of these genera contain homology in three specific areas of their transcripts.  The homology comes from the amino and carboxyl regions of preVP2, a small 21-residue-long domain near the carboxyl terminal of VP3, and similar small ORFs sequences.

Question: Which of the Symplocos and Erodium genera contain more species?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_type": {
      "type": "string",
      "description": "The type of comparison being made."
    },
    "genera_compared": {
      "type": "array",
      "description": "Details of the genera involved in the comparison.",
      "items": {
        "type": "object",
        "properties": {
          "genus_name": {
            "type": "string",
            "description": "The name of the genus."
          },
          "species_count": {
            "type": "integer",
            "description": "The number of species in the genus."
          }
        },
        "required": [
          "genus_name",
          "species_count"
        ],
        "additionalProperties": false
      }
    },
    "genus_with_more_species": {
      "type": "string",
      "description": "The name of the genus that contains more species."
    },
    "species_difference": {
      "type": "integer",
      "description": "The numerical difference in species count between the two genera."
    }
  },
  "required": [
    "comparison_type",
    "genera_compared",
    "genus_with_more_species",
    "species_difference"
  ],
  "additionalProperties": false
}
