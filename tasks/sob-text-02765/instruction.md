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
Billie Jean King: Billie Jean King ("née" Moffitt; born November 22, 1943) is an American former World No. 1 professional tennis player.  King won 39 Grand Slam titles: 12 in singles, 16 in women's doubles, and 11 in mixed doubles.  King won the singles title at the inaugural WTA Tour Championships.  King often represented the United States in the Federation Cup and the Wightman Cup.  She was a member of the victorious United States team in seven Federation Cups and nine Wightman Cups.  For three years, King was the United States' captain in the Federation Cup.

1980 Avon Championships of Los Angeles: The 1980 Avon Championships of Los Angeles was a women's tennis tournament played on indoor carpet courts at the Forum in Los Angeles, California in the United States that was part of the 1980 Avon Championships circuit.  It was the seventh edition of the tournament and was held from February 4 through February 10, 1980.  First-seeded Martina Navratilova won the singles title and earned $24,000 first-prize money.

1980 Avon Championships of Cincinnati: The 1980 Avon Championships of Cincinnati was a women's tennis tournament played on indoor carpet courts at the Riverfront Coliseum in Cincinnati, Ohio in the United States that was part of the 1980 Avon Championships Circuit.  It was the inaugural edition of the tournament and was held from January 7 through January 13, 1980.  Second-seeded Tracy Austin won the singles title and earned $30,000 first-prize money.

1980 Avon Championships of Boston: The 1980 Avon Championships of Boston was a women's tennis tournament played on indoor carpet courts at the Boston University Walter Brown Arena in Boston, Massachusetts in the United States that was part of the 1980 Avon Championships circuit.  It was the seventh edition of the tournament and was held from March 10 through March 16, 1980.  First-seeded Tracy Austin won the singles title and earned $24,000 first-prize money.

1980 WTA Tour: The 1980 Avon Championships World Championship Series was the 10th season since the foundation of the Women's Tennis Association.  It commenced on January 7, 1980, and concluded on December 24, 1980, after 36 events.  The Avon Championships World Championship Series was the elite tour for professional women's tennis organised by the Women's Tennis Association (WTA).  The year is divided into two sponsors with the first three months sponsored by "Avon Series" and the latter part by "Colgate Series".  It included the four Grand Slam tournaments and a series of other events.  ITF tournaments were not part of the tour, although they awarded points for the WTA World Ranking.

1980 Avon Championships of Seattle: The 1980 Avon Championships of Seattle was a women's tennis tournament played on indoor carpet courts at the Seattle Center Arena in Seattle, Washington in the United States that was part of the 1980 Avon Championships Circuit.  It was the fourth edition of the tournament and was held from January 28 through February 3, 1980.  Second-seeded Tracy Austin won the singles title and earned $30,000 first-prize money.

1980 Avon Championships of Houston: The 1980 Avon Championships of Houston was a women's tennis tournament played on indoor carpet courts at the Summit in Houston, Texas in the United States that was part of the 1980 Avon Championships Circuit.  It was the 10th edition of the tournament and was held from February 25 through March 2, 1980.  Third-seeded Billie Jean King won the singles title and earned $30,000 first-prize money.

1980 Avon Championships of Chicago: The 1980 Avon Championships of Chicago was a women's tennis tournament played on indoor carpet courts at the International Amphitheatre in Chicago, Illinois in the United States that was part of the 1980 Avon Championships Circuit.  It was the ninth edition of the tournament and was held from January 21 through January 27, 1980.  First-seeded Martina Navratilova won the singles title and earned $40,000 first-prize money.

1980 Avon Championships of California: The 1980 Avon Championships of California, also known as the Avon Championships of Oakland, was a women's tennis tournament played on indoor carpet courts at the Oakland Coliseum in Oakland, California in the United States that was part of the 1980 Avon Championships Circuit.  It was the ninth edition of the tournament and was held from February 11 through February 17, 1980.  First-seeded Martina Navratilova won the singles title, her second consecutive at the event, and earned $30,000 first-prize money.

1980 Avon Championships of Detroit: The 1980 Avon Championships of Detroit was a women's tennis tournament played on indoor carpet courts at the Cobo Hall & Arena in Detroit, Michigan in the United States that was part of the 1980 Avon Championships circuit.  It was the ninth edition of the tournament and was held from February 18 through February 24, 1980.  Second-seeded Billie Jean King won the singles title and earned $35,000 first-prize money.

Question: How many Grand Slam titles did the winner of the 1980 Avon Championships of Houston win ? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "tournament_name": {
      "type": "string",
      "description": "The name of the tennis tournament."
    },
    "tournament_year": {
      "type": "integer",
      "description": "The year the tournament was held."
    },
    "winner_name": {
      "type": "string",
      "description": "The name of the singles winner of the tournament."
    },
    "winner_grand_slam_titles": {
      "type": "integer",
      "description": "The total number of Grand Slam titles won by the tournament winner."
    },
    "grand_slam_titles_breakdown": {
      "type": "object",
      "properties": {
        "singles": {
          "type": "integer",
          "description": "Number of Grand Slam singles titles."
        },
        "womens_doubles": {
          "type": "integer",
          "description": "Number of Grand Slam women's doubles titles."
        },
        "mixed_doubles": {
          "type": "integer",
          "description": "Number of Grand Slam mixed doubles titles."
        }
      },
      "required": [
        "singles",
        "womens_doubles",
        "mixed_doubles"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "tournament_name",
    "tournament_year",
    "winner_name",
    "winner_grand_slam_titles",
    "grand_slam_titles_breakdown"
  ],
  "additionalProperties": false
}
