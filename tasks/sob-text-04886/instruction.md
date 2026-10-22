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
Fallopia: Fallopia is a genus of about 12–15 species of flowering plants in the buckwheat family, often included in a wider treatment of the related genus "Polygonum" in the past.  The genus is native to temperate and subtropical regions of the Northern Hemisphere.  The genus includes herbaceous perennial plants, herbaceous vines, and woody vines.

Fallopia japonica: Fallopia japonica, synonym "Reynoutria japonica", commonly known as Asian knotweed or Japanese knotweed, is a large, herbaceous perennial plant of the knotweed and buckwheat family Polygonaceae.  It is native to East Asia in Japan, China and Korea.  In North America and Europe, the species has successfully established in numerous habitats and is classified as an invasive species in several countries.

Deathcamas: Deathcamas or death camas refers to several species of flowering plant in the tribe Melanthieae.  The name alludes to the great similarity of appearance between these toxic plants, which were formerly classified together in the genus "Zigadenus", and the edible camases ("Camassia"), with which they also often share habitat.  Other common names for these plants include deadly zigadene, hog potato and mystery-grass.

Fallopia baldschuanica: Fallopia baldschuanica (syn.  "Polygonum baldschuanicum") is an Asian species of flowering plant in the knotweed family known by several common names, including Russian-vine, Bukhara fleeceflower, Chinese fleecevine, mile-a-minute and silver lace vine.  It is native to Asia (China, Russia, Kazakhstan, etc.), and it can be found growing wild in parts of Europe and North and Central America as an introduced species.

Toxicoscordion brevibracteatum: Toxicoscordion brevibracteatum (syn.  "Zigadenus brevibracteatus") is a species of flowering plant known by the common name desert deathcamas.  It is native to Baja California, Sonora, and California, where it grows in sandy desert habitat among creosote and Joshua trees.

Fallopia scandens: Fallopia scandens (climbing false buckwheat) is a species of "Fallopia" native to North America.  It is a herbaceous perennial plant which grows from to 1 – tall.  Although they are semi-erect during bloom, when they are producing fruit, they hang from their pedicels in a downward position.  Both the fruit and flower are greenish-white in appearance.  In North America, it is often misidentified with "fallopia dumetorum", a species endemic to Europe.

Fallopia multiflora: Fallopia multiflora is a synonym for "Reynoutria multiflora" also called tuber fleeceflower, Chinese knotweed, and heshouwu (HSW, ), is a species of flowering plant in the buckwheat family Polygonaceae.  It is native to central and southern China.

Zigadenus: Zigadenus is a genus of flowering plants now containing only one species, Zigadenus glaberrimus, the sandbog death camas, found in the southeastern United States from Mississippi to Virginia.  Around 20 species were formerly included in the genus, but have now been moved to other genera.

Fallopia aubertii: Fallopia aubertii (syn.  "Polygonum aubertii") is a species of flowering plant in the knotweed family Polygonaceae.

Question: Which plant has more species, Zigadenus or Fallopia? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_result": {
      "type": "string",
      "description": "The genus with more species."
    },
    "compared_genera": {
      "type": "array",
      "description": "Details for each genus being compared.",
      "items": {
        "type": "object",
        "properties": {
          "genus_name": {
            "type": "string",
            "description": "The name of the plant genus."
          },
          "species_count": {
            "type": "integer",
            "description": "The number of species currently recognized for the genus."
          }
        },
        "required": [
          "genus_name",
          "species_count"
        ],
        "additionalProperties": false
      }
    },
    "comparison_statement": {
      "type": "string",
      "description": "A statement summarizing the comparison of species counts."
    }
  },
  "required": [
    "comparison_result",
    "compared_genera",
    "comparison_statement"
  ],
  "additionalProperties": false
}
