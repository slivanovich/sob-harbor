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
Million Dollar Arm (soundtrack): Million Dollar Arm (Original Motion Picture Soundtrack) is the soundtrack album of the American biographical drama film of the same name, directed by Craig Gillespie.  A. R. Rahman composed all seven of the original songs as well as the score for the film.  Artists Iggy Azalea, KT Tunstall, Wale, Sukhwinder Singh, Raghav Mathur have collaborated with the composer for the soundtrack.  Kendrick Lamar also recorded a song that is featured only in the film.  The soundtrack album was digitally released by Walt Disney Records on May 13, 2014, followed by a CD release on May 19.

We Could Be Kings: "We Could Be Kings" is a song by Scottish recording artist KT Tunstall and Academy Award winning composer A.R.Rahman for the film "Million Dollar Arm".  It was released on May 12, 2014.  The song is the third soundtrack written and released by Tunstall after "The Kid"'s "Boy", and "Miracle".

Mark Ciardi: Mark Thomas Ciardi (born August 19, 1961; pronounced CHAR-dee) is an American film producer and former Major League Baseball pitcher.  He is currently the Founder & CEO of Apex Entertainment.  Mark has a rich breadth of experience as a Film Executive, and Producer.  Apex Entertainment is an independent content production firm that also serves as a financier for media properties.  Prior to Apex, Mark was the co-founder of Mayhem Pictures that had an overall first look deal with Walt Disney Studios for twelve years.  At Mayhem, Ciardi produced films including "The Rookie", "Miracle", Invincible, The Game Plan, Secretariat, and Million Dollar Arm and Kevin Costner's McFarland USA.  Awaiting release is the worldwide best-selling novel, Fallen.  He also produced the Emmy Award winning, ESPN 30 for 30 documentary titled "Big Shot".

Hamilton (album): Hamilton is the cast album to the 2015 musical "Hamilton".  The musical is based on the 2004 biography of Alexander Hamilton written by Ron Chernow, with music, lyrics, and book by Lin-Manuel Miranda.  The recording stars Lin-Manuel Miranda, Leslie Odom Jr., Phillipa Soo, Renée Elise Goldsberry, Christopher Jackson, Daveed Diggs, Anthony Ramos, Okieriete Onaodowan, Jasmine Cephas Jones, and Jonathan Groff.  It also features Jon Rua, Thayne Jasperson, Sydney James Harcourt, Ariana DeBose, and Sasha Hutchings.  It achieved the largest first week sales for a digital cast album and is the highest-charting cast album since 1963.  It was the highest-selling Broadway cast album of 2015 and peaked at number one on the Rap Album chart, the first cast album to ever do so.

Million Dollar Listing Miami: Million Dollar Listing Miami is an American reality television series that premiered June 25, 2014, on Bravo.  It features three Miami-based real estate agents – Chad Carroll, Chris Leavitt, and Samantha DeBianchi – as they balance their personal and professional lives.  Announced in October 2013, "Million Dollar Listing Miami" is the second spin-off of "Million Dollar Listing Los Angeles", following "Million Dollar Listing New York".

Million Dollar Reload: Formed in 2006 in Co Tyrone Northern Ireland by Phil Conalane and Kie McMurray.  Conalane, Andrew Mackle and McMurray were musicians, playing in various cover bands in Northern Ireland before deciding to collaborate on writing of original material drawing from their shared musical interests.  The results were soon recorded and formed the basis of Million Dollar Reload's first EP, `Needle, Blackout, Fly`.  Drummer Davy Cassa was then recruited for purposes of the recording sessions before eventually being invited to join as a full-time member of Million Dollar Reload.  Brian Mallon was recruited by McMurray as a second guitarist for live performances of the bands new, original material, he would continue to become a full-time member.  Before starting the recording their debut album, Million Dollar Reload were recruited(minus drummer Cassa) by Steven Adler of Guns N' Roses as his backing band in his post Guns N' Roses career playing under Adler's Appetite.  The band performed with Adler in Ireland after he had fired his own band during the European leg of their 2006 tour.  This proved to be the catalyst for Million Dollar Reload to enter the studio speedily and begin the recording process for their debut album.

Million Dollar Quartet: "Million Dollar Quartet" is a recording of an impromptu jam session involving Elvis Presley, Jerry Lee Lewis, Carl Perkins, and Johnny Cash made on December 4, 1956, at the Sun Record Studios in Memphis, Tennessee.  An article about the session was published in the "Memphis Press-Scimitar" under the title "Million Dollar Quartet".  The recording was first released in Europe in 1981 as "The Million Dollar Quartet" with 17 tracks.  A few years later more tracks were discovered and released as "The Complete Million Dollar Session".  In 1990, the recordings were released in the United States as "Elvis Presley - The Million Dollar Quartet".  This session is considered a seminal moment in rock and roll.

Rinku Singh: Rinku Singh (born August 8, 1988 in Lucknow, India) is a left-handed baseball pitcher who is currently a free agent.  Singh was signed by the Pittsburgh Pirates organization after he won a pitching contest on a 2008 reality television show, "The Million Dollar Arm".  He was the first Indian to play professional baseball and has spent several seasons in the minor leagues, only reaching as high as the A level.  He is the subject of the movie "Million Dollar Arm".

Million Dollar Arm: Million Dollar Arm is a 2014 American biographical sports drama film directed by Craig Gillespie and produced by Walt Disney Pictures from a screenplay written by Thomas McCarthy.  The film is based on the true story of baseball pitchers Rinku Singh and Dinesh Patel who were discovered by sports agent J. B. Bernstein after winning a reality show competition.

Lin-Manuel Miranda: Lin-Manuel Miranda ( ; born January 16, 1980) is an American composer, lyricist, playwright, and actor best known for creating and starring in the Broadway musicals "Hamilton" and "In the Heights".  He co-wrote the songs for Disney's "Moana" soundtrack (2016) and is set to star in their upcoming film "Mary Poppins Returns".  Miranda's awards include a Pulitzer Prize, two Grammy Awards, an Emmy Award, a MacArthur Fellowship, and three Tony Awards.

Question: What type of media does Lin-Manuel Miranda and Million Dollar Arm have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_media_type": {
      "type": "string",
      "description": "The type of media that both entities have in common."
    },
    "entities_involved": {
      "type": "array",
      "description": "Details about the entities and their associated media types.",
      "items": {
        "type": "object",
        "properties": {
          "entity_name": {
            "type": "string",
            "description": "The name of the entity."
          },
          "media_types": {
            "type": "array",
            "description": "A list of media types associated with this entity.",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "entity_name",
          "media_types"
        ],
        "additionalProperties": false
      }
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation of how the common media type was determined."
    }
  },
  "required": [
    "common_media_type",
    "entities_involved",
    "reasoning"
  ],
  "additionalProperties": false
}
