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
Tupelo Bay Formation: The Tupelo Bay Formation is a geologic formation in South Carolina.  It preserves fossils dating back to the Paleogene period.

Georgian Bay Formation: The Georgian Bay Formation is a geologic formation in Michigan.  It preserves fossils dating back to the Ordovician period.

Ellis Bay Formation: The Ellis Bay Formation is a geologic formation in Quebec.  It preserves fossils dating back to the Ordovician period.

Sargent Bay Formation: The Sargent Bay Formation is a geologic formation in Quebec.  It preserves fossils dating back to the Silurian period.

Bush Bay Formation: The Bush Bay Formation is a geologic formation in Michigan.  It preserves fossils dating back to the Silurian period.

Egmont Bay Formation: The Egmont Bay Formation is a geologic formation in Prince Edward Island.  It preserves fossils dating back to the Carboniferous period.

Shallow Bay Formation: The Shallow Bay Formation is a geologic formation in Newfoundland and Labrador.  It preserves fossils dating back to the Ordovician period.

Red Bay Formation: The Red Bay Formation is a geologic formation in Florida.  It preserves fossils dating back to the Neogene period.

Back Bay Formation: The Back Bay Formation is a geologic formation in New Brunswick.  It preserves fossils dating back to the Silurian period.

New Brunswick: New Brunswick (French: "Nouveau-Brunswick" ; ) is one of Canada's three Maritime provinces (together with Prince Edward Island and Nova Scotia) and is the only constitutionally bilingual (English–French) province.  The principal cities are Fredericton, the capital, Greater Moncton, currently the largest metropolitan (CMA) area and the most populous city, and the port city of Saint John, which was the first incorporated city in Canada and largest in the province for 231 years until 2016.

Question: Which one of Canada's three Maritime provinces is The Back Bay Formation  a geologic formation in

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "formation_name": {
      "type": "string",
      "description": "The name of the geologic formation."
    },
    "located_in_province_or_state": {
      "type": "string",
      "description": "The province or state where the formation is located."
    },
    "is_maritime_province": {
      "type": "boolean",
      "description": "Indicates if the location is one of Canada's Maritime provinces."
    },
    "maritime_provinces_of_canada": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of Canada's Maritime provinces mentioned in the context."
    },
    "answer_maritime_province": {
      "type": "string",
      "description": "The specific Maritime province where the formation is located, if applicable."
    }
  },
  "required": [
    "formation_name",
    "located_in_province_or_state",
    "is_maritime_province",
    "maritime_provinces_of_canada",
    "answer_maritime_province"
  ],
  "additionalProperties": false
}
