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
2009 Fergana Challenger – Doubles: Konstantin Kravchuk and Łukasz Kubot didn't defend their 2009 title.  Kubot chose to not play and Kravchuk (who partnered up with Lukáš Lacko) lost to more late champions - Pavel Chekhov and Alexey Kedryuk in the quarterfinals.

Henri Kontinen: Henri Kontinen (] ; born 19 June 1990) is a Finnish tennis player.

2016 Open 13 – Doubles: Marin Draganja and Henri Kontinen were the defending champions, but Kontinen chose not to participate.  Draganja played alongside Julian Knowle, but lost in the quarterfinals to Teymuraz Gabashvili and Nick Kyrgios. <br>

2016 Ricoh Open – Men's Doubles: Ivo Karlović and Łukasz Kubot were the defending champions, but Karlović chose not to participate this year and Kubot chose to compete in Stuttgart instead. <br>

2014 Abierto Mexicano Telcel – Men's Doubles: Łukasz Kubot and David Marrero were the defending champions, but chose not to compete together.  Kubot played alongside Robert Lindstedt, but lost to Feliciano López and Max Mirnyi in the quarterfinals.  Marrero teamed up with Ivo Karlović, but lost to López and Mirnyi in the first round.  <br>

Łukasz Kubot: Łukasz Kubot (; born May 16, 1982) is a Polish professional tennis player.  Kubot is a doubles specialist and won the 2014 Australian Open men's doubles title with Robert Lindstedt as well as the 2017 Wimbledon men's doubles title with Marcelo Melo.  He has also had success in singles, achieving a career-high singles ranking of World No. 41 in April 2010 and reaching the quarterfinals of the 2013 Wimbledon Championships.  In 2013 he was awarded the Gold Cross of Merit by Polish President Bronisław Komorowski.

2015 Australian Open – Men's Doubles: Łukasz Kubot and Robert Lindstedt were the defending champions, but chose not to participate together.  Kubot teamed up with Jérémy Chardy, but lost in the second round to Alex Bolt and Andrew Whittington.  Lindstedt played alongside Marcin Matkowski, but lost in the second round to Jonathan Erlich and Treat Huey.

2017 Western &amp; Southern Open – Men's Doubles: Ivan Dodig and Marcelo Melo were the defending champions, but chose not to participate together.  Dodig teamed up with Rohan Bopanna, but lost in the quarterfinals to Melo who partnered Łukasz Kubot.  Kubot and Melo lost in the semifinals to Jamie Murray and Bruno Soares.

2010 Serbia Open – Doubles: Łukasz Kubot and Oliver Marach were the defenders of title, but Kubot chose not to compete this year and Marach chose to play in Munich instead.

2016 Moselle Open – Doubles: Łukasz Kubot and Édouard Roger-Vasselin were the defending champions, but Kubot chose not to participate this year.  Roger-Vasselin played alongside Julien Benneteau, but lost in the first round to Marcus Daniell and Marcelo Demoliner.

Question: What are both Łukasz Kubot and Henri Kontinen?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_profession": {
      "type": "string",
      "description": "The shared profession of both individuals."
    },
    "number_of_players_mentioned": {
      "type": "integer",
      "description": "The total number of players mentioned in the question."
    },
    "players": {
      "type": "array",
      "description": "Details about each player mentioned.",
      "items": {
        "type": "object",
        "properties": {
          "player_name": {
            "type": "string",
            "description": "The full name of the player."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the player."
          },
          "birth_date": {
            "type": "string",
            "description": "The birth date of the player."
          },
          "is_doubles_specialist": {
            "type": "boolean",
            "description": "Indicates if the player is a doubles specialist."
          }
        },
        "required": [
          "player_name",
          "nationality",
          "birth_date"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "common_profession",
    "number_of_players_mentioned",
    "players"
  ],
  "additionalProperties": false
}
