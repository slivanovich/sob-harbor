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
Fragaria × bringhurstii: Fragaria" × "bringhurstii is a naturally occurring hybrid species of strawberry native to the West Coast of the United States.  The species results from the natural intercrossing of "Fragaria vesca" and "Fragaria chiloensis", native species whose ranges overlap in that region.

Manettia: Manettia is a genus of flowering plants in the family Rubiaceae.  There are between 80 and 123 species.  They are distributed in the West Indies, Mexico, and Central and South America.  Most are vines.  The genus was named after Saverio Manetti.

Fragaria × vescana: Fragaria × vescana is a hybrid strawberry cultivar that was created in an effort to combine the best traits of the garden strawberry ("Fragaria" × "ananassa"), which has large berries and vigorous plants, with the woodland strawberry ("Fragaria vesca"), which has an exquisite flavour, but small berries.

Fragaria × Comarum hybrids: There are several commercially important hybrids between "Fragaria" and "Comarum" species in existence, but they have not yet received formal botanical names as hybrids between those genera.  Both "Fragaria" and "Comarum" have at different times been considered to be part of the genus "Potentilla", and these hybrids have been named Potentilla" x "rosea, or are sometimes referred to as "Fragaria" × "Potentilla" hybrids.

Fragaria nipponica: Fragaria nipponica is a species of strawberry native to the western side of the Japanese island of Honshū, with a variety "Fragaria nipponica" var.  "yakusimensis" on Yakushima.  Some botanists treat it as a synonym of "Fragaria yezoensis".

Fragaria: Fragaria is a genus of flowering plants in the rose family, Rosaceae, commonly known as strawberries for their edible fruits.  There are more than 20 described species and many hybrids and cultivars.  The most common strawberries grown commercially are cultivars of the garden strawberry, a hybrid known as "Fragaria" × "ananassa".  Strawberries have a taste that varies by cultivar, and ranges from quite sweet to rather tart.  Strawberries are an important commercial fruit crop, widely grown in all temperate regions of the world.

1105 Fragaria: 1105 Fragaria (1929 AB) is Main-belt asteroid discovered on January 1, 1929, by Karl Wilhelm Reinmuth at the Landessternwarte Heidelberg-Königstuhl in Heidelberg, Germany.  It was named after Fragaria, the genus of flowering plants in the rose family.  It is a member of the Eos family.

Strawberry: The garden strawberry (or simply strawberry; Fragaria × ananassa) is a widely grown hybrid species of the genus "Fragaria", collectively known as the strawberries.  It is cultivated worldwide for its fruit.  The fruit is widely appreciated for its characteristic aroma, bright red color, juicy texture, and sweetness.  It is consumed in large quantities, either fresh or in such prepared foods as preserves, juice, pies, ice creams, milkshakes, and chocolates. Artificial strawberry flavorings and aromas are also widely used in many products like lip gloss, candy, hand sanitizers, perfume, and many others.

Fragaria cascadensis: Fragaria cascadensis, is a species of strawberry ("Fragaria"), found in the Cascades Mountains described in 2012.  The vernacular name "Cascade strawberry" was suggested by the describing author.

Fragaria iturupensis: Fragaria iturupensis, the Iturup strawberry, is a species of strawberry, endemic to Iturup in the Kuril Islands.  It is noted to have relatively large berries for a wild species, similar in appearance to those of "Fragaria virginiana".

Question: Are Manettia and Fragaria both edible?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "genera_edibility_status": {
      "type": "array",
      "description": "List of genera mentioned in the question and their edibility status based on the context.",
      "items": {
        "type": "object",
        "properties": {
          "genus_name": {
            "type": "string",
            "description": "The name of the genus."
          },
          "is_edible": {
            "type": "boolean",
            "description": "True if the genus is described as edible in the context, false otherwise."
          }
        },
        "required": [
          "genus_name",
          "is_edible"
        ],
        "additionalProperties": false
      }
    },
    "are_both_edible": {
      "type": "boolean",
      "description": "The final answer to whether both genera are edible."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for the edibility status of both genera."
    }
  },
  "required": [
    "genera_edibility_status",
    "are_both_edible",
    "reasoning"
  ],
  "additionalProperties": false
}
