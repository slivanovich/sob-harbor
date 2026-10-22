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
SpongeBob SquarePants (season 7): The seventh season of the American animated television series "SpongeBob SquarePants", created by marine biologist and animator Stephen Hillenburg, originally aired on Nickelodeon in the United States from July 19, 2009 to June 11, 2011.  It contained 26 episodes, beginning with the episodes "Tentacle Vision" and "I Heart Dancing".  The series chronicles the exploits and adventures of the title character and his various friends in the fictional underwater city of Bikini Bottom.

SpongeBob SquarePants (season 4): The fourth season of the American animated television series "SpongeBob SquarePants", created by former marine biologist and animator Stephen Hillenburg, aired on Nickelodeon from May 6, 2005 to July 24, 2007, and contained 20 episodes, beginning with the episodes "Fear of a Krabby Patty" and "Shell of a Man".  The series chronicles the exploits and adventures of the title character and his various friends in the fictional underwater city of Bikini Bottom.  The season was executive produced by series creator Hillenburg, while writer Paul Tibbitt acted as the supervising/co-executive producer and showrunner.  The show underwent a hiatus on television as Hillenburg halted the production in 2002 to work on the film adaptation of the series, "The SpongeBob SquarePants Movie".  Once the film was finalized and the previous season had completed broadcast on television, Hillenburg wanted to end the show, but the success of the series led to more episodes, so Tibbitt took over Hillenburg's position as showrunner and began working on a fourth season for broadcast in 2005.  Hillenburg remained with the show, but in a smaller advisory role in which he reviewed each episode and offered suggestions to the show's production crew.

List of SpongeBob SquarePants episodes: "SpongeBob SquarePants" is an American animated television series created by marine biologist and animator Stephen Hillenburg for Nickelodeon.  The series is set in the fictional underwater city of Bikini Bottom, and centers on the adventures and endeavors of SpongeBob SquarePants, an over-optimistic sea sponge that annoys other characters.  Many of the ideas for the show originated in an unpublished, educational comic book titled "The Intertidal Zone", which Hillenburg created in the mid-1980s.  He began developing "SpongeBob SquarePants" into a television series in 1996 after the cancellation of "Rocko's Modern Life", another Nickelodeon television series which Hillenburg previously directed.

List of SpongeBob SquarePants guest stars: In addition to the show's regular cast of voice actors, guest stars have been featured on "SpongeBob SquarePants", an American animated television series created by marine biologist and animator Stephen Hillenburg for Nickelodeon.  "SpongeBob SquarePants" chronicles the adventures and endeavors of the title character and his various friends in the fictional underwater city of Bikini Bottom.  Many of the ideas for the show originated in an unpublished, educational comic book titled "The Intertidal Zone", which Hillenburg created in the mid-1980s.  He began developing "SpongeBob SquarePants" into a television series in 1996 upon the cancellation of "Rocko's Modern Life", which Hillenburg directed.  The pilot episode first aired on Nickelodeon in the United States on May 1, 1999.  The show's ninth season premiered in 2012, and episodes of "SpongeBob SquarePants" have aired.  A feature-length film adaptation of the show, "The SpongeBob SquarePants Movie", was released in 2004; in 2015, a sequel, "", was released.

SpongeBob SquarePants (season 5): The fifth season of the American animated television series "SpongeBob SquarePants", created by former marine biologist and animator Stephen Hillenburg, aired on Nickelodeon from February 19, 2007 to July 19, 2009, and contained 20 episodes, beginning with the special episode "Friend or Foe".  The series chronicles the exploits and adventures of the title character and his various friends in the fictional underwater city of Bikini Bottom.  The season was executive produced by series creator Hillenburg and writer Paul Tibbitt, who also acted as the showrunner.

Help Wanted (SpongeBob SquarePants): "Help Wanted" is the pilot episode of the American animated television series "SpongeBob SquarePants".  It originally aired on Nickelodeon in the United States on May 1, 1999, following the television airing of the 1999 Kids' Choice Awards.  The episode follows the protagonist, an anthropomorphic sea sponge named SpongeBob SquarePants, attempting to get a job at a local restaurant called the Krusty Krab.  However, he is tasked to find a seemingly non-existent high-caliber spatula because the owner, Mr. Krabs, considers him unqualified for the position.  Eventually, crowds of ravenous anchovies stop by the Krusty Krab and demand meals.  SpongeBob returns from his errand, having fulfilled the request of Mr. Krabs and found a mechanical spatula.  He utilizes the spatula to fulfill the anchovies' hunger.  SpongeBob is then welcomed by Mr. Krabs as a Krusty Krab employee.

