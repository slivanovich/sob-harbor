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
6 Balloons: 6 Balloons is an upcoming American drama film written and directed by Marja-Lewis Ryan.  It stars Abbi Jacobson, Dave Franco, Tim Matheson and Jane Kaczmarek.

Jane Kaczmarek: Jane Frances Kaczmarek (born December 21, 1955) is an American actress.  She is best known for playing the character of Lois on the television series "Malcolm in the Middle" (2000–06).  Kaczmarek is a three-time Golden Globe and seven-time Emmy Award nominee.

Valor (TV series): Valor is an upcoming American drama television series, created by Kyle Jarrow.  The show is produced by CBS Television Studios and Warner Bros.  Television, with Anna Fricke and Kyle Jarrow serving as showrunners.  The series is set to premiere on The CW on October 9, 2017 as part of the 2017–18 U.S. television season.

Alice Hirson: Alice Hirson (born March 10, 1929) is an American actress best known for her roles on television.  She began her career on stage, before roles on the daytime soap operas.  She is best known for her roles as Mavis Anderson in the CBS prime time soap opera, "Dallas", and as Lois Morgan, the mother of the title character on the ABC sitcom, "Ellen".

Reverie (TV series): Reverie is an upcoming American drama television series set to be broadcast on NBC.  The series was commissioned on May 12, 2017.  The first season will contain only 10 episodes, for creative and scheduling reasons.

The Front Runner (film): The Front Runner is an upcoming American drama film directed by Jason Reitman, based on the book "All the Truth Is Out: The Week Politics Went Tabloid" by Matt Bai.  Reitman co-wrote the screenplay with Bai and Jay Carson.  The film stars Hugh Jackman as politician Gary Hart, with Vera Farmiga, Kaitlyn Dever, Sara Paxton, Molly Ephraim, and J. K. Simmons also starring.

Pose (TV series): Pose is an upcoming American drama television series.  The series was launched by FX in early 2017 and will premiere on FX in early 2018.  The first season will be executive produced by Ryan Murphy, Nina Jacobson, and Brad Simpson, and will be written by Murphy, Brad Falchuk, and newcomer Stephen Canals.

Tiger (upcoming American film): Tiger is an upcoming American drama film directed by Alister Grierson, with a screenplay by Prem Singh and Michael Pugliese based on the true story of Sikh boxer Pardeep "Tiger" Nagra.  The film introduces Singh as Nagra, with Mickey Rourke and Janel Parrish also starring.

Thora Bjorg Helga: Thora Bjorg Helga (born 16 April 1989) is an Icelandic actress best known for starring in Ragnar Bragason's "Metalhead".  Helga won the 2014 Icelandic Academy Award for Best Actress for her role in the film which premiered at the Toronto International Film Festival in September 2013.  She also starred in Baltasar Kormákur's film The Deep in 2013, earning her a 2013 Icelandic Academy Award Best Supporting Actress nomination.  Helga also stars in the upcoming American film Autumn Lights.

Rise (TV series): Rise (formerly known as Drama High) is an upcoming American drama television series created by Jason Katims and Jeffrey Seller based on the young adult novel "Drama High" by Michael Sokolove, starring Josh Radnor in the lead role as Lou Mazzuchelli, based on real-life teacher Lou Volpe.  The pilot was ordered to series by NBC on May 4, 2017 along with "The Brave", making both series the first regular series orders by the network for the 2017–18 United States network television schedule.  The first season will consist of 10 episodes.

Question: 6 Balloons is an upcoming American drama film starring an actress best known for playing the character of Lois on what television series?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film mentioned in the question."
    },
    "film_genre": {
      "type": "string",
      "description": "The genre of the film."
    },
    "actress_name": {
      "type": "string",
      "description": "The name of the actress starring in the film."
    },
    "known_for_role": {
      "type": "string",
      "description": "The character role the actress is best known for."
    },
    "television_series_title": {
      "type": "string",
      "description": "The title of the television series where the actress played the known role."
    }
  },
  "required": [
    "film_title",
    "film_genre",
    "actress_name",
    "known_for_role",
    "television_series_title"
  ],
  "additionalProperties": false
}
