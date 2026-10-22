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
Star Wars: Episode III – Revenge of the Sith: Star Wars: Episode III – Revenge of the Sith is a 2005 American epic space opera film written and directed by George Lucas.  It is the sixth entry of the "Star Wars" film series and stars Ewan McGregor, Natalie Portman, Hayden Christensen, Ian McDiarmid, Samuel L. Jackson, Christopher Lee, Anthony Daniels, Kenny Baker, and Frank Oz.  A sequel to "" (1999) and "" (2002), the film is the third and final installment of the "Star Wars" prequel trilogy.

Starkiller: Starkiller, born Galen Marek and also known as The Apprentice, is the Dark Jedi anti-hero protagonist of the "" project.  In 2014, Lucasfilm rebranded him as part of the "Star Wars Legends" non-canonical story-line, and the character has not been re-introduced yet into the "Star Wars" canon.  He is raised by Darth Vader and is made his secret apprentice under the name "Starkiller" due to being potent with using the Force for destructive purposes and described as less of an assassin and more of a "Force wrecking ball".  The character's name is taken from Luke Skywalker's original name, "Annikin Starkiller".  The character's likeness and voice are provided by Samuel Witwer.  Despite "The Force Unleashed" being of non-canonical "Legends" status, Witwer still remains part of the "Star Wars" canon by voicing Darth Maul in the animated series "Star Wars: The Clone Wars" and "Star Wars Rebels".

Alec Smight: Alec Dow Smight is an American film editor and television director born in New York City.  He was a producer and director on the successful series "" and has directed two episodes of its spin-off "".  Son of the well-known television and film director Jack Smight, his editing work includes "Chicago Hope", numerous television pilots, "Northern Exposure", and "L.A. Law".

The Empire Strikes Back: The Empire Strikes Back (also known as Star Wars: Episode V – The Empire Strikes Back) is a 1980 American epic space opera film directed by Irvin Kershner.  Leigh Brackett and Lawrence Kasdan wrote the screenplay, with George Lucas writing the film's story and serving as executive producer.  The second installment in the original "Star Wars" trilogy, it was produced by Gary Kurtz for Lucasfilm and stars Mark Hamill, Harrison Ford, Carrie Fisher, Billy Dee Williams, Anthony Daniels, David Prowse, Kenny Baker, Peter Mayhew, and Frank Oz.

Chewco: Chewco Investments L. P., was a limited partnership associated with the Enron scandal, which resulted in the bankruptcy of Enron.  It was named after the Star Wars character Chewbacca, because it was created to hide losses from the Joint Energy Development Investment Limited, known by its acronym "JEDI".  Like Chewbacca, the Jedi Knights were prominent characters in Star Wars.

Star Wars: Episode II – Attack of the Clones: Star Wars: Episode II – Attack of the Clones is a 2002 American epic space opera film directed by George Lucas and written by Lucas and Jonathan Hales.  It is the second installment of the "Star Wars" prequel trilogy, and stars Ewan McGregor, Natalie Portman, Hayden Christensen, Ian McDiarmid, Samuel L. Jackson, Christopher Lee, Temuera Morrison, Anthony Daniels, Kenny Baker and Frank Oz.

Star Wars: Episode I – The Phantom Menace: Star Wars: Episode I – The Phantom Menace is a 1999 American epic space opera film written and directed by George Lucas, produced by Lucasfilm and distributed by 20th Century Fox.  It is the first installment in the "Star Wars" prequel trilogy and stars Liam Neeson, Ewan McGregor, Natalie Portman, Jake Lloyd, Ian McDiarmid, Anthony Daniels, Kenny Baker, Ahmed Best, Pernilla August, Brian Blessed, Ray Park, and Frank Oz.

Jack Smight: Jack Smight (March 9, 1925 – September 1, 2003) was an American theatre and film director.

Frank Oz: Frank Oz (born Frank Richard Oznowicz; born May 25, 1944) is an English-born American puppeteer, filmmaker and actor.  His career began as a puppeteer, where he performed the Muppet characters of Miss Piggy, Fozzie Bear, Animal, and Sam Eagle in "The Muppet Show", and Cookie Monster, Bert, and Grover in "Sesame Street".  He is also known for being the puppeteer and voice of Yoda in the "Star Wars" films.

Return of the Jedi: Return of the Jedi (also known as Star Wars: Episode VI – Return of the Jedi) is a 1983 American epic space opera film directed by Richard Marquand.  The screenplay by Lawrence Kasdan and George Lucas was from a story by Lucas, who was also the executive producer.  It was the third installment in the original "Star Wars" trilogy and the first film to use THX technology.  The film is set one year after "The Empire Strikes Back" and was produced by Howard Kazanjian for Lucasfilm Ltd.  The film stars Mark Hamill, Harrison Ford, Carrie Fisher, Billy Dee Williams, Anthony Daniels, David Prowse, Kenny Baker, Peter Mayhew and Frank Oz.

Question: Frank Oz, who worked closely with American theatre and film director Jack Smight, was known for being the puppeteer and voice of which Star Wars character?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "character_name": {
      "type": "string",
      "description": "The name of the Star Wars character."
    },
    "performer_name": {
      "type": "string",
      "description": "The name of the person who performed the character."
    },
    "performance_role": {
      "type": "string",
      "description": "The specific role performed for the character (e.g., puppeteer and voice)."
    },
    "media_franchise": {
      "type": "string",
      "description": "The media franchise the character belongs to."
    }
  },
  "required": [
    "character_name",
    "performer_name",
    "performance_role",
    "media_franchise"
  ],
  "additionalProperties": false
}
