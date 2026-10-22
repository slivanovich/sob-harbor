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
Sarah Iversen: Sarah Iversen (born 10 April 1990) is a Danish handball player.  She currently plays for Nykøbing Falster and the Denmark women's national handball team.

Klavs Bruun Jørgensen: Klavs Hørlykke Bruun Jørgensen (born3 April 1974) is a Danish handball player and coach for the Denmark women's national handball team.  As a player, he led FCK Håndbold to the Danish championship in May 2008.  He has previously played for many years by Danish Handball League rivals GOG, with whom he won two Danish titles.  For a short period he played for German league side SG Wallau-Massenheim

Line Haugsted: Line Haugsted (born 11 November 1994) is a Danish handball player for Viborg HK and the Denmark women's national handball team.

Alice Keighley: Alice Keighley (born 1993) is an Australian team handball and beach handball player.  As a member of the Australian national team, Alice played in the 2011 World Women's Handball Championship in Brazil and in the 2015 IHF Four Nations Tournament in Kazakhstan.  As a member of the Australian Women's Junior Handball Team, she competed in the 2013 IHF Intercontinental World Cup Challenge Trophy in Mexico and the 2012 IHF Oceania Continental Challenge Trophy.  In 2010, she was selected in the Australian Youth Olympic handball team to attend the 2010 Summer Youth Olympics, where the team came 6th.  As a member of the Australia women's national beach handball team, she competed in the 2012 Beach Handball World Championships in Oman, the World Games 2013 in Colombia and the 2014 Beach Handball World Championships in Brazil.

Mie Højlund: Mie Højlund (born 24 October 1997) is a Danish handball player.  She currently plays for Odense Håndbold and the Denmark women's national handball team.

Denmark women's national junior handball team: The Denmark women's junior national handball team is the national under–19 Handball team of Denmark.  Controlled by the Danish Handball Federation it represents Denmark in international matches.

Christina Elm: Christina Elm (born 16 June 1995) is a Danish handball player.  She currently plays for København Håndbold and the Denmark women's national handball team.

Denmark women's national handball team: The Denmark women's national handball team is the national team of Denmark.  It is governed by the Dansk Håndbold Forbund and takes part in international handball competitions.

Bogdan Wenta: Bogdan Wenta (born 19 November 1961) is a former Polish handball player, a member of Poland national handball team in 1981–1994 and Germany national handball team in 1997–2000, a participant of the Olympic Games Sydney 2000, five-time Polish Champion (1984, 1985, 1986, 1987, 1988), former head coach of Poland.  One of the best handball player in history of Polish handball.

Denmark women's national youth handball team: The Denmark women's youth national handball team is the national under–17 Handball team of Denmark.  Controlled by the Danish Handball Federation it represents Denmark in international matches.

Question: Mie Højlund, is a Danish handball player, she currently plays for which organization, and the Denmark women's national handball team?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the handball player."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the player."
    },
    "current_club": {
      "type": "string",
      "description": "The name of the club the player currently plays for."
    },
    "national_team": {
      "type": "string",
      "description": "The name of the national team the player plays for."
    }
  },
  "required": [
    "player_name",
    "nationality",
    "current_club",
    "national_team"
  ],
  "additionalProperties": false
}
