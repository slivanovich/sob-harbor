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
Acorn squash: Acorn squash ("Cucurbita pepo" var.  turbinata), also called pepper squash or Des Moines squash, is a winter squash with distinctive longitudinal ridges on its exterior and sweet, yellow-orange flesh inside.  Although considered a winter squash, acorn squash belongs to the same species ("Cucurbita pepo") as all summer squashes (including zucchini and crookneck squash), and is commonly mistaken for a gourd.

Annona: Annona is a genus of flowering plants in the pawpaw/sugar apple family, Annonaceae.  It is the second largest genus in the family after "Guatteria", containing approximately 166 species of mostly neotropical and afrotropical trees and shrubs.

Cucurbita: Cucurbita (Latin for gourd) is a genus of herbaceous vines in the gourd family, Cucurbitaceae, also known as cucurbits, native to the Andes and Mesoamerica.  Five species are grown worldwide for their edible fruit, variously known as squash, pumpkin, or gourd depending on species, variety, and local parlance, and for their seeds.  First cultivated in the Americas before being brought to Europe by returning explorers after their discovery of the New World, plants in the genus "Cucurbita" are important sources of human food and oil.  Other kinds of gourd, also called bottle-gourds, are native to Africa and belong to the genus "Lagenaria", which is in the same family and subfamily as "Cucurbita" but in a different tribe.  These other gourds are used as utensils or vessels, and their young fruits are eaten much like those of Cucurbita species.

Summer squash: Summer squash are squashes that are harvested when immature, while the rind is still tender and edible.  Nearly all summer squashes are varieties of "Cucurbita pepo", though not all "Cucurbita pepo" are considered summer squashes.  Most summer squash have a bushy growth habit, unlike the rambling vines of many winter squashes.  The name "summer squash" refers to the short storage life of these squashes, unlike that of winter squashes.

Annona glabra: Annona glabra is a tropical fruit tree in the family Annonaceae, in the same genus as the Soursop and Cherimoya.  Common names include pond apple, alligator apple (so called because American alligators often eat the fruit), swamp apple, corkwood, bobwood, and monkey apple.  The tree is native to Florida in the United States, the Caribbean, Central and South America, and West Africa.  It is common in the Everglades.  The "A. glabra" tree is considered an invasive species in Sri Lanka and Australia.  It grows in swamps, is tolerant of saltwater, and cannot grow in dry soil.

Cucurbita sororia: Cucurbita sororia is a plant species of the genus "Cucurbita", sometimes considered to be a subspecies of "Cucurbita argyrosperma", "C. a." subsp.  "sororia".  It ranges from northern Mexico to Nicaragua, mostly along the Pacific coast.  This species was originally considered closely related to "Cucurbita texana" but "C. sororia" was later shown to be an ancestor of "Cucurbita argyrosperma", with which it hybridizes well.

Annona crassiflora: Annona crassiflora, commonly known as marolo, araticum cortiça, araticum do cerrado or bruto, is a flowering plant in the Annonaceae family.  The flowers of a marolo look like jellyfish wearing hats, and the fruits are sweet and very rough.  It is native to Brazil and Paraguay and the fruit is eaten by native peoples in the Brazilian Cerrado.  Although it is considered to have potential for cultivation, it has not been domesticated to date.

Annona asplundiana: Annona asplundiana is a species of plant in the Annonaceae family.  It is native to Peru, Ecuador and Brazil.  It is considered as a vulnerable species by the IUCN.

Question: Both Cucurbita and Annona are considered what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_biological_rank": {
      "type": "string",
      "description": "The common biological classification rank for both entities."
    },
    "entities_classified": {
      "type": "array",
      "description": "Details about each entity that shares the common classification.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the biological entity."
          },
          "description": {
            "type": "string",
            "description": "A brief description of the entity from the context."
          },
          "family": {
            "type": "string",
            "description": "The family to which the entity belongs."
          }
        },
        "required": [
          "name",
          "description",
          "family"
        ],
        "additionalProperties": false
      }
    },
    "number_of_entities": {
      "type": "integer",
      "description": "The count of entities sharing this classification."
    }
  },
  "required": [
    "common_biological_rank",
    "entities_classified",
    "number_of_entities"
  ],
  "additionalProperties": false
}
