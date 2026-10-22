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
List of The Beverly Hillbillies episodes: "The Beverly Hillbillies" is an American sitcom that aired on CBS from September 26, 1962 to March 23, 1971.  Originally filmed in black and white for the first three seasons (1962-1965), the first color-filmed episode ("Admiral Jed Clampett") was aired on September 15, 1965, and all subsequent episodes from 1965 to 1971 were filmed in color.  During its nine-season run, 274 episodes aired -- 106 in black-and-white, 168 in color.  "The Beverly Hillbillies" was the most-watched television show on the 1962–63 and 1963–64 United States network television schedules, and was also the number-one-rated television show of the 1963–64 United States network television season.

List of The Lucy Show episodes: The following is a list of episodes of "The Lucy Show", an American sitcom television series that ran on CBS from October 1, 1962 to March 11, 1968.

Vivian Vance: Vivian Vance (born Vivian Roberta Jones; July 26, 1909 – August 17, 1979) was an American television and theater actress and singer.  Vance is best known for her role as Ethel Mertz, sidekick to Lucille Ball on the American television sitcom "I Love Lucy", and as Vivian Bagley on "The Lucy Show".

List of I Love Lucy episodes: "I Love Lucy" is an American television sitcom starring Lucille Ball, Desi Arnaz, Vivian Vance, and William Frawley.  The black-and-white series originally ran from October 15, 1951, to May 6, 1957, on the Columbia Broadcasting System (CBS).  All 180 episodes aired on Mondays.

The Lucy–Desi Comedy Hour: The Lucy–Desi Comedy Hour is a collection of thirteen black-and-white one-hour specials airing occasionally from 1957 to 1960 (as opposed to a thirty-minute regular series).  The first five were shown as specials during the 1957–58 television season.  The remaining eight were originally shown as part of "Westinghouse Desilu Playhouse".  Its original network title was The Ford Lucille Ball-Desi Arnaz Show for the first season, and The Westinghouse Desilu Playhouse Presents The Lucille Ball–Desi Arnaz Show for the following seasons.  The successor to the classic comedy, "I Love Lucy", the programs featured the same cast members: Lucille Ball, Desi Arnaz, Vivian Vance, William Frawley, and Little Ricky (billed as Richard Keith in his post-"Lucy–Desi" acting assignments).  The production schedule avoided the grind of a regular weekly series.

Ethel Mertz: Ethel Mae Mertz (née Potter) (alternately "Ethel Louise" and "Ethel Roberta"), played by Vivian Vance, is one of the four main fictional characters in the highly popular 1950s American television sitcom "I Love Lucy".  Ethel is the middle-aged landlady of the main character, Lucy Ricardo, played by Lucille Ball.  Ethel was most likely born about 1905 and was raised in Albuquerque, New Mexico (episode #113).  She is married to Fred Mertz, played by William Frawley, with whom she had a career in vaudeville.  The two female characters are close friends, habitually scheming together; Ethel is generally the voice of reason as a counterpart to Lucy's hare-brained ideas.

Candy Moore: Candy Moore (born August 26, 1947) is an American actress from Maplewood, New Jersey.  Moore began her career appearing on television series such as "Leave It to Beaver" and "Letter to Loretta".  In 1962, she was cast as Lucille Ball's daughter, Chris Carmichael, on CBS's "The Lucy Show".  Moore remained a regular on "The Lucy Show" through the end of the 1964–65 season, after which the premise of the show was retooled and most of the supporting cast was written out.  Moore also appeared nine times on ABC's "The Donna Reed Show", five of which as Angie Quinn, the girlfriend of series character Jeff Stone (Paul Petersen).

Here's Lucy: Here's Lucy is an American sitcom starring Lucille Ball.  The series co-starred her long-time partner Gale Gordon and her real-life children Lucie Arnaz and Desi Arnaz, Jr..  It was broadcast on CBS from 1968 to 1974.  It was Ball's third network sitcom following "I Love Lucy" (1951–57) and "The Lucy Show" (1962–68).

I Love Lucy: I Love Lucy is an American television sitcom starring Lucille Ball, Desi Arnaz, Vivian Vance, and William Frawley.  The black-and-white series originally ran from October 15, 1951 to May 6, 1957 on CBS.  After the series ended in 1957, a modified version continued for three more seasons with 13 one-hour specials; it ran from 1957 to 1960.  It was first known as "The Lucille Ball-Desi Arnaz Show" and later in reruns as "The Lucy–Desi Comedy Hour".

The Lucy Show: The Lucy Show is an American sitcom that aired on CBS from 1962–68.  It was Lucille Ball's follow-up to "I Love Lucy".  A significant change in cast and premise for the 1965–66 season divides the program into two distinct eras; aside from Ball, only Gale Gordon, who joined the program for its second season, remained.  For the first three seasons, Vivian Vance was the co-star.

Question: The Lucy Show is an American sitcom that aired on CBS from 1962–68, for the first three seasons, Vivian Vance was the co-star, Vance was an American television and theater actress and singer, best known for her role as who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress."
    },
    "best_known_role": {
      "type": "string",
      "description": "The role the actress is best known for."
    },
    "show_of_best_known_role": {
      "type": "string",
      "description": "The television show where the actress played her best known role."
    },
    "other_notable_role": {
      "type": "string",
      "description": "Another significant role played by the actress."
    },
    "show_of_other_notable_role": {
      "type": "string",
      "description": "The television show where the actress played the other notable role."
    },
    "lucy_show_details": {
      "type": "object",
      "properties": {
        "series_name": {
          "type": "string",
          "description": "The name of the sitcom mentioned in the question."
        },
        "network": {
          "type": "string",
          "description": "The network the sitcom aired on."
        },
        "run_years": {
          "type": "string",
          "description": "The years the sitcom aired."
        },
        "co_star_seasons": {
          "type": "integer",
          "description": "The number of seasons Vivian Vance co-starred on The Lucy Show."
        }
      },
      "required": [
        "series_name",
        "network",
        "run_years",
        "co_star_seasons"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actress_name",
    "best_known_role",
    "show_of_best_known_role",
    "other_notable_role",
    "show_of_other_notable_role",
    "lucy_show_details"
  ],
  "additionalProperties": false
}
