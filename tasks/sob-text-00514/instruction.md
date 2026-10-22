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
Don't Trust the B---- in Apartment 23: Don't Trust the B---- in Apartment 23 is an American sitcom created by Nahnatchka Khan that aired on ABC in the United States from April 11, 2012, to January 15, 2013.  The series originally aired as a mid-season replacement during the 2011–12 television schedule.

Kublai Khan (song): "Kublai Khan" is a single by Hip Hop duo Jedi Mind Tricks, released in 2003 through Babygrande Records .  The song was the second single released from the duo's third album "Visions of Gandhi", following "Animal Rap", and followed by "Rise of the Machines".  "Kublai Khan" is a sequel to the group's 2000 single "Genghis Khan", this time, named after Genghis' grandson Kublai Khan.  The song, like "Genghis Khan", features an intense symphonic sample, courtesy of group producer Stoupe the Enemy of Mankind.  New York City rapper Tragedy Khadafi, who appeared on "Genghis", also appears on the track.  Former JMT member Jus Allah, who split from the group in 2001, is replaced by Goretex, of the group Non Phixion.

Kali Troy: Kali Bianca Troy (born March 7, 1971) is an American voice actress also known as Kittie.

Barbara Jo Allen: Barbara Jo Allen (September 2, 1906 – September 14, 1974) was an actress also known as Vera Vague, the spinster character she created and portrayed on radio and in films during the 1940s and 1950s.  She based the character on a woman she had seen delivering a PTA literature lecture in a confused manner.  As Vague, she popularized the catch phrase "You dear boy!"

Lincoln Lover: "Lincoln Lover" is the fourth episode of the third season and the twenty-seventh overall episode of the animated comedy series "American Dad! ".  It aired on Fox in the United States on November 5, 2006, and is written by Rick Wiener, Kenny Schwartz and Nahnatchka Khan and directed by Brent Woods.

Fresh Off the Boat: Fresh Off the Boat is an American sitcom series, starring Hudson Yang, Randall Park, and Constance Wu.  Created by Nahnatchka Khan, it is loosely inspired by the life of chef and food personality Eddie Huang and his book "".  It is the first American television sitcom starring an Asian-American family to air on network primetime since Margaret Cho's "All American Girl", which aired for one season in 1994.  Its style has been compared to the comedy series "Everybody Hates Chris".  The flashback technique with voice-over narration from the present day (first season only) is similar to "The Wonder Years".

Nahnatchka Khan: Nahnatchka Khan is an American television writer and producer.

List of Fresh Off the Boat episodes: "Fresh Off the Boat" is an American television sitcom broadcast on ABC created by Nahnatchka Khan.  The story follows the course of Eddie Huang's Taiwanese family as they make their way from Washington, D.C. to Orlando, Florida to open up a steak restaurant.  The series premiered on February 4, 2015.  On May 7, 2015, the show was renewed by ABC for a second season.  On March 3, 2016, ABC renewed the series for a third season, which premiered on October 11, 2016.  On May 12, 2017, ABC renewed the series for a fourth season, which is set to premiere on October 3, 2017.

Arden Myrin: Arden VanAmringe Myrin ( ;) is an American actress and comedian.  Arden became a new cast member on Showtime’s "Shameless" Season 7, and recently appeared in the world premiere of Steve Martin's new play "Meteor Shower" at the Long Wharf Theatre.  Her television credits include "Orange Is the New Black, Hung, Key & Peele, Inside Amy Schumer, W/ Bob and David, Psych, Bones, Fresh Off The Boat, Suburgatory, 2 Broke Girls, Reno 911! ," and "Gilmore Girls" among others.  Arden will be seen next in the feature film "Extracurricular Activities".

Stan of Arabia: Part 1: "Stan of Arabia: Part 1" is the fifth episode of the second season and the twelfth overall episode of the animated comedy series "American Dad! ".  It aired on Fox in the United States on November 6, 2005, and is written by Nahnatchka Khan and directed by Rodney Clouden.

Question: What Shameless actress also appears on an American sitcom created by Nahnatchka Khan?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The full name of the actress."
    },
    "shameless_appearance": {
      "type": "boolean",
      "description": "Indicates if the actress was a cast member on Shameless."
    },
    "sitcom_details": {
      "type": "object",
      "properties": {
        "sitcom_title": {
          "type": "string",
          "description": "The title of the American sitcom created by Nahnatchka Khan."
        },
        "creator_name": {
          "type": "string",
          "description": "The name of the creator of the sitcom."
        },
        "actress_appeared_in_sitcom": {
          "type": "boolean",
          "description": "Indicates if the actress appeared in this specific sitcom."
        }
      },
      "required": [
        "sitcom_title",
        "creator_name",
        "actress_appeared_in_sitcom"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actress_name",
    "shameless_appearance",
    "sitcom_details"
  ],
  "additionalProperties": false
}
