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
Thelymitra: Thelymitra, commonly known as sun orchids, is a genus of more than 100 species of plants in the orchid family, Orchidaceae.  Unlike most other orchids, sun orchids lack a highly modified labellum and all three petals are similar in size, shape and colour.  The column is, however highly modified and usually has prominent wings or glands which are helpful in identifying the species.  Most sun orchids close their flowers at night, in cloudy or cool weather, giving rise to their common name.  The scientific name means "woman's hood" and refers to the hooded column present in most, but not all species.  Most species are endemic to Australia although some are found as far from there as the Philippines and Indonesia.  The type species, "Thelymitra longifolia", the first to be formally described, was collected in New Zealand.

Coelia: Coelia is a genus of orchids (family Orchidaceae, tribe Epidendreae, subtribe Coeliinae).  It contains 5 species, native to Mexico, Central America and the West Indies.

Paracaleana: Paracaleana commonly known as duck orchids, is a genus of flowering plants in the orchid family, Orchidaceae that is found in Australia and New Zealand.  The Australian species are found in all states but have not been recorded in the Northern Territory.  Orchids in this genus are similar to "Caleana major", but there are differences in the flowers and in the insects that pollinate them.  "Paraceleana" orchids, as well as hammer orchids ("Drakaea") are pollinated by male thynnid wasps.  Duck orchids have a single leaf and one or a few, dull-coloured, inconspicuous flowers.

Caladenia: Caladenia, commonly known as spider orchids, is a genus of 350 species of plants in the orchid family, Orchidaceae.  Spider orchids are terrestrial herbs with a single hairy leaf and a hairy stem.  The labellum is fringed or toothed in most species and there are small projections called calli on the labellum.  The flowers have adaptations to attract particular species of insects for pollination.  The genus is divided into three groups on the basis of flower shape, broadly, spider orchids, zebra orchids and cowslip orchids, although other common names are often used.  Although they occur in other countries, most are Australian and 136 species occur in Western Australia, making it the most species-rich orchid genus in that state.

Platanthera: The genus Platanthera belongs to the subfamily Orchidoideae of the family Orchidaceae, and comprises about 100 species of orchids.  The members of this genus, known as the butterfly orchids or fringed orchids, were previously included in the genus "Orchis", which is a close relative (along with the genus "Habenaria").  They are distributed throughout the temperate regions of the Northern Hemisphere.  They are terrestrial and have tubercules.

Calochilus: Calochilus, commonly known as beard orchids, is a genus of about 30 species of plants in the orchid family, Orchidaceae.  Beard orchids are terrestrial, herbs with a single leaf at the base of the plant, or no leaves.  Their most striking feature is a densely hairy labellum, giving rise to their common name.  Beard orchids, unlike some other Australian orchids, do not reproduce using daughter tubers, but self-pollinate when cross-pollination has not occurred.  Most species occur in Australia but some are found in New Zealand, New Guinea and New Caledonia.

Coelia (disambiguation): Coelia is a genus of orchids.

Genoplesium: Genoplesium commonly known as midge orchids, is a genus of about 50 species of flowering plants in the orchid family, Orchidaceae and is found in Australia, New Zealand and New Caledonia.  Midge orchids are terrestrial herbs with a single leaf at the base of the plant.  They are similar to orchids in the genus "Prasophyllum" in that plants without flowers have a hollow, onion-like leaf.  The flowers are small but often scented and attractive to their insect pollinators.  There is disagreement about which species belong to this genus and some taxonomists suggest that most belong in the genus "Corunastylis".

Hakonechloa: "Hakonechloa is a genus of bunchgrass in the Molinieae tribe of the Poaceae family (grasses), native to eastern Asia.

Microtis (plant): Microtis, commonly known as onion orchids or mignonette orchids is a genus of about 20 species of plants in the orchid family, Orchidaceae.  Onion orchids are terrestrial herbs with a single leaf at the base of the plant.  They are similar to orchids in the genus "Prasophyllum" in that they have an onion-like leaf.  The flowers are small but often scented and attractive to their insect pollinators.  They are widespread in Asia, Australia and some Pacific islands.

Question: Are both Coelia and Hakonechloa a genus of orchids?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "is_both_orchid_genera": {
      "type": "boolean",
      "description": "True if both specified genera are orchid genera, false otherwise."
    },
    "genera_checked": {
      "type": "array",
      "description": "Details for each genus checked.",
      "items": {
        "type": "object",
        "properties": {
          "genus_name": {
            "type": "string",
            "description": "The name of the genus."
          },
          "is_orchid": {
            "type": "boolean",
            "description": "True if the genus belongs to the Orchidaceae family, false otherwise."
          },
          "plant_family": {
            "type": "string",
            "description": "The plant family the genus belongs to."
          }
        },
        "required": [
          "genus_name",
          "is_orchid",
          "plant_family"
        ],
        "additionalProperties": false
      }
    },
    "conclusion_reasoning": {
      "type": "string",
      "description": "Explanation for the conclusion based on the findings."
    }
  },
  "required": [
    "is_both_orchid_genera",
    "genera_checked",
    "conclusion_reasoning"
  ],
  "additionalProperties": false
}
