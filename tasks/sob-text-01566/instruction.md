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
Bridesmaids (2011 film): Bridesmaids is a 2011 American comedy film directed by Paul Feig, written by Annie Mumolo and Kristen Wiig, and produced by Judd Apatow, Barry Mendel and Clayton Townsend.  The plot centers on Annie (Wiig), who suffers a series of misfortunes after being asked to serve as maid of honor for her best friend, Lillian, played by Maya Rudolph.  Rose Byrne, Melissa McCarthy, Ellie Kemper, and Wendi McLendon-Covey co-star as Lillian's bridesmaids, with Chris O'Dowd, Rebel Wilson, Matt Lucas, Michael Hitchcock, and Jill Clayburgh, in her final film appearance, in supporting roles.

I Am David (film): I Am David is a 2003 American drama film directed by Paul Feig in his directorial debut.  It is based on the novel of the same name (originally published in the USA under the name "North to Freedom") by Anne Holm.  The film was produced by Walden Media and Lions Gate Entertainment.

The Heat (film): The Heat is a 2013 American buddy cop action comedy film directed by Paul Feig and written by Katie Dippold.  The film centers on FBI Special Agent Sarah Ashburn (Sandra Bullock) and Boston Detective Shannon Mullins (Melissa McCarthy), who must take down a mobster in Boston.  Demián Bichir, Marlon Wayans and Michael Rapaport also star.

Spy (2015 film): Spy is a 2015 American action comedy spy film written and directed by Paul Feig.  Starring Melissa McCarthy, Jason Statham, Rose Byrne, Miranda Hart, Bobby Cannavale, Allison Janney, and Jude Law, the film follows the transformation of desk-bound CIA analyst Susan Cooper (McCarthy) into a field agent who attempts to foil the black market sale of a suitcase nuke.

The Nix brothers: Evan Nix (born December 10, 1983) and Adam Nix (born October 11, 1986), known together professionally as the Nix Bros., are American film directors, producers, and musicians.  They are most well known for filming the series "The Grawlix" on Funny Or Die, a weekly comedy show featuring regular appearances by comedians Adam Cayton-Holland, Ben Roy, and Andrew Orvedahl, and for directing an episode of Paul Feig's 2015 comedy series "Other Space".  The two are also known as the founding members of the synthpop comedy band Total Ghost, a group for which they won best music video at the Festivus film festival in Denver, Colorado.  The Nix Bros. later directed the Festivus spinoff Laugh Track Comedy Festival in 2011 and 2012.

Ski Patrol (1990 film): Ski Patrol is a 1990 American comedy film directed by Richard Correll, and starring Roger Rose, Yvette Nipar, Paul Feig, T. K. Carter, Leslie Jordan, George Lopez, Ray Walston, and Martin Mull.

Ghostbusters (2016 film): Ghostbusters (also known as Ghostbusters: Answer the Call and marketed as such on home release) is a 2016 supernatural comedy film directed by Paul Feig and written by Feig and Katie Dippold.  The film stars Melissa McCarthy, Kristen Wiig, Kate McKinnon, Leslie Jones, Neil Casey, Andy García, Cecily Strong, and Chris Hemsworth.  It is the third feature film in the "Ghostbusters" franchise, and serves as a reboot of the series.  The story focuses on four women who begin a ghost-catching business in New York City.  It also marks the fourth collaboration between Feig and McCarthy.

Unaccompanied Minors: Unaccompanied Minors (also known as Grounded in the United Kingdom and Ireland) is a 2006 Christmas comedy film directed by Paul Feig and starring Lewis Black, Wilmer Valderrama, Tyler James Williams, Dyllan Christopher, Brett Kelly, Gia Mantegna, and Quinn Shephard.  It is based on a true story by Susan Burton first told on the public radio show "This American Life", under the title "In the Event of an Emergency, Put Your Sister in an Upright Position".

Good Girls (Elle King song): "Good Girls" is a song written and recorded by American singer and songwriter Elle King for the soundtrack of the 2016 supernatural comedy film, "Ghostbusters".  The song was co-written and produced by Dave Bassett.  It was released digitally on June 3, 2016 through RCA Records as the soundtrack's lead single and impacted American Triple A radio on June 13, 2016.

Kate McKinnon: Kathryn McKinnon Berthold (born January 6, 1984), known professionally as Kate McKinnon, is an American comedian and actress.  A cast member on "Saturday Night Live" and "The Big Gay Sketch Show," she also starred as Dr. Jillian Holtzmann in the 2016 "Ghostbusters" reboot.

Question: Who played Dr. Jillian Holtzmann in a 2016 supernatural comedy film directed by Paul Feig?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_genre": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The genre(s) of the film."
    },
    "director_name": {
      "type": "string",
      "description": "The name of the film's director."
    },
    "character_name": {
      "type": "string",
      "description": "The name of the character in the film."
    },
    "actress_full_name": {
      "type": "string",
      "description": "The full name of the actress who played the character."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "film_genre",
    "director_name",
    "character_name",
    "actress_full_name"
  ],
  "additionalProperties": false
}
