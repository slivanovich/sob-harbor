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
Joseph Bishara: Joseph Bishara (born July 26, 1970) is an American composer, producer, and actor, best known for his work scoring films such as "Insidious", "11-11-11", "Dark Skies", and "The Conjuring".  Bishara's career began with the 1998 Biblical drama "Joseph's Gift", though he composes music for mainly horror films and has collaborated several times with director James Wan.  Projects by directors John Carpenter and Joseph Zito, and musicians Ray Manzarek and Diamanda Galás have incorporated Bishara's work.  He has also functioned as a producer on "Repo!  The Genetic Opera" and other projects.

Jenma Natchathiram: Jenma Natchathiram (தமிழ்: ஜென்ம நட்சத்திரம், English: Birth Star) is a 1991 Tamil supernatural horror film directed and Screenplays by Thakkali Srinivasan for Thirai Gangai Films.  The film dialogue were written by Ma.  Pandarinathan, and story were written by Krishnan respectively.  Music by Premi - Srini assets to the soundtrack.  It Stars Baby Vichithra played titular role with Pramoth, Sindhuja and Vivek played pivotal role.  The film was unofficial remake of "The Omen", 1976 British/American supernatural horror drama film directed by Richard Donner.

TC Smith: TC Smith, also known as "TC/TNT," is an American singer and live programmer best known for her work with Triggerpimp, Anna Thema, TCR, Satiate, and Meridian Dream (with Rae DiLeo) as well as her voiceover work with producer Joseph Bishara.  Her voice talents have been featured in movie trailers for films such "The Village", "The Amityville Horror (2005)", and "Silent Hill".  Her voice work also appears in the movie score for "The Gravedancers", a 2005 horror film, along with Melora Creager of Rasputina.

Shutter (2008 film): Shutter is a 2008 American supernatural horror film directed by Masayuki Ochiai and starring Joshua Jackson, Rachael Taylor, and Megumi Okina.  The film is a remake of the 2004 Thai horror film of the same name and was released on March 21, 2008.  Despite a generally negative reaction, the film was a box office success grossing nearly 6 times its budget.

The Amityville Horror (1979 film): The Amityville Horror is a 1979 American supernatural horror film directed by Stuart Rosenberg, based on Jay Anson's 1977 book of the same name.  It stars James Brolin and Margot Kidder as a young couple who purchase a home they come to find haunted by combative supernatural forces.  The story is based on the alleged experiences of the Lutz family who bought a new home on 112 Ocean Avenue in Amityville, New York, a house where a mass murder had been committed the year before.  It is the first film based on the Amityville horror.

The Conjuring: The Conjuring is a 2013 American supernatural horror film directed by James Wan and written by Chad Hayes and Carey W. Hayes.  It is the first installment in "The Conjuring" series.  Patrick Wilson and Vera Farmiga star as Ed and Lorraine Warren, paranormal investigators and authors associated with prominent cases of haunting.  Their purportedly real-life reports inspired "The Amityville Horror" story and film franchise.  The Warrens come to the assistance of the Perron family (Ron Livingston and Lili Taylor), who are experiencing increasingly disturbing events in their farmhouse in Rhode Island in 1971.

Exeter (film): Exeter is a 2015 American supernatural horror film directed by Marcus Nispel.  The film opened in the UK at the Glasgow Horror Film Festival in February 27, 2015.  The film was released on DVD in the UK on May 7, 2015.  "Exeter" made its US debut in July 2, 2015 on DirecTV Cinema.

The Rage: Carrie 2: The Rage: Carrie 2 is a 1999 American supernatural horror film directed by Katt Shea and a sequel to the 1976 horror film "Carrie", based on the novel of the same name by Stephen King, and features Carrie White's baby half sister Rachel Lang in the lead role.  Directed by Katt Shea, the film stars Emily Bergl, Jason London, Dylan Bruno, J. Smith-Cameron, and Amy Irving who reprises her role of Sue Snell from the previous film.

Special Effects (album): Special Effects is the fifteenth studio album by American rapper Tech N9ne.  It was released on May 4, 2015, by Strange Music.  The album is broken up into several portions representing days of the week, with collaborations with artists including Corey Taylor, B.o.B, Lil Wayne, 2 Chainz, T.I., Hopsin, E-40, Yo Gotti, Audio Push and Eminem, among others.  The album also features fellow Strange Music artists Krizz Kaliko, Big Scoob and Ces Cru.  Production on the album was handled by Seven, Strange Music's in-house producer, Excision along with Joseph Bishara who was the composer of "Insidious" and "The Conjuring".

The Apparition: The Apparition is a 2012 American supernatural horror film, written and directed by Todd Lincoln, making his directorial debut, and starring Ashley Greene, Sebastian Stan, Tom Felton, Julianna Guill and Rick Gomez.  The plot follows three college students who, after the death of their friend, must battle a supernatural force they summoned themselves.  The film was loosely inspired by the Philip experiment conducted in 1972.  The film was a box office bomb and was cited by critics as one of the worst horror movies of 2012.  It was also the last Warner Bros.  Pictures horror film to be released under its own label before resorting to New Line Cinema to release all future horror movies made by Warner Bros.

Question: which American supernatural horror film was composed by Joseph Bishara

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_info": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film."
        },
        "release_year": {
          "type": "integer",
          "description": "The year the film was released."
        },
        "genres": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of genres the film belongs to."
        },
        "country_of_origin": {
          "type": "string",
          "description": "The country where the film was produced."
        },
        "director": {
          "type": "string",
          "description": "The director of the film."
        }
      },
      "required": [
        "title",
        "release_year",
        "genres",
        "country_of_origin",
        "director"
      ],
      "additionalProperties": false
    },
    "composer_info": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the composer."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "composition_role": {
      "type": "string",
      "description": "The role of Joseph Bishara in the film's music production."
    },
    "meets_query_criteria": {
      "type": "boolean",
      "description": "True if the film is an American supernatural horror film composed by Joseph Bishara."
    }
  },
  "required": [
    "film_info",
    "composer_info",
    "composition_role",
    "meets_query_criteria"
  ],
  "additionalProperties": false
}
