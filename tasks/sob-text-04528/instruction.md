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
Raymond Vanier: Raymond Vanier (6 August 1895 – 15 August 1965) was a pioneering French aviator.  Vanier played a key role in the development of French and Spanish civil aviation, despite being less well-known to the general public than Jean Mermoz, Henri Guillaumet or Antoine de Saint-Exupéry.

Lycée Jean Mermoz (Senegal): Lycée Jean Mermoz is a French international school in Dakar, Senegal.  It serves "maternelle" (preschool) until "terminale" (final year of "lycée" or senior high school).

Institut aéronautique Jean Mermoz: Institut aéronautique Jean Mermoz (IAJM) is a flight training organisation and resourcing services.  Professional airline pilots have been trained at IAJM since 1957.

Pauline Vanier: The Honourable Pauline Vanier, PC, CC, DStJ (March 28, 1898 – March 23, 1991), born Pauline Archer in Montreal, married Georges Vanier on September 29, 1921.  Georges would become one of Canada's first professional diplomats, Canada's first ambassador to France and Canada's first Canadian-born French-speaking Governor General of Canada from 1959 until his death in March 1967.  With her extensive diplomatic experience, Pauline filled the role of vice-regal consort with as much distinction as her husband filled his.  Georges and Pauline Vanier created the Vanier Institute of the Family in 1965.

Jean Vanier Catholic Secondary School: Jean Vanier Catholic Secondary School (JVCSS), simply Jean Vanier or Vanier is a Roman Catholic high school, part of the Toronto Catholic District School Board (TCDSB), in the Eglinton East neighbourhood of Scarborough in Toronto, Ontario, Canada.  The school was opened as Tabor Park Vocational School (1964-1986) by the Scarborough Board of Education and later owned by the Toronto District School Board, after which the building was leased to the TCDSB in 1989.

Lycée Jean Mermoz: Lycée Jean Mermoz may refer to:

Avenue Berthelot: Avenue Berthelot is a street in the 7th (Guillotière) and 8th arrondissement (Bachut) of Lyon which connects the bridge Galliéni at the east to the A43 highway via the Avenue Jean Mermoz which extends it to the west.

47th Vanier Cup: The 2011 Vanier Cup, the 47th edition of the Canadian university football championship, took place on Friday, November 25, 2011 at BC Place in Vancouver.  The McMaster Marauders defeated the Laval Rouge et Or 41-38 in only the second ever Vanier Cup to go into overtime.  The Marauders won their first ever national championship while the Rouge et Or lost a Vanier Cup game for the first time.  BC Place underwent a renovation, including a retractable roof, and hosted the Vanier Cup on the same weekend it hosted the Grey Cup.  This marked the first time the two games were played at the same venue on the same weekend since 2007.  This Vanier Cup is notable for being considered one of the best Canadian football games ever played.

Jean Mermoz: Jean Mermoz (9 December 1901, Aubenton, Aisne – 7 December 1936) was a French aviator, viewed as a hero by many in both Argentina and his native France, where many schools bear his name.  In Brazil, he also is recognized as a pioneer aviator.

Lycée Franco-Argentin Jean Mermoz: Lycée Franco-Argentin Jean Mermoz (Spanish: Liceo Jean Mermoz ) is a large French– Argentine school constituted by three educational levels.  The school building is situated in the Buenos Aires neighbourhood of Núñez, Argentina.

Question: Which one is younger, Raymond Vanier or Jean Mermoz? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "individuals_compared": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "birth_date": {
            "type": "string",
            "format": "date"
          }
        },
        "required": [
          "name",
          "birth_date"
        ],
        "additionalProperties": false
      }
    },
    "younger_individual_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_date": {
          "type": "string",
          "format": "date"
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "comparison_summary": {
      "type": "string"
    }
  },
  "required": [
    "individuals_compared",
    "younger_individual_details",
    "comparison_summary"
  ],
  "additionalProperties": false
}
