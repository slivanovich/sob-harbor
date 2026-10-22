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
The Woman He Loved: The Woman He Loved is a 1988 HTV romantic drama television about the abdication of Edward VIII.  Directed by Charles Jarrott, it stars Anthony Andrews, Jane Seymour and Olivia de Havilland.  Jane Seymour was nominated for a Golden Globe Award for Best Actress – Miniseries or Television Film at the 46th Golden Globe Awards and Olivia de Havilland was nominated for a Primetime Emmy Award for Outstanding Supporting Actress in a Miniseries or a Movie.  Costume designer Robin Fraser-Paye was also nominated for Primetime Emmy Award for Outstanding Costume Design for a Miniseries or a Special.

Jon Cassar: John Francis "Jon" Cassar (born April 27, 1958) is a Maltese-Canadian television director and producer, known for his work on the first seven seasons of "24".  In 2006, he won the Primetime Emmy Award for Outstanding Directing for a Drama Series for his work on the episode "".  In 2011, he produced and directed all episodes of the Canadian-American miniseries "The Kennedys", for which he won the Directors Guild of America Award for Outstanding Directing – Television Film and was nominated for the Primetime Emmy Award for Outstanding Miniseries or Movie.

List of Primetime Emmy Awards received by Netflix: Netflix is an American on-demand internet streaming media provider.  In 2013 Netflix became the first streaming platform to win a Primetime Emmy Award. " House of Cards" became the first original online-only web television series to receive major nominations for the 65th Primetime Emmy Awards.  "House of Cards" scored nine nominations, including Primetime Emmy Award for Outstanding Drama Series.  Meanwhile its first episode, "Chapter 1", received four nominations becoming the first webisode (online-only episode) of a television series to receive a major Primetime Emmy Award nomination.  Eigil Bryld won for Outstanding Cinematography for a Single-Camera Series, meanwhile David Fincher won for Outstanding Directing for a Drama Series.  Both, Bryld and Fincher won for the episode "Chapter 1", making it the first Emmy-awarded webisode.  The Following year "House of Cards" repeated in the category Outstanding Directing for a Drama Series, with Carl Franklin directing "Chapter 14".  Furthemore the political drama got its first nomination for writing for "Chapter 14", written by Beau Willimon.

Bobby Cannavale: Robert Cannavale ( ; ] ; born May 3, 1970) is an American actor known for his leading role as Bobby Caffey in the first two seasons of the crime drama series "Third Watch".  Cannavale also had a recurring role on the NBC comedy series "Will & Grace" as Will Truman's long-term boyfriend Officer Vincent "Vince" D'Angelo, for which he won the 2005 Primetime Emmy Award for Outstanding Guest Actor in a Comedy Series, and portrayed Gyp Rosetti during the third season of the HBO drama series "Boardwalk Empire", for which he won the 2013 Primetime Emmy Award for Outstanding Supporting Actor in a Drama Series.  In 2016, he starred in the HBO drama series "Vinyl", produced by Martin Scorsese and Mick Jagger.

A Woman of Independent Means: A Woman of Independent Means is an 1995 American television miniseries starring Sally Field.  Sally Field also producer.  Field was nominated for Emmy Award, Golden Globe Award and Screen Actors Guild Awards.  The series was also nominated in the category Primetime Emmy Award for Outstanding Miniseries and Primetime Emmy Award for Outstanding Casting for a Miniseries, Movie, or a Special and won Emmy for Outstanding Individual Achievement in Costume Design for a Miniseries or a Special in 1995.

Barry Pepper: Barry Robert Pepper (born April 4, 1970) is a Canadian actor.  He is best known for roles such as Private Daniel Jackson in "Saving Private Ryan" (1998), Corrections Officer Dean Stanton in "The Green Mile" (1999), Jonnie Goodboy Tyler in "Battlefield Earth" (2000), Roger Maris in "61*" (2001), Sergeant Michael Strank in "Flags of Our Fathers" (2006) and "Lucky" Ned Pepper in "True Grit" (2010).  He has been nominated for three Screen Actors Guild Awards and a Golden Globe Award.  For his role as Robert F. Kennedy in the miniseries "The Kennedys" (2011), Pepper won the Primetime Emmy Award for Outstanding Lead Actor in a Miniseries or Movie.

