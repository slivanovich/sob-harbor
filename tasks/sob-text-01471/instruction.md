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
1968 Wimbledon Championships – Men's Singles: Rod Laver defeated Tony Roche 6–3, 6–4, 6–2 in the final to win the Gentlemen's Singles title at the 1968 Wimbledon Championships.  It was Laver's third Wimbledon title, and his seventh grand slam overall.  This was the first year when professional tennis players were allowed to compete at the Wimbledon Championships.  Previously only amateur tennis players could compete.

Challenge of Champions: The "Challenge of Champions" was created to be one of the richest prize money tennis events in the world.  Created by Leo E. Fenn III in 1985 as an Invitation Only Tennis Tournament which would feature daily matches which were the equivalent to the Finals of the US Open or Wimbledon.  It was usually held before the Masters and invited only the top eight men's tennis players in the world according to their rankings on the ATP poll.  In 1985, creator & founder 24-year-old Leo E. Fenn III partnered with 28-year-old Mark Myden to form a company called Special Events Productions.  SEP produced the "Challenge of Champions" Tournament which became a major player in professional tennis.  These two entrepreneurs became the youngest producers in history of professional tennis.  Leo & Mark acquired major fortune 500 corporate sponsors such as AT&T, VISA, Cadillac, Fila Sportswear, DeBeers Diamonds as well as negotiated two days of live weekend television coverage on NBC.  Their title sponsorship package sold to AT&T was the largest single vent sponsorship package in professional tennis that year.  Leo negotiated with the brand new Thomas Mack Center Arena in Las Vegas to host the inaugural event.  The event rights were eventually sold to Pro Serve and concluded following the 1989 Challenge.

Ryan Harrison (tennis): Ryan Harrison (born May 7, 1992) is an American professional tennis player.  Harrison has won one career ATP title, his lone victory so far coming at the 2017 Memphis Open.  He is currently the 5th-highest ranked U.S.men's singles player.

Serena Williams: Serena Jameka Williams (born September 26, 1981) is an American professional tennis player.  The Women's Tennis Association (WTA) has ranked her world No. 1 in singles on eight occasions, from 2002 to 2017.  She became the world No. 1 for the first time on July 8, 2002.  On the sixth occasion, she held the ranking for 186 consecutive weeks, tying the record set by Steffi Graf for the most consecutive weeks as world No. 1 by a female tennis player.  In total, she has been world No. 1 for 319 weeks, which ranks her third in the Open Era among female tennis players.  Some commentators, players and sports writers regard her as the greatest female tennis player of all time.

Virginia Slims Circuit: The Virginia Slims Circuit was a tennis tour consisting of a group of originally nine female professional players.  Formed in 1970, the Virginia Slims Circuit eventually became the basis for the later named WTA Tour.  The players, dubbed the "Original 9", rebelled against the United States Lawn Tennis Association (USLTA) due to the wide inequality between the amount of prize money paid to male tennis players and to female tennis players.

Michael Venus (tennis): Michael Venus (born 16 October 1987) is a New Zealand professional tennis player.  He reached a career high singles ranking of 274 in July 2011, but is much better known as a leading doubles player with a huge serve.  His highest ranking in this discipline is 12, gained in July 2017.  He won the final of the 2017 French Open partnering with American Ryan Harrison, and followed that with a runner-up finish in the 2017 US Open mixed doubles with Chan Hao-ching of Chinese Taipei as his partner.

Christian Harrison: Christian Harrison (born May 29, 1994) is an American professional tennis player.  He is the younger brother of Ryan Harrison.

Jared Donaldson: Jared Donaldson (born October 9, 1996) is an American professional tennis player from Glocester, Rhode Island.  Jared is a "Next Generation" star on the ATP World Tour of Tennis as he is among a handful of top under-21-years-of-age professional tennis players in the world.  He has won an ATP Challenger title in each of singles and doubles.

John Peers: John William Peers (born 25 July 1988) is an Australian professional tennis player who competed mainly on the ATP Challenger Tour both in singles and doubles until 2013, when he began to focus solely on doubles and began competing on the ATP World Tour.

Athletic DNA: Athletic DNA (ADNA) is an American sports apparel company.  Founded in Seattle in 2007, ADNA began by training young tennis athletes, which evolved into sponsoring Select Junior Tennis players, and then expanded to manufacturing clothing for youth and adult tennis players.  ADNA has since spread to professional tennis, and currently sponsors players on the ATP Tour & WTA Tour.

Question: Are both Ryan Harrison and John Peers American professional tennis players?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question posed."
    },
    "player_nationalities": {
      "type": "array",
      "description": "A list of players and their respective nationalities.",
      "items": {
        "type": "object",
        "properties": {
          "player_name": {
            "type": "string",
            "description": "The name of the tennis player."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the tennis player."
          }
        },
        "required": [
          "player_name",
          "nationality"
        ],
        "additionalProperties": false
      }
    },
    "all_players_are_american": {
      "type": "boolean",
      "description": "Indicates whether all specified players are American."
    },
    "final_answer": {
      "type": "boolean",
      "description": "The boolean answer to the question."
    }
  },
  "required": [
    "question_asked",
    "player_nationalities",
    "all_players_are_american",
    "final_answer"
  ],
  "additionalProperties": false
}
