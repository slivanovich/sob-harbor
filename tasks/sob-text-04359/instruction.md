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
Hawaii Five-0 (2010 TV series, season 6): The sixth season of the CBS police procedural drama series "Hawaii Five-0" premiered on Friday, September 25, 2015 and concluded on May 13, 2016.  It contained 25 episodes.

Pilot (CSI: Crime Scene Investigation): "Pilot" is the and the series premiere of the American crime drama "".  It first aired on October 6, 2000 on the CBS network in the United States.  The premise of the show revolves around the crime scene investigators working for the Las Vegas Police Department.  The pilot introduces the main characters of Gil Grissom (William Petersen), Catherine Willows (Marg Helgenberger), Nick Stokes (George Eads), Warrick Brown (Gary Dourdan) and Jim Brass (Paul Guilfoyle).  The pilot was written by series creator Anthony E. Zuiker and directed by Danny Cannon.

CSI: Crime Scene Investigation: CSI: Crime Scene Investigation, also referred to as CSI and CSI: Las Vegas, is an American procedural forensics crime drama television series.  It originally ran on CBS from 2000 to 2015, spanning fifteen seasons.  The series, starring William Petersen, Marg Helgenberger, Laurence Fishburne, Ted Danson, Elisabeth Shue, and Jorja Fox is the first in the "CSI" franchise.  The series concluded with a feature-length finale titled "".

Lethal Vows: Lethal Vows is an American drama/thriller television movie, based on a true story of Richard K Overton, his ex-wife Dorothy Boyer, and Overton's third and late wife Janet Overton.  Starring John Ritter, Marg Helgenberger and Megan Gallagher, the movie premiered October 13, 1999, on CBS.

Marg Helgenberger: Mary Marg Helgenberger (born November 16, 1958) is an American actress.  She began her career in the early 1980s and first came to attention for playing the role of Siobhan Ryan on the daytime soap opera "Ryan's Hope" from 1982 to 1986.  She is best known for her roles as Catherine Willows in the CBS police procedural drama "" (2000–12, 2013) and the subsequent TV movie "Immortality" (2015) and as K.C. Koloski in the ABC drama "China Beach" (1988–91), which earned her the 1990 Emmy Award for Outstanding Supporting Actress in a Drama Series.

Hawaii Five-0 (2010 TV series, season 7): The seventh season of the CBS police procedural drama series "Hawaii Five-0" premiered on Friday September 23, 2016, and concluded on May 12, 2017.  The season contained 25 episodes, and the series's 150th episode.  For the 2016-17 U.S. television season, the seventh season of "Hawaii Five-0" ranked #15 with an average of 12.15 million viewers, and in the 18–49 demographic ranked 43rd with a 1.8/7 Rating/Share.

Trouble Sleeping: "Trouble Sleeping" is a song by English singer-songwriter Corinne Bailey Rae from her self-titled debut album (2006).  It was written by Rae, John Beck and Steve Chrisanthou, and was released as the album's third single on 29 May 2006.  Rae performed this song and "Like a Star" on the 27 November 2006 episode of the NBC comedy-drama series "Studio 60 on the Sunset Strip".  "Trouble Sleeping" was also featured on the NBC medical drama "ER" and on the CBS police procedural drama "NCIS".

Catherine Willows: Director Catherine Willows is a fictional character, portrayed by Marg Helgenberger, from the CBS crime drama "."  Helgenberger made her franchise debut in ""'s episode "Pilot".  Helgenberger received several award nominations for her portrayal of Catherine, including two Primetime Emmy Award nominations and two Golden Globe Award nominations.

Suzanne Shepherd: Suzanne Shepherd is an American actress and theater director.  She is best known for her portrayal of Karen's overbearing mother in the film "Goodfellas", Carmela Soprano's mother Mary De Angelis in the HBO television series "The Sopranos", and the assistant school principal in "Uncle Buck".  She also played the role of Mrs. Scarlini in the film 2000 film "Requiem for a Dream", and Big Ethel in "A Dirty Shame".  Shepherd studied acting with Sanford Meisner, and later went on to teach Meisner's program of acting study, the first woman to do so.  She was a founding member of the Compass Players in the early 1960s, along with such other actors as Alan Alda and Alan Arkin.  In 2016, she played the role of Lucille Abetemarco the mother of Detective Anthony Abetemarco played by former "Sopranos" co-star Steve Schirripa in "Good Cop Bad Cop" the 2nd episode of the 7th season of the CBS police procedural drama "Blue Bloods".  Her daughter is artist Kate Shepherd.

Tom Degnan: Tom Degnan (born September 24, 1982 in Bucks County, Pennsylvania) is an American actor.  He is best known for his role on "One Life to Live" as Joey Buchanan from 2010 to 2011.  He also appeared in "As the World Turns" in 2009 as Riley Morgan/Adam Munson.  Additional appearances include "Handsome Harry", alongside Steve Buscemi, and "Little Miss Perfect", alongside Lilla Crawford.  In 2013 he played the role of Fire Marshall Rick Kelly in the 10th episode of the 4th season of the CBS police procedural drama "Blue Bloods" in the episode "Mistaken Identity".  He has also played roles in the TV shows "Lipstick Jungle", "Law & Order", "The Unusuals", "The Good Wife", "White Collar", "The Following", "Magic City", "Person of Interest", "The Michael J. Fox Show", "Madam Secretary", and "The Sonnet Project".  In 2013 he played the role of Chris Van Helsing in the made-for-TV movie "Gothica" and played the role of Matt in the 2014 made-for-TV movie "Tin Man".  In 2015 he played the role of Jim in the romance-drama film "To Whom It May Concern" and played the role of Tom in the short story drama film "Seclusion".  Degnan also had a recurring role on CBS's "Limitless".

Question: What character did Mary Marg Helgenberger portray where she received several award nominations in the CBS police procedural drama?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "character_name": {
      "type": "string",
      "description": "The name of the character portrayed by the actress."
    },
    "actor_name": {
      "type": "string",
      "description": "The full name of the actress."
    },
    "drama_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the CBS police procedural drama."
        },
        "network": {
          "type": "string",
          "description": "The television network the drama aired on."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the television series."
        }
      },
      "required": [
        "title",
        "network",
        "genre"
      ],
      "additionalProperties": false
    },
    "award_nominations": {
      "type": "array",
      "description": "A list of award nominations received for the portrayal of the character.",
      "items": {
        "type": "object",
        "properties": {
          "award_type": {
            "type": "string",
            "description": "The type of award for which the nomination was received."
          },
          "count": {
            "type": "integer",
            "description": "The number of nominations received for this specific award type."
          }
        },
        "required": [
          "award_type",
          "count"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "character_name",
    "actor_name",
    "drama_details",
    "award_nominations"
  ],
  "additionalProperties": false
}
