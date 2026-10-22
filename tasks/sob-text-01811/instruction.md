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
List of Melissa &amp; Joey episodes: "Melissa & Joey" is an American television sitcom starring Melissa Joan Hart and Joey Lawrence.  The series revolves around Melanie "Mel" Burke (Hart), an up-and-coming local politician who hires Joseph "Joe" Longo (Lawrence), a recently divorced commodities broker, as the nanny for her niece and nephew.  The series premiered on August 17, 2010 on ABC Family.

Emily Hart: Emily Anne Hart (born May 2, 1986) is an American actress and voice actress.  She is the younger sister of former "Clarissa Explains It All" and "Sabrina the Teenage Witch" star Melissa Joan Hart.  She is best known for her roles as Sabrina Spellman in "" and Amanda Wiccan in "Sabrina the Teenage Witch".

Melissa &amp; Joey: Melissa & Joey is an American sitcom television series starring Melissa Joan Hart and Joey Lawrence that aired for four seasons between 2010 and 2015 on ABC Family.  The series follows local politician Mel Burke (Hart) and Joe Longo (Lawrence), whom Mel hires to look after her niece (Taylor Spreitler) and nephew (Nick Robinson) after a Ponzi scheme leaves Joe broke.

Taylor Spreitler: Taylor Danielle Spreitler (born October 23, 1993) is an American actress.  She portrayed the role of Mia McCormick on "Days of Our Lives" and Lennox Scanlon on "Melissa & Joey".

Mute (2005 film): Mute is a 2005 short film by Melissa Joan Hart, and is her directorial debut.  The film was first released on September 21, 2005 at the Palm Springs International Short Film Festival and stars her sister Emily Hart as Eileen, a woman determined to get revenge on her sister.

Melissa Joan Hart: Melissa Joan Hart (born April 18, 1976) is an American actress, voice actress, director, producer, singer, fashion designer, and businesswoman.  She is known for her title roles in the sitcoms "Clarissa Explains It All" (1991–1994), "Sabrina the Teenage Witch" (1996–2003), and "Melissa & Joey" (2010–2015).

Chriselle Almeida: Chriselle Almeida is an actress of Indian origin.  She was born in Mumbai, India and raised in Fairfield, CT.  She started her career Off-Broadway in New York Cityand currently lives in Los Angeles.  She received a Bachelor of Fine Arts in Acting from the University of Connecticut-Storrs and received a full scholarship towards her Master of Fine Arts in Acting from University of California, Los Angeles.  Her role as a Bollywood starlet who has an affair with a female journalist in [["When Kiran met Karen" caused some controversy in India.  She also was a guest star playing the role of Lakshmi, a prospective bride for [[Raj Koothrappali]] who turns out to be a closet lesbian in "[[The Big Bang Theory]]" episode, [[The Big Bang Theory (season 5)|"The Transporter Malfunction"]].  It was a dream come true working with the master of comedy [[Chuck Lorre]].  Other credits include "[[Grey's Anatomy]]" where she worked across [[Geena Davis]], "[[Melissa and Joey]]" with [[Melissa Joan Hart]], "[[Gossip Girl]]" with [[Jessica Szohr]] and "[[Sex and the City 2]]" with all for leads [[Sarah Jessica Parker]], [[Kristin Davis]], [[Cynthia Nixon]] and [[Kim Cattrall]].  Other Acting Credits include [[Body of Proof]], [[Loosely Exactly Nicole]] and [[Miss Indian America]]Through the years her national commercials including [[Verizon]], [[Bank of America]], [[Toyota]] [[KFC]].  Most recently she was nominated for Best Lead Actress at the [[Idyllwild-Pine Cove, California]] Film Festival for a short film.

Holiday in Handcuffs: Holiday in Handcuffs is an American crime comedy television movie that originally aired on ABC Family on December 9, 2007, as a part of the network's 25 Days of Christmas programming block.  The film stars Melissa Joan Hart, Mario Lopez, Markie Post, Timothy Bottoms, June Lockhart, Kyle Howard and Vanessa Lee Evigan.

Clarissa Explains It All: Clarissa Explains It All is an American teen sitcom created by Mitchell Kriegman for Nickelodeon.  In the series, Clarissa Darling, played by Melissa Joan Hart, is a teenager who addresses the audience directly to describe the things that are happening in her life, dealing with typical adolescent concerns such as school, boys, pimples, wearing her first training bra and an annoying little brother.

Silencing Mary: Silencing Mary, also released as Campus Justice, is a 1998 television film directed by Craig R. Baxley.  The film was made to warn people about rape and popular teen actress Melissa Joan Hart was cast in the lead to draw a young audience.

Question: Which "Days of our Lives" actress once worked on a sitcom with Melissa Joan Hart?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress who worked on 'Days of Our Lives' and a sitcom with Melissa Joan Hart."
    },
    "worked_on_days_of_our_lives": {
      "type": "boolean",
      "description": "True if the actress worked on 'Days of Our Lives'."
    },
    "worked_with_melissa_joan_hart_on_sitcom": {
      "type": "object",
      "properties": {
        "sitcom_name": {
          "type": "string",
          "description": "The name of the sitcom where the actress worked with Melissa Joan Hart."
        },
        "actress_role_on_sitcom": {
          "type": "string",
          "description": "The role played by the actress on the sitcom."
        },
        "melissa_joan_hart_role_on_sitcom": {
          "type": "string",
          "description": "The role played by Melissa Joan Hart on the sitcom."
        }
      },
      "required": [
        "sitcom_name",
        "actress_role_on_sitcom",
        "melissa_joan_hart_role_on_sitcom"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actress_name",
    "worked_on_days_of_our_lives",
    "worked_with_melissa_joan_hart_on_sitcom"
  ],
  "additionalProperties": false
}
