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
Marines, Let's Go: Marines, Let's Go is a 1961 CinemaScope colour Korean War film about three Marine buddies (Tom Tryon, David Hedison and Tom Reese) on shore leave in Japan and at war in Korea.  It was produced and directed by Raoul Walsh, who also wrote the story.  Walsh had previously had successes with films about the U.S. Marine Corps in World War I ("What Price Glory? "), the 1920s ("The Cock-Eyed World" and "Sadie Thompson"), and World War II ("Battle Cry").  This was the next-to-last film of Walsh's long directing career.

The Son of Robin Hood: The Son of Robin Hood is a 1958 adventure DeLuxe color CinemaScope film directed by George Sherman, starring David Hedison and June Laverick.  The son of the legendary Robin Hood helps save his countrymen from the tyrannical rule of an evil aristocrat.  Unfortunately, the "son" is a sham and after several unsuccessful attempts to stop the nasty nobleman, the merry men decide to send for Robin's real son.  Imagine their surprise when they discover that Robin Jr. is a she!  Still the men rally around her and the imposter.  Together they defeat the evil-doer and the country is again safe.

David Hedison: Albert David Hedison, Jr. (born May 20, 1927) is an American film, television, and stage actor.  He was billed as Al Hedison in his early film work.  In 1959, when he was cast in the role of Victor Sebastian in the short-lived espionage television series "Five Fingers", NBC insisted that he change his name.  He proposed that he use his middle name and he has been billed as David Hedison ever since.  He is known for his role as Captain Lee Crane in Irwin Allen's television series "Voyage to the Bottom of the Sea" and as CIA agent Felix Leiter in two James Bond films, "Live and Let Die" and "Licence to Kill".

The ABC Afternoon Playbreak: The ABC Afternoon Playbreak is an American television anthology series that was broadcast on ABC from 1973 to 1975.  The ninety-minute dramas aired once a month and featured some of the more popular television and film stars of the 1970s (Diana Hyland, Bradford Dillman, Patty Duke, Diane Baker, David Hedison).

The Fly (1958 film): The Fly is a 1958 American science fiction-horror film produced and directed by Kurt Neumann.  The screenplay by James Clavell was based on the 1957 short story of the same name by George Langelaan.  The film stars David Hedison, Patricia Owens, Vincent Price and Herbert Marshall.

Rolf Becker: Rolf Becker (born 31 March 1935 in Leipzig, Germany) is a German television actor.  By his first wife, actress Monika Hansen, he is the father of actor Ben Becker, and actress and singer Meret Becker.

Gazzara: Gazzara is a 2012 film set in New York, based on the life and career of actor Ben Gazzara who writer/director Joseph Rezwin met in 1977 on the set of John Cassavetes’ "Opening Night".  Their conversations about acting and art, fears and desires, life and death all culminate in the final Central Park sequence where Ben persuades Joe it is time to cut the cord, end the obsession with him and Cassavetes and pursue his passion of art and filmmaking in his own individual way as Ben did throughout his entire life.

Ben Bagdikian: Ben Haig Bagdikian (January 30, 1920 – March 11, 2016) was an Armenian-American educator and journalist.  He was a significant American media critic and the dean of the University of California, Berkeley Graduate School of Journalism.

Creditors (2015 film): Creditors is a British drama film written and directed by Ben Cura, based on the play of the same title by August Strindberg and starring Christian McKay, Andrea Deck, Ben Cura, Tom Bateman and Simon Callow.  Set in present-day England and Spain in this adaptation, it had its world premiere at the 2015 Nordic International Film Festival in New York City as part of the festival's Official Selection, where it was nominated for and was awarded the Honorable Mention for Best Nordic Narrative Feature.  The film was a United Kingdom production by London-based company Tough Dance, founded by Ben Cura and Andrea Deck.  Spanish company Cuibar Productions financed the film.  Paris-based sales agents New Morning Films took on world sales of the film in early 2015.  The film is actor Ben Cura's debut as a director, screenwriter, and producer.

Shadows of Liberty: Shadows of Liberty is a 2012 British documentary film directed by Canadian filmmaker Jean-Philippe Tremblay.  The documentary examines the impact of corporate media and concentration of media ownership on journalism and the news.  It is based on the book "The Media Monopoly" by Ben Bagdikian.  The film’s title is borrowed from a Thomas Paine quote: "When men yield up the privilege of thinking, the last shadow of liberty quits the horizon."

Question: Who was a television actor Ben Bagdikian or David Hedison?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "television_actor_identified": {
      "type": "string",
      "description": "The name of the person identified as a television actor."
    },
    "is_television_actor": {
      "type": "boolean",
      "description": "Indicates whether the identified person is a television actor."
    },
    "professions": {
      "type": "array",
      "description": "A list of professions held by the identified person.",
      "items": {
        "type": "string"
      }
    },
    "television_appearances": {
      "type": "array",
      "description": "Details of the identified person's television appearances.",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the television series or anthology."
          },
          "type": {
            "type": "string",
            "description": "The type of television appearance (e.g., 'series', 'anthology_series')."
          },
          "role": {
            "type": "string",
            "description": "The character played in the television appearance, if specified."
          },
          "year_info": {
            "type": "string",
            "description": "Relevant year information for the television appearance (e.g., 'cast in 1959', '1973 to 1975')."
          }
        },
        "required": [
          "title",
          "type"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "television_actor_identified",
    "is_television_actor",
    "professions",
    "television_appearances"
  ],
  "additionalProperties": false
}
