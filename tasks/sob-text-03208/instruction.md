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
Lysimachia clethroides: Lysimachia clethroides, common name gooseneck loosestrife, is a species of flowering plant, traditionally classified in the family Primulaceae.  It was transferred to the family Myrsinaceae based on a molecular phylogenetic study, but this family was later merged into the Primulaceae.

Stylogyne: Stylogyne is a genus of shrubs and trees in the family Primulaceae.  Its members are found throughout tropical parts of the Americas, with the greatest diversity in South America.  It is closely related to the genera "Ardisia" and "Geissanthus", and various species have been transferred between the three genera.  All three were formerly placed in the family Myrsinaceae, which is now treated as a subfamily (Myrsinoideae) of the Primulaceae.

Lysimachia monelli: Lysimachia monelli (commonly known as the garden pimpernel or blue pimpernel and formerly known as Anagallis monelli) is a species of flowering plant in the family Primulaceae, native to the Mediterranean region.  It is not to be confused with "Lysimachia foemina", which has very similar blue flowers, but broader leaves and can be found also in colder climates.  In a comparison of DNA sequences, "L. monelli" was shown to be most closely related to "L. foemina".  The latter had been thought by many to be closest to "L. arvensis", and some authors had even included "L. foemina" as a subspecies of "L. arvensis".  The three species were among several transferred from "Anagallis" to "Lysimachia" in a 2009 paper.

Myrsine: Myrsine is a genus of flowering plants in the family Primulaceae.  It was formerly placed in the family Myrsinaceae before this was merged into the Primulaceae.  It is found nearly worldwide, primarily in tropical and subtropical areas.  It contains about 200 species, including several notable radiations, such as the matipo of New Zealand and the kōlea of Hawaiʻ i (the New Zealand "black matipo", "Pittosporum tenuifolium", is not related to "Myrsine").  In the United States, members of this genus are known as colicwood.  Some species, especially "M. africana", are grown as ornamental shrubs.

Dodecatheon poeticum: Dodecatheon poeticum is commonly known as the poet's shooting star or the Narcissus shooting star.  "D. poeticum" is a species of the genus "Dodecatheon" which is native to the states of Oregon and Washington in western North America.  The genus "Dodecatheon" contains herbaceous flowering plants and is also a part of the primrose family Primulaceae.  This plant has basal clumps of leaves and drooping flowers that occur at the apex of tall stems that rise from where the leaves join.

Anagallis: Anagallis is a genus of about 20–25 species of flowering plants in the family Primulaceae, commonly called pimpernel and perhaps best known for the scarlet pimpernel referred to in literature.  The botanical name is from the Greek, "ana", "again", and "agallein", "to delight in", and refers to the opening and closing of the flowers in response to environmental conditions.

Parathesis: Parathesis is a genus of flowering plants in the family Primulaceae.  There are about 95 species distributed from Mexico to South America and the Caribbean.  Plants of this genus can be distinguished by glandular papillae on the lobes of the flower corolla and bright yellow anthers.

Lysimachia foemina: Lysimachia foemina (commonly known as Poorman's Weatherglass and formerly known as Anagallis foemina) is a low-growing annual herbaceous plant of the genus "Lysimachia" belonging to the Primulaceae family.  In a comparison of DNA sequences, "L. foemina" was shown to be most closely related to "L. monelli".  It had been thought by many to be closest to "L. arvensis", and some authors had even included "L. foemina" as a subspecies of "L. arvensis".  The three species were among several transferred from "Anagallis" to "Lysimachia" in a 2009 paper.

Lysimachia: Lysimachia is a genus consisting of 193 accepted species of flowering plants traditionally classified in the family Primulaceae.  Based on a molecular phylogenetic study it was transferred to the family Myrsinaceae, before this family was later merged into the Primulaceae.

Canistrum: Canistrum is a genus of the botanical family Bromeliaceae, subfamily Bromelioideae.

Question: While Anagallis is a genus of flowering plans in the family Primulaceae, what genus is the Canistrum in?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "plant_genus_name": {
      "type": "string",
      "description": "The name of the plant genus."
    },
    "botanical_family": {
      "type": "string",
      "description": "The botanical family to which the genus belongs."
    },
    "botanical_subfamily": {
      "type": "string",
      "description": "The botanical subfamily to which the genus belongs."
    }
  },
  "required": [
    "plant_genus_name",
    "botanical_family",
    "botanical_subfamily"
  ],
  "additionalProperties": false
}
