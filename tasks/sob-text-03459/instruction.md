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
2010 Farmers Classic – Doubles: Bob and Mike Bryan successfully defended their title, defeating Eric Butorac and Jean-Julien Rojer in the finals 6–7, 6–2, [10–7].  The twin brothers set a record of 62 career doubles titles on the ATP Tour, surpassing The Woodies (Todd Woodbridge and Mark Woodforde).  Rojer, who was a UCLA tennis player (1999-2002), returned to play on his college home court.

Andrés Gimeno: Andrés Gimeno Tolaguera (born 3 August 1937) is a retired Spanish tennis player.  His greatest achievement came in 1972, when he won the French Open.

1972 French Open: The 1972 French Open was a tennis tournament that took place on the outdoor clay courts at the Stade Roland Garros in Paris, France.  The tournament ran from 22 May until 4 June.  It was the 71st staging of the French Open, and the second Grand Slam tennis event of 1972.  Andrés Gimeno and Billie Jean King won the singles title.

Wimbledon Pro: The Wimbledon World Lawn Tennis Professional Championships also known as the Wimbledon Pro, was a men's tennis tournament held in August 1967.  The tournament was sponsored and broadcast by the BBC to mark the invention of colour television.  It was the first tournament staged at Wimbledon that was open to male professional tennis players and it had a prize fund of US$45,000.  The singles competition was an eight-man knockout event won by Rod Laver, who received £3,000, whilst the doubles was a four team knockout event won by Andrés Gimeno and Pancho Gonzales.

Patrick Proisy: Patrick Proisy (born 10 September 1949) is a French former professional tennis player best remembered for reaching the finals of the French Open in 1972 losing against Spaniard Andrés Gimeno in four sets.  He added to that one more final (in Florence, 1976) and singles titles in Hilversum, 1977 and Perth, 1972.  Proisy reached a career-high singles ranking of World No. 16 in October 1972.

Alberto Arilla: Alberto Arilla (born December 24, 1937 in Barcelona) is a former Spanish male tennis player.  He usually partnered with his younger brother José Luis, Manuel Santana or Andrés Gimeno in Davis Cup competition, in which he played a total of 8 matches.

1972 Suisse Open Gstaad: The 1972 Suisse Open Gstaad was a men's tennis tournament played on outdoor clay courts in Gstaad, Switzerland.  It was the 27th edition of the tournament and was held from July 10 through July 16, 1972.  The tournament was part of the Grand Prix tennis circuit and was categorized as a Group C event.  Andrés Gimeno won the singles title.  No doubles event took place that year.

1968 Men's National Tennis League: The 1968 Men's National Tennis League (NTL) was the inaugural series of professional tennis tournaments founded by George McCall, among others: Rod Laver, Roy Emerson, Ken Rosewall, Andrés Gimeno, Pancho Gonzales and Fred Stolle.

Albert Costa: Costa began playing tennis at the age of five.  He first came to the tennis world's attention as an outstanding junior player.  In 1993, he reached the French Open junior final and won the Orange Bowl.  He turned professional later that year and quickly established a reputation as a strong clay court player.  Spanish former player and commentator for Spanish television Andrés Gimeno used to call him "the man with two forehands", because he could hit with the same accuracy and strength both forehand and backhand.  In 1994, he won two challenger series events and was named the ATP's Newcomer of the Year.

Mark Woodforde: Mark Raymond Woodforde, OAM (born 23 September 1965) is a former professional tennis player from Australia.  He is best known as one half of "The Woodies", a doubles partnership with Todd Woodbridge.

Question: Which tennis player is older, Mark Woodforde or Andrés Gimeno?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_one_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_year": {
          "type": "integer"
        },
        "birth_month": {
          "type": "string"
        },
        "birth_day": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "birth_year",
        "birth_month",
        "birth_day"
      ],
      "additionalProperties": false
    },
    "player_two_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_year": {
          "type": "integer"
        },
        "birth_month": {
          "type": "string"
        },
        "birth_day": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "birth_year",
        "birth_month",
        "birth_day"
      ],
      "additionalProperties": false
    },
    "older_player_name": {
      "type": "string"
    },
    "age_difference_in_years": {
      "type": "integer"
    }
  },
  "required": [
    "player_one_details",
    "player_two_details",
    "older_player_name",
    "age_difference_in_years"
  ],
  "additionalProperties": false
}
