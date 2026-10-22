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
2000 Women's Cricket World Cup Final: The 2000 Women's Cricket World Cup Final was a women's One Day International cricket match between New Zealand and Australia played on 23 December 2000 at the Bert Sutcliffe Oval in Lincoln, New Zealand.  It was the culmination of the 2000 Women's Cricket World Cup, the seventh Women's Cricket World Cup.  New Zealand won by 4 runs, clinching their first World Cup title, after finishing as runners-up in both the 1993 and 1997 tournaments.  Rick Eyre of "ESPNcricinfo" suggested that it was "the greatest World Cup final ever."

Jaya Sharma: Jaya Sharma (born 17 September 1980 in Ghaziabad) is an Indian cricketer who has played one women's test match and 77 women's one-day internationals including the 2005 Women's Cricket World Cup in South Africa.  Sharma was the first female recipient of the BCCI player of the year award (2007).

Sarah Illingworth: Sarah Louise Illingworth (born 9 September 1963) is a former New Zealand cricketer.  Illingworth played in six women's Test matches, captaining New Zealand in them all, racking up six draws.  New Zealand won 18, lost 10 and had one no result in the 29 women's one-day internationals she captained New Zealand in.  She was born in Lancaster, England. She was the first woman wicket-keeper to effect in 6 dismissals in an innings of a Women's Cricket World Cup match and also holds the joint record for effecting in most dismissals in a Women's Cricket World Cup match along with Venkatacher Kalpana

Alyssa Healy: Alyssa Jean Healy (born 24 March 1990 on the Gold Coast, Queensland) is a cricketer who plays for New South Wales and the Australian women's team.  She made her international debut in February 2010.

Kim Price: Kim Price (born 9 December 1962) in Cape Town.  She is a former South African cricketer who played 26 women's one-day internationals including the 1997 Women's Cricket World Cup in India and the 2000 Women's Cricket World Cup in New Zealand.

Sandamali Dolawatta: Sadamali Kumuduni Dolawatte (born 10 February 1983, Colombo) is a Sri Lankan cricketer who has captained the Sri Lankan women's team in eight one-day internationals, six of them at the 2005 Women's Cricket World Cup.  She has batted in positions from opening to number 10, but her highest score in women's ODI cricket is still the 10 she managed against England in 2005–06.  She regularly bowled leg breaks before captaining the side, but in eight matches as captain she has not bowled more than five overs in any game.

Stephanie Power: Stephanie Judith Power, born 19 April 1957 in Trinidad and Tobago, is a West Indies cricketer.  She has played one Women's Test Match and 34 Women's One-day Internationals for the West Indies in the 1993 Women's Cricket World Cup, 1997 Women's Cricket World Cup and the 2005 Women's Cricket World Cup.

Susan Goatman: Susan Goatman, born 5 February 1945 in Thanet, Kent, is a retired cricketer who has played three women's Test matches for England and 21 women's one-day internationals including at the 1973 Women's Cricket World Cup in England and the 1982 Women's Cricket World Cup in New Zealand.

Rasanjali Silva: Sendapperuma Archchige Rasanjali Chandima de Alwis (née Silva; born 26 November 1971) is a Sri Lankan cricketer who played one women's test match and 22 women's one-day internationals including the 1997 Women's Cricket World Cup in India and the 2000 Women's Cricket World Cup in New Zealand.  Silva later married Sri Lankan Wicket Keeper Guy de Alwis.  They are one of only three married couples along with and the English Roger Prideaux and Ruth Prideaux (née Westbrook) and the Australians Mitchell Starc and Alyssa Starc (née Healy) to have both played Test cricket.

Alison Hodgkinson: Alison Lucille Hodgkinson (born 30 January 1977) in East London.  She is a South African cricketer who has played three women's test matches and 38 women's one-day internationals for South Africa including the 2000 Women's Cricket World Cup in New Zealand and the 2005 Women's Cricket World Cup in South Africa.

Question: Sendapperuma Archchige Rasanjali Chandima de Alwis, is a Sri Lankan cricketer who played one women's test match and 22 women's one-day internationals including the 1997 Women's Cricket World Cup in India and the 2000 Women's Cricket World Cup in New Zealand, one of only three married couples along with the Australians Mitchell Starc, and Alyssa Starc, a cricketer who plays for New South Wales and the Australian women's team, born in which year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The full name of the cricketer whose birth year is being sought."
    },
    "birth_year": {
      "type": "integer",
      "description": "The year the cricketer was born."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the cricketer."
    },
    "team_played_for": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Teams the cricketer plays or played for."
    },
    "related_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person related to the cricketer."
        },
        "relationship": {
          "type": "string",
          "description": "The type of relationship (e.g., spouse)."
        }
      },
      "required": [
        "name",
        "relationship"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "birth_year",
    "nationality",
    "team_played_for",
    "related_person"
  ],
  "additionalProperties": false
}
