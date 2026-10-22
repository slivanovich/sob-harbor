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
Kav Sandhu: KAV (Kav Sandhu) is a British musician from Leicester UK, based in Los Angeles.  KAV played guitar with British band Happy Mondays for 4 years after helping reform the band with frontman Shaun Ryder in 2004.  He launched his solo project under moniker "KAV" in 2008 with long-time friend and drummer Jim (James) Portas.  His solo material has been compared by the media to everyone from Iggy & The Stooges, Black Rebel Motorcycle Club, Primal Scream, Kasabian, The Rolling Stones & Bob Dylan.  He plays live with a full live band, which sometimes features guest musicians from various bands.

Keen's myotis: Keen's myotis ("Myotis keenii") is a species of vesper bat.  It is found in British Columbia in Canada and in Washington and Alaska in the United States.  It is named after the Rev. John Henry Keen, who collected the specimen that formed the basis for the first scientific description of the species.  Classification for Keen's myotis formerly included the Northern long-eared Myotis ("Myotis septentrionalis"), resulting in older studies confusing the species for one another.

Shaun Ryder: Shaun William George Ryder (born 23 August 1962) is an English musician and singer-songwriter.  He is best known as the lead singer of the Happy Mondays and Black Grape.  He was the runner-up of the tenth series of "I'm a Celebrity...Get Me Out of Here! ".

Amateur Night in the Big Top: Amateur Night in the Big Top is the first official solo album by Shaun Ryder, of Happy Mondays and Black Grape.  The album is subtitled "Clowns and Pet Sounds".  It was released in September, 2003 and co-produced by Pete Carroll, Shane Norton and Cabaret Voltaire's Stephen Mallinder.  It was recorded in Perth, Australia and released on the Offworld Sounds record label run by Ryder's cousin Pete Carroll and Mallinder.

All the Aces: All The Aces is a compilation album by the band Motörhead, released in 1993.  It includes 14 of their most popular songs, 2 enhanced multimedia sections and 8 previously unreleased live songs by The Muggers (a band formed by "Fast" Eddie Clarke and Phil "Philthy Animal" Taylor of Motörhead with John "Speedy" Keen and Billy Rath).

Dare (song): "Dare" (styled as "挑戦 (DARE)") is a song by British virtual band Gorillaz, taken as the second single from their second studio album, "Demon Days".  The track is sung by Rosie Wilson (also known as Roses Gabor) with backing vocals from Damon Albarn and features vocals by Happy Mondays frontman Shaun Ryder.  It peaked at No. 1 in the UK Singles Chart in September 2005, becoming the band's only UK No. 1.  In 2016, vocals of the song were interpolated in Friction's song "Dare (Hold It Down)".  In 2017 the song was featured in an episode of the British soap-opera ￼￼EastEnders.

Speedy Keen: John David Percy "Speedy" Keen (29 March 1945 – 12 March 2002), was a songwriter, vocalist, drummer and keyboard player, best known for his association with the rock band Thunderclap Newman.  He wrote "Something in the Air" (1969) for the band, which reached No. 1 in the UK Singles Chart and released two solo albums.

Demon Days: Demon Days is the second studio album by British virtual band Gorillaz, released on 11 May 2005 in Japan and on 23 May internationally by Parlophone Records and in the United States by Virgin Records.  The album features contributions from De La Soul, Neneh Cherry, Martina Topley-Bird, Roots Manuva, MF DOOM, Ike Turner, Bootie Brown of the Pharcyde, Shaun Ryder, Dennis Hopper, the London Community Gospel Choir, and a children's choir.  Frontman Damon Albarn brought in Danger Mouse as producer.

Happy Mondays: Happy Mondays are an English alternative rock band from Salford, Greater Manchester.  Formed in 1980, the band's original line-up was Shaun Ryder (vocals), his brother Paul Ryder (bass), Mark Day (guitar), Paul Davis (keyboard), and Gary Whelan (drums).  Mark "Bez" Berry later joined the band onstage as a dancer/percussionist.  Rowetta joined the band as a guest vocalist in 1990.

Something in the Air: "Something in the Air" is a song recorded by Thunderclap Newman, written by Speedy Keen who also sang the song.  It was a number 1 single for three weeks in the UK Singles Chart in July 1969.  The song has been used for films, television and adverts, and has been covered by several artists.  The track was also included on Thunderclap Newman's only album release "Hollywood Dream" over a year later.

Question: Who is older, Speedy Keen or Shaun Ryder?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1_name": {
      "type": "string",
      "description": "The name of the first person being compared."
    },
    "person_1_birth_year": {
      "type": "integer",
      "description": "The birth year of the first person."
    },
    "person_2_name": {
      "type": "string",
      "description": "The name of the second person being compared."
    },
    "person_2_birth_year": {
      "type": "integer",
      "description": "The birth year of the second person."
    },
    "older_person_name": {
      "type": "string",
      "description": "The name of the person who is older."
    },
    "age_difference_years": {
      "type": "integer",
      "description": "The difference in birth years between the two people."
    },
    "comparison_statement": {
      "type": "string",
      "description": "A statement summarizing the age comparison."
    }
  },
  "required": [
    "person_1_name",
    "person_1_birth_year",
    "person_2_name",
    "person_2_birth_year",
    "older_person_name",
    "age_difference_years",
    "comparison_statement"
  ],
  "additionalProperties": false
}
