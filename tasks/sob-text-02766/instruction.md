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
Wired All Wrong: Wired All Wrong is a nu metal band formed by musician/producers Matt Mahaffey of Self and Jeff Turzo previously of God Lives Underwater.  The two have been longtime friends since a mix-up of their bands on MTV.  Partly due to the unfortunate deaths of David Reilly from GLU and Mike Mahaffey from Self, Matt and Jeff were able to shift their attention away from their other bands.  Their debut album, "Break out the Battle Tapes", came out on September 12, 2006.

Pavement (band): Pavement was an American indie rock band that formed in Stockton, California in 1989.  The group mainly consisted of Stephen Malkmus (vocals and guitar), Scott Kannberg (guitar and vocals), Mark Ibold (bass), Steve West (drums) and Bob Nastanovich (percussion and vocals).  Initially conceived as a recording project, the band at first avoided press or live performances, while attracting considerable underground attention with their early releases.  Gradually evolving into a more polished band, Pavement recorded five full-length albums and nine EPs over the course of their decade-long career, though they disbanded with some acrimony in 1999 as the members moved on to other projects.  In 2010, they undertook a well-received reunion tour.

Scott Garrett (musician): Scott Garrett (March 16, 1966, Washington, D.C.) is an American drummer.  He is known as the drummer for Wired All Wrong and Coloursound, and has been support drummer for J since 1997.  He was also temporary drummer at the last few shows of God Lives Underwater.  Bands Garrett played with include Neverland, Pop's Cool Love, The Cult, The Mission UK and Dag Nasty.

Hypersonic Hyperphonic: Hypersonic Hyperphonic is the second studio album by Tinfed, released on December 3, 1996 by Re-Constriction Records.  "Sonic Boom" noted that "Tinfed is one of those bands who would fit perfectly on tour with the likes of God Lives Underwater, Stabbing Westward, Filter & Gravity Kills which means they should do rather well with the current crossover audience."

No More Love: "No More Love" is a song by the band God Lives Underwater.  It was originally released on their self-titled EP album "God Lives Underwater" in 1995, resulting in significant airplay.  The song was featured in the 1995 movie Johnny Mnemonic (film).

God Lives Underwater: God Lives Underwater was an industrial rock band from rural Perkiomenville, Pennsylvania (near Philadelphia), formed in 1993 by band members David Reilly and Jeff Turzo.  God Lives Underwater was originally signed to American Recordings after being discovered by Rick Rubin, who subsequently produced the band's first two albums.  Prior to the band's breakup, there were two other members, Andrew McGee and Adam Kary.

God Lives Underwater (EP): God Lives Underwater was the first EP released by God Lives Underwater in 1995 but recorded in 1993. " No More Love" was also released on the band's second album "Empty".  The song "Drag Me Down" was featured in the movie "The Doom Generation" and the song "No More Love" was featured in the movie "Johnny Mnemonic".

List of KMFDM concert tours: KMFDM is an industrial music act, founded in 1984 by Sascha Konietzko in Hamburg, Germany.  Since then, KMFDM has performed in North America, Europe, Asia, and Australia.  KMFDM's earliest performances were as a local act in Hamburg.  Their first major tour was in support of Ministry in 1990.  Since then, KMFDM has headlined all of their tours, with support from bands such as Sister Machine Gun, Die Warzau, Chemlab, God Lives Underwater, DJ?  Acucrack, and Army of the Universe.

List of God Lives Underwater concerts: The following is a list of God Lives Underwater concerts.  They began touring in 1995, before the release of their first studio album, "Empty".  The Life in the So-Called Space Age Tour began February 19, 1998.  The tour ended late in the year it started.  God Lives Underwater performed for the last time at Hollywood, California on July 13, 2000.  Lead singer David Reilly began touring solo in late 2001.  On September 28, 2004, God Lives Underwater released "Up off the Floor", but did not have a supporting tour.  Wired All Wrong, a project by band members after God Lives Underwater break-up, began touring October 6, 2006.

Sean Beavan: Sean Beavan is a musician, record producer, and audio engineer best known for his work with Nine Inch Nails, Marilyn Manson, Guns N' Roses, God Lives Underwater, and Slayer.  His production style is typically heavy, with heavily saturated guitars, but his work is diverse and wide ranging as exemplified by bands like No Doubt to System of a Down, to indie bands like Thrice, and 8mm.

Question: What type of music do both God Lives Underwater and Pavement bands perform?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Names of the bands being compared."
    },
    "common_music_type": {
      "type": "string",
      "description": "The music type that both bands perform."
    },
    "individual_band_details": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string",
            "description": "The name of the band."
          },
          "genre": {
            "type": "string",
            "description": "The specific genre of the band."
          }
        },
        "required": [
          "band_name",
          "genre"
        ],
        "additionalProperties": false
      },
      "description": "Details about each band's specific genre."
    }
  },
  "required": [
    "band_names",
    "common_music_type",
    "individual_band_details"
  ],
  "additionalProperties": false
}
