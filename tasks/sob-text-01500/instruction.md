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
Arboretum de Neuville-de-Poitou: The Arboretum de Neuville-de-Poitou is a municipal arboretum located in Neuville-de-Poitou, Vienne, Poitou-Charentes, France.  The arboretum was created along a former railway track, and now displays 380 types of trees and shrubs planted along a 3-kilometer walking path.  It is open daily without charge.

Hypocalymma: Hypocalymma is a genus of evergreen shrubs in the myrtle family Myrtaceae described as a genus in 1840.  The entire genus is endemic to southern Western Australia.

North American azaleas: North American azaleas are flowering shrubs in the genus "Rhododendron", section "Pentanthera", subsection Pentanthera, so named because they all have five stamens.  Most are in the United States, with one species found in Canada and one being found in Mexico.  North American azaleas are commonly confused with azaleas of Asian origin, the evergreen azaleas.  North American azaleas are deciduous and produce two types of buds.  One is a larger and produces about 20 flowers while the other bud produces a leafy shoot.  The flower color, fragrance, and number of stamens vary among species.

Viguiera: Viguiera is a genus of flowering plants in the sunflower family, Asteraceae.  The name honours French physician L. G. Alexandre Viguier (1790–1867).  It contains around 150 species, which are commonly known as goldeneyes and are native to the New World.  These are herbs to bushy shrubs that bear yellow or orange daisy-like flowers.

Central Asian northern desert: The Central Asian northern desert is an ecoregion in the deserts and xeric shrublands biome, located in the Central Asian countries of Kazakhstan and Uzbekistan.  The annual precipitation ranges from 100 to , the winters are cold at -10 to and the summers hot at around 25 °C .  There are a range of habitat types including salt flats, clay desert, rocky desert and some sand desert.  The vegetation consists of scanty xeric shrubs including "Artemisia" and "Salsola".  The fauna is varied, as well as mammals and birds, there are a large number of reptiles and many species of invertebrate.  Some protected areas are included in this ecoregion but other parts are being degraded by conversion to farmland, overgrazing and poaching.

Trellis (architecture): A trellis (treillage) is an architectural structure, usually made from an open framework or lattice of interwoven or intersecting pieces of wood, bamboo or metal that is normally made to support and display climbing plants, especially shrubs.  There are many types of trellis for different places and for different plants, from agricultural types, especially in viticulture, which are covered at vine training systems, to garden uses for climbers such as grapevines, clematis, ivy, and climbing roses or other support based growing plants.  The rose trellis is especially common in Europe and other rose-growing areas, and many climbing rose varieties require a trellis to reach their potential as garden plants.  Some plants will climb and wrap themselves round a trellis without much artificial help being needed while others need training by passing the growing shoots through the trellis and/or tying them to the framework.

Middletown Nature Gardens: The Middletown Nature Gardens is located off Randolph Road in Middletown, Connecticut.  In 1995, the city of Middletown, CT purchased the 18 acre of land and dedicated it open space.  This piece of land serves as a natural habitat to many plants and animals.  There are many trails to walk about surrounded by an array of diverse trees and shrubs.  Some of the types of trees and shrubs include red cedar, flowering dogwood, highbush blueberries, white pine, and speckled alder.  The main trail is a 0.5 mi loop.  Mulched side trails, which branch off the main trail, add another 0.5 mi to walk.  Community volunteers maintain the park.  They have erected many bluebird boxes and bat houses to house some of the natural wildlife of the park.  There are also vernal pools, which are habitats for salamanders and wood frogs in the southeast corner of the park.  There is even a 200-year-old sugar maple, which is called the “bee tree,” in which a large colony of bees has made it their home.

Marywood University: Marywood University is a co-educational, Catholic liberal arts university located on a 115 acre campus in Scranton, Pennsylvania, United States, within the Diocese of Scranton.  Established in 1915 by the Sisters, Servants of the Immaculate Heart of Mary, Marywood currently enrolls more than 3,400 students in a variety of undergraduate, graduate, and doctoral programs.  The university has a national arboretum with more than 100 types of trees and shrubs.  Marywood's Catholic identity coupled with its mission to educate students to "live responsibility in an interdependent world" encourages students to be socially responsible agents of change.

Elaeodendron melanocarpum: Elaeodendron melanocarpum is a species of shrubs or small trees endemic to northern Australia.  The natural range extends from The Kimberley across The Top End to Cape York Peninsula and southwards to South East Queensland.  The species occurs in monsoon forest and drier types of rainforests, commonly along streams.

Phyllanthus: Phyllanthus is the largest genus in the flowering plant family Phyllanthaceae.  Estimates of the number species in this genus vary widely, from 750 to 1200.  "Phyllanthus" has a remarkable diversity of growth forms including annual and perennial herbs, shrubs, climbers, floating aquatics, and pachycaulous succulents.  Some have flattened leaflike stems called cladodes.  It has a wide variety of floral morphologies and chromosome numbers and has one of the widest range of pollen types of any seed plant genus.

Question: Hypocalymma and Viguiera, are types of shrubs?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_entities": {
      "type": "array",
      "description": "The entities mentioned in the question.",
      "items": {
        "type": "string"
      }
    },
    "entity_details": {
      "type": "array",
      "description": "Details about each entity's growth forms.",
      "items": {
        "type": "object",
        "properties": {
          "entity_name": {
            "type": "string",
            "description": "The name of the plant genus."
          },
          "is_described_as_shrub": {
            "type": "boolean",
            "description": "True if the entity is described as a shrub in the context."
          },
          "other_growth_forms": {
            "type": "array",
            "description": "Other growth forms mentioned for the entity, if any.",
            "items": {
              "type": "string"
            }
          },
          "is_exclusively_shrub": {
            "type": "boolean",
            "description": "True if the entity is described ONLY as a shrub, without other growth forms."
          }
        },
        "required": [
          "entity_name",
          "is_described_as_shrub",
          "other_growth_forms",
          "is_exclusively_shrub"
        ],
        "additionalProperties": false
      }
    },
    "are_both_exclusively_shrubs": {
      "type": "boolean",
      "description": "True if both entities are exclusively described as shrubs."
    },
    "final_answer": {
      "type": "boolean",
      "description": "The boolean answer to the question: Are Hypocalymma and Viguiera types of shrubs? (Interpreted as 'Are both exclusively types of shrubs?')"
    }
  },
  "required": [
    "question_entities",
    "entity_details",
    "are_both_exclusively_shrubs",
    "final_answer"
  ],
  "additionalProperties": false
}
