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
Abelia spathulata: Abelia spathulata is a species of "Abelia" in the honeysuckle family.  The plant is endemic to Japan in the eastern side of Honshu, the west and central Kantō region, and the northwestern part of Kyushu and Shikoku.

Honeysuckle: Honeysuckles ("Lonicera", ; syn.  "Caprifolium" Mill. ) are arching shrubs or twining bines in the family Caprifoliaceae, native to the Northern Hemisphere.  Approximately 180 species of honeysuckle have been identified.  About 100 of these species can be found in China and approximately 20 native species have been identified in Europe, 20 in India, and 20 in North America.  Widely known species include "Lonicera periclymenum" (honeysuckle or woodbine), "Lonicera japonica" (Japanese honeysuckle, white honeysuckle, or Chinese honeysuckle) and "Lonicera sempervirens" (coral honeysuckle, trumpet honeysuckle, or woodbine honeysuckle).  Hummingbirds are attracted to the flowers on some of these plants, especially "L. sempervirens" and "L. ciliosa" (orange honeysuckle).  Honeysuckle derives its name from the edible sweet nectar obtainable from its tubular flowers.  The name "Lonicera" stems from Adam Lonicer, a Renaissance botanist.

Abelia mosanensis: Abelia mosanensis is a species of "Abelia" in the honeysuckle family.  The plant inhabits the Korean Peninsula.  It is deciduous, up to 2 meters high, and blooms from May to June.

Lonicera fragrantissima: Lonicera fragrantissima is a species of flowering plant in the honeysuckle family known by the common names winter honeysuckle, fragrant honeysuckle, January jasmine, Chinese honeysuckle, kiss-me-at-the-gate, and sweet breath of spring.  It is native to China and has been an introduced species to other parts of the world.  It was brought to the attention of western gardeners by Scottish plant hunter Robert Fortune, who was plant hunting in China for the Royal Horticultural Society.  Fortune introduced "Lonicera fragrantissima" to England in 1845, and a few years later it was introduced to the United States.  In 1853 the editor of American gardening magazine "The Horticulturist" wrote that the previous year he had been sent a specimen from a plant that had been flowering in the gardens of Hatfield House, the Marquess of Salisbury's stately home in Hertfordshire.  The first mention of a specimen for commercial sale in an American plant catalogue is in 1860.

Abelia corymbosa: Abelia corymbosa (syn.  "Zabelia corymbosa") is a species of flowering plant in the honeysuckle family, Caprifoliaceae.  It is native to Central Asia, where it occurs in Kazakhstan, Kyrgyzstan, and Tajikistan.

Lonicera sempervirens: Lonicera sempervirens (also coral honeysuckle, trumpet honeysuckle, or scarlet honeysuckle) is a species of honeysuckle native to the eastern United States but can grow in many areas due to its hardiness Most often grown as a plant for wildlife, ruby-throated hummingbirds use it in their natural range as well as other birds, butterflies, and bees.  It is also grown as an ornamental for its attractive flowers, especially as a native alternative to the invasive Japanese honeysuckle.  Several cultivars have been selected for variation in flower color, including 'Magnifica' (flowers red outside, yellow inside), 'Sulphurea' (yellow flowers), and 'Superba' (bright scarlet flowers).

Lonicera involucrata: Lonicera involucrata (bearberry honeysuckle, bracted honeysuckle, twinberry honeysuckle, Californian Honeysuckle, twin-berry, black twinberry) is a species of honeysuckle native to northern and western North America, from southern Alaska east across boreal Canada to Quebec, and south through the western United States to California, and to Chihuahua in northwestern Mexico.  It grows at elevations from sea level to 2,900 m.

Abelia chinensis: Abelia chinensis is a species of flowering plant in the honeysuckle family Caprifoliaceae.  It was described by Robert Brown in 1818.  The plant inhabits China, Taiwan and Japan.  It has reddish stems and glossy, small leaves that become reddish-brown before autumn.  It is one of the most cold-resistant species within the genus.

Abelia: Abelia is a genus of about 30 species and many hybrids in the honeysuckle family Caprifoliaceae.  Some authors, including the Angiosperm Phylogeny Group, consider "Abelia" and related genera to belong instead in the segregate family Linnaeaceae, also including such genera as "Linnaea", "Abelia", "Dipelta", "Kolkwitzia", and "Zabelia", but not such others as "Lonicera" or "Symphoricarpos," included by them instead in a more narrowly viewed Caprifoliaceae.

Lonicera caprifolium: Lonicera caprifolium, the Italian woodbine, perfoliate honeysuckle, goat-leaf honeysuckle, Italian honeysuckle, or perfoliate woodbine, is a species of perennial flowering plants in the genus "Lonicera" of the Caprifoliaceae family.  It is native to parts of Europe, and naturalised in South East Britain and northeastern North America.  It can readily be distinguished from Europe's most common species, "Lonicera periclymenum", by its topmost leaves which are perfoliate as the Latin name suggests (that is, the stem appears to grow through the centre of the leaf).  It is a vigorous, deciduous climber growing up to 8 metres.  It bears masses of very fragrant, cream-coloured flowers, tinged with pink, appearing in midsummer.

Question: Does Honeysuckle or Abelia have more species?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_entities": {
      "type": "array",
      "description": "List of genera being compared with their respective species counts.",
      "items": {
        "type": "object",
        "properties": {
          "genus_name": {
            "type": "string",
            "description": "The name of the genus."
          },
          "species_count": {
            "type": "integer",
            "description": "The approximate number of species identified for this genus."
          }
        },
        "required": [
          "genus_name",
          "species_count"
        ],
        "additionalProperties": false
      }
    },
    "comparison_result": {
      "type": "object",
      "description": "The outcome of the comparison, indicating which entity has more species and the difference.",
      "properties": {
        "entity_with_more_species": {
          "type": "string",
          "description": "The name of the genus that has more species."
        },
        "species_difference": {
          "type": "integer",
          "description": "The numerical difference in species count between the two genera."
        }
      },
      "required": [
        "entity_with_more_species",
        "species_difference"
      ],
      "additionalProperties": false
    },
    "question_answered": {
      "type": "boolean",
      "description": "Indicates whether the question about which genus has more species was answered."
    }
  },
  "required": [
    "comparison_entities",
    "comparison_result",
    "question_answered"
  ],
  "additionalProperties": false
}
