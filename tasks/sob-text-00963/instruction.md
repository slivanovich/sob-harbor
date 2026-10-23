{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGary Donnelly (Irish republican): Gary Donnelly is an Irish republican, former Real Irish Republican Army (Real IRA) prisoner, and as of May 24, 2014, an elected member of Derry and Strabane District Council.\n\n1987 Tokyo Indoor – Doubles: Mike De Palmer and Gary Donnelly were the defending champions, but Donnelly did not participate this year.  De Palmer partnered Paul Annacone, losing in the quarterfinals.\n\n1987 Schenectady Open – Doubles: Gary Donnelly and Gary Muller won the title, defeating Brad Pearce and Jim Pugh 7–6, 6–2 in the final.\n\nGary Donnelly: Gary Donnelly (born June 3, 1962) is a former professional tennis player from the United States.\n\nReal Irish Republican Army: The Real Irish Republican Army or Real IRA (RIRA), is a dissident Irish republican paramilitary organisation which aims to bring about a united Ireland.  It formed in 1997 following a split in the Provisional IRA by dissident members, who rejected the IRA's ceasefire that year.  Like the Provisional IRA before it, the RIRA sees itself as the only rightful successor to the original Irish Republican Army and styles itself as \"the Real Irish Republican Army\" in English or \"Óglaigh na hÉireann\" in Irish.  It is an illegal organisation in the Republic of Ireland and designated as proscribed terrorist organisation in the United Kingdom and the United States.\n\n1987 Volvo International – Doubles: Peter Fleming and John McEnroe were the defending champions but they competed with different partners that year, Fleming with Gary Donnelly and McEnroe with his brother Patrick.\n\nÓglaigh na hÉireann (Real IRA splinter group): Óglaigh na hÉireann (ONH; ] ) is the title taken by a small dissident Irish republican paramilitary group that has taken part in the dissident Irish republican campaign.  The organisation started carrying out attacks around 2009 and was formed after a split within the Real IRA.\n\n1987 WCT Scottsdale Open – Doubles: Leonardo Lavalle and Mike Leach were the defending champions, but Lavalle did not participate this year.  Leach partnered Gary Donnelly, losing in the first round.\n\nSergei Aksenov: Sergei Alexandrovich Aksenov (Russian: Серге́й Алекса́ндрович Аксёнов ; born April 3, 1971) is a Russian political dissident, publicist, former prisoner, member of National Bolshevik Party since 1997, cofounder of coalition The Other Russia and one of the leaders of the political party The Other Russia.\n\n1988 OTB Open – Men's Doubles: Gary Donnelly and Gary Muller were the defending champions, but did not participate this year.\n\nQuestion: Gary Donnelly was a former prisoner of which dissident Irish faction?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person in question.\"\n    },\n    \"organization_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the organization.\"\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type or description of the organization.\"\n        },\n        \"is_dissident_faction\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the organization is a dissident faction.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"type\",\n        \"is_dissident_faction\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"relationship_to_organization\": {\n      \"type\": \"string\",\n      \"description\": \"The person's relationship or status concerning the organization.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"organization_details\",\n    \"relationship_to_organization\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person in question."
      },
      "organization_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the organization."
          },
          "type": {
            "type": "string",
            "description": "The type or description of the organization."
          },
          "is_dissident_faction": {
            "type": "boolean",
            "description": "Indicates if the organization is a dissident faction."
          }
        },
        "required": [
          "name",
          "type",
          "is_dissident_faction"
        ],
        "additionalProperties": false
      },
      "relationship_to_organization": {
        "type": "string",
        "description": "The person's relationship or status concerning the organization."
      }
    },
    "required": [
      "person_name",
      "organization_details",
      "relationship_to_organization"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
