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
List of Ghost Whisperer episodes: The following is an episode list for the CBS drama, "Ghost Whisperer".  The show's title is a reference to the main character, Melinda Gordon (portrayed by Jennifer Love Hewitt), who has the ability to see and communicate with the dead.  The series began on September 23, 2005, and ended on May 21, 2010.  As of 2011, all seasons are available on DVD.  The show was not renewed for a sixth season and was cancelled by CBS on May 18, 2010.

Ghost Whisperer (season 1): The first season of "Ghost Whisperer", an American television series created by John Gray, commenced airing in the United States on September 23, 2005, concluded May 5, 2006, and consisted of 22 episodes.  The series follows the life of Melinda Gordon (Jennifer Love Hewitt), who has the ability to see and communicate with ghosts.  While trying to live as normal a life as possible—she is married and owns an antique store—Melinda helps earthbound spirits resolve their problems and cross over into the Light, or the spirit world.  Her tasks are difficult and at times she struggles with people who push her away and disbelieve her ability.  In addition, the ghosts are mysterious and sometimes menacing in the beginning and Melinda must use the clues available to her to understand the spirit's needs and help them.

Grace Fulton: Grace Caroline Fulton (born July 17, 1996) is an American actress, best known for playing Young Melinda Gordon on "Ghost Whisperer", Haley Farrell in "Bones", and Young Natalie Wood in "The Mystery of Natalie Wood".  She also played the character Sydney Briggs in "Home of the Brave".  She starred in the television film "Back When We Were Grownups", playing Young Biddy.

Ghost Whisperer (season 3): The third season of "Ghost Whisperer", an American television series created by John Gray, commenced airing in the United States on September 28, 2007, concluded May 16, 2008, and was originally intended to consist of 22 episodes.  However, due to the Writer's Strike it was shortened to 18 episodes.  The series follows the life of Melinda Gordon (Jennifer Love Hewitt), who has the ability to see and communicate with ghosts.  While trying to live as normal a life as possible—she is married and owns an antique store—Melinda helps earthbound spirits resolve their problems and cross over into the Light, or the spirit world.  Her tasks are difficult and at times she struggles with people who push her away and disbelieve her ability.  In addition, the ghosts are mysterious and sometimes menacing in the beginning and Melinda must use the clues available to her to understand the spirit's needs and help them.

Melinda Gordon: Melinda Irene Gordon is the title character of the American paranormal television series "Ghost Whisperer" created by John Gray.  Gordon was portrayed by American actress Jennifer Love Hewitt.

Jennifer Love Hewitt: Jennifer Love Hewitt (born February 21, 1979) is an American actress, television producer and director, singer/songwriter and author.  Hewitt began her acting career as a child by appearing in television commercials and the Disney Channel series "Kids Incorporated".  She rose to fame for her role as Sarah Reeves Merrin on the Fox teen drama "Party of Five" (1995–99).  She later starred in the horror film "I Know What You Did Last Summer" (1997) and its 1998 sequel.

Ghost Whisperer (season 2): The second season of "Ghost Whisperer", an American television series created by John Gray, commenced airing in the United States on September 22, 2006, concluded May 11, 2007, and consisted of 22 episodes.  The series follows the life of Melinda Gordon (Jennifer Love Hewitt), who has the ability to see and communicate with ghosts.  While trying to live as normal a life as possible—she is married and owns an antique store—Melinda helps earthbound spirits resolve their problems and cross over into the Light, or the spirit world.  Her tasks are difficult and at times she struggles with people who push her away and disbelieve her ability.  In addition, the ghosts are mysterious and sometimes menacing in the beginning and Melinda must use the clues available to her to understand the spirit's needs and help them.

Ghost Whisperer (season 5): The fifth and final season of "Ghost Whisperer", an American television series created by John Gray, commenced airing in the United States on September 25, 2009, concluded May 21, 2010, and consisted of 22 episodes.  The series follows the life of Melinda Gordon (Jennifer Love Hewitt), who has the ability to see and communicate with ghosts.  While trying to live as normal a life as possible—she is married and owns an antique store—Melinda helps earthbound spirits resolve their problems and cross over into the Light, or the spirit world.  Her tasks are difficult and at times she struggles with people who push her away and disbelieve her ability.  In addition, the ghosts are mysterious and sometimes menacing in the beginning and Melinda must use the clues available to her to understand the spirit's needs and help them.

Ghost Whisperer (video game): Ghost Whisperer is a casual hidden-object mystery adventure game developed by Legacy Games for Microsoft Windows and Mac OS.  The game is based on the CBS supernatural television drama Ghost Whisperer starring Melinda Gordon (Jennifer Love Hewitt).  The game contains two different cases to solve: "Forgotten Toys" and "A Brush with Death".

Ghost Whisperer (season 4): The fourth season of "Ghost Whisperer", an American television series created by John Gray, commenced airing in the United States on October 3, 2008, concluded May 15, 2009, and consisted of 23 episodes.  The series follows the life of Melinda Gordon (Jennifer Love Hewitt), who has the ability to see and communicate with ghosts.  While trying to live as normal a life as possible—she is married and owns an antique store—Melinda helps earthbound spirits resolve their problems and cross over into the Light, or the spirit world.  Her tasks are difficult and at times she struggles with people who push her away and disbelieve her ability.  In addition, the ghosts are mysterious and sometimes menacing in the beginning and Melinda must use the clues available to her to understand the spirit's needs and help them.

Question: In what year was the actress born who played Melinda Gordon on Ghost Whisperer?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "character_name": {
      "type": "string",
      "description": "The name of the character in the series."
    },
    "actress_name": {
      "type": "string",
      "description": "The name of the actress who portrayed the character."
    },
    "actress_birth_year": {
      "type": "integer",
      "description": "The birth year of the actress."
    }
  },
  "required": [
    "character_name",
    "actress_name",
    "actress_birth_year"
  ],
  "additionalProperties": false
}
