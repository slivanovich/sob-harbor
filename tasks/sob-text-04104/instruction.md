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
South Park (season 5): Season five of "South Park", an American animated television series created by Trey Parker and Matt Stone, began airing on June 20, 2001.  The fifth season concluded after 14 episodes on December 12, 2001.  The 14-episode season length would become a standard for later years of the series (up until the seventeenth season).

South Park (season 9): Season nine of "South Park", an American animated television series created by Trey Parker and Matt Stone, began airing on March 9, 2005.  The ninth season concluded after 14 episodes on December 7, 2005.  All of the episodes in the ninth season were written and directed by Trey Parker.

South Park (season 15): The fifteenth season of the American animated sitcom "South Park" began airing on Comedy Central on April 27, 2011 and ended on November 16, 2011.  In response to reactions to the mid-season finale episode "You're Getting Old", which seemed to insinuate that creators Trey Parker and Matt Stone were wrapping up the series, Comedy Central proclaimed through the media that "South Park" was renewed for two more seasons, and the duo were signed through 2013.  Shortly before the airing of the season finale episode "The Poor Kid", "South Park" was extended again until 2016, taking the show to 20 seasons.  Parker was the director and writer for all episodes, and Robert Lopez was the writer in this eleventh episode for the fifteenth season.

Eric Cartman: Eric Theodore Cartman, often referred to as just Cartman, is a main character in the animated television series "South Park", created by Matt Stone and Trey Parker, and voiced by Trey Parker.  Cartman, generally referred to by his surname, is one of four central characters in "South Park", along with his friends Stan Marsh, Kyle Broflovski, and Kenny McCormick.  Cartman first appeared, originally named Kenny, in prototypical form in a 1992 animated short "Jesus vs. Frosty", and a 1995 animated short "Jesus vs. Santa", and first appeared on television in the pilot episode of "South Park", "Cartman Gets an Anal Probe", on August 13, 1997.

South Park (season 2): Season two of "South Park", an American animated television series created by Trey Parker and Matt Stone, began airing on April 1, 1998.  The second season concluded after 18 episodes on January 20, 1999; it remains the longest season of "South Park" to date.  While most of the episodes were directed by series creator Trey Parker, Season 2 includes two episodes directed by Eric Stough.

South Park (season 17): The seventeenth season of the animated television series "South Park" premiered on Comedy Central on September 25, 2013 and ended on December 11, 2013.

South Park (season 8): Season eight of "South Park", an American animated television series created by Trey Parker and Matt Stone, began airing on March 17, 2004.  The eighth season concluded after 14 episodes on December 15, 2004, and was written and directed by Trey Parker.  The season deals with various topics that were relevant at the time of release.  The episodes portray a spectrum of topics, from effect of large scale retails corporations to immigration.

List of South Park episodes: "South Park" is an American animated television sitcom created by Trey Parker and Matt Stone for Comedy Central that debuted on August 13, 1997.  The series originated from a pair of animated shorts titled "The Spirit of Christmas", and the first episode of "South Park" originally aired on August 13, 1997 on Comedy Central.  Intended for mature audiences, the show has become infamous for its crude language and dark, surreal humor that lampoons a wide range of topics.  The story revolves around four boys—Stan Marsh, Kyle Broflovski, Eric Cartman, and Kenny McCormick—and their bizarre adventures in and around the eponymous Colorado town.

South Park (season 7): Season seven of "South Park", an American animated television series created by Trey Parker and Matt Stone, began airing on March 19, 2003.  The seventh season concluded after 15 episodes on December 17, 2003, and was written and directed by Trey Parker.

South Park (season 10): The tenth season of "South Park", an American animated television series created by Trey Parker and Matt Stone, began airing on March 22, 2006.  The tenth season concluded after 14 episodes on November 15, 2006.  This is the first season in which Kenny does not die and the last season featuring Isaac Hayes (the voice of Chef) as Hayes quit the show following the backlash behind season nine's "Trapped in the Closet" episode.  This season also had a minor controversy when the Halloween episode "Hell on Earth 2006" depicted "The Crocodile Hunter's" Steve Irwin with a stingray lodged in his chest getting thrown out of Satan's Halloween party for not being in costume.  Episode 2 in this season is the last one with the Braniff Airlines logo.  All the episodes in this season were written and directed by Trey Parker.

Question: What is the name of this season that premiered on Comedy Central on September 25, 2013 created by Trey Parker and Matt Stone?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "season_name": {
      "type": "string",
      "description": "The full name of the season, including the show title and season number."
    },
    "season_number": {
      "type": "integer",
      "description": "The numerical identifier for the season."
    },
    "premiere_date": {
      "type": "string",
      "format": "date",
      "description": "The date the season premiered."
    },
    "creators": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The creators of the television series."
    }
  },
  "required": [
    "season_name",
    "season_number",
    "premiere_date",
    "creators"
  ],
  "additionalProperties": false
}
