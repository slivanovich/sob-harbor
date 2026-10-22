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
Winnie the Pooh (song): "Winnie the Pooh" is the title song for the franchise of the same name.  It is musically emblematic of the most successful branding Disney currently owns and has been used in most merchandising models of the brand since the song's first publication in 1966 in the musical film featurette "Winnie the Pooh and the Honey Tree".  In film, the song is generally utilized in the title sequence.  The lyric gives an overview of the characters and the roles each plays in relation to Pooh himself.  The song has been used in every theatrically released Pooh film as well as most of the television series.  The songwriters are the Sherman Brothers, who have written the grand majority of Winnie the Pooh songs and musical numbers since 1966.  It is unknown who performed the song.  The song was also performed by Carly Simon.  A music video was released for this version and it was included in "The Many Adventures of Winnie the Pooh" DVD.

The Rain Rain Rain Came Down Down Down: "The Rain Rain Rain Came Down Down Down" is a narrative song from the Walt Disney musical film featurette, "Winnie the Pooh and the Blustery Day".  The song is also incorporated into the 1977 musical film "The Many Adventures of Winnie the Pooh" which is an amalgamation of three Winnie-the-Pooh featurettes including "Blustery Day".  The song was written by the Sherman Brothers who have written most of the music for the Winnie-the-Pooh franchise over the many years.  It was sung by an unidentified off-screen chorus with occasional lines sung by veteran character actor Sterling Holloway who provided the voice of Pooh.

Winnie-the-Pooh: Winnie-the-Pooh, also called Pooh Bear, is a fictional anthropomorphic teddy bear created by English author A. A. Milne.

Little Black Rain Cloud: "Little Black Rain Cloud" is a song from the 1966 musical film featurette "Winnie the Pooh and the Honey Tree".  An instrumental version is played in the next featurette "Winnie the Pooh and the Blustery Day".  The song was also subsequently incorporated into the 1977 musical film, "The Many Adventures of Winnie the Pooh" which is an amalgamation of the three previous Winnie-the-Pooh featurettes including "Honey Tree".  In the song Winnie the Pooh comments about the on-screen actions where he is pretending to be a "Little Black Rain Cloud", as the title implies.  It's Pooh's hope that the Honey Bees will not notice him as he approaches their coveted honey.

Up, Down and Touch the Ground: "Up, Down and Touch the Ground" is a song from the 1966 musical film featurette "Winnie the Pooh and the Honey Tree".  The song was also subsequently incorporated into the 1977 musical film, "The Many Adventures of Winnie the Pooh" which is an amalgamation of the three previous Winnie-the-Pooh featurettes including "The Honey Tree".  In the song Winnie the Pooh's exercise makes him hungry, and although he over-eats (it leads to his stuck-in-Rabbit's door incident later in the film), he is proud of his fat stomach and he exercises to gain weight and grow even rounder.  Halfway through the song however, he bends down too far, accidentally ripping the stitching on his bottom as a result of becoming fat, but upon seeing his bottom in the mirror, he quickly ties it together again.  By the end of the song Pooh has rationalized his over-eating by calling his hunger, "healthy".

Winnie the Pooh and Tigger Too: Winnie the Pooh and Tigger Too is a 1974 animated featurette from Disney released as a double feature with "The Island at the Top of the World".  It was nominated for an Academy Award for Best Animated Short Film, but lost to "Closed Mondays".  It was later added as a segment to the 1977 film "The Many Adventures of Winnie the Pooh".  A soundtrack album was released simultaneously and featured such songs as "The Honey Tree" and "Birthday, Birthday."  The film, whose name is a play on the slogan "Tippecanoe and Tyler too" made famous during the 1840 United States presidential election, is based on the third, fourth and seventh chapters from "The House at Pooh Corner" by A. A. Milne.

Hip Hip Pooh-Ray!: "Hip Hip Pooh-Ray!"  is a song from the 1968 musical film featurette "Winnie the Pooh and the Blustery Day".  It is sung by the cast as a release from the dramatic tension of the story.  The song is also incorporated into (and used as the promotional tagline for) the 1977 musical film "The Many Adventures of Winnie the Pooh" which is an amalgamation of three Winnie-the-Pooh featurettes including "Blustery Day".  In the song, Pooh and Piglet are hailed as heroes (Pooh for saving Piglet's life, and Piglet for giving Owl his grand home in the beech tree).

Gopher (Winnie-the-Pooh): Gopher is a fictional grey anthropomorphic gopher, character who first appeared in the 1966 Disney animated film "Winnie the Pooh and the Honey Tree", introducing himself as Samuel J. Gopher.  He has a habit of whistling out his sibilant consonants, one of various traits he has in common with the beaver in "Lady and the Tramp", by whom he may have been inspired.  While he never made appearances in any episodes of "Welcome to Pooh Corner", Gopher was fleshed out a bit further in the television series "The New Adventures of Winnie the Pooh".  He is portrayed as generally hard-working, especially in his tunnels (which he inevitably falls into at least once).  He does not appear in the original books Winnie the Pooh and The House at Pooh Corner by A. A. Milne until 1966 (a fact that is regularly pointed out in "Winnie the Pooh and the Honey Tree", when he breaks the fourth wall by saying he's "not in the book, y'know", also trying to say that he would not be in a phone book).  Gopher's voice was originally done by Howard Morris, who retired from the role and was replaced by Michael Gough.

Rumbly in My Tumbly: "Rumbly in My Tumbly" is a song from the 1966 musical film featurette "Winnie the Pooh and the Honey Tree".  The song is also incorporated into the 1977 musical film, "The Many Adventures of Winnie the Pooh" which is an amalgamation of the first three Winnie-the-Pooh featurettes including "Honey Tree".

Mind over Matter (song): "Mind Over Matter" is a song from the 1966 musical film featurette "Winnie the Pooh and the Honey Tree".  The song was also subsequently incorporated into the 1977 musical film, "The Many Adventures of Winnie the Pooh" which is an amalgamation of the three previous Winnie-the-Pooh featurettes including "Honey Tree".

Question: "Rumbly in My Tumbly" is a song from the 1966 musical film featurette "Winnie the Pooh and the Honey Tree", is also incorporated into the 1977 musical film, "The Many Adventures of Winnie the Pooh" which is an amalgamation of the first three featurettes, of which fictional anthropomorphic teddy bear, created by English author A. A. Milne?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song mentioned in the question."
    },
    "primary_film_featurette": {
      "type": "string",
      "description": "The initial musical film featurette where the song first appeared."
    },
    "amalgamation_film": {
      "type": "string",
      "description": "The later musical film that incorporated the song and was an amalgamation of featurettes."
    },
    "character_details": {
      "type": "object",
      "properties": {
        "character_name": {
          "type": "string",
          "description": "The name of the fictional character."
        },
        "character_type": {
          "type": "string",
          "description": "A description of the character's nature."
        },
        "creator": {
          "type": "string",
          "description": "The author who created the character."
        }
      },
      "required": [
        "character_name",
        "character_type",
        "creator"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "song_title",
    "primary_film_featurette",
    "amalgamation_film",
    "character_details"
  ],
  "additionalProperties": false
}
