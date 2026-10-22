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
UEFA Euro 2004 Group A: Group A of UEFA Euro 2004 was one of four groups in the final tournament's initial group stage.  It began on 12 June and was completed on 20 June.  The group consisted of hosts Portugal, Spain, Russia and Greece.

UEFA Euro 2004 Group B: Group B of UEFA Euro 2004 was one of four groups in the final tournament's initial group stage.  It began on 13 June and was completed on 21 June.  The group consisted of defending champions France, England, Croatia and Switzerland.

UEFA Euro 1984 Group 2: Group 2 of UEFA Euro 1984 was one of only two groups in the final tournament's initial group stage.  It began on 14 June and was completed on 20 June.  The group consisted of West Germany, Spain, Portugal, and Romania.

UEFA Euro 1996 Group B: Group B of UEFA Euro 1996 was one of four groups in the final tournament's initial group stage.  It began on 9 June and was completed on 18 June.  The group consisted of France, Spain, Bulgaria and Romania.

France national football team: The France national football team (French: "Équipe de France de football" ) represents France in international football.  The team's colours are blue, white and red, and the "coq gaulois" its symbol.  France are colloquially known as "Les Bleus" (The Blues).

UEFA Euro 1996 Group A: Group A of UEFA Euro 1996 was one of four groups in the final tournament's initial group stage.  It began on 8 June and was completed on 18 June.  The group consisted of hosts England, Switzerland, the Netherlands and Scotland.

UEFA Euro 1992 Group 1: Group 1 of UEFA Euro 1992 was one of only two groups in the final tournament's initial group stage.  It began on 10 June and was completed on 17 June.  The group consisted of hosts Sweden, fellow Scandinavians Denmark, France and England.

UEFA Euro 2004 Group C: Group C of UEFA Euro 2004 was one of four groups in the final tournament's initial group stage.  It began on 14 June and was completed on 22 June.  The group consisted of Italy, Denmark, Sweden and Bulgaria.

UEFA Euro 1984 Group 1: Group 1 of UEFA Euro 1984 was one of only two groups in the final tournament's initial group stage.  It began on 12 June and was completed on 19 June.  The group consisted of hosts France, Belgium, Denmark, and Yugoslavia.

UEFA Euro 1992 Group 2: Group 2 of UEFA Euro 1992 was one of only two groups in the final tournament's initial group stage.  It began on 12 June and was completed on 18 June.  The group consisted of the Netherlands, Scotland, Germany and the CIS, a team composed of players from 12 of the 15 former Soviet Union members.

Question: Group 1 of UEFA Euro 1992 was one of only two groups in the final tournament's initial group stage, it consisted of hosts Sweden, fellow Scandinavians Denmark, France and England, the France national football team, represents which country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "team_name": {
      "type": "string",
      "description": "The official name of the national football team."
    },
    "represented_country": {
      "type": "string",
      "description": "The country that the national football team represents."
    },
    "team_attributes": {
      "type": "object",
      "properties": {
        "colloquial_name": {
          "type": "string",
          "description": "The common or informal name for the team."
        },
        "symbol": {
          "type": "string",
          "description": "The symbol associated with the team."
        },
        "colors": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The primary colors of the team's kit."
        }
      },
      "required": [
        "colloquial_name",
        "symbol",
        "colors"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "team_name",
    "represented_country",
    "team_attributes"
  ],
  "additionalProperties": false
}
