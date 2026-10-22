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
2014 Wimbledon Championships – Men's Doubles: Bob and Mike Bryan were the defending champions, but lost to Vasek Pospisil and Jack Sock in the final, 7–6, 6–7, 6–4, 3–6, 7–5.

2016 BNP Paribas Open – Men's Doubles: Vasek Pospisil and Jack Sock were the defending champions, but lost in the final to Pierre-Hugues Herbert and Nicolas Mahut, 3–6, 6–7.

1976 Volvo International – Doubles: Haroon Rahim and Erik Van Dillen were the defending champions but only Van Dillen competed that year with Dick Crealy.

Steve Johnson (tennis): Steve "Stevie" Johnson Jr. (born December 24, 1989) is an American professional tennis player.  For 1 week in August 2016 he was the top ranked American in men's singles.  He has a career high ranking of world number 21.  He has won four ATP Challenger Tour titles and two ATP Tour 250 titles at Nottingham on grass and at Houston on clay.  He won a bronze medal in men's doubles at the 2016 Olympics with Jack Sock.

Jack Sock: Jack Sock (born September 24, 1992) is an American professional tennis player who is currently ranked world No. 21 in men's singles by the Association of Tennis Professionals (ATP).  He is one of the top ranked American men in both singles and doubles on the ATP Tour.  A former junior US Open champion, Sock's singles success is highlighted by 7 ATP finals, including three titles.  His career best result came at the 2017 Indian Wells Masters, where he reached the semi-finals.

2016 China Open – Men's Doubles: Vasek Pospisil and Jack Sock were the defending champions, but Pospisil chose to play in Tokyo instead.  Sock played alongside Bernard Tomic but lost in the final to Pablo Carreño Busta and Rafael Nadal, who won 6−7, 6−2, [10−8].

Dick Crealy: Richard Crealy (born 18 September 1944) is an Australian former tennis player most notable for reaching the finals of the Australian Open in 1970, being a member of the 1970 Australian Davis Cup Team, and winning four Grand Slam titles in doubles.

2012 US Open – Mixed Doubles: Melanie Oudin and Jack Sock were the defending champions but lost to Sania Mirza and Colin Fleming in the second round.  <br> Kim Clijsters played her last professional match, in any format, losing in the second round with Bob Bryan to Ekaterina Makarova and Bruno Soares.  Unseeded pair Makarova and Soares ended up winning the title after defeating fourth seeds Květa Peschke and Marcin Matkowski in the final 6–7, 6–1, [12–10].

2014 Nielsen Pro Tennis Championships – Singles: Jack Sock was the defending champion but decided not to participate. <br>

1970 Swedish Open: The 1970 Swedish Open was a combined men's and women's tennis tournament played on outdoor clay courts held in Båstad, Sweden and was part of the Grand Prix circuit of the 1970 Tour.  It was the 23rd edition of the tournament and was held from 2 July through 12 July 1970.  Dick Crealy and Peaches Bartkowicz won the singles titles.

Question: Did Dick Crealy and Jack Sock play the same sport?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "played_same_sport": {
      "type": "boolean",
      "description": "Indicates whether Dick Crealy and Jack Sock played the same sport."
    },
    "common_sport": {
      "type": "string",
      "description": "The name of the sport they both played."
    },
    "player_details": {
      "type": "array",
      "description": "Details for each player mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "player_name": {
            "type": "string",
            "description": "The name of the player."
          },
          "sport_mentioned_in_context": {
            "type": "string",
            "description": "The sport associated with the player as stated in the context."
          }
        },
        "required": [
          "player_name",
          "sport_mentioned_in_context"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "played_same_sport",
    "common_sport",
    "player_details"
  ],
  "additionalProperties": false
}
