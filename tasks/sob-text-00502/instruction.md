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
Nelson Wheatcroft: Nelson Wheatcroft (1852-1897) was an English born actor and drama teacher.  He famously ran a drama school, at the Charles Frohman Empire Theatre, in the late Victorian era.  He was married to Adeline Stanhope(Wheatcroft)(1856-1935).  Their son Stanhope Wheatcroft(1888-1966) was a silent film actor.

List of Entourage episodes: "Entourage" is an American comedy-drama television series created for HBO by Doug Ellin, who also serves as an executive producer along with Mark Wahlberg, Stephen Levinson, Dennis Biggs, Rob Weiss and Ally Musika.  The series, loosely based on Wahlberg's own experiences of the film industry, follows Vincent Chase (Adrian Grenier), a New York born actor living in Los Angeles as he struggles with the ups and downs of a career in Hollywood.  He is aided, and often hindered, by his entourage, which consists of his half-brother and struggling actor Johnny "Drama" Chase (Kevin Dillon), his childhood friend and manager Eric "E" Murphy (Kevin Connolly), his ruthless agent Ari Gold (Jeremy Piven) and his other long-time friend Turtle (Jerry Ferrara).  "Entourage" premiered on HBO on July 18, 2004 and aired its final episode on September 11, 2011.  A total of 96 episodes were aired over eight seasons.

Joseph Jefferson: Joseph Jefferson, commonly known as Joe Jefferson (February 20, 1829 – April 23, 1905), was an American actor.  He was the third actor of this name in a family of actors and managers, and one of the most famous of all 19th century American comedians.  Jefferson was particularly well known for his adaptation and portrayal of Rip Van Winkle on the stage, reprising the role in several silent film adaptations.  Through his appearances in the latter, he is believed to be the earliest born actor to appear in a film.

Tulips (film): Tulips is a 1981 American comedy-drama film starring Gabe Kaplan and Bernadette Peters.  The director was officially credited as "Stan Ferris", but the film was actually directed by the trio of Rex Bromfield, Mark Warren and Al Waxman.

Steve Arbuckle: Stephen "Steve" George Arbuckle is a Canadian born actor born in the village of Donkin (Arbuckle Lane), Cape Breton Island, Nova Scotia.  He started his career as a theatre actor at Cape Breton University, then made his first move into film in 2003 with the lead role in the short film "Todd and the Book of Pure Evil", which also starred Julian Richings and John Bregar.  He appeared as Oliver Peele in 2010 in the pilot episode of the CBS show "Blue Bloods".  Arbuckle is now living in Toronto, Ontario.

R U Professional: "R U Professional" is a 2009 satirical song by the American indie rock band The Mae Shi, inspired by a July 2008 outburst by actor Christian Bale on the set of "Terminator Salvation".  Bale was filming with actress Bryce Dallas Howard when he berated director of photography, Shane Hurlbut, for walking into his line of sight.  An audio recording of the incident appeared on website TMZ on February 2, 2009.  The Mae Shi composed and recorded the song later in the same day, and released it the next day.  The group stated that the piece was created to honor Bale.  The song parodies Bale by sampling his voice from the 2008 diatribe.  The chorus incorporates Bale's use of the word "professional" from his flare-up.  The lyrics reference several films the actor starred in, including "Newsies", "Swing Kids", "American Psycho", and "The Dark Knight".

Shaun Chen: Shaun Chen (, born "Tey Kim Soon", 3 November 1978) is a Malaysia - born actor based in Singapore.  Chen is most notable for starring in the long-running drama series "Holland V" and for playing villains in several drama series.  He received his first award, the Rocket Award, at the Star Awards 2015 Show 1, for being the most improved artiste in 2014.  He starred as the lead character in both "Blessings" and "".  He further clinched the Best Actor award for "" and was voted into the Top 10 Most Popular Male Artistes list at the Star Awards 2015 Show 2.

Gabe Kaplan: Gabriel Weston "Gabe" Kaplan (born March 31, 1945) is an American comedian, actor, poker commentator, and professional poker player.

Richard Calabro: Richard Calabro (born 14 April 1979) is a Yorkshire born actor who began his career in the children's TV drama "The Ward", playing 'prankster' Digger Reily, until the character was eventually written out of the series in 1992.  More recently, Calabro starred with Angela Griffiths in award winning hospital drama "Holby City".

Morgan Weisser: Morgan Weisser (born May 12, 1971) is an American actor and the son of German born actor Norbert Weisser.

Question: What 1945-born actor starred in Tulips?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "release_year": {
          "type": "integer"
        },
        "genre": {
          "type": "string"
        }
      },
      "required": [
        "title",
        "release_year",
        "genre"
      ],
      "additionalProperties": false
    },
    "role_description": {
      "type": "string"
    }
  },
  "required": [
    "actor",
    "film",
    "role_description"
  ],
  "additionalProperties": false
}
