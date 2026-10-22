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
Crippled Summer: "Crippled Summer" is the seventh episode and mid-season finale of the fourteenth season of the American animated television series "South Park", and the 202nd overall episode of the series.  It originally aired on Comedy Central in the United States on April 28, 2010.  In the episode, the South Park children try to help Towelie overcome his drug addiction, while Nathan and his lackey Mimsy plot to destroy Jimmy during athletic competitions at a summer camp for handicapped children.

Titties and Dragons: "Titties and Dragons" is the ninth episode in the seventeenth season of the American animated television series "South Park".  The 246th episode of the series overall, it premiered on Comedy Central in the United States on December 4, 2013.  It is the conclusion of a three-episode story arc that began with "Black Friday", and continued with "A Song of Ass and Fire".  The story centers upon the children of South Park, role playing as characters from "Game of Thrones", split into two factions over whether to collectively purchase bargain-priced Xbox One or PlayStation 4 video game consoles at an upcoming Black Friday sale at the local mall, where Randy Marsh has been made the Captain of mall security.  The episode received critical acclaim.

You're Getting Old: "You're Getting Old" is the seventh episode and the mid-season finale of the fifteenth season of the American animated television series "South Park", and the 216th episode of the series overall.  It first aired on Comedy Central in the United States on June 8, 2011.  In the episode, Stan begins to develop a profound sense of cynicism after celebrating his tenth birthday, where he is literally seeing everything as "crap".  Meanwhile, Randy latches onto a new music genre, "tween wave," in an attempt to fit in, which causes problems in his marriage with Sharon.

Fatbeard: "Fatbeard" is the seventh episode of the thirteenth season of the American animated television series "South Park".  The 188th overall episode of the series, it originally aired on Comedy Central in the United States on April 22, 2009 and in the United Kingdom on April 24, 2009.  It was the mid-season finale, marking the final "South Park" episode for six months.  In the episode, Cartman misinterprets news reports about piracy in the Indian Ocean to mean the return of the classic era of swashbuckling pirates, and misleads a handful of South Park boys to voyage to Mogadishu to start a pirate crew.

Pinkeye (South Park): "Pinkeye" is the seventh episode in the first season of the American animated television series "South Park".  It originally aired on Comedy Central in the United States on October 29, 1997.  In "Pinkeye", Kenny is killed and, through a freak accident, he is brought back to life as a zombie and starts terrorizing South Park residents, who believe the rise of the living dead is an epidemic of "pinkeye".

Ass Burgers: "Ass Burgers" is the eighth episode of "South Park"' s fifteenth season and the 217th episode of the series overall.  It first aired in the U.S. on October 5, 2011, on Comedy Central.  The episode picks up where the previous episode, "You're Getting Old", left off.  Stan's cynicism is mistakenly blamed on his recent vaccinations and diagnosed as Asperger syndrome, a criticism of anti-vaccination proponents.  Cartman mishears the condition as "ass burgers" and opens a food stand in which the secret ingredient involves stuffing his underwear with hamburgers.  The episode is rated TV-MA-L in the United States.

Erection Day: "Erection Day" is the seventh episode in the ninth season of the American animated television series "South Park".  The 132nd episode overall, it first aired on Comedy Central in the United States on April 20, 2005.  In the episode, South Park Elementary's talent show is coming up and everyone expects Jimmy to win.  Jimmy is elated to perform his stand-up comedy routines, but begins to suffer from unwanted erections and tries to resolve the problem.

A Song of Ass and Fire: "A Song of Ass and Fire" is the eighth episode in the seventeenth season of the American animated television series "South Park".  The 245th episode of the series overall, it first aired on Comedy Central in the United States on November 20, 2013.  The episode serves as a continuation of the previous episode, "Black Friday", in which the children of South Park, role-playing as characters from "Game of Thrones", are split into two factions over whether to collectively purchase bargain-priced Xbox One or PlayStation 4 video game consoles at an upcoming Black Friday sale at the local mall, where Randy Marsh has been made the Captain of mall security.  The story arc concludes with the following episode, "Titties and Dragons".

Black Friday (South Park): "Black Friday" is the seventh episode in the seventeenth season of the American animated television series "South Park".  The 244th episode of the series overall, it premiered on Comedy Central in the United States on November 13, 2013.  The episode is the first of a three-episode story arc, which continues with "A Song of Ass and Fire", and concludes with "Titties and Dragons".  The plot, which employs themes and motifs from the TV series "Game of Thrones", concerns the characters' anticipation of a Black Friday sale, with Randy Marsh taking a temporary job as a mall security guard to gain an advantage over the holiday shopping crowds, and the children of South Park split into two factions over whether to collectively purchase bargain-priced Xbox One or PlayStation 4 video game consoles to facilitate their online group gaming.

Super Fun Time: "Super Fun Time" is the seventh episode in the twelfth season of the American animated television series "South Park".  The 174th episode of the series overall, it originally aired on Comedy Central in the United States on April 23, 2008.  In the episode, Cartman and Butters narrowly escape a horrific hostage situation at South Park's Pioneer Village, where historical reenactors take their jobs far too seriously.

Question: What is the seventh episode of South Park before Ass Burgers?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "episode_title": {
      "type": "string",
      "description": "The title of the South Park episode."
    },
    "season_details": {
      "type": "object",
      "properties": {
        "season_number": {
          "type": "integer",
          "description": "The season number of the episode."
        },
        "episode_number_in_season": {
          "type": "integer",
          "description": "The episode number within its season."
        }
      },
      "required": [
        "season_number",
        "episode_number_in_season"
      ],
      "additionalProperties": false
    },
    "overall_episode_number": {
      "type": "integer",
      "description": "The overall episode number in the series."
    },
    "air_date": {
      "type": "string",
      "description": "The original air date of the episode."
    },
    "relationship_to_target_episode": {
      "type": "object",
      "properties": {
        "target_episode_title": {
          "type": "string",
          "description": "The title of the episode used as the reference point (Ass Burgers)."
        },
        "is_immediately_preceding": {
          "type": "boolean",
          "description": "True if this episode directly precedes the target episode in overall series order."
        },
        "is_seventh_episode_of_its_season": {
          "type": "boolean",
          "description": "True if this episode is the seventh episode of its respective season."
        }
      },
      "required": [
        "target_episode_title",
        "is_immediately_preceding",
        "is_seventh_episode_of_its_season"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "episode_title",
    "season_details",
    "overall_episode_number",
    "air_date",
    "relationship_to_target_episode"
  ],
  "additionalProperties": false
}
