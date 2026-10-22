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
Corokia: Corokia is a genus in the Argophyllaceae family comprising about ten species native to New Zealand and one native to Australia.  "Corokia" species are shrubs or small trees with zigzagging (divaricating) branches.  In fact, "Corokia cotoneaster" is commonly known as "wire-netting bush".  The stems of the shrubs are dark when mature, covered with downy or silky hairs (tomentum) when young.  In spring, they produce clusters of small, star shaped yellow blossoms.  Berries are red or yellow.  The shrubs prefer forests and rocky areas, sun or light shade, reasonably well drained soil, and moderate watering.

Gerrardina: Gerrardina is a genus of two species of trees, shrubs, and scrambling shrubs found in southeastern Africa.  Until recently, the genus was placed in the polyphyletic family Flacourtiaceae, but it was abnormal there due to its apical placentation, small embryos, and mucilaginous foliar epidermis.  Analyses of DNA data indicated that the genus did not fit in any known plant family and not clearly in any then-recognized order, and a new family, Gerrardinaceae, was thus created for it.  Later analyses of additional DNA data and data from wood anatomy indicated that the family should be placed in the order Huerteales.

Acacia: Acacia, commonly known as the wattles or acacias, is a large genus of shrubs and trees in the subfamily Mimosoideae of the pea family Fabaceae.  Initially it comprised a group of plant species native to Africa and Australia, with the first species "A. nilotica" described by Linnaeus.  Controversy erupted in the early 2000s when it became evident that the genus as it stood was not monophyletic, and that several divergent lineages needed to be placed in separate genera.  It turned out that one lineage comprising over 900 species mainly native to Australia was not closely related to the mainly African lineage that contained "A. nilotica"—the first and type species.  This meant that the Australian lineage (by far the most prolific in number of species) would need to be renamed.  Botanist Les Pedley named this group Racosperma, which was inconsistently adopted.  Australian botanists proposed that this would be more disruptive than setting a different type species ("A. penninervis") and allowing this large number of species to remain "Acacia", resulting in the two African lineages being renamed "Vachellia" and "Senegalia", and the two New World lineages renamed "Acaciella" and "Mariosousa".  This was officially adopted, but many botanists from Africa and elsewhere disagreed that this was necessary.

Crotalaria: Crotalaria is a genus of herbaceous plants and woody shrubs in the Family Fabaceae (Subfamily Faboideae) commonly known as rattlepods.  The "Crotalaria" genus includes about 500 species of herbs and shrubs.  Africa is the continent with a majority of "Crotalaria" species (approximately 400 species).  "Crotalaria" are mainly found in damp grassland, especially in floodplains, depressions and along edges of swamps and rivers, but also in deciduous bush land, roadsides and fields.  Some species of "Crotalaria" are grown as ornamentals.  The common name rattlepod or rattlebox is derived from the fact that the seeds become loose in the pod as they mature, and rattle when the pod is shaken.  The name derives from the Ancient Greek κρόταλον , meaning "castanet", and is the same root as the name for the rattlesnakes ("Crotalus").

Anemonopsis: Anemonopsis, the false anemone, is a monotypic genus in the family Ranunculaceae, containing only the species Anemonopsis macrophylla, endemic to Japan's main island of Honshu.

Hemiandra: Hemiandra, commonly known as snakebush, is a genus of plants of the family Lamiaceae, first described in 1810.  The genus is endemic to Australia (Queensland and Western Australia).  They are all prostrate to smallish shrubs allied to "Westringia".  The red, lilac, pink, or white flowers are 2-lipped, the lower lip enlarged and spotted.  The stiff, narrow leaves often have prickly tips.

Westringia: Westringia is a genus of Australian shrubs.  As with other members of the mint family their upper petal (or lip) is divided into two lobes.  There are four stamens - the upper two are fertile while the lower two are reduced to staminodes.  The leaves are in whorls of 3 or 4.

Asteropeia: Asteropeia is a genus of flowering plants.  The genus contains 8 known species of shrubs and small trees, all endemic to Madagascar.  It is the sole genus in family Asteropeiaceae.  Members of the family are evergreen trees or shrubs.

Lophomyrtus: Lophomyrtus is a genus of the myrtle family described as a genus in 1941.  The entire genus is endemic to New Zealand.  It consists of evergreen shrubs or trees, noted for their colorful leaves, which are purple, chocolate, red or bronze-green.  There are also a number of cultivars.  Planting in full sun aids the leaf color to develop.  In cool climates, the plant may need to be placed in a sheltered area.  They will also grow in semi shade.  This genus is closely related to the Australian "Lenwebbia" which also has four petals and similar though less colourful leaves.

Dryandra moth: The Dryandra moth ("Carthaea saturnioides") is a species of moth that is considered to be the sole member of the family Carthaeidae.  Its closest relatives are the Saturniidae and it bears a resemblance to many species of that family, bearing prominent eye spots on all wings.  The common name is derived from the "Dryandra" shrubs of the genus "Banksia", on which the larva of this species feed, and is hence restricted to the south-west of Western Australia where these shrubs grow.  Other "Grevillea" shrubs may also be used as host plants.

Question: Which is a genus of Australian shrubs, Anemonopsis or Westringia? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_type": {
      "type": "string",
      "description": "The type of question being answered, e.g., genus identification."
    },
    "genera_compared": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of genera mentioned in the question for comparison."
    },
    "correct_genus": {
      "type": "string",
      "description": "The genus that is the correct answer to the question."
    },
    "correct_genus_attributes": {
      "type": "object",
      "properties": {
        "native_region": {
          "type": "string",
          "description": "The native region of the correct genus."
        },
        "plant_type": {
          "type": "string",
          "description": "The general plant type of the correct genus (e.g., shrubs, trees)."
        }
      },
      "required": [
        "native_region",
        "plant_type"
      ],
      "additionalProperties": false
    },
    "incorrect_genus": {
      "type": "string",
      "description": "The genus that is not the correct answer."
    },
    "incorrect_genus_attributes": {
      "type": "object",
      "properties": {
        "native_region": {
          "type": "string",
          "description": "The native region of the incorrect genus."
        }
      },
      "required": [
        "native_region"
      ],
      "additionalProperties": false
    },
    "comparison_criteria": {
      "type": "string",
      "description": "The criteria used to compare the genera and determine the answer."
    }
  },
  "required": [
    "question_type",
    "genera_compared",
    "correct_genus",
    "correct_genus_attributes",
    "incorrect_genus",
    "incorrect_genus_attributes",
    "comparison_criteria"
  ],
  "additionalProperties": false
}
