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
Clausura 2017 Copa MX Final: The Clausura 2017 Copa MX Final was the final of the Clausura 2017 Copa MX, the tenth edition of the Copa MX under its current format and 77th overall organized by the Mexican Football Federation, the governing body of association football in Mexico.

Apertura 2015 Copa MX Final: The Apertura 2015 Copa MX Final was the final of the Apertura 2015 Copa MX, the seventh edition of the Copa MX under its current format and 74th overall organized by the Mexican Football Federation, the governing body of association football in Mexico.

Clausura 2014 Copa MX Final: The Clausura 2014 Copa MX Final was the final of the Clausura 2014 Copa MX the fourth edition of the Copa MX under its current format and 71st overall organized by the Mexican Football Federation, the governing body of association football in Mexico.

Corona (beer): Corona Extra is a pale lager produced by Cervecería Modelo in Mexico for domestic distribution and export to all other countries besides the United States, and by Constellation Brands in Mexico for export to the United States.

Clausura 2016 Copa MX Final: The Clausura 2016 Copa MX Final was the final of the Clausura 2016 Copa MX, the eighth edition of the Copa MX under its current format and 75th overall organized by the Mexican Football Federation, the governing body of association football in Mexico.

Clausura 2015 Copa MX Final: The Clausura 2015 Copa MX Final was the final of the Clausura 2015 Copa MX, the sixth edition of the Copa MX under its current format and 73rd overall organized by the Mexican Football Federation, the governing body of association football in Mexico.

Apertura 2014 Copa MX Final: The Apertura 2014 Copa MX Final was the final of the Apertura 2014 Copa MX, the fifth edition of the Copa MX under its current format and 72nd overall organized by the Mexican Football Federation, the governing body of association football in Mexico.

Copa MX: The Copa MX (formerly called Copa Tower, Copa Eliminatoria, and Copa México) is a Mexican football cup competition that was established in 1907.  After a lengthy hiatus that began in 1997, it was restored in 2012.  The cup is currently sponsored by Corona Extra and thus officially known as the Copa Corona MX.

Apertura 2016 Copa MX Final: The Apertura 2016 Copa MX Final was the final of the Apertura 2016 Copa MX, the ninth edition of the Copa MX under its current format and 76th overall organized by the Mexican Football Federation, the governing body of association football in Mexico.

Apertura 2013 Copa MX Final: The Apertura 2013 Copa MX Final was the final of the Apertura 2013 Copa MX the third edition of the Copa MX under its current format and 70th overall organized by the Mexican Football Federation, the governing body of association football in Mexico.

Question: The drink which currently sponsors the Copa MX is produced by who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "sponsoring_drink_name": {
      "type": "string",
      "description": "The name of the drink that sponsors the competition."
    },
    "producer_entity": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the entity that produces the sponsoring drink."
        },
        "country_of_origin": {
          "type": "string",
          "description": "The country where the producer is located or primarily operates."
        }
      },
      "required": [
        "name",
        "country_of_origin"
      ],
      "additionalProperties": false
    },
    "sponsored_competition_name": {
      "type": "string",
      "description": "The name of the competition being sponsored."
    }
  },
  "required": [
    "sponsoring_drink_name",
    "producer_entity",
    "sponsored_competition_name"
  ],
  "additionalProperties": false
}
