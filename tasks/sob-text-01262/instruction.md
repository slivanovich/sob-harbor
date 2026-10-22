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
Down Cathedral: Down Cathedral, the Cathedral Church of the Holy and Undivided Trinity, is a Church of Ireland cathedral located in the town of Downpatrick in Northern Ireland.  It stands on Cathedral Hill overlooking the town.  It is one of two cathedrals in the Diocese of Down and Dromore (the other is Dromore Cathedral) in the Province of Armagh.  The cathedral is centre point in Downpatrick.

Carlisle Cathedral: The Cathedral Church of the Holy and Undivided Trinity, otherwise called Carlisle Cathedral, is the seat of the Anglican Bishop of Carlisle.  It is located in Carlisle, in Cumbria, North West England.  It was founded as an Augustinian priory and became a cathedral in 1133.

Diocese of Bristol: The Diocese of Bristol is a Church of England diocese in the Province of Canterbury, England.  It is based in the city of Bristol and covers South Gloucestershire and parts of north Wiltshire to Swindon.  The diocese is headed by the Bishop of Bristol and the Episcopal seat is located at the Cathedral Church of the Holy and Undivided Trinity, commonly known as Bristol Cathedral.

The Cathedral Church of the Holy and Undivided Trinity: The Cathedral Church of the Holy and Undivided Trinity

Dean of Down: The Dean of Down is based in The Cathedral Church of the Holy and Undivided Trinity, Downpatrick within the Diocese of Down and Dromore of the Church of Ireland.

North West England: North West England, one of nine official regions of England, consists of the five counties of Cheshire, Cumbria, Greater Manchester, Lancashire and Merseyside.  The North West had a population of 7,052,000 in 2011.  It is the third most populated region in the United Kingdom after the South East and Greater London.

Bristol Cathedral: Bristol Cathedral, formally the Cathedral Church of the Holy and Undivided Trinity, is the Church of England cathedral in the city of Bristol, England.  Founded in 1140 and consecrated in 1148, it was originally St Augustine's Abbey but after the Dissolution of the Monasteries it became in 1542 the seat of the newly created Bishop of Bristol and the cathedral of the new Diocese of Bristol.  It is a Grade I listed building.

Bishop of Down: The Bishop of Down was an episcopal title which took its name from the town of Downpatrick in Northern Ireland.  The bishop's seat (Cathedra) was located on the site of the present cathedral church of the Holy and Undivided Trinity in the Church of Ireland.

Norwich Cathedral: Norwich Cathedral is an English cathedral located in Norwich, Norfolk, dedicated to the "Holy and Undivided Trinity".  It is the cathedral church for the Church of England Diocese of Norwich and is one of the Norwich 12 heritage sites.

Dean of Bristol: The Dean of Bristol is the head of the Chapter of the Cathedral Church of the Holy and Undivided Trinity, Bristol, England.  The current Dean is the Very Reverend David Hoyle, whose nomination was approved by Elizabeth II on 22 December 2009 and who was installed at the cathedral on 29 May 2010.

Question: What was the population in 2011 of the English region where The Cathedral Church of the Holy and Undivided Trinity is located ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "cathedral_dedication": {
      "type": "string",
      "description": "The formal dedication of the cathedral."
    },
    "cathedral_common_name": {
      "type": "string",
      "description": "The common name of the specific cathedral identified."
    },
    "cathedral_location_city": {
      "type": "string",
      "description": "The city where the cathedral is located."
    },
    "english_region": {
      "type": "string",
      "description": "The English region where the cathedral is located."
    },
    "region_population": {
      "type": "integer",
      "description": "The population of the identified English region."
    },
    "population_year": {
      "type": "integer",
      "description": "The year for which the population data is provided."
    }
  },
  "required": [
    "cathedral_dedication",
    "cathedral_common_name",
    "cathedral_location_city",
    "english_region",
    "region_population",
    "population_year"
  ],
  "additionalProperties": false
}
