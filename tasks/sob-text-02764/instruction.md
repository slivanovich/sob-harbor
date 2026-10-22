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
James Stenbeck: James Stenbeck is a fictional character on CBS's daytime drama As the World Turns.  He has been portrayed by Anthony Herrera.  On November 10, 2009, Tom Pelphrey debuted in the role of Stenbeck in a bizarre plot twist which had Stenbeck reverted to a version of himself from his younger years due to the properties of a lotus from the Amazon Rainforest.

Anthony Herrera: Anthony John Herrera (January 19, 1944 – June 21, 2011) was an American actor.

Abigail Williams (As the World Turns): Abigail Williams is a fictional character on the American TV soap opera "As the World Turns".  She was played by Emmy Rossum as a child, and Kristina Sisco as a teenager.  She is a former resident of Oakdale.  Abigail (played by Sisco) returned to As the World Turns on July 30, 2010 before it ended in September.

Barbara Ryan: Barbara Ryan Coleman (formerly Stenbeck, St. Clair, Dixon, Munson and Montgomery) is a fictional character from the American CBS soap opera "As the World Turns".  In the early 1970s, Barbara was played by a succession of actresses, but the actress most associated with the role is Colleen Zenk, who played her since September 1, 1978.  Better known as simply Barbara Ryan she is portrayed as a heroine who experienced many tragedies, mostly at the hands of her controlling ex-husband, the villainous James Stenbeck (Anthony Herrera).

Alison Stewart (As the World Turns): Alison Stewart is a fictional character on the daytime soap opera, "As the World Turns".  She was last portrayed by Marnie Schulenburg from March 23, 2007, to September 17, 2010.  She also made a guest appearance on "The Young and the Restless" on February 22, 2007.  Alison (again played by Schulenburg) also appeared in a 2007 web-only miniseries called "L.A. Diaries" which chronologically took place before the actress's first appearance on "As the World Turns".

As the World Turns: As the World Turns (often referred to as ATWT) is an American television soap opera that aired on CBS for 54 years from April 2, 1956, to September 17, 2010.  Irna Phillips created "As the World Turns" as a sister show to her other soap opera "Guiding Light".  Running for 54 years, "As the World Turns" holds the second-longest continuous run of any daytime network soap opera on American television, surpassed only by "Guiding Light".  "As the World Turns" was produced for the first 43 years in Manhattan and in Brooklyn from 2000 until 2010.

Our Private World: Our Private World is an American serial.  It was the first prime-time spin-off from a daytime soap ("As the World Turns", the number one daytime soap opera at the time).  Created by Irna Phillips and William J. Bell, it premiered on May 5, 1965 and aired Wednesdays and Fridays over the summer; the multiple-episode-per-week format was inspired by ABC's hit show "Peyton Place".  The final episode aired on September 10 of the same year.  "Our Private World" starred Eileen Fulton as Lisa Miller Hughes, the same heroine she had played on "As the World Turns", as well as Nicolas Coster.  A total of 38 half-hour episodes were produced.

Andrew Kavovit: Andrew Michael Kavovit (born July 19, 1971, Bronx, New York) is an American actor best known as one of the portrayers of Paul Ryan (formerly Stenbeck) as a youngster in the CBS soap opera "As the World Turns", a role he played from 1986 to 1991, and for which he was awarded the Daytime Emmy Award in 1990.

Scott Holmes: Scott Holmes (born May 30, 1952 in West Grove, Pennsylvania) is a retired American actor, best known for the role of District Attorney Tom Hughes in the CBS soap opera "As the World Turns", a role he played from 1987 through ATWT's 2010 cancellation.  Prior to joining "As the World Turns", Holmes appeared on "Ryan's Hope" from 1984-86.  After the cancellation of "As the World Turns", Scott Holmes retired to South Carolina.

Patrick Tovatt: Patrick Tovatt (born December 11, 1940 in Garrett Ridge, Colorado) is an American actor.  He is perhaps best known for his roles on several soap operas, including Zane Lindquist on "Another World" (1985-1986); Matt McCleary on "Search for Tomorrow" (1986); and Cal Stricklyn on "As the World Turns" (1988-1998, 2001).  He was nominated for an Emmy Award for Outstanding Supporting Actor in 1994 for his work on "As the World Turns."

Question: What is the nationality of the actor who played the villainous James Stenbeck on "As the World Turns?"

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_details": {
      "type": "object",
      "properties": {
        "actor_name": {
          "type": "string",
          "description": "The name of the actor."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the actor."
        }
      },
      "required": [
        "actor_name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "character_details": {
      "type": "object",
      "properties": {
        "character_name": {
          "type": "string",
          "description": "The name of the character played by the actor."
        },
        "character_description": {
          "type": "string",
          "description": "A description of the character's role or nature."
        }
      },
      "required": [
        "character_name",
        "character_description"
      ],
      "additionalProperties": false
    },
    "soap_opera_name": {
      "type": "string",
      "description": "The name of the soap opera."
    },
    "final_answer": {
      "type": "string",
      "description": "The nationality of the actor who played the specified character."
    }
  },
  "required": [
    "actor_details",
    "character_details",
    "soap_opera_name",
    "final_answer"
  ],
  "additionalProperties": false
}