SpongeBob SquarePants (season 6): The sixth season of the American animated television series "SpongeBob SquarePants", created by former marine biologist and animator Stephen Hillenburg, aired on Nickelodeon from March 3, 2008 to July 5, 2010, and contained 26 episodes, beginning with the episode "Krabby Road".  The series chronicles the exploits and adventures of the title character and his various friends in the fictional underwater city of Bikini Bottom.  The season was executive produced by series creator Hillenburg and supervising producer Paul Tibbitt, who also acted as the showrunner.  In 2009, the show celebrated its tenth anniversary on television.  The documentary film titled "" premiered on July 17, 2009, and marked the anniversary. " SpongeBob's Truth or Square", a television film, and the special episode "To SquarePants or Not to SquarePants" were broadcast on Nickelodeon, as part of the celebration.

SpongeBob's Runaway Roadtrip: SpongeBob's Runaway Roadtrip is an anthology series of five episodes in the American animated television series "SpongeBob SquarePants", as part of its eighth season.  As the name suggests, the miniseries consisted of five Vacation themed episodes, the first four leading up to the premiere of the fifth.  It is the second miniseries based on the Nickelodeon cartoon series "SpongeBob SquarePants", which was originally released direct-to-DVD on September 20, 2011.

Friend or Foe (SpongeBob SquarePants): "Friend or Foe" is the first episode of the fifth season and the 81st overall episode of the American animated television sitcom "SpongeBob SquarePants".  It was written by Casey Alexander, Zeus Cervas, Mike Mitchell, Steven Banks and Tim Hill, and the animation was directed by supervising director, Alan Smart and Tom Yasumi.  Alexander, Cervas and Mitchell also function as storyboard directors.  The episode originally aired on Nickelodeon in the United States on April 13, 2007.

SpongeBob SquarePants (season 3): The third season of the American animated television series "SpongeBob SquarePants", created by Stephen Hillenburg, aired on Nickelodeon from October 5, 2001 to October 11, 2004, and consists of 20 episodes.  The series chronicles the exploits and adventures of the title character and his various friends in the fictional underwater city of Bikini Bottom.  The season was executive produced by series creator Hillenburg, who also acted as the showrunner.  Hillenburg halted production on the show to work on the 2004 film adaptation of the series, "The SpongeBob SquarePants Movie".  After production on the film, Hillenburg resigned from the show as its showrunner, and appointed staff writer Paul Tibbitt to overtake the position.  Season 3 was originally set to end the series after the release of the film, but the success prevented the series from ending, leading to a fourth season.

Question: what is name of the first episode of the season of American animated television series "SpongeBob SquarePants" which was aired on Nickelodeon from February 19, 2007 to July 19, 2009, and contained 20 episodes?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "series_title": {
      "type": "string",
      "description": "The title of the animated television series."
    },
    "season_details": {
      "type": "object",
      "properties": {
        "season_number": {
          "type": "integer",
          "description": "The number of the season."
        },
        "air_dates": {
          "type": "object",
          "properties": {
            "start_date": {
              "type": "string",
              "description": "The start date of the season's original airing."
            },
            "end_date": {
              "type": "string",
              "description": "The end date of the season's original airing."
            }
          },
          "required": [
            "start_date",
            "end_date"
          ],
          "additionalProperties": false
        },
        "episode_count": {
          "type": "integer",
          "description": "The total number of episodes in the season."
        }
      },
      "required": [
        "season_number",
        "air_dates",
        "episode_count"
      ],
      "additionalProperties": false
    },
    "first_episode_name": {
      "type": "string",
      "description": "The name of the first episode of the specified season."
    }
  },
  "required": [
    "series_title",
    "season_details",
    "first_episode_name"
  ],
  "additionalProperties": false
}
