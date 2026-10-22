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
2013 Morocco Tennis Tour – Kenitra – Singles: Dominic Thiem became the inaugural champion when Teymuraz Gabashvili retired 7–6, 5–1.

2016 Karshi Challenger – Singles: Teymuraz Gabashvili was the defending champion but chose not to participate.

2016 Open 13 – Singles: Gilles Simon was the defending champion, but lost in the first round to Teymuraz Gabashvili.

Dominic Thiem: Dominic Thiem (] ; born 3 September 1993) is an Austrian professional tennis player who has an ATP high ranking of world No. 7 which he first achieved on 6 June 2016.  He has won eight singles titles on the ATP Tour.

2014 Samarkand Challenger – Singles: Teymuraz Gabashvili was the defending champion but decided not to participate.

2016 Fergana Challenger – Men's Singles: Teymuraz Gabashvili was the defending champion, but decided not to defend his title.

2009 Baden Open – Singles: Teymuraz Gabashvili was the defending champion; however, he chose not to play this year.

2014 Tashkent Challenger – Doubles: Mikhail Elgin and Teymuraz Gabashvili were the defending champions, but Gabashvili chose not to compete this year.  Elgin played alongside Alexander Kudryavtsev and lost in the first round to Frank Moser and Alexander Satschko.

2014 Karshi Challenger – Singles: Teymuraz Gabashvili was the defending champion, but decided not to compete.

Nino Serdarušić: Nino Serdarušić (born 13 December 1996) is a Croatian tennis player.  Serdarušić had a career high junior ranking of 21, and partnering Petros Chrysochos, made the doubles semifinals of the 2014 Wimbledon Championships boys' doubles.  He made his ATP main draw debut at the 2014 ATP Vegeta Croatia Open Umag in the doubles event, partnering Dino Marcan, losing in the first round to the second seeds Pablo Cuevas and Horacio Zeballos in three sets.  In 2016, he made his first appearance in an ATP singles final - also in the Croatia Open - losing in straight sets to Teymuraz Gabashvili.

Question: How many singles titles on the ATP tour have been won by the person who replaced Teymuraz Gabashvili as inaugural champion?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the tennis player identified as the inaugural champion."
    },
    "event_details": {
      "type": "object",
      "properties": {
        "event_name": {
          "type": "string",
          "description": "The name of the event where the player became the inaugural champion."
        },
        "event_year": {
          "type": "integer",
          "description": "The year the event took place."
        },
        "opponent_name": {
          "type": "string",
          "description": "The name of the opponent in the final match of the event."
        },
        "opponent_outcome": {
          "type": "string",
          "description": "The outcome for the opponent in the final match."
        }
      },
      "required": [
        "event_name",
        "event_year",
        "opponent_name",
        "opponent_outcome"
      ],
      "additionalProperties": false
    },
    "singles_titles_count": {
      "type": "integer",
      "description": "The total number of singles titles won by the identified player on the ATP Tour."
    }
  },
  "required": [
    "player_name",
    "event_details",
    "singles_titles_count"
  ],
  "additionalProperties": false
}
