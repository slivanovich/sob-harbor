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
Opulence (EP): Opulence is the debut extended play (EP) by American rapper and recording artist Brooke Candy, released as digital download by RCA Records on 6 May 2014.  The EP is preceded by the release of title track and lead single "Opulence" and is Candy's first major label release.  The EP features production from Diplo, Kool Kojak, Jesse Shatkin and Shea Taylor among others, including a feature with producer Cory Enemy and songwriting work from Mozella, Jesse St. John and Sia, this later also serving as the executive producer of the project.

Chandelier (song): "Chandelier" is a song by Australian singer Sia from her sixth studio album, "1000 Forms of Fear" (2014).  Written by Sia and Jesse Shatkin and produced by Shatkin and Greg Kurstin, the song was released on 17 March 2014 as the lead single from the album.  It's an electropop song, featuring electronica, R&B and reggae influences.  Lyrically, the song has a melancholic theme, detailing the demoralisation and rationalisation of alcoholism through the typical thought process of a "party girl".

Piece by Piece (Kelly Clarkson album): Piece by Piece is the seventh studio album by American singer Kelly Clarkson.  It was released on February 27, 2015, by RCA Records.  It was her final album under her recording contract with the label, to which she signed after winning the first season of "American Idol" in 2002, and made the switch to Atlantic in 2016. The album saw Clarkson reuniting with frequent collaborators Greg Kurstin, Jesse Shatkin, Jason Halbert, Eric Olson, and Chris DeStefano.  Her pregnancy hindered her efforts to write several songs, five of which ended up on the album.  She also gathered material from songwriters such as Sia, Matthew Koma, MoZella, Bonnie McKee, David Jost, Semi Precious Weapons lead singer Justin Tranter, and former Cobra Starship member Ryland Blackinton, among others.  Inspired by the orchestral production on "Wrapped in Red", Clarkson wanted all the songs on "Piece by Piece" to resonate like its own film soundtrack, taking a cue from the soundtracks of the feature motion pictures "Cruel Intentions" (1999) and "Love Actually" (2003) and commissioning orchestral arrangements by Joseph Trapanese.

Take You High: "Take You High" is a song by American recording artist Kelly Clarkson from her seventh studio album, "Piece by Piece" (2015).  Written by Jesse Shatkin and MoZella, the song is produced by Shatkin.  A midtempo EDM gospel tune, it is a song of encouragement and escapism, in which the singer lends a hand to the despondent.  Musically featuring an auto-tuned EDM breakdown, Shatkin described its sound as "an electronic banger" and "a little left-of-center", while Clarkson commented that it reminded her of the music of soundtrack to the 1999 film "Cruel Intentions".

Alive (Sia song): "Alive" is the lead single from Australian singer and songwriter Sia's seventh studio album "This Is Acting" (2016).  It was co-written by Sia, Adele, and Tobias Jesso Jr. The song was produced by Jesse Shatkin.  "Alive" was released on 25 September 2015.  The song was originally intended for Adele's third studio album, "25", along with "Bird Set Free".  However, since Adele decided not to use the songs, she let Sia use them for her seventh studio album.  Musically, it is a midtempo pop and synth-pop song.

Sledgehammer (Rihanna song): "Sledgehammer" is a song recorded by Barbadian singer Rihanna.  It was released on June 27, 2016 as a single to promote "Star Trek Beyond".  It plays during the film's closing credits but is not included on the film's soundtrack.  The song was written by Sia Furler (Sia), Robyn Fenty (Rihanna) and Jesse Shatkin.  A music video for the song was released on June 30, 2016, and shows Rihanna performing magical acts on a foreign planet.  The video was shot entirely on IMAX cameras.

Unstoppable (Sia song): "Unstoppable" is a song by Australian singer-songwriter Sia Furler (often referred to mononymously as Sia), taken from her seventh studio album "This Is Acting" (2016).  The song was written by Sia and Christopher Braide, and produced by Jesse Shatkin.  It was released as the album's final promotional single on January 20, 2016.  In July, a new version of the song was made for Gillette's 2016 Olympic ad campaign, "Pretty Isn't Perfect" which features a verse from Pusha T.

Jesse Shatkin: Jesse Samuel Shatkin is an American songwriter, producer and engineer.  He has worked with Sia, Kelly Clarkson, Fitz and the Tantrums and One Direction, among others.  Shatkin was nominated in 2014 for Grammy Awards as both a producer (Record of the Year) and as a songwriter (Song of the Year).  Both nominations were based on his work on the Sia track "Chandelier", which he co-wrote and co-produced.  He was also nominated in the Record of the Year category in 2013 as an engineer on Clarkson's single "Stronger (What Doesn't Kill You)".

Reaper (song): "Reaper" is a song from Australian singer and songwriter Sia's seventh studio album "This Is Acting" (2016).  The song was co-written by Sia, Kanye West, Noah Goldstein, Charles Misodi Njapa (better known by his stage name 88-Keys), and Dom $olo, originally for Rihanna's album "Anti" (2016).  "Reaper" was co-produced by West, Dom $olo, Goldstein, 88-Keys, Jesse Shatkin, and Jake Sinclair.  Sia and West had previously collaborated on the latter's song "Wolves".

Invincible (Kelly Clarkson song): "Invincible" is a song by American singer Kelly Clarkson from her seventh studio album, "Piece by Piece" (2015).  It was written by Sia, Jesse Shatkin, Steve Mostyn, and Warren Felder.  Produced by Shatkin, the track is an orchestral synthpop anthem about self-empowerment.  "Invincible" features uncredited vocals from Sia, as well as string arrangements by Oliver Kraus.  It was first released as the first promotional single from "Piece by Piece" on February 23, 2015, but then issued as the album's second single to Hot Adult Contemporary radio stations on May 18, 2015 through RCA Records.

Question: Jesse Shatkin worked on which 2014 Sia track?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "primary_artist": {
      "type": "string",
      "description": "The main artist of the song."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the song was released."
    },
    "collaborator_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the collaborator."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The roles Jesse Shatkin had on the song."
        },
        "grammy_nominations": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "year": {
                "type": "integer",
                "description": "The year of the Grammy nomination."
              },
              "category": {
                "type": "string",
                "description": "The category of the Grammy nomination."
              }
            },
            "required": [
              "year",
              "category"
            ],
            "additionalProperties": false
          },
          "description": "Grammy nominations related to Jesse Shatkin's work on this specific song."
        }
      },
      "required": [
        "name",
        "roles",
        "grammy_nominations"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "song_title",
    "primary_artist",
    "release_year",
    "collaborator_details"
  ],
  "additionalProperties": false
}
