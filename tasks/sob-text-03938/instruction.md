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
Adenanthos cuneatus: Adenanthos cuneatus, also known as coastal jugflower, flame bush, bridle bush and sweat bush, is a shrub of the family Proteaceae native to the south coast of Western Australia.  The French naturalist Jacques Labillardière originally described it in 1805.  Within the genus "Adenanthos", it lies in the section "Adenanthos" and is most closely related to "A. stictus".  "A. cuneatus" has hybridized with four other species of "Adenanthos".  Growing to 2 m high and wide, it is erect to prostrate in habit, with wedge-shaped lobed leaves covered in fine silvery hair.  The single red flowers are insignificant, and appear all year, though especially in late spring.  The reddish new growth occurs over the summer.

Dryopteris: Dryopteris , commonly called wood fern, male fern (referring in particular to "Dryopteris filix-mas"), or buckler fern, is a genus of about 250 species of ferns with distribution in Eastern Asia, the Americas, Europe, Africa, and the Pacific islands, with the highest species diversity in eastern Asia.  Many of the species have stout, slowly creeping rootstocks that form a crown, with a vase-like ring of fronds.  The sori are round, with a peltate indusium.  The stipes have prominent scales.

Dryopteris goldiana: Dryopteris goldiana, commonly called Goldie's wood fern, or giant wood fern is a fern native to the eastern United States and adjacent areas of Canada, from New Brunswick to Ontario and Georgia.  It is the largest native North American species of "Dryopteris" and along with ostrich fern it is one of the largest ferns in eastern North America.  Specimens are known with fronds six feet (1.8 meters) tall.  "D. goldiana" hybridizes with many other species of "Dryopteris" and the hybrids tend to be larger than the pure species.  It was named by William Hooker in honor of its discoverer, John Goldie.

Dryopteris clintoniana: Dryopteris clintoniana, commonly known as Clinton's wood fern, is a fern of hybrid origin native to the northern hemisphere.  It is a fertile hexaploid, arising as a species by doubling of its chromosome number from a hybrid between "Dryopteris cristata", a tetraploid, and "Dryopteris goldiana", a diploid.  It is more northern in its range than either parent species.

Adenanthos: Adenanthos is a genus of Australian native shrubs in the flowering plant family Proteaceae.  Variable in habit and leaf shape, it is the only genus in the family where solitary flowers are the norm.  It was discovered in 1791, and formally published by Jacques Labillardière in 1805.  The type species is "Adenanthos cuneatus", and 33 species are recognised.  The genus is placed in subfamily Proteoideae, and is held to be most closely related to several South African genera.

Dryopteris intermedia: Dryopteris intermedia, the intermediate wood fern, is an evergreen eastern North American species also occasionally found in Europe.  It is a diploid species, and is the parent of several species of hybrid origin, including "Dryopteris carthusiana".

Adenanthos terminalis: Adenanthos terminalis, commonly known as gland flower, yellow gland flower or adenanthos, is a one metre tall shrub in the family Proteaceae.  It is found in south eastern regions of Australia, in the states of South Australia and Victoria, and is the most widespread of the two "Adenanthos" species occurring outside of Western Australia.

Dryopteris crassirhizoma: Dryopteris crassirhizoma is a fern species in the genus "Dryopteris".  It is an element (Traditional: 貫眾, Simplified: 贯众) of the Yupingfeng Asian soup formulation derivative.

Adenanthos sect. Adenanthos: Adenanthos" sect.  "Adenanthos is a taxonomic section of the flowering plant genus "Adenanthos" (Proteaceae).  It comprises 29 species.  The centre of diversity is southwest  Western Australia, with two species extending into South Australia and western Victoria.

Dryopteris cristata: Dryopteris cristata is a species of fern native to wetlands throughout the Northern Hemisphere.  It is known as crested wood fern or crested buckler-fern.  This plant is a tetraploid species of hybrid origin, one parent being "Dryopteris ludoviciana" and the other being the unknown, apparently extinct species, dubbed "Dryopteris semicristata", which is also one of the presumed parents of "Dryopteris carthusiana".  "D. cristata" in turn is one of the parents of "Dryopteris clintoniana", another fern of hybrid origin.

Question: Does Dryopteris or Adenanthos have more species?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_result": {
      "type": "boolean",
      "description": "True if the first genus mentioned in the question (Dryopteris) has more species, false otherwise."
    },
    "genus_with_more_species": {
      "type": "string",
      "description": "The name of the genus that has more species."
    },
    "genera_comparison": {
      "type": "array",
      "description": "Details of the genera being compared, including their species counts.",
      "items": {
        "type": "object",
        "properties": {
          "genus_name": {
            "type": "string",
            "description": "The name of the genus."
          },
          "species_count": {
            "type": "integer",
            "description": "The number of species recognized for this genus."
          }
        },
        "required": [
          "genus_name",
          "species_count"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "comparison_result",
    "genus_with_more_species",
    "genera_comparison"
  ],
  "additionalProperties": false
}
