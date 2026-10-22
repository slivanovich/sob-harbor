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
Aphanisma: Aphanisma is a monotypic genus which contains the sole species Aphanisma blitoides, a rare annual plant known by the common names San Diego coastalcreeper or simply aphanisma.  This is a beach-dwelling plant native to the coastline of Baja California and southern California, including the Channel Islands.  It is a succulent saline-adapted plant found in sand or scrub at the immediate coastline.  It has many thin, sprawling stems, few reduced green leaves, and tiny flowers.  The older stems are bright red.  This plant is becoming more rare due to the disappearance of its coastal habitat.  It is extirpated from much of its native range.

Apophyllum: Apophyllum is a genus of plant native to Australia.  It contains only one species, which by definition makes the genus a monotypic genus.  This single species is called Apophyllum anomalum, commonly called warrior bush or broom bush.

Thyridia repens: Thyridia repens, with common names creeping monkeyflower, Native musk, Maori musk, and native monkey flower, is a herbaceous succulent plant native to New Zealand and Australia that grows as low mats.  Its flowers are light purple or white.  It is the only species in the genus Thyridia.

Commersonia borealis: Commersonia borealis (E.Pritz.)  C.F.Wilkins & Whitlock is a species of plant native to Western Australia in the Commersonia genus that was first described by Ernst Georg Pritzel.  Prior to 2011 it was referred to as "Rulingia borealis", until all species were moved to the genus "Commersonia", except for "R. cuneata", "R. loxophylla", "R. luteiflora", and "R. procumbens", which were moved to the genus "Androcalva".

Bryophyllum pinnatum: Bryophyllum pinnatum, also known as the air plant, cathedral bells, life plant, miracle leaf, and Goethe plant is a succulent plant native to Madagascar, which is a popular houseplant and has become naturalized in tropical and subtropical areas.  It is distinctive for the profusion of miniature plantlets that form on the margins of its phylloclades, a trait it has in common with some other members of its genus.

Heuchera micrantha: Heuchera micrantha is a species of flowering plant in the saxifrage family known by the common name crevice alumroot.  It is native to western North America from British Columbia to California, where it grows on rocky slopes and cliffs.  This plant is quite variable in appearance.  There are a number of wild and cultivated varieties.  The leaves are lobed and usually coated in glandular hairs.  They are green to reddish-green or purple-green in color and may have very long, gland-dotted petioles.  The plant produces an erect inflorescence up to a meter high bearing many clusters of pink, white, or greenish flowers.  Each rounded flower has fleshy, hairy lobes tipped with tiny petals and protruding stamens and stigma.

Zamioculcas: Zamioculcas (common name "Zanzibar Gem", "Zuzu Plant" or Emerald Palm) is a genus of flowering plant in the family Araceae, containing the single species Zamioculcas zamiifolia.  It is a tropical perennial plant native to eastern Africa, from Kenya south to northeastern South Africa.  Dutch nurseries started wide-scale commercial propagation of the plant around 1996.

Heuchera: Heuchera is a genus of evergreen, herbaceous perennial plants in the family Saxifragaceae, all native to North America.  Common names include alumroot and coral bells.

Mesembryanthemum crystallinum: Mesembryanthemum crystallinum is a prostrate succulent plant native to Africa, Sinai and southern Europe, and naturalized in North America, South America and Australia.  The plant is covered with large, glistening bladder cells or water vesicles, reflected in its common names of common ice plant, crystalline ice plant or ice plant.

Bryophyllum daigremontianum: Bryophyllum daigremontianum, commonly called devil’s backbone, mother-of-thousands, alligator plant, or Mexican hat plant is a succulent plant native to Madagascar.  Like other members of its genus "Bryophyllum", it is able to propagate vegetatively from plantlets that develop on its phylloclade margins.  All parts of the plant contain a very toxic steroid known as daigremontianin.

Question: Are both Heuchera and Apophyllum genus of plant native to Australia?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question asked."
    },
    "genus_1_name": {
      "type": "string",
      "description": "The name of the first genus mentioned in the question."
    },
    "genus_1_native_to_australia": {
      "type": "boolean",
      "description": "True if the first genus is native to Australia, false otherwise."
    },
    "genus_2_name": {
      "type": "string",
      "description": "The name of the second genus mentioned in the question."
    },
    "genus_2_native_to_australia": {
      "type": "boolean",
      "description": "True if the second genus is native to Australia, false otherwise."
    },
    "both_native_to_australia": {
      "type": "boolean",
      "description": "The final answer to whether both genera are native to Australia."
    }
  },
  "required": [
    "question_asked",
    "genus_1_name",
    "genus_1_native_to_australia",
    "genus_2_name",
    "genus_2_native_to_australia",
    "both_native_to_australia"
  ],
  "additionalProperties": false
}