Blythe Danner: Blythe Katherine Danner (born February 3, 1943) is an American actress.  She won two Primetime Emmy Awards for Best Supporting Actress in a Drama Series for her role as Izzy Huffstodt on "Huff" (2004–2006), and a Tony Award for Best Featured Actress in a Play for her performance in "Butterflies Are Free" (1969–1972).  Danner was nominated for two Primetime Emmy Awards for Outstanding Guest Actress in a Comedy Series for portraying Marilyn Truman on "Will & Grace" (2001–2006), and the Primetime Emmy Award for Outstanding Lead Actress in a Miniseries or a Movie for her roles in "We Were the Mulvaneys" (2002) and "Back When We Were Grownups" (2004).  For the latter, she was also nominated for the Golden Globe Award for Best Actress – Miniseries or Television Film.

Elisabeth Moss: Elisabeth Singleton Moss (born July 24, 1982) is an American film, stage, and television actor.  She is known for her roles as Zoey Bartlet, the youngest daughter of President Josiah Bartlet, on the NBC television series "The West Wing" (1999–2006); Peggy Olson, secretary-turned-copywriter, on the AMC series "Mad Men" (2007–2015), which earned her six Emmy Awards nominations and a Golden Globe nomination; Det. Robin Griffin in the BBC miniseries "Top of the Lake" (2013, 2017), which won her a Golden Globe for Best Actress in a Miniseries or TV Film; and Offred on the Hulu series "The Handmaid's Tale", for which she won the Primetime Emmy Award for Outstanding Lead Actress in a Drama Series and the Primetime Emmy Award for Outstanding Drama Series, as producer.

Robert F. Colesberry: Robert F. "Bob" Colesberry, Jr. (March 7, 1946 – February 9, 2004) was an American film and television producer, best known as a co-creator of the television series "The Wire" (2002–2008) for HBO, executive producer of the miniseries "The Corner" (2000), and a producer for Martin Scorsese's "After Hours" (1985), Alan Parker's "Mississippi Burning" (1988), and Billy Crystal's "61*" (2001).  Colesberry was also an occasional actor.

The Corner: The Corner is a 2000 HBO drama television miniseries based on the nonfiction book "" (1997) by David Simon and Ed Burns, and adapted for television by Simon and David Mills.  It premiered on premium cable network HBO in the United States on April 16, 2000 and concluded its six-part run on May 21, 2000.  The series was released on DVD on July 22, 2003.  It won the Primetime Emmy Award for Outstanding Miniseries in 2000.

Question: What is the name of the 2000 HBO drama television miniseries which won a Primetime Emmy Award in the same year and whose executive producer was Robert F. "Bob" Colesberry?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "miniseries_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the miniseries."
        },
        "release_year": {
          "type": "integer",
          "description": "The year the miniseries was released."
        },
        "network": {
          "type": "string",
          "description": "The television network that aired the miniseries."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the miniseries."
        }
      },
      "required": [
        "name",
        "release_year",
        "network",
        "genre"
      ],
      "additionalProperties": false
    },
    "award_information": {
      "type": "object",
      "properties": {
        "award_name": {
          "type": "string",
          "description": "The name of the award won by the miniseries."
        },
        "award_year": {
          "type": "integer",
          "description": "The year the award was won."
        }
      },
      "required": [
        "award_name",
        "award_year"
      ],
      "additionalProperties": false
    },
    "executive_producer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the executive producer."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "miniseries_details",
    "award_information",
    "executive_producer"
  ],
  "additionalProperties": false
}
