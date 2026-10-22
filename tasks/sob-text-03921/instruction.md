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
Macropidia: Macropidia fuliginosa, the sole species of genus Macropidia, is a perennial rhizomatous flowering plant.  Commonly known as the black kangaroo paw, it is endemic to Southwest Australia, specifically from Perth to Geraldton in the north of the region.

Gum Tree, Kentucky: Gum Tree is an unincorporated community located in Monroe County, Kentucky, United States.  It is concentrated around the intersection of Kentucky Route 678, Kentucky Route 870, and Kentucky Route 1366, west of Tompkinsville and north of Gamaliel.  Gum Tree is home to one of Monroe County's voting precincts, which had over 900 registered voters as of 2014.

Gum tree: Gum tree is a common name for smooth-barked trees and shrubs in three closely related genera of Eucalypt:

Eucalyptus tereticornis: Eucalyptus tereticornis is a species of tree native to eastern Australia.  It has a strong, hard and durable heartwood, with a density of about 1100 kg m.  It is used for construction in heavy engineering, such as for railway sleepers.  The leaves of "E. tereticornis" are used in the production of cineole based eucalyptus oil.  "E. tereticornis" has several common names, including forest red gum, blue gum, flooded gum, grey gum, mountain gum, Queensland blue gum, red gum, bastard box, red ironbark, red irongum and slaty gum.

Gum arabic: Gum arabic, also known as acacia gum, is a natural gum consisting of the hardened sap of various species of the acacia tree.  Originally, gum arabic was collected from "Acacia nilotica" which was called the "gum arabic tree"; in the present day, gum arabic is predominantly collected from two related species, namely "Acacia senegal" and "Vachellia (Acacia) seyal".  Producers harvest the gum commercially from wild trees, mostly in Sudan (80%) and throughout the Sahel, from Senegal to Somalia—though it is historically cultivated in Arabia and West Asia.

Gonipterus scutellatus: Gonipterus scutellatus is a species of weevil in the Curculionidae family.  It is commonly known as the eucalyptus snout beetle, the eucalyptus weevil or the gum tree weevil.  It feeds and breeds on "Eucalyptus" trees and is endemic to Australia.

Senegalia senegal: Senegalia senegal (until recently known as "Acacia senegal") is a small thorny deciduous tree from the genus "Senegalia", which is known by several common names, including Gum acacia, Gum arabic tree, Senegal gum and Sudan gum arabic.  In parts of India, it is known as Kher or Khor.  It is native to semi-desert regions of Sub-Saharan Africa, as well as Oman, Pakistan, west coastal India.  It grows to a height of 5-12 m, with a trunk up to 30 cm in diameter.  "S. senegal" is the source of the world's highest quality gum arabic, known locally as hashab gum in contrast to the related, but inferior, gum arabic from Red acacia or talah gum.

Anaphes nitens: Anaphes nitens is a species of fairyfly, a chalcid wasp in the family Mymaridae.  Native to Australia, it is an egg parasitoid of the gum tree snout beetle ("Gonipterus scutellatus"), a pest of "Eucalyptus" trees, and has been used in biological pest control of that species.

Eucalyptus salubris: Eucalyptus salubris, commonly known as gimlet, fluted gum tree, gimlet gum and silver-topped gimlet, is a gum tree endemic to low-rainfall areas of the wheatbelt and goldfields regions of Western Australia.

Functional chewing gum: Functional chewing gum is the name given to types of chewing gum which impart some practical function instead of, or in addition to, the usual enjoyment provided by a traditional chewing gum as a confectionery product.  Examples of this include nicotine gum which is used to aid smoking cessation & so-called Think Gum which designers say they believe may enhance mental functioning.  It could be argued that most gum (at least the mint varieties) provides some function in that they can improve bad breath, but such an effect is so widespread that the term 'functional' is almost always applied to gum with some additional function.  Medical uses for 'functional chewing gum' include a reported reduction in the duration of post-operative ileus following abdominal and specifically gastrointestinal surgery.

Question: Are Macropidia and Gum tree both types of trees?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_one_name": {
      "type": "string",
      "description": "The name of the first entity in the question."
    },
    "entity_one_is_tree": {
      "type": "boolean",
      "description": "Indicates if the first entity is classified as a tree based on the context."
    },
    "entity_one_classification": {
      "type": "string",
      "description": "The classification of the first entity as described in the context."
    },
    "entity_two_name": {
      "type": "string",
      "description": "The name of the second entity in the question."
    },
    "entity_two_is_tree": {
      "type": "boolean",
      "description": "Indicates if the second entity is classified as a tree based on the context."
    },
    "entity_two_classification": {
      "type": "string",
      "description": "The classification of the second entity as described in the context."
    },
    "both_are_trees": {
      "type": "boolean",
      "description": "The final answer to whether both entities are types of trees."
    }
  },
  "required": [
    "entity_one_name",
    "entity_one_is_tree",
    "entity_one_classification",
    "entity_two_name",
    "entity_two_is_tree",
    "entity_two_classification",
    "both_are_trees"
  ],
  "additionalProperties": false
}
