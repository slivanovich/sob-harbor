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
Milwaukee Brewers Wall of Honor: The Milwaukee Brewers Wall of Honor was established in 2014 to commemorate Brewers players who have made significant contributions to the team.  Retired players who have met any one of seven conditions while playing for the Brewers will be enshrined in to the Wall of Honor.  Active players will be enshrined upon retirement.  These criteria include 2,000 or more plate appearances, 1,000 or more innings pitched, 250 or more games pitched, winning of a major award (Major League Baseball Most Valuable Player Award, Cy Young Award, Rookie of the Year Award, or Fireman of the Year Award), managing a pennant-winning team, being recognized with a statue on the Miller Park Plaza, and being elected to the National Baseball Hall of Fame.

Paul O. Zelinsky: Zelinsky had been one Caldecott runner-up in 1985, 1987, and 1995, the latter for "Swamp Angel" by Anne Isaacs (Dutton, 1994).  Twenty years later, they were joint runners-up for the Phoenix Picture Book Award from the Children's Literature Association, which annually recognizes the best picture book that did not win a major award 20 years earlier.  "Books are considered not only for the quality of their illustrations, but for the way pictures and text work together."

Hank Aaron Award: The Hank Aaron Award is given annually to the Major League Baseball (MLB) players selected as the top hitter in each league, as voted on by baseball fans and members of the media.  It was introduced in 1999 to commemorate the 25th anniversary of Hank Aaron's surpassing of Babe Ruth's career home run mark of 714 home runs.  The award was the first major award to be introduced by Major League Baseball in 19 years.

Perfect game (disambiguation): A Perfect game is a baseball win credited to a single pitcher that throws a complete game of at least nine innings without allowing any opponent to reach first base.  This term may also refer to:

George Will: George Frederick Will (born May 4, 1941) is an American conservative political commentator.  Will writes regular columns for "The Washington Post" and provides commentary for NBC News and MSNBC.  In 1986, "The Wall Street Journal" called him "perhaps the most powerful journalist in America", in a league with Walter Lippmann (1889–1974).  His numerous awards include the Pulitzer Prize for commentary in 1977.

Andrew Clements: Andrew Clements (born May 29, 1949) is an American writer of many children's books.  His debut novel "Frindle" won annual book awards determined by the vote of U.S. schoolchildren in about twenty different U.S. states.  In June 2015 it was named the Phoenix Award winner for 2016 as the best book that did not win a major award when it was published in 1996.

Men at Work: The Craft of Baseball: Men at Work: The Craft of Baseball is a "New York Times" best-selling 1990 book about baseball.  It was written by American Pulitzer Prize–winning author George Will, and published by Macmillan Publishers.  The book focuses on four successful Major League Baseball figures, three of them players, representing different aspects of baseball: a manager, a pitcher, a hitter, and a fielder.

America East Conference baseball awards: At the end of each regular season, the America East Conference names major award winners in baseball.  Currently, it names a Coach, Pitcher, Player, and Rookie of the Year.  With the exception of Rookie of the Year, which was added in 1996, the awards date to the 1990 season, the conference's first season of baseball.  Through the 1996 season, the awards were known as the major awards of the North Atlantic Conference, the America East's former name.

List of all-time Major League Baseball win–loss records: List of all-time Major League Baseball win–loss records

Win probability: Win probability is a statistical tool which suggests a sports team's chances of winning at any given point in a game, based on the performance of historical teams in the same situation.  The art of estimating win probability involves choosing which pieces of context matter.  Baseball win probability estimates often include whether a team is home or away, inning, number of outs, which bases are occupied, and the score difference.  Because baseball proceeds batter by batter, each new batter introduces a discrete state.  There are a limited number of possible states, and so baseball win probability tools usually have enough data to make an informed estimate.

Question: What major award did the writer of Men at Work: The Craft of Baseball win in 1977?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "author_name": {
      "type": "string",
      "description": "The name of the author of the book."
    },
    "book_title": {
      "type": "string",
      "description": "The title of the book mentioned in the question."
    },
    "award_details": {
      "type": "object",
      "properties": {
        "award_name": {
          "type": "string",
          "description": "The name of the major award won by the author."
        },
        "award_year": {
          "type": "integer",
          "description": "The year the award was won."
        }
      },
      "required": [
        "award_name",
        "award_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "author_name",
    "book_title",
    "award_details"
  ],
  "additionalProperties": false
}
