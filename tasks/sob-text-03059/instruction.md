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
L.A. Hair: L.A. Hair is an American reality television series on WE tv.  The series debuted on May 31, 2012 and was originally titled "Hair Divas: Hollywood".  The series follows celebrity stylist Kim Kimble and her staff at her salon, Kimble Hair Studio.  WE tv announced in October 2012 that the series had been renewed for a ten episode second season, which debuted on June 6, 2013.  WE tv has ordered a 12-episode third season that premiered on May 22, 2014.  On March 3, 2015 WE tv renewed the show for a fourth season that premiered in July 2015.  The fifth season of "L.A. Hair" premiered on January 5, 2017.

Locations in Veronica Mars: "Veronica Mars" is an American television series created by Rob Thomas.  The series premiered on September 22, 2004, during UPN's last two years, and ended on May 22, 2007, after a season on UPN's successor, The CW Television Network.  Set in the fictional town of Neptune, the series starred Kristen Bell as the title character, a student who progressed from high school to college during the series while moonlighting as a private investigator under the wing of her detective father.

Almost Naked Animals: Almost Naked Animals is a Canadian animated television series that is produced for YTV.  The series premiered on January 7, 2011 on YTV.  The series was created by Noah Z. Jones, who is also the creator of the Disney Channel animated series "Fish Hooks" and the Disney XD animated series "Pickle and Peanut".  The series ended on May 22, 2013.

Veronica Mars: Veronica Mars is an American teen noir mystery drama television series created by screenwriter Rob Thomas.  The series is set in the fictional town of Neptune, California, and stars Kristen Bell as the eponymous character.  The series premiered on September 22, 2004, during television network UPN's final two years, and ended on May 22, 2007, after a season on UPN's successor, The CW, airing for three seasons total.  "Veronica Mars" was produced by Warner Bros.  Television, Silver Pictures Television, Stu Segall Productions, and Rob Thomas Productions.  Joel Silver and Rob Thomas were executive producers for the entire run of the series, while Diane Ruggiero was promoted in the third season.

Fight for My Way: Fight for My Way (; lit.  "Third-Rate My Way") is a South Korean television series starring Park Seo-joon and Kim Ji-won, with Ahn Jae-hong and Song Ha-yoon.  It premiered on May 22, 2017 every Monday and Tuesday at 22:00 (KST) on KBS2.

Cloudy with a Chance of Meatballs (TV series): Cloudy with a Chance of Meatballs (also called Cloudy: The Series) is a Canadian-American animated comedy television series produced by DHX Media and Sony Pictures Animation in association with Corus Entertainment.  It is the first television series to be produced by Sony Pictures Animation.  Based on the children's book and the film series of the same name, the series was flash animated using Toon Boom Harmony.  Originally commissioned by Teletoon, the series premiered in the United States on March 6, 2017, on Cartoon Network, with a sneak peek airing on February 20, 2017.  In Canada, the series premiered on April 6, 2017, on YTV.

List of Veronica Mars characters: "Veronica Mars" is an American television series created by Rob Thomas.  The series premiered on September 22, 2004, during UPN's last two years, and ended on May 22, 2007, after a season on UPN's successor, The CW Television Network.  Balancing murder mystery, high-school and college drama, the series features social commentary with sarcasm and off-beat humor in a style often compared to film noir.  Set in the fictional town of Neptune, the series starred Kristen Bell as the title character, a student who progressed from high school to college during the series while moonlighting as a private investigator under the wing of her detective father.

Song Ha-yoon: Song Ha-yoon (born Kim Mi-sun on December 2, 1986) is a South Korean actress.  She debuted as Kim Byul () but changed her stage name to Song Ha-yoon in 2012.  She is best known for her role in the drama "Fight for My Way" (2017).

Kim Su-ro, The Iron King: Kim Su-ro, The Iron King () is a 2010 South Korean television series on the life of Suro of Geumgwan Gaya, starring Ji Sung, Bae Jong-ok, Yu Oh-seong, Seo Ji-hye, Go Joo-won, Kang Byul and Lee Pil-mo.  It aired on MBC from May 29 to September 18, 2010 on Saturdays and Sundays at 21:45 for 32 episodes.

List of Max &amp; Ruby episodes: "Max & Ruby" is an animated children's television series based on the book series by Rosemary Wells.  In Canada, the series debuted on Treehouse TV on May 3, 2002, and in the United States, the series premiered on Nick Jr. on October 21.  A sixth season of the series premiered on September 18, 2016, with a new main voice cast and theme song.  New episodes of the series are scheduled to premiere Fall 2017.

Question: Which television series premiered on May 22, 2017 and stars an actress who debuted as Kim Byul?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "series_name": {
      "type": "string",
      "description": "The name of the television series."
    },
    "premiere_date": {
      "type": "string",
      "format": "date",
      "description": "The date the series premiered."
    },
    "star_details": {
      "type": "object",
      "properties": {
        "star_name": {
          "type": "string",
          "description": "The current stage name of the actress."
        },
        "debut_name": {
          "type": "string",
          "description": "The name the actress debuted under."
        },
        "known_for_series": {
          "type": "string",
          "description": "The series the actress is best known for."
        }
      },
      "required": [
        "star_name",
        "debut_name",
        "known_for_series"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "series_name",
    "premiere_date",
    "star_details"
  ],
  "additionalProperties": false
}
