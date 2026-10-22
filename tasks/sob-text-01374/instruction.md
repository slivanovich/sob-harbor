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
1996 ATP Tour World Championships: The 1996 ATP Tour World Championships and the Phoenix ATP Tour World Doubles Championships were tennis tournaments played on indoor carpet courts.  It was the 27th edition of the year-end singles championships, the 23rd edition of the year-end doubles championships and both were part of the 1996 ATP Tour.  The singles tournament took place at the EXPO 2000 Tennis Dome in Hanover in Germany from November 19 through November 24, 1996, while the doubles tournament took place at the Hartford Civic Center in Hartford, Connecticut, in the United States from November 13 through November 17, 1996.

1998 ATP Tour World Championships: The 1998 ATP Tour World Championships (also known for the doubles event as the "Phoenix ATP Tour World Doubles Championship" for sponsorship reasons) was a tennis tournament played on indoor carpet courts.  The surface was called "GreenSet On Wood" which had a wood base coated in synthetic material and provided a medium-pace surface.  It was the 29th edition of the year-end singles championships, the 25th edition of the year-end doubles championships, and both were part of the 1998 ATP Tour.  The singles event took place at the EXPO 2000 Tennis Dome in Hanover, Germany, from 24 November through 29 November 1998, and the doubles event at the Hartford Civic Center in Hartford, Connecticut, United States, from 18 November through 22 November 1998.

1999 ATP Tour World Championships: The 1999 ATP Tour World Championships (also known for the doubles event as the "Phoenix ATP Tour World Doubles Championship" for sponsorship reasons) was a tennis tournament played on indoor carpet courts.  The surface was called "GreenSet On Wood" which had a wood base coated in synthetic material and provided a medium-pace surface.  It was the 30th edition of the year-end singles championships, the 26th edition of the year-end doubles championships, and both were part of the 1999 ATP Tour.  The singles event took place at the EXPO 2000 Tennis Dome in Hanover, Germany, from November 23 through November 28, 1999, and the doubles event at the Hartford Civic Center in Hartford, Connecticut, United States, from November 17 through November 21, 1999.

1990 ATP Tour World Championships: The 1990 ATP Tour World Championships (also known as the 1990 IBM ATP Tour World Championships for sponsorship reasons) were held in Frankfurt, Germany between November 13 and November 18, 1990.

1990 ATP Tour World Championships – Doubles: The 1990 ATP Tour World Championships was a doubles event held in Gold Coast, Australia between November 19 and November 25, 1990.  Guy Forget and Jakob Hlasek won the doubles title at the 1990 ATP Tour World Championships tennis tournament, defeating Sergio Casal and Emilio Sánchez in the final 6–4, 7–6, 5–7, 6–4.

1991 ATP Tour World Championships – Singles: Andre Agassi was the defending champion, but Jim Courier defeated him in the semifinal.

1990 ATP Tour: The 1990 IBM ATP Tour was the first season of the ATP Tour, the newly formed tennis circuit which came in to replace the Grand Prix and WCT tournaments.  It was the elite tour for professional tennis organized by the Association of Tennis Professionals.  In 1990 the IBM ATP Tour included the four Grand Slam tournaments, the ATP Tour World Championships, the ATP Championship Series, Single-Week, the ATP Championship Series and the ATP World Series.  The World Team Cup and Davis Cup are included in this calendar but did not count towards the Tour.

1997 ATP Tour World Championships: The 1997 ATP Tour World Championships (also known for the doubles event as the "Phoenix ATP Tour World Doubles Championship" for sponsorship reasons) were tennis tournaments played on indoor hard courts for the singles event, and indoor carpet courts for the doubles event.  It was the 28th edition of the year-end singles championships, the 24th edition of the year-end doubles championships, and both were part of the 1997 ATP Tour.  The singles event took place at the EXPO 2000 Tennis Dome in Hanover, Germany, from November 11 through November 16, 1997, and the doubles event at the Hartford Civic Center in Hartford, Connecticut, United States, from November 17 through November 23, 1997.

Andre Agassi: Andre Kirk Agassi ( ; born April 29, 1970) is an American retired professional tennis player and former World No. 1 who was one of the sport's most dominant players from the early 1990s to the mid-2000s.  Generally considered by critics and fellow players to be one of the greatest tennis players of all time, Agassi has been called the greatest service returner in the history of the game.  Described by the BBC upon his retirement as "perhaps the biggest worldwide star in the sport's history", Agassi compiled performances that, along with his unorthodox apparel and attitude, saw him cited as one of the most charismatic players in history.  As a result, he is credited for helping to revive the popularity of tennis during the 1990s.

1991 ATP Tour World Championships: The 1991 ATP Tour World Championships (The singles event was also known as the 1991 IBM ATP Tour World Championships whilst the doubles event was also known as the 1991 Standard Bank ATP Tour World Doubles Final for sponsorship reasons) was held in Frankfurt, Germany between November 12 and November 17, 1991.

Question: What 1970 American born tennis player won the 1990 ATP Tour World Championships – Singles?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The full name of the tennis player."
    },
    "player_nationality": {
      "type": "string",
      "description": "The nationality of the tennis player."
    },
    "player_birth_year": {
      "type": "integer",
      "description": "The birth year of the tennis player."
    },
    "tournament_won": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the tournament won."
        },
        "year": {
          "type": "integer",
          "description": "The year the tournament was held."
        },
        "event_type": {
          "type": "string",
          "description": "The specific event type (e.g., Singles, Doubles)."
        }
      },
      "required": [
        "name",
        "year",
        "event_type"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "player_nationality",
    "player_birth_year",
    "tournament_won"
  ],
  "additionalProperties": false
}
