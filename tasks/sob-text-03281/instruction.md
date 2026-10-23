{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAllosauridae: Allosauridae is a family of medium to large bipedal, carnivorous allosauriod neotheropod dinosaurs from the Late Jurassic and Early Cretaceous.  Allosauridae is a fairly old taxonomic group, having been first named by the American paleontologist Othniel Charles March in 1878.  Constituent groups include \"Allosaurus\", \"Erectopus\", and \"Saurophaganax\".  Many taxa, including \"Antrodemus\" and \"Epanterias\", have been at some point included as members of Allosauridae.  Originally described in 1870, Antrodemus has since been identified as a nomen dubium, and generally collapsible with \"Allosaurus\".  \"Epanterias\" has also been subject to some controversy shifting from a separate genus, to an especially large \"Allosaurus fragilis\" Allosarids are characterized by an astragalus with a restriction of the ascending process to the lateral part of the bone, a larger medial than lateral condyle, and a horizontal groove across the face of the condyles.  Allosauridae is an extremely widely dispersed family, with members discovered on every continent except Antarctica and India.\n\nVicia: Vicia is a genus of about 140 species of flowering plants that are part of the legume family (Fabaceae), and which are commonly known as vetches.  Member species are native to Europe, North America, South America, Asia and Africa.  Some other genera of their subfamily Faboideae also have names containing \"vetch\", for example the vetchlings (\"Lathyrus\") or the milk-vetches (\"Astragalus\").  The broad bean (\"Vicia faba\") is sometimes separated in a monotypic genus \"Faba\"; although not often used today, it is of historical importance in plant taxonomy as the namesake of the order Fabales, the Fabaceae and the Faboideae.  The tribe Vicieae in which the vetches are placed is named after the genus' current name.  Among the closest living relatives of vetches are the lentils (\"Lens\") and the true peas (\"Pisum\").\n\nAstragalus: Astragalus is a large genus of about 3,000 species of herbs and small shrubs, belonging to the legume family Fabaceae and the subfamily Faboideae.  It is the largest genus of plants in terms of described species.  The genus is native to temperate regions of the Northern Hemisphere.  Common names include milkvetch (most species), locoweed (in North America, some species) and goat's-thorn (\"A. gummifer\", \"A. tragacanthus\").  Some pale-flowered vetches are similar in appearance, but vetches are more vine-like.\n\nParrotia: Parrotia persica (commonly called Persian ironwood) is a deciduous tree in the family Hamamelidaceae, closely related to the witch-hazel genus \"Hamamelis\".  It is native to northern Iran and southern Azerbaijan (where it is called \"Dəmirağac\") and it is endemic in the Alborz mountains.\n\nAstragalus sinuatus: Astragalus sinuatus is a species of flowering plant in the legume family known by the common name Whited's milkvetch.  It is endemic to Washington in the United States, where it is limited to one creek drainage on the western edge of the Columbia Basin.  Its range measures about ten square miles in Chelan and Kittitas Counties in the central part of the state.\n\nQuestion: Are Astragalus and Parrotia part of the same family?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"genus_1_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the first genus in question.\"\n    },\n    \"genus_1_family\": {\n      \"type\": \"string\",\n      \"description\": \"The taxonomic family of the first genus.\"\n    },\n    \"genus_2_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the second genus in question.\"\n    },\n    \"genus_2_family\": {\n      \"type\": \"string\",\n      \"description\": \"The taxonomic family of the second genus.\"\n    },\n    \"are_same_family\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if both genera belong to the same family, false otherwise.\"\n    }\n  },\n  \"required\": [\n    \"genus_1_name\",\n    \"genus_1_family\",\n    \"genus_2_name\",\n    \"genus_2_family\",\n    \"are_same_family\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "genus_1_name": {
        "type": "string",
        "description": "The name of the first genus in question."
      },
      "genus_1_family": {
        "type": "string",
        "description": "The taxonomic family of the first genus."
      },
      "genus_2_name": {
        "type": "string",
        "description": "The name of the second genus in question."
      },
      "genus_2_family": {
        "type": "string",
        "description": "The taxonomic family of the second genus."
      },
      "are_same_family": {
        "type": "boolean",
        "description": "True if both genera belong to the same family, false otherwise."
      }
    },
    "required": [
      "genus_1_name",
      "genus_1_family",
      "genus_2_name",
      "genus_2_family",
      "are_same_family"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
