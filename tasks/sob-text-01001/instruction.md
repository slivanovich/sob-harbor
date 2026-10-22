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
The Offspring: The Offspring is an American rock band from Garden Grove, California, formed in 1984.  Originally formed under the name Manic Subsidal, the band has consisted of lead vocalist and rhythm guitarist Dexter Holland, bassist Greg K., lead guitarist Kevin "Noodles" Wasserman and drummer Pete Parada since 2007.  While Holland, Greg K., and Noodles have been constant members since the band was formed, the Offspring has gone through a number of drummers.  Their longest-serving drummer was Ron Welty, who had been a member of The Offspring for 16 years; he was replaced by Atom Willard in 2003, and then four years later by Parada.  The band is often credited—alongside fellow California punk bands Green Day, Bad Religion, NOFX, Pennywise and Rancid—for reviving mainstream interest in punk rock in the 1990s.  They have sold over 40 million records worldwide, being considered one of the best-selling punk rock bands of all time.

Laïko: Laïkó (Greek: λαϊκό τραγούδι , ] , "song of the people"; "popular song", pl: "laïká" ["tragoudia"]), is a Greek music genre composed in Greek language in accordance with the tradition of the Greek people.  Also called "folk song" or "urban folk music" (Gr: αστική λαϊκή μουσική or λαϊκά τραγούδια "laïká tragoudia"), in its plural form is a Greek music genre which has taken many forms over the years.  Laïkó followed after the commercialization of rebetiko music.  It was strong dominated by Greek folk music and is used to describe the whole of the Greek popular music.  When used in context it refers mostly to the form it took in the period from the 1950s to the 1980s.

Ska: Ska ( ; Jamaican: [skjæ] ) is a music genre that originated in Jamaica in the late 1950s and was the precursor to rocksteady and reggae.  Ska combined elements of Caribbean mento and calypso with American jazz and rhythm and blues.  It is characterized by a walking bass line accented with rhythms on the off-beat.  Ska developed in Jamaica in the 1960s when Prince Buster, Clement "Coxsone" Dodd, and Duke Reid formed sound systems to play American rhythm and blues and then began recording their own songs.  Some suggest ska dates to earlier times, however.  In the early 1960s, ska was the dominant music genre of Jamaica and was popular with British mods.  Later it became popular with many skinheads.

Chalga: Chalga is a Bulgarian music genre, often referred to as pop-folk, short for "popular folk".  Chalga or pop-folk is essentially a folk-inspired dance music genre, with a blend of Bulgarian music (Bulgarian ethno-pop genre) and also primary influences from Greek, Turkish, Arabic, Romani, Albanian and Russian music.

Afro-soul: Afro-soul is a music genre that is a fusion between soul music and African sound.  Its distinctive feature from any other African Music genre is the emotional vocals, especially of the lead singer.

Songwriter: A songwriter is a professional who is paid to write lyrics and melodies for songs, typically for a popular music genre such as rock or country music.  A songwriter can also be called a composer, although the latter term tends to be used mainly for individuals from the classical music genre.  The pressure from the music industry to produce popular hits means that songwriting is often an activity for which the tasks are distributed between a number of people.  For example, a songwriter who excels at writing lyrics might be paired with a songwriter with the task of creating original melodies.  Pop songs may be written by group members from the band or by staff writers – songwriters directly employed by music publishers.  Some songwriters serve as their own music publishers, while others have outside publishers.

Fantezi: Fantezi, is a Turkish music genre composed in Turkish language in accordance with the tradition of the Turkish people.  Also called folk song or urban folk music , in its plural form is a Turkish music genre which has taken many forms over the years.  Fantezi followed after the commercialization of Turkish classical music and Kanto music.  It was strong dominated by Turkish folk music.  When used in context it refers mostly to the form it took in the period from the 1920s to the 1980s. It is a vocal works emerged in 20th century, in free style, and usually having several part, each part composed in different tempo or method.

Let's Active: Let's Active is an American rock group formed in Winston-Salem, North Carolina in 1981, and often identified with the jangle pop guitar work of the group's frontman and songwriter Mitch Easter.  After disbanding in 1990, the group reformed in August 2014 to play a benefit show in North Carolina.

SchlagerTV: SchlagerTV is a Schlager music television channel aimed at the European and North-American markets which launched in January, 2009.  The programming consists mainly of music videos and music programs in the German language.  The main music genre is the popular Schlager music genre from Germany and Austria.  The channel is founded by Jur Bron and Gerard Ardesch and officially owned by their company TV Digitaal BV.  In December 2011, the Brava TV Group announced that Strengholt BV became co-owner of SchlagerTV, though sister channel TV Oranje remains solely owned by TV Digitaal BV.  Since 12 May 2016 it is part of MuziekKiosk.

Kadongo Kamu: Kadongo Kamu is a music genre native to Uganda and is the oldest mainstream music genre in the country.  The word "kadongo kamu" is a term in the Ganda language that means "one little guitar".  To understand why the genre has this name, one has to understand the stylistic structure of the music which is created with only one acoustic guitar, a dry acoustic non-electric six-string guitar.  But this is not always the case and many times other instruments are involved.  However the true style of the music relies only on one acoustic guitar as instrumentation, hence the "one little guitar" name.

Question: The Offspring and Let's Active, are of which music genre?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "genre_name": {
      "type": "string",
      "description": "The common music genre shared by the listed bands."
    },
    "bands_info": {
      "type": "array",
      "description": "Information about each band that belongs to the specified genre.",
      "items": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string",
            "description": "The name of the band."
          },
          "origin_country": {
            "type": "string",
            "description": "The country where the band was formed."
          },
          "formation_year": {
            "type": "integer",
            "description": "The year the band was formed."
          }
        },
        "required": [
          "band_name",
          "origin_country",
          "formation_year"
        ],
        "additionalProperties": false
      }
    },
    "number_of_bands_in_genre": {
      "type": "integer",
      "description": "The total number of bands identified as belonging to this genre."
    }
  },
  "required": [
    "genre_name",
    "bands_info",
    "number_of_bands_in_genre"
  ],
  "additionalProperties": false
}
