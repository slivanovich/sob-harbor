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
They Came Together: They Came Together is a 2014 American satirical romantic comedy film directed by David Wain and written by Wain and Michael Showalter.  It is a parody of romantic comedies infused with Showalter and Wain's absurd approach.  The film had its world premiere at the 2014 Sundance Film Festival, and was released theatrically (with a simultaneous release on iTunes) on June 27, 2014.

Wet Hot American Summer: Wet Hot American Summer is a 2001 American satirical  comedy film directed by David Wain from a screenplay written by Wain and Michael Showalter.  The film features an ensemble cast, including Janeane Garofalo, David Hyde Pierce, Molly Shannon, Paul Rudd, Christopher Meloni, Michael Showalter (and various other members of MTV's sketch comedy group "The State"), Elizabeth Banks, Ken Marino, Michael Ian Black, Bradley Cooper, Amy Poehler, Zak Orth, and A. D. Miles.  The film takes place during the last full day at a fictional summer camp in 1981, and spoofs the sex comedies aimed at teen audiences of that era.

Wet Hot American Summer: Ten Years Later: Wet Hot American Summer: Ten Years Later is a satirical comedy web television series written by David Wain and Michael Showalter, and directed by Wain.  The Netflix series is a sequel to both Wain's 2001 film "Wet Hot American Summer", and the 2015 prequel television series "".  The series consists of eight episodes, and was released on August 4, 2017.

The Bounty Hunter (2010 film): The Bounty Hunter is a 2010 American action comedy film directed by Andy Tennant, starring Jennifer Aniston and Gerard Butler.  The story centers on a bounty hunter (Butler) hired to retrieve his ex-wife (Aniston) who has skipped bail.  The film was released in the United States on March 19, 2010.

Wet Hot American Summer (series): The Wet Hot American Summer series is an American satirical comedy film and two Netflix series' directed by David Wain and written by Wain and Michael Showalter.  The series features an ensemble cast, including Janeane Garofalo, Molly Shannon, Paul Rudd, Christopher Meloni, Michael Showalter (and various other members of MTV's sketch comedy group The State), Elizabeth Banks, Ken Marino, Michael Ian Black, Bradley Cooper, Amy Poehler, Zak Orth, David Hyde Pierce and A. D. Miles.  The film takes place during the last full day at a fictional summer camp in 1981, and spoofs the sex comedies aimed at teen audiences of that era.  The first Netflix series was a prequel to the film focusing on the first day of camp in 1981.  The second Netflix series sees the camp counselors return to Camp Firewood 10 years later, as originally planned in the final scene of the 2001 film.

Role Models: Role Models is a 2008 American comedy film directed by David Wain and written by David Wain, Timothy Dowling, Paul Rudd and Ken Marino.  It is about two energy drink salesmen who are ordered to perform 150 hours of community service as punishment for various offenses.  For their service, the two men work at a program designed to pair kids with adult role models.  The film stars Seann William Scott, Paul Rudd, Christopher Mintz-Plasse, Bobb'e J. Thompson, Jane Lynch and Elizabeth Banks.

The Ten: The Ten is a 2007 American comedy film, directed by David Wain and cowritten by Wain and Ken Marino, released through ThinkFilm.  The film was released on August 3, 2007.  The DVD was released on January 15, 2008.

Wanderlust (2012 film): Wanderlust is a 2012 American comedy film directed by David Wain, starring Jennifer Aniston and Paul Rudd, as a married couple who try to escape modern society by finding themselves on a commune in Georgia, after the economy crashes down on their dreams in New York City.

Paul Rudd: Paul Stephen Rudd (born April 6, 1969) is an American actor, comedian, writer, and producer.  He studied theatre at the University of Kansas and the British American Drama Academy, before making his acting debut in 1992 with NBC's drama series "Sisters".  He is known for his starring roles in the film "The Cider House Rules" (1999), "" (1995), and the comedy films "Clueless" (1995), "Wet Hot American Summer" (2001), "" (2004), "The 40-Year-Old Virgin" (2005), "Knocked Up" (2007), "Role Models" (2008), "I Love You, Man" (2009), "Dinner for Schmucks" (2010), "Our Idiot Brother" (2011), "Wanderlust" (2012), "This Is 40" (2012), and "" (2013), and for playing the superhero Ant-Man in Marvel Studios' "Ant-Man" (2015) and "" (2016).

Wet Hot American Summer: First Day of Camp: Wet Hot American Summer: First Day of Camp is a 2015 satirical comedy web television series written by David Wain and Michael Showalter, and directed by Wain.  The eight-episode Netflix series is a prequel to Wain's 2001 film "Wet Hot American Summer", a parody of teen sex comedies which has since developed a cult following.  Although many of the original film's ensemble cast have gone on to high-profile work, all of the then-adult actors returned for this series, playing even younger versions of their original roles.  The episodes were released for online viewing at the end of July 2015.

Question: At what mid-western college did the man who co-starred with Jennifer Aniston in a 2012 film directed by David Wain receive his education?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the actor identified from the film criteria."
        },
        "education": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "institution_name": {
                "type": "string",
                "description": "The name of the educational institution."
              },
              "field_of_study": {
                "type": "string",
                "description": "The field of study at the institution."
              }
            },
            "required": [
              "institution_name"
            ],
            "additionalProperties": false
          },
          "description": "A list of educational institutions attended by the actor."
        }
      },
      "required": [
        "name",
        "education"
      ],
      "additionalProperties": false
    },
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film that matches the criteria."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "director": {
          "type": "string",
          "description": "The director of the film."
        },
        "co_star": {
          "type": "string",
          "description": "The name of the co-star mentioned in the question."
        }
      },
      "required": [
        "title",
        "release_year",
        "director",
        "co_star"
      ],
      "additionalProperties": false
    },
    "college_answer": {
      "type": "string",
      "description": "The name of the mid-western college where the actor received education."
    }
  },
  "required": [
    "actor_details",
    "film_details",
    "college_answer"
  ],
  "additionalProperties": false
}
