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
1981 South Australian Open – Singles: Mark Edmondson won the title, defeating Brad Drewett 7–5, 6–2 in the final.

Mark Edmondson: Mark Edmondson (sometimes mistakenly spelt Edmundson) (born June 1954 in Gosford, New South Wales) is a retired Australian professional tennis player.

1983 Australian Open – Men's Doubles: The Men's Doubles tournament at the 1983 Australian Open was held from 29 November through 11 December 1983 on the outdoor grass courts at the Kooyong Stadium in Melbourne, Australia.  Mark Edmondson and Paul McNamee won the title, defeating Steve Denton and Sherwood Stewart in the final.

1976 Australian Open – Men's Singles: Mark Edmondson upset defending champion John Newcombe 6–7, 6–3, 7–6, 6–1 in the final to win the Men's Singles tennis title at the 1976 Australian Open.  Ranked 212 in the world at the time, Edmondson is still the lowest ranked player ever to win a grand slam since the rankings were introduced in 1973.  Edmondson is also the most recent Australian player to win the Australian Open Men's singles title.

1983 French Open – Men's Doubles: The Men's Doubles tournament at the 1983 French Open was held from 23 May until 5 June 1983 on the outdoor clay courts at the Stade Roland Garros in Paris, France.  Anders Järryd and Hans Simonsson won the title, defeating Mark Edmondson and Sherwood Stewart in the final.

Pierre Barthès: Pierre Barthès (born 13 September 1941) is a French retired professional tour tennis player.

1986 Bavarian Tennis Championships – Doubles: Mark Edmondson and Kim Warwick were the defending champions, but Warwick did not participate this year.  Edmondson partnered Tomáš Šmíd, losing in the semifinals.

1982 South Australian Open – Singles: Mark Edmondson was the defending champion, but did not participate this year.

1984 Volvo International – Doubles: Mark Edmondson and Sherwood Stewart were the defending champions but lost in the semifinals to Brian Gottfried and Tomáš Šmíd.

Hans Simonsson: Hans Simonsson (born 1 May 1962 in Färgaryd) is a retired professional tennis player from Sweden.  Primarily a doubles specialist, he won 12 ATP Tour titles in his career.  He won the French Open doubles title in 1983 with his countryman Anders Järryd.  He also played in the 1983 Davis Cup final for Sweden.  He reached his career high doubles ranking of No. 10 in the world on 2 January 1984.  Simonsson again reached the French Open doubles final in 1985, but he and Schlomo Glickstein were defeated by Mark Edmondson and Kim Warwick.  The Swede finished his career prematurely at the age of 25.  He's the brother of Stefan Simonsson.

Question: Are Pierre Barthès and Mark Edmondson both now retired?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_1_name": {
      "type": "string",
      "description": "The name of the first player mentioned in the question."
    },
    "player_1_is_retired": {
      "type": "boolean",
      "description": "Indicates if the first player is retired."
    },
    "player_2_name": {
      "type": "string",
      "description": "The name of the second player mentioned in the question."
    },
    "player_2_is_retired": {
      "type": "boolean",
      "description": "Indicates if the second player is retired."
    },
    "are_both_retired": {
      "type": "boolean",
      "description": "The final answer to whether both players are retired."
    }
  },
  "required": [
    "player_1_name",
    "player_1_is_retired",
    "player_2_name",
    "player_2_is_retired",
    "are_both_retired"
  ],
  "additionalProperties": false
}
