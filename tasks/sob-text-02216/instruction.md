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
Verticordia sect. Verticordia: Verticordia" sect.  "Verticordia is one of eleven sections in the subgenus "Verticordia".  It includes eight species of plants in the genus "Verticordia".  Plants in this section are open to bushy shrubs up to 1 m tall with needle-like leaves, feather-like sepals and anthers opening by slanting pores.  When Johannes Conrad Schauer described other subgenera in "Verticordia", subgenus "Verticordia" became an autonym after Augustin de Candolle who described the genus in 1828.  When Alex George reviewed the genus in 1991, he took the name of this section from that of the subgenus.

Verticordia sect. Corymbiformis: Verticordia" sect.  "Corymbiformis is one of eleven sections in the subgenus "Verticordia".  It includes five species of plants in the genus "Verticordia".  Plants in this section are mostly compact shrubs 0.3-1 m tall with a constricted floral cup, fringed or divided sepal lobes and dense heads of small flowers.  When Alex George reviewed the genus in 1991 he formally described this section, publishing the description in the journal Nuytsia.  The name "Corymbiformis" is derived from the Latin word "corymbus" meaning "a bunch of flowers" and the suffix "-formis" meaning "shaped" referring to the flower arrangement of the species in this section.

Verticordia sect. Infuscata: Verticordia" sect.  "Infuscata is one of eleven sections in the subgenus "Verticordia".  It includes two species of plants in the genus "Verticordia".  Plants in this section are small shrubs with greyish foliage, unusual flowers and an odour of mice.  The floral cup has a tuft of hairs around its base, dull purple or cream-coloured flowers with divided sepals and petals with a transparent margin.  When Alex George reviewed the genus in 1991 he formally described this section, publishing the description in the journal Nuytsia.  The name "Infuscata" is derived from the Latin word "fusca" meaning "dark" or "dusky" referring to the dullish colour of plants in this section.

Verticordia subg. Verticordia: Verticordia" subg.  "Verticordia is a botanical name for a grouping of similar plant species in the genus "Verticordia".  This subgenus contains eleven sections, classifying thirty six species, of Alex George's infrageneric arrangement.  A number of anatomical features differentiate the contained species from the other two subgenera.

Ericaceae: The Ericaceae are a family of flowering plants, commonly known as the heath or heather family, found most commonly in acid and infertile growing conditions.  The family is large, with c. 4250 known species spread across 124 genera, making it the 14th most species-rich family of flowering plants.  The many well-known and economically important members of the Ericaceae include the cranberry, blueberry, huckleberry, rhododendron (including azaleas), and various common heaths and heathers ("Erica", "Cassiope", "Daboecia", and "Calluna" for example).

Verticordia sect. Pilocosta: Verticordia" sect.  "Pilocosta is one of eleven sections in the subgenus "Verticordia".  It includes three species of plants in the genus "Verticordia".  Plants in this section are mostly small, bushy shrubs greyish, needle-like leaves and hairy, rather than feathery flowers.  Plants in this section have a flower cup with 10 hairy ribs, fringed sepals and a style which is hairy and has a distinct cap.  When Alex George reviewed the genus in 1991 he formally described this section, publishing the description in the journal Nuytsia.  The name "Pilocosta" is from the Latin words "pilus" meaning "hair" and "costa" meaning "rib" referring to the hairy ribs on the floral cup.

Verticordia sect. Penicillaris: Verticordia" sect.  "Penicillaris is one of eleven sections in the subgenus "Verticordia".  It includes two species of plants in the genus "Verticordia".  Plants in this section are small, rounded shrubs with tiny leaves and sticky flowers.  Like those in section "Micrantha", the plants often smell faintly of mice.  When Alex George reviewed the genus in 1991 he formally described this section, publishing the description in the journal Nuytsia.  The name "Penicillaris" is from the type species from this section.

Verticordia sect. Micrantha: Verticordia" sect.  "Micrantha is one of eleven sections in the subgenus "Verticordia".  It includes three species of plants in the genus "Verticordia".  Plants in this section small shrubs with tiny flowers smelling faintly like mice.  The floral cup has five ribs on its sides.  When Alex George reviewed the genus in 1991 he formally described this section, publishing the description in the journal Nuytsia The name "Micrantha" is derived from the Ancient Greek "mikros" meaning "small" and "anthos" meaning "flower" in reference to the small flowers of plants in this section.

Verticordia sect. Elachoschista: Verticordia" sect.  "Elachoschista is one of eleven sections in the subgenus "Verticordia".  It includes a single species in the genus "Verticordia".  Plants in this section resemble those in section "Infuscata" except that the sepal lobes are not divided but may have an irregularly toothed edge.  Plants in this section superficially resemble some of the smaller "Darwinia" species.  The leaves are crowded and the flower are cream-coloured, turning greenish-brown as they age.  When Alex George reviewed the genus in 1991 he formally described this section, publishing the description in the journal Nuytsia.  The name "Elachoschista" is derived from the Ancient Greek words "elachys" meaning "little" and "schizo" meaning "cut" referring to the sepals which have almost smooth edges.

Verticordia: Verticordia is a genus of more than 100 species of plants commonly known as featherflowers, in the myrtle family, Myrtaceae.  They range in form from very small shrubs such as "V. verticordina" to trees like "V. cunninghamii", some spindly, others dense and bushy, but the majority are woody shrubs up to 2.0 m tall.  The flowers are variously described as "feathery", "woolly" or "hairy" and are found in most colours except blue.  They often appear to be in rounded groups or spikes but in fact are always single, each flower borne on a separate stalk in a leaf axil.  Each flower has five sepals and five petals all of a similar size with the sepals often having feathery or hairy lobes.  There are usually ten stamens alternating with variously shaped staminodes.  The style is simple, usually not extending beyond the petals and often has hairs near the tip.  All but two species are found in Southwest Australia, the other two occurring in the Northern Territory.

Question: Which group of plants contains more species, Verticordia or Ericaceae?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_groups": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "group_name": {
            "type": "string",
            "description": "The name of the plant group."
          },
          "species_count": {
            "type": "integer",
            "description": "The approximate number of species in the group."
          },
          "count_description": {
            "type": "string",
            "description": "A descriptive phrase for the species count if not an exact number."
          }
        },
        "required": [
          "group_name",
          "species_count"
        ],
        "additionalProperties": false
      },
      "minItems": 2,
      "maxItems": 2
    },
    "group_with_more_species": {
      "type": "string",
      "description": "The name of the group that contains more species."
    },
    "comparison_result": {
      "type": "string",
      "description": "A statement summarizing which group has more species."
    }
  },
  "required": [
    "comparison_groups",
    "group_with_more_species",
    "comparison_result"
  ],
  "additionalProperties": false
}
