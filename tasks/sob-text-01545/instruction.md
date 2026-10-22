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
Razorlight: Razorlight is an English indie rock band formed in 2002 by lead singer and rhythm guitarist Johnny Borrell.  The band are primarily known in the UK, having topped the charts with the 2006 single "America" and its parent self-titled album, their second.  Along with Borrell, the current lineup of the band consists of drummer David Sullivan Kaplan, lead guitarist Gus Robertson, and bassist João Mello.

Der Schneemann: Der Schneemann, also known as The Snowman, Snowman in July or The Magic Snowman, is a 1944 animated short film, created in Germany under the Nazi regime.  It was written by cartoonist Horst von Möllendorff and animated by Hans Fischerkoesen.  It was animated in Potsdam, Germany, near UFA's Neubabelsberg Studios.

The Courteeners: Courteeners are an English indie rock band formed in Middleton in 2006 by Liam Fray (lead guitar/vocals), Michael Campbell (drums/backing vocals), Daniel "Conan" Moores (rhythm guitar) and Mark Cuppello (bass); the latter was replaced by the band's producer Joe Cross in 2015.  They also tour with pianist Adam Payne, who has been featured on every album.  In December 2012, the band dropped "The" from their name, continuing simply as "Courteeners".

Jubilee Bunt-a-thon: Jubilee Bunt-a-thon is a 2012 animated short film directed by Nick Park, which stars his characters Wallace and Gromit.

The Snowman and the Snowdog: The Snowman and The Snowdog is a 2012 animated short film.  It is the sequel to "The Snowman", and was created to mark the 30th anniversary of the original short film.  "The Snowman and The Snowdog" is dedicated to John Coates (the film's producer, who died in September 2012) and features a new song called "Light the Night" by former Razorlight drummer Andy Burrows.  "The Snowman and The Snowdog" won the Televisual Bulldog Award 2013 in the Best Children's category.

Paperman: Paperman is a 2012 American black-and-white computer-cel animated romantic comedy short film produced by Walt Disney Animation Studios and directed by John Kahrs.  The short blends traditional animation and computer animation, and won both the Academy Award for Best Animated Short Film at the 85th Academy Awards and the Annie Award for Best Animated Short Subject at the 40th Annie Awards.  "Paperman" was the first animated short film produced by Walt Disney Animation Studios to win an Academy Award since "It's Tough to Be a Bird" in 1970.

Kali the Little Vampire: Kali the Little Vampire (Portuguese: Kali, o pequeno vampiro) is a 2012 animated short film directed by Regina Pessoa.

No Light, No Light: No Light, No Light is a song by English indie rock band Florence and the Machine from their second studio album, "Ceremonials" (2011).  The song was written by band members Florence Welch and Isabella Summers while the production was handled by Paul Epworth.  Island Records released the song as the second single from the album on 16 January 2012.  The song was the first one written for the album in the band's tour bus in Amsterdam.  Lyrically, in the song, Welch is expressing frustration about the state of her fragile relationship and she further tries to keep it together.  "No Light, No Light" received positive reviews by music critics who generally praised Welch's vocals and the drum-led instrumentation.  It was also placed on several critics' year-end lists of best singles.  The song peaked at number fifty on the UK Singles Chart, the Irish Singles Chart and number thirty nine on the US "Billboard" Alternative Songs chart.

Wild Life (film): Wild Life is a 2011 Canadian animated short film by Wendy Tilby and Amanda Forbis.  The film debuted at the 2011 Worldwide Short Film Festival in Toronto in June 2011 and online on January 6, 2012.  The film was nominated for Best Animated Short Film at the 84th Academy Awards, and Best Animated Short Subject at the 39th Annie Awards as well as a Genie Award for Best Animated Short at the 32nd Genie Awards.

A Morning Stroll: A Morning Stroll is an English animated short film by Grant Orchard.  The film was screened at the 2011 Brooklyn Film Festival as well as the 2012 Sundance Film Festival where it won Best Animation and the Jury Prize in Animated Short Film respectively.  The film was also nominated Best Animated Short Film at the 84th Academy Awards as well as Best Short Animation at the 65th British Academy Film Awards.

Question: What English indie rock band formed in 2002 had their song called "Light the Night" featured in the 2012 animated short film, The Snowman and the Snowdog?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the English indie rock band."
    },
    "formation_year": {
      "type": "integer",
      "description": "The year the band was formed."
    },
    "genre": {
      "type": "string",
      "description": "The musical genre of the band."
    },
    "featured_song": {
      "type": "object",
      "properties": {
        "song_title": {
          "type": "string",
          "description": "The title of the song featured in the film."
        },
        "film_title": {
          "type": "string",
          "description": "The title of the animated short film where the song was featured."
        },
        "song_artist_relationship_to_band": {
          "type": "string",
          "description": "Describes the relationship of the song's artist to the band."
        }
      },
      "required": [
        "song_title",
        "film_title",
        "song_artist_relationship_to_band"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "band_name",
    "formation_year",
    "genre",
    "featured_song"
  ],
  "additionalProperties": false
}
