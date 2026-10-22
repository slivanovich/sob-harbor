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
Stapeliae: The genera of plants within the tribe Stapeliae are all to varying degrees stem succulents.  Many of the species resemble cacti, though are not closely related, as an example of convergent evolution.  The stems are often angular, mostly four-angled in cross-section, but in some species there are six or more, with some species of "Hoodia" having more than thirty angles.  In size they vary from less than 2.5 cm/1" in length to over 2 m/6" tall.  The leaves are in most species reduced to rudiments, sometimes hardened and thorn-like, arranged on bumps or tubercles on the angles.  Some species, however, still have recognisable leaves, most notably the Indian species "Frerea indica", and some members of "Tridentea".  Stapeliads are most abundant in warm, dry climates.  In Africa, there are two separate regions where Stapeliads have most diversified: northeast Africa, and Southern Africa.  Several species are endemic to the small island of Socotra off the Horn of Africa.  The Arabian Peninsula, and most specifically the country of Yemen, contain another concentration of species.  Several more are found in the drier parts of Pakistan, Afghanistan, India, Nepal, and Myanmar.  A single species, "Caralluma europea" is found in Europe, in the very southern part of the Iberian peninsula.  Stapeliads are often regarded as a climax group within the family because of their often structurally complex flowers. Certain aspects of these reproductive parts mirror the pollination systems in the Orchid family and represent a case of parallel evolution though both groups are quite unrelated and have developed similar, though not identical means to achieve the ultimate goal of pollination and therefore reproduction.  Most stapeliads use flies as pollinators, that are attracted to odours resembling dung or rotting meat, emanating from the flowers.  Many of the flowers also bear some physical resemblance to rotting animal carcasses, leading to their popular name of Carrion Flowers.  However, not all stapeliads smell bad, or attract flies.  Some species use beetles, bees, wasps, butterflies or moths as pollinators.  Stapeliad flowers range in size from mere millimetres in species of "Echidnopsis" and "Pseudolithos" to those of "Stapelia gigantea" that can reach 40 cm/16" in diameter, and are some the largest of flowers to be found on any species of succulent.

Echidnopsis dammaniana: Echidnopsis dammaniana is a succulent species in the genus "Echidnopsis".  The plants have angled stems and purple flowers.  It is found in Ethiopia, Kenya and Somalia and is unusual in collections.  It can be found at Gibraltar Botanic Gardens.

Lechenaultia: Lechenaultia is a genus of plants in the Goodeniaceae family.  Some species of this genus are used like ornamental plants. "Lechenaultia" species are diverse in form: they may be woody or herbaceous, upright or prostrate with leaves flat, needle-like or virtually absent in mature plants.  The genus differs from other Goodeniaceae in the structure of the stigma and the fertilization mechanism.  They are found in Australia and New Guinea (one species).

Echidnopsis: Echidnopsis is a genus of succulent, cactus-like plants in the Apocynaceae, first described as a genus in 1871.  They are native to eastern Africa and the Arabian Peninsula.

Question: Are Echidnopsis and Lechenaultia both genuses of plants? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_one_name": {
      "type": "string",
      "description": "The name of the first plant entity mentioned in the question."
    },
    "entity_one_is_genus": {
      "type": "boolean",
      "description": "True if the first entity is identified as a genus in the context."
    },
    "entity_one_family": {
      "type": "string",
      "description": "The plant family to which the first entity belongs, if specified."
    },
    "entity_two_name": {
      "type": "string",
      "description": "The name of the second plant entity mentioned in the question."
    },
    "entity_two_is_genus": {
      "type": "boolean",
      "description": "True if the second entity is identified as a genus in the context."
    },
    "entity_two_family": {
      "type": "string",
      "description": "The plant family to which the second entity belongs, if specified."
    },
    "are_both_genera": {
      "type": "boolean",
      "description": "The final answer to whether both entities are genera."
    }
  },
  "required": [
    "entity_one_name",
    "entity_one_is_genus",
    "entity_one_family",
    "entity_two_name",
    "entity_two_is_genus",
    "entity_two_family",
    "are_both_genera"
  ],
  "additionalProperties": false
}
