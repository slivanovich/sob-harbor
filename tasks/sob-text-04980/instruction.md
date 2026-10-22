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
Malcolm &amp; Eddie: Malcolm & Eddie is an American television sitcom that premiered August 26, 1996 on UPN, and ran for four seasons, airing its final episode on May 22, 2000.  This series starred Malcolm-Jamal Warner and Eddie Griffin in the lead roles.  The program was produced by Jeff Franklin Productions in association with TriStar Television in its first three seasons and by Columbia TriStar Television in its final season.

Full House (season 3): The third season of "Full House", an American family sitcom created by Jeff Franklin, premiered on ABC in the U.S. on September 22, 1989, and concluded on May 4, 1990.  The season was partially directed by Franklin and produced by Jeff Franklin Productions, Miller-Boyett Productions, and Lorimar Television, with Don Van Atta as the producer.  It consists of 24 episodes, most of which were directed by Bill Foster.

Stunt Dawgs: Stunt Dawgs is an animated comedic adventure series (1992–1993) about a team of stunt performers and their bulldog named Human who also solve problems heroically.  The series was produced by Franklin/Waterman 2 and Rainforest Entertainment and co-created by Jeff Franklin, best known for co-producing "Full House".

List of Fuller House episodes: "Fuller House" is an American family sitcom and sequel to the 1987–95 television series "Full House", airing as a Netflix original series.  It was created by Jeff Franklin, and is produced by Jeff Franklin Productions and Miller-Boyett Productions in association with Warner Horizon Television.  The series centers around D.J. Tanner-Fuller, a veterinarian and widowed mother of three sons, whose sister and best friend—the mother to a teenage daughter—provide support in her sons' upbringings by moving in with her.

Fuller House (TV series): Fuller House is an American sitcom created by Jeff Franklin that airs as a Netflix original series, and is a sequel to the 1987–1995 television series "Full House".  It centers around D.J. Tanner-Fuller, a veterinarian and widowed mother of three sons, whose sister Stephanie and best friend Kimmy—along with her teenage daughter—live together at the Tanners' childhood home in San Francisco, California.  Most of the original series ensemble cast have reprised their roles on "Fuller House", either as regular cast members or in guest appearances, with the exception of Mary-Kate and Ashley Olsen, who alternated the role of Michelle Tanner in "Full House."

Full House: Full House is an American sitcom created by Jeff Franklin for ABC.  The show chronicles the events of widowed father, Danny Tanner, who enlists his brother-in-law and best friend to help raise his three daughters.  It aired from September 22, 1987, to May 23, 1995, broadcasting eight seasons and 192 episodes.

Hangin' with Mr. Cooper: Hangin' with Mr. Cooper is an American television sitcom that originally aired on ABC from September 22, 1992 to August 30, 1997, starring Mark Curry and Holly Robinson.  The show took place in Curry's hometown of Oakland, California.  "Hangin' with Mr. Cooper" was produced by Jeff Franklin Productions, in association with Warner Bros.  Television (it was produced by Lorimar Television for the first season only, before it was absorbed by Warner Bros.), and also became produced by Bickley-Warren Productions by the third season.  The show originally aired on Tuesdays in prime time after sister series "Full House" (which was also created by Jeff Franklin and set in the San Francisco Bay Area).  The show found its niche as an addition to the "TGIF" Friday night lineup on ABC, and was part of the lineup from September 1993 to May 1996 (spanning the show's second, third and fourth seasons; airing in-between "Step By Step" and the news magazine series "20/20"), before moving to Saturdays for its fifth and final season.

High Tide (TV series): High Tide is an American television series created by Jeff Franklin and Steve Waterman and starring Rick Springfield and Yannick Bisson.  The syndicated procedural aired from 1994 to 1997 and lasted 66 episodes over three seasons.

Katy Garretson: Kathleen "Katy" Garretson (born May 15, 1963 in Nuremberg, Germany) is an American television director and producer, known for directing the sitcoms Fraiser, 2 Broke Girls, Fuller House and others as well as producing on the Garage Sale Mystery movies.  She received the Frank Capra Achievement Award from the Directors Guild of America (DGA) in 2012 and had other nominations from the DGA for her work.

Kirk (TV series): Kirk is an American family sitcom which aired on The WB from August 23, 1995 to January 12, 1997.  The series was created by Ross Brown, and produced by Bickley-Warren Productions and Jeff Franklin Productions in association with Warner Bros.  Television.  "Kirk" was the follow-up starring vehicle for Kirk Cameron after his seven-year role as Mike Seaver on the popular ABC sitcom "Growing Pains".

Question: What is the American sitcom created by Jeff Franklin and directed by Kathleen Garretson?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "series_title": {
      "type": "string",
      "description": "The title of the American sitcom."
    },
    "series_type": {
      "type": "string",
      "description": "The genre or type of the television series."
    },
    "is_american": {
      "type": "boolean",
      "description": "Indicates if the series is American."
    },
    "creator": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the creator of the series."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "director": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the director of the series."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "series_title",
    "series_type",
    "is_american",
    "creator",
    "director"
  ],
  "additionalProperties": false
}
