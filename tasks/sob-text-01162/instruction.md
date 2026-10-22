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
Lupinus kingii: Lupinus kingii (King's lupine) is a species of Lupinus, family Fabaceae, which can be found in Arizona, Colorado, Nevada, New Mexico, Utah.  Both the leaves and the pods are hairy with the later being 10 mm long.  In Utah, it is found only at Bryce Canyon National Park.

Anagyrine: Anagyrine is a teratogenic alkaloid commonly found in many species of lupinus plants.  The toxin can cause crooked calf disease if a cow ingests the plant during certain periods of pregnancy.

Lupinus pilosus: Lupinus pilosus, commonly known as blue lupine, (Hebrew: תורמוס ההרים‎ ‎ , Arabic: ترمس برّي‎ ‎ ) is a species of flowering plant from the order of Lamiales which is endemic to Israel where it is found in Mediterranean scrubland.  It has a 30 - long stem and 3 - long legume.  The species blooms from February to May.  The species have white coloured flowers which are 1 - long and pods the diameter of which is 3 - .  In Israel the Lupinus pilosus has blue flowers with white vertical spot at the middle.

Tom Dorman State Nature Preserve: The Palisades harbor many rare species for the Bluegrass due to the unusual landscape.  The state endangered plants found on Tom Dorman's cliffs are starry cleft phlox ("Phlox bifida" var.  "stellaria"), Eggleston's violet ("Viola egglestonii"), and tufted hair-grass ("Deschampsia cespitosa"); the latter being one of only two populations known in the state.  The plants listed as state threatened found here are Kentucky viburnum ("Viburnum molle") and False melic ("Schizachne purpurascens").  The rare Yellowwood tree is also found in this preserve.

Heterotheca: Heterotheca, (common names goldenasters, camphorweed, or telegraph weed) are North American plants in the sunflower family.

Lupinus: Lupinus, commonly known as lupin or lupine (North America), is a genus of flowering plants in the legume family, Fabaceae.  The genus includes over 200 species, with centers of diversity in North and South America.  Smaller centers occur in North Africa and the Mediterranean.  Seeds of various species of lupins have been used as a food for over 3000 years around the Mediterranean and for as much as 6000 years in the Andean highland, but they have never been accorded the same status as soybeans or dry peas and other pulse crops.  The pearl lupin of the Andean highlands of South America, "Lupinus mutabilis", known locally as "tarwi" or "chocho", was extensively cultivated, but no conscious genetic improvement other than to select for larger and water-permeable seeds seems to have been made.  Users soaked the seed in running water to remove most of the bitter alkaloids and then cooked or toasted the seeds to make them edible, or else boiled and dried them to make "kirku".  Spanish domination led to a change in the eating habits of the indigenous peoples, and only recently has interest in using lupins as a food been renewed.

Lupinus subg. Platycarpos: The genus "Lupinus" L. and, in particular, its North-American species, were divided by Sereno Watson (1873) into three parts: "Lupinus", "Platycarpos" and "Lupinnelus".  Differences in habit and in the number of ovules were accepted as the basis for this classification.  A majority of perennial and annual species from the American continent described by Watson were referred to "Lupinus".  To the "Platycarpos" section were attributed some annual species with two ovules in the ovary and two seeds in the pod ("L. densiflorus" Benth., "L. microcarpus" Sims.  and others).  Section "Lupinnelus" consisted of one species ("L. uncialis"), with axillary and solitary flowers, scarcely reflexed banner, and also with two ovules in the ovary.  Presently, the existence of such species seems doubtful.

Rafflesiaceae: The Rafflesiaceae are a family of rare parasitic plants found in the tropical forests of east and southeast Asia, including "Rafflesia arnoldii", which has the largest flowers of all plants.  The plants are endoparasites of vines in the genus "Tetrastigma" (Vitaceae) and lack stems, leaves, roots, and any photosynthetic tissue.  They rely entirely on their host plants for both water and nutrients, and only then emerge as flowers from the roots or lower stems of the host plants.

Lupinine: Lupinine is a bitter tasting quinolizidine alkaloid present in "Lupinus" species (lupins), plants of the family Fabaceae.  The scientific literature contains many reports on the isolation and synthesis of this compound.  The characteristically bitter taste of lupin beans, attributable to the alkaloids which they contain, renders them unsuitable for human and animal consumption.  However, because lupin beans have potential nutritional value due to their high protein content, efforts have been made to reduce their alkaloid content, as well as to develop "sweet" varieties of "Lupinus".

Lupinus sparsiflorus: Lupinus sparsiflorus (Coulter's lupine) is a species of lupin native to North America.  In the United States it occurs in California, Nevada, Arizona and Utah, and in Mexico it is found in Baja California and Sonora.  Other common names include Mojave lupine, a name it shares with "Lupinus odoratus".

Question: On which continent are Heterotheca and Lupinus plants found?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "plant_genera": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "genus_name": {
            "type": "string"
          },
          "found_continents": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "genus_name",
          "found_continents"
        ],
        "additionalProperties": false
      }
    },
    "common_continents": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "answer_continent_count": {
      "type": "integer"
    }
  },
  "required": [
    "plant_genera",
    "common_continents",
    "answer_continent_count"
  ],
  "additionalProperties": false
}
