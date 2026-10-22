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
1969 New Year Honours: The New Year Honours 1969 were appointments in many of the Commonwealth realms of Queen Elizabeth II to various orders and honours to reward and highlight good works by citizens of those countries.  They were announced in supplements to the "London Gazette" of 20 December 1968 to celebrate the year passed and mark the beginning of 1969.  At this time honours for Australians were awarded both in the United Kingdom honours, on the advice of the premiers of Australian states, and also in a separate Australia honours list.

1989 New Year Honours: The New Year Honours 1989 were appointments by most of the Commonwealth realms of Queen Elizabeth II to various orders and honours to reward and highlight good works by citizens of those countries, and honorary ones to citizens of other countries.  They were announced on 31 December 1988 to celebrate the year passed and mark the beginning of 1989 in the United Kingdom, Australia, New Zealand, Mauritius, the Bahamas, Grenada, Papua New Guinea, the Solomon Islands, Saint Vincent and The Grenadines, Belize, Antigua and Barbuda, and Saint Christopher and Nevis.

1984 New Year Honours: The New Year Honours 1984 were appointments by most of the Commonwealth realms of Queen Elizabeth II to various orders and honours to reward and highlight good works by citizens of those countries, and honorary ones to citizens of other countries.  They were announced on 31 December 1983 to celebrate the year passed and mark the beginning of 1984 in the United Kingdom, New Zealand and the Cook Islands, Fiji, the Bahamas, Papua New Guinea, the Solomon Islands, Saint Lucia, Saint Vincent and the Grenadines, and Antigua and Barbuda.

1961 New Year Honours: The New Year Honours 1961 were appointments by many of the Commonwealth realms of Queen Elizabeth II to various orders and honours to reward and highlight good works by citizens of those countries.  They were announced on 31 December 1960 in the United Kingdom, Australia, New Zealand, Nigeria, and Rhodesia and Nyasaland to celebrate the year passed and mark the beginning of 1961.

1966 New Year Honours: The New Year Honours 1966 were appointments in many of the Commonwealth realms of Queen Elizabeth II to various orders and honours to reward and highlight good works by citizens of those countries.  They were announced in supplements to the "London Gazette" of 31 December 1965 to celebrate the year passed and mark the beginning of 1966.  At this time honours for Australians were awarded both in the United Kingdom honours, on the advice of the premiers of Australian states, and also in a separate Australia honours list.

Commonwealth realm: A Commonwealth realm is a sovereign state that is a member of the Commonwealth of Nations and shares the same person, currently Elizabeth II, as its head of state and reigning constitutional monarch, but retains a crown legally distinct from the other realms.  As of 2017, there are 16 Commonwealth realms: Antigua and Barbuda, Australia, Barbados, Belize, Canada, Grenada, Jamaica, New Zealand, Papua New Guinea, Saint Kitts and Nevis, Saint Lucia, Saint Vincent and the Grenadines, Solomon Islands, The Bahamas, Tuvalu and the United Kingdom.

1988 New Year Honours: The New Year Honours 1988 were appointments by most of the Commonwealth realms of Queen Elizabeth II to various orders and honours to reward and highlight good works by citizens of those countries, and honorary ones to citizens of other countries.  They were announced on 31 December 1987 to celebrate the year passed and mark the beginning of 1988 in the United Kingdom, Australia, New Zealand, Mauritius, the Bahamas, Grenada, Papua New Guinea, the Solomon Islands, Saint Lucia, Saint Vincent and the Grenadines, Belize, Antigua and Barbuba, and Gibraltar.

1986 New Year Honours: The New Year Honours 1986 were appointments by most of the Commonwealth realms of Queen Elizabeth II to various orders and honours to reward and highlight good works by citizens of those countries, and honorary ones to citizens of other countries.  They were announced on 30 December 1985 to celebrate the year passed and mark the beginning of 1986 in the United Kingdom, New Zealand, Mauritius, Fiji, the Bahamas, Grenada, Papua New Guinea, the Solomon Islands, Saint Lucia, Saint Vincent and the Grenadines, Belize, Antigua and Barbuda, and Saint Christopher and Nevis.

1983 New Year Honours: The New Year Honours 1983 were appointments by most of the Commonwealth realms of Queen Elizabeth II to various orders and honours to reward and highlight good works by citizens of those countries, and honorary ones to citizens of other countries.  They were announced on 31 December 1982 to celebrate the year passed and mark the beginning of 1983 in the United Kingdom, Australia, New Zealand and Cook Islands, the Bahamas, Fiji, Papua New Guinea, Solomon Islands, Tuvalu, St. Lucia, St. Vincent & Grenadines, and Antigua & Barbuda.

1985 New Year Honours: The New Year Honours 1985 were appointments by most of the Commonwealth realms of Queen Elizabeth II to various orders and honours to reward and highlight good works by citizens of those countries, and honorary ones to citizens of other countries.  They were announced on 31 December 1984 to celebrate the year passed and mark the beginning of 1985 in the United Kingdom, New Zealand, Barbados, Mauritius, Fiji, the Bahamas, Papua New Guinea, the Solomon Islands, Tuvalu, Saint Lucia Saint Vincent and the Grenadines, Antigua and Barbuda, and Saint Christopher and Nevis.

Question: The New Year Honours 1961 were appointments by many of the Commonwealth realms of Queen Elizabeth II to various orders and honours to reward and highlight good works by citizens of those countries, which type of location is a sovereign state that is a member of the Commonwealth of Nations and shares the same person, currently Elizabeth II, as its head of state and reigning constitutional monarch, but retains a crown legally distinct from the other realms?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "defined_term": {
      "type": "string",
      "description": "The term being defined."
    },
    "definition": {
      "type": "string",
      "description": "The complete definition of the term."
    },
    "attributes": {
      "type": "object",
      "properties": {
        "is_sovereign_state": {
          "type": "boolean",
          "description": "Indicates if the entity is a sovereign state."
        },
        "is_member_of_commonwealth_of_nations": {
          "type": "boolean",
          "description": "Indicates if the entity is a member of the Commonwealth of Nations."
        },
        "head_of_state": {
          "type": "object",
          "properties": {
            "person": {
              "type": "string",
              "description": "The person who is the head of state."
            },
            "role": {
              "type": "string",
              "description": "The role of the head of state."
            },
            "shared_with_other_realms": {
              "type": "boolean",
              "description": "Indicates if the head of state is shared with other realms."
            }
          },
          "required": [
            "person",
            "role",
            "shared_with_other_realms"
          ],
          "additionalProperties": false
        },
        "crown_status": {
          "type": "string",
          "description": "Describes the legal status of its crown relative to other realms."
        }
      },
      "required": [
        "is_sovereign_state",
        "is_member_of_commonwealth_of_nations",
        "head_of_state",
        "crown_status"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "defined_term",
    "definition",
    "attributes"
  ],
  "additionalProperties": false
}
