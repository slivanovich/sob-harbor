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
Cladorhiza segonzaci: Cladorhiza segonzaci is a species of sponge in the taxonomic category of Demospongiae.  The body of the sponge consists of a spicule and fibers and is water absorbent.

Aptera: Aptera is an obsolete taxonomic category, which included the Apterygota along with various other wingless arthropods.

Heterostropha: Heterostropha was a previously used taxonomic category, an order of sea snails, within the superorder Heterobranchia.  In the most current gastropod taxonomy, that of Bouchet & Rocroi, this taxon is no longer in use.

Sigmurethra: Sigmurethra is a taxonomic category of air-breathing land snails and slugs, terrestrial pulmonate gastropod molluscs.  This is an informal group which includes the majority of land snails and slugs.

Helleborine: Helleborine is the common name for a number of species of orchid.  It does not correspond to any currently used taxonomic category.  Some of the plants called helleborines are classified in the genus "Epipactis", some in genus "Cephalanthera".  A genus "Helleborine" was formerly recognised but has now been absorbed into the Grass pink genus "Calapogon".

Gammaridae: Gammaridae is a family of amphipods.  In North America they are included among the folk taxonomic category of "scuds", and otherwise gammarids is usually used as a common name.

Austrocylindropuntia: Austrocylindropuntia is a genus of cacti (family Cactaceae) with 11 recognized species, which were once included in the genus "Opuntia".  Some are native to South America.

Cladorhiza inversa: Cladorhiza inversa is a species of sponge in the taxonomic category of Demospongiae.  The body of the sponge consists of a spicule and fibers and is water absorbent.

Ceratopteris: Ceratopteris is the only genus among homosporous ferns that is exclusively aquatic.  It is pan-tropical and classified in the Ceratopteridoideae subfamily of the Pteridaceae.

Eogastropoda: Eogastropoda was a previously used taxonomic category of snails or gastropods, a subclass which was erected by Ponder and Lindberg in 1997.  It was one of two great divisions (subclasses) of the class Gastropoda, the snails.  The other subclass of gastropods was the Orthogastropoda.

Question: Austrocylindropuntia and Ceratopteris are both examples of what taxonomic category?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_names": {
      "type": "array",
      "description": "The names of the entities for which a common taxonomic category is sought.",
      "items": {
        "type": "string"
      }
    },
    "shared_taxonomic_level": {
      "type": "string",
      "description": "The common taxonomic category that both entities belong to."
    },
    "is_current_category": {
      "type": "boolean",
      "description": "Indicates whether the identified taxonomic category is currently recognized."
    }
  },
  "required": [
    "entity_names",
    "shared_taxonomic_level",
    "is_current_category"
  ],
  "additionalProperties": false
}
