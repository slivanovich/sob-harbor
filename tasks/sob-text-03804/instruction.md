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
Vacation (2015 film): Vacation is a 2015 American comedy film written and directed by Jonathan Goldstein and John Francis Daley (in their directorial debuts).  It stars Ed Helms, Christina Applegate, Skyler Gisondo, Steele Stebbins, Leslie Mann, Chris Hemsworth, Beverly D'Angelo, and Chevy Chase.  It is the fifth installment of the "Vacation" film series serving as a soft reboot.  It is also the second not to carry the "National Lampoon" name after "Vegas Vacation", and was released by New Line Cinema and Warner Bros. on July 29, 2015.  It has an approval rating of 26% on Rotten Tomatoes and grossed $104.9 million on a $31 million budget.

Hotel Hell Vacation: Hotel Hell Vacation is an American online comedy short film released on February 7, 2010 on HomeAway's website.  Chevy Chase and Beverly D'Angelo reprise their roles as Clark and Ellen Griswold.  It was the first time Clark and Ellen had been seen in a "Vacation" film since 1997's "Vegas Vacation"; they later appeared together again in 2015's "Vacation".  The fourteen-minute short premiered as a series of commercials during the Super Bowl to help promote HomeAway, Inc.  Although sanctioned by Warner Bros. (which holds the underlying rights to the "Vacation" series characters and concepts), this film was not sponsored by National Lampoon, Inc., which initiated the "Vacation" series.

National Lampoon's Christmas Vacation: National Lampoon's Christmas Vacation is a 1989 American Christmas comedy film directed by Jeremiah S. Chechik.  It is the third installment in National Lampoon's "Vacation" film series, and was written by John Hughes, based on his short story in "National Lampoon" magazine, "Christmas '59".  The film stars Chevy Chase, Beverly D'Angelo and Randy Quaid, with Juliette Lewis and Johnny Galecki as the Griswold children Audrey and Rusty, respectively.

National Lampoon's Vacation: National Lampoon's Vacation, sometimes referred to as Vacation, is a 1983 American road comedy film directed by Harold Ramis and starring Chevy Chase, Beverly D'Angelo, Randy Quaid, Dana Barron, and Anthony Michael Hall.  John Candy, Imogene Coca, Christie Brinkley, and a young Jane Krakowski appear in supporting roles.  The screenplay was written by John Hughes, based on his short story "Vacation '58" which appeared in "National Lampoon.

Holiday Road: "Holiday Road" is a 1983 single written and recorded by Fleetwood Mac guitarist Lindsey Buckingham.  The song was featured in the 1983 film "National Lampoon's Vacation".  The song was also used in the sequels "National Lampoon's European Vacation", "Vegas Vacation" and "Vacation".  While the song only peaked at No. 82 on the "Billboard" Hot 100 chart, it has since become one of Buckingham's best known songs.

National Lampoon's Christmas Vacation 2: National Lampoon's Christmas Vacation 2: Cousin Eddie's Island Adventure is a 2003 American made-for-television comedy film.  It premiered December 20, 2003 on NBC and stars Randy Quaid and Miriam Flynn reprising their roles as Cousin Eddie and Catherine, along with Dana Barron reprising her role as Audrey Griswold.  It is the sequel to the 1989 film, "National Lampoon's Christmas Vacation", although it is more of a spin-off than a direct chapter of the National Lampoon's "Vacation" film series, because Chevy Chase and Beverly D'Angelo did not appear.

National Lampoon's European Vacation: European Vacation (originally given the working title Vacation '2' Europe) is a 1985 American comedy film directed by Amy Heckerling and written by John Hughes and Robert Klane based on a story by Hughes.  The second film in National Lampoon's "Vacation" film series, it stars Chevy Chase and Beverly D'Angelo.  Dana Hill and Jason Lively replace Dana Barron and Anthony Michael Hall as Griswald children Audrey and Rusty.  After Hall declined to reprise his role (he decided to star in "Weird Science" instead), the producers decided to recast both children.

Vegas Vacation: Vegas Vacation is a 1997 American comedy film directed by Stephen Kessler.  It is the fourth installment in "National Lampoon"’s "Vacation" film series, and was written by Elisa Bell, based on a story by Bell and Bob Ducsay.  The film stars Chevy Chase, Beverly D'Angelo and Randy Quaid, with Ethan Embry and Marisol Nichols as Griswold children Rusty and Audrey.  The film opened at #4 at the box office and grossed over $36.4 million domestically.  "Vegas Vacation" became the first theatrical "Vacation" film not to carry the National Lampoon label or a screenwriting credit from John Hughes.

National Lampoon, Inc.: National Lampoon, Inc. was incorporated in 1970 to launch the National Lampoon magazine.  They leveraged that success into radio, film , television, and live stage.  The Company developed and produced a number of iconic films, including "National Lampoon's Animal House" and the "National Lampoon Vacation" franchise.

National Lampoon's Vacation (film series): The National Lampoon's Vacation film series is a comedy film series initially based on John Hughes' short story "Vacation '58" that was originally published by "National Lampoon" magazine.  The series is distributed by Warner Bros. and consists of seven films, two of which are not sponsored by "National Lampoon".  In recent years, the series has been the inspiration for various advertising campaigns featuring some of the original cast members.  The series portrays the misadventures of the Griswold family, whose attempts to enjoy vacations and holidays are plagued with continual disasters and strangely embarrassing predicaments.

Question: The Griswold family's vacation misadventures feature in both "Hotel Hell Vacation" and the "National Lampoon Vacation" series, as sanctioned by what company?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "sanctioning_company_name": {
      "type": "string",
      "description": "The name of the company that sanctioned the works."
    },
    "sanctioned_entities": {
      "type": "array",
      "description": "A list of films or film series that were sanctioned.",
      "items": {
        "type": "string"
      }
    },
    "sanction_relationship": {
      "type": "string",
      "description": "The nature of the relationship between the company and the entities, e.g., 'sanctioned' or 'distributed'."
    }
  },
  "required": [
    "sanctioning_company_name",
    "sanctioned_entities",
    "sanction_relationship"
  ],
  "additionalProperties": false
}
