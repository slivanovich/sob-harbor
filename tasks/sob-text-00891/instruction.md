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
Sigmurethra: Sigmurethra is a taxonomic category of air-breathing land snails and slugs, terrestrial pulmonate gastropod molluscs.  This is an informal group which includes the majority of land snails and slugs.

Tithonia: Tithonia is a genus of flowering plants in the sunflower tribe within the Asteraceae family.

Eogastropoda: Eogastropoda was a previously used taxonomic category of snails or gastropods, a subclass which was erected by Ponder and Lindberg in 1997.  It was one of two great divisions (subclasses) of the class Gastropoda, the snails.  The other subclass of gastropods was the Orthogastropoda.

Cladorhiza segonzaci: Cladorhiza segonzaci is a species of sponge in the taxonomic category of Demospongiae.  The body of the sponge consists of a spicule and fibers and is water absorbent.

Helleborine: Helleborine is the common name for a number of species of orchid.  It does not correspond to any currently used taxonomic category.  Some of the plants called helleborines are classified in the genus "Epipactis", some in genus "Cephalanthera".  A genus "Helleborine" was formerly recognised but has now been absorbed into the Grass pink genus "Calapogon".

Aptera: Aptera is an obsolete taxonomic category, which included the Apterygota along with various other wingless arthropods.

Pachysandra: Pachysandra is a genus of five species of evergreen perennials or subshrubs, belonging to the boxwood family Buxaceae.  The species are native to eastern Asia and southeast North America, some reaching a height of 20 - , with only weakly woody stems.  The leaves are alternate, leathery, with an entirely too coarsely toothed margin, and are typically 5 - long.  The small uni-sexual blooms are greenish-white and produced in late spring or early summer.

Cladorhiza inversa: Cladorhiza inversa is a species of sponge in the taxonomic category of Demospongiae.  The body of the sponge consists of a spicule and fibers and is water absorbent.

Heterostropha: Heterostropha was a previously used taxonomic category, an order of sea snails, within the superorder Heterobranchia.  In the most current gastropod taxonomy, that of Bouchet & Rocroi, this taxon is no longer in use.

Gammaridae: Gammaridae is a family of amphipods.  In North America they are included among the folk taxonomic category of "scuds", and otherwise gammarids is usually used as a common name.

Question: Do both Tithonia and Pachysandra belong to the taxonomic category of genus?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "is_both_genus": {
      "type": "boolean",
      "description": "True if both entities belong to the taxonomic category of genus, false otherwise."
    },
    "entity_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first entity."
        },
        "taxonomic_category": {
          "type": "string",
          "description": "The taxonomic category of the first entity."
        }
      },
      "required": [
        "name",
        "taxonomic_category"
      ],
      "additionalProperties": false
    },
    "entity_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second entity."
        },
        "taxonomic_category": {
          "type": "string",
          "description": "The taxonomic category of the second entity."
        }
      },
      "required": [
        "name",
        "taxonomic_category"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "is_both_genus",
    "entity_1",
    "entity_2"
  ],
  "additionalProperties": false
}
