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
America's Got Talent (season 2): The second season of America's Got Talent, an American television reality show talent competition, premiered on the NBC network on June 5, 2007 with a two-hour episode.  Tabloid talk show host Jerry Springer succeeded Regis Philbin as host.  Piers Morgan and David Hasselhoff returned as judges, joined by newcomer Sharon Osbourne.  Brandy Norwood voluntarily stepped down as judge after a wrongful death lawsuit was brought against her for her involvement in a fatal car collision.

Floyd (30 Rock): "Floyd" is the of the fourth season of the American television comedy series "30 Rock", and the 74th overall episode of the series.  It was written by series producer Paula Pell, and directed by Millicent Shelton.  The episode originally aired on the National Broadcasting Company (NBC) network in the United States on March 25, 2010.  Cheyenne Jackson, Kristin McGee, and Jason Sudeikis guest star in this episode, and there are cameo appearances by Kathie Lee Gifford, Lester Holt, Hoda Kotb, and Meredith Vieira.

The Joey Bishop Show (talk show): The Joey Bishop Show is an American talk show that had its first broadcast on ABC on April 17, 1967, hosted by Joey Bishop and featuring Regis Philbin in his first ongoing role with national television exposure, as Bishop's sidekick/announcer (similar to Ed McMahon's job with Johnny Carson).  Created to challenge "The Tonight Show Starring Johnny Carson", the show lasted 33 months, with the last show airing on December 26, 1969.

The Neighbors (game show): The Neighbors is an American game show.  It aired on ABC from December 29, 1975 to April 9, 1976.  It included five female neighbors as contestants, who were asked gossip questions about each other.  Regis Philbin co-hosted the show with Jane Nelson, and Joe Seiter was the announcer.  It was produced by Bill Carruthers.

List of Live episodes: The daytime talk show "Live with Kelly and Ryan", starring Kelly Ripa and Ryan Seacrest, officially debuted on May 1, 2017, but is a continuation of the series that previously co-starred Regis Philbin or Michael Strahan.

Kathie Lee Gifford: Kathryn "Kathie" Lee Gifford (née Epstein, previously Johnson; born August 16, 1953) is an American television host, singer, songwriter, comedian, and actress, best known for her 15-year run (1985–2000) on the talk show "Live!  with Regis and Kathie Lee", which she co-hosted with Regis Philbin.  She has received 11 Daytime Emmy nominations and won her first Daytime Emmy in 2010 as part of the "Today" team.

Scott Flansburg: Scott Flansburg (born December 28, 1963) is an American man who is often called a mental calculator.  Dubbed "The Human Calculator" by Regis Philbin, in 2001 he was entered into the "Guinness Book of World Records" for speed of mental calculation.  He is the annual host and ambassador for World Maths Day, and is a math educator and media personality.  Flansburg has published the books "Math Magic" and "Math Magic for Your Kids".

Who Wants to Be Me?: Who Wants To Be Me?  is a 2000 book by Regis Philbin.  It is a response to the success of the game show "Who Wants to Be a Millionaire? " and deals with more antics about the show and Philbin's life.

America's Got Talent (season 1): The first season of "America's Got Talent" premiered on June 21, 2006 and concluded on August 17, 2006.  The audition tour took place in April 2006, stopping at Los Angeles, New York, and Chicago.  Regis Philbin was the host for this season.  David Hasselhoff, Brandy Norwood, and Piers Morgan were the judges.  This season's winner was Bianca Ryan.

J. J. Philbin: Jennifer Joy "J. J." Philbin (born August 30, 1974) is an American producer and screenwriter.  She is best known for her work on the drama series "The O.C." and is the daughter of television star Regis Philbin and his wife Joy Philbin.

Question: What series features a cameo by co host of a show with Regis Philbin, in the episode "Floyd"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "series_name": {
      "type": "string",
      "description": "The name of the television series."
    },
    "episode_name": {
      "type": "string",
      "description": "The name of the specific episode mentioned."
    },
    "cameo_details": {
      "type": "object",
      "properties": {
        "person_name": {
          "type": "string",
          "description": "The name of the person who made a cameo appearance."
        },
        "co_hosted_show_with_regis": {
          "type": "string",
          "description": "The name of the show this person co-hosted with Regis Philbin."
        },
        "co_host_role": {
          "type": "string",
          "description": "The role of the person in the show co-hosted with Regis Philbin."
        }
      },
      "required": [
        "person_name",
        "co_hosted_show_with_regis",
        "co_host_role"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "series_name",
    "episode_name",
    "cameo_details"
  ],
  "additionalProperties": false
}
