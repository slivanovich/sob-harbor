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
Giving Up the Gun: "Giving Up the Gun" is the second single from Vampire Weekend's second album "Contra".  The song was originally performed by L'Homme Run, a comedic rap duo that featured Vampire Weekend vocalist Ezra Koenig.  The video was released February 19, 2010.  Koenig got the idea for the song from Noel Perrin's 1979 book titled "Giving Up the Gun" given to him by his father.

Free the Universe: Free the Universe is the second full-length studio album released by Major Lazer, collaborative music group headed by record producer Diplo.  The album was released on April 16, 2013, and features appearances by Vampire Weekend's Ezra Koenig, Dirty Projectors' Amber Coffman, Santigold, Peaches, Tyga, Flux Pavilion, Bruno Mars, Wyclef Jean, Shaggy, and more.  The album peaked at No. 34 in both the "Billboard" 200 and the UK Albums Chart.

White Women (album): White Women is the fourth studio album by Canadian electro-funk duo Chromeo, released on May 12, 2014 by Last Gang Records.  The album features contributions from Vampire Weekend's Ezra Koenig, Toro y Moi, Solange Knowles, LCD Soundsystem's Pat Mahoney, and Fool's Gold duo Oliver.

King Adora: King Adora was a rock group formed in Birmingham, England in 1998.  The band released debut album "Vibrate You" in May 2001 (charting at No. 30 on the UK Albums Chart) and follow-up "Who Do You Love? " in March 2004.  The band was notable for their short, riotous live shows and built a small, dedicated fanbase.  Lack of label support and changing tastes in the UK guitar music scene led King Adora to split in 2005.  In 2010, the band reformed to play shows in Birmingham and London, but has been inactive since.

Ezra Koenig: Ezra Michael Koenig (born April 8, 1984) is an American musician, singer, songwriter, and radio personality.  He is the lead vocalist and guitarist of the indie rock band Vampire Weekend.

Hold Up (song): "Hold Up" is a song recorded by American singer Beyoncé for her sixth studio album, "Lemonade" (2016).  The song was serviced to rhythmic radios in the United States on August 16, 2016 as the third single from the album.  It was written by Diplo, Ezra Koenig, Beyoncé, Emile Haynie, Josh Tillman, MNEK and Sean "Melo-X" Rhoden.

If I Loved You: Gentlemen Prefer Broadway: If I Loved You: Gentlemen Prefer Broadway — An Evening of Love Duets is a show conceived and directed by American-Canadian singer-songwriter Rufus Wainwright, which premiered on June 14, 2014 during Luminato in Toronto, Ontario, Canada.  The concert featured men singing classic love songs to one another, and included a full orchestra and performances by Wainwright and special guests Boy George, David Byrne, Josh Groban and Steven Page.  Countertenor Brennan Hall, Brent Carver, Glen Hansard, Ezra Koenig and Andrew Rannells also appeared.  The program featured songs written by gay men, including Noël Coward, Lorenz Hart, Jerry Herman and Cole Porter.

Vampire Weekend: Vampire Weekend is an American rock band from New York City, formed in 2006.  They are currently signed to XL Recordings.  The band consists of lead vocalist and guitarist Ezra Koenig, drummer and percussionist Chris Tomson and bassist and backing vocalist Chris Baio.  The band's first album "Vampire Weekend" (2008) – which included the singles "Mansard Roof", "A-Punk", "Oxford Comma", "Cape Cod Kwassa Kwassa" and "The Kids Don't Stand a Chance" – was acclaimed by critics for its world music influences.  Their following album, "Contra" (2010), was similarly acclaimed and garnered strong commercial success.  Their third studio album, "Modern Vampires of the City" (2013), won the group a Grammy Award for Best Alternative Music Album in 2014.

The High Society: The High Society are a glam rock group from Birmingham, United Kingdom formed in 2006 by Matt "Maxi" Browne and Martyn "The Nelsta" Nelson following the breakup of their previous band King Adora.  They have one release to date, the self-titled EP "The High Society", released in 2009.  Following the reunion of King Adora, the group's future is unknown.

Step (Vampire Weekend song): "Step" is a song by American indie rock band Vampire Weekend.  Written and composed by band members Ezra Koenig and Rostam Batmanglij and produced by Ariel Rechtshaid and Batmanglij, the song was released as the fourth and final single from the band's third studio album "Modern Vampires of the City".  The song was inspired by American hip-hop group Souls of Mischief's song "Step to My Girl".

Question: what does King Adora and Ezra Koenig have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first entity."
        },
        "type": {
          "type": "string",
          "description": "The type of the first entity (e.g., music group)."
        },
        "genre": {
          "type": "string",
          "description": "The music genre associated with the first entity."
        }
      },
      "required": [
        "name",
        "type",
        "genre"
      ],
      "additionalProperties": false
    },
    "entity_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second entity."
        },
        "type": {
          "type": "string",
          "description": "The type of the second entity (e.g., musician)."
        },
        "associated_band_genre": {
          "type": "string",
          "description": "The music genre of the band the second entity is associated with."
        }
      },
      "required": [
        "name",
        "type",
        "associated_band_genre"
      ],
      "additionalProperties": false
    },
    "common_attribute_category": {
      "type": "string",
      "description": "The category of the attribute that both entities share."
    },
    "shared_attribute_value": {
      "type": "string",
      "description": "The specific value of the attribute that both entities share."
    }
  },
  "required": [
    "entity_1",
    "entity_2",
    "common_attribute_category",
    "shared_attribute_value"
  ],
  "additionalProperties": false
}
