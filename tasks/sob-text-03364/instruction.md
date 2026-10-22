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
Vanessa Low: Vanessa Low (born 17 July 1990) is a German-born Australian Paralympic athlete competing in T42 sprint and long jump events. .  Born in Germany, she earns the Australian nationality in June 2017.

Tim Howar: Tim Howar (born 24 November 1969 in Spirit River, Alberta) is a Canadian actor, singer and dancer, known as a London-based rock vocalist with Mike + The Mechanics.

Notorious (The Saturdays song): "Notorious" is a song by British-Irish girl group The Saturdays, released as the lead single from the third studio album, "On Your Radar".  The song was written by Ina Wroldsen and Steve Mac, who also produced the song.  The single was released digitally on 22 May 2011.  "Notorious" was recorded in 2011 after the band were looking for a new sound to release in their third album.  According to the lyrics in the song the band are loving life, they like to go out and enjoy themselves however they work hard and they all have a bad and naughty side to them.  The lyrics of the song has been described as "playful".  Vanessa White said the song was a more "grown up" approach to the music they have released before.  The group performed the song live for the first time on "So You Think You Can Dance" and the song received its first radio airplay on "The Chris Moyles Show".

Twist (band): Twist were a rock band from Birmingham, England, consisting of Emma Fox (vocals/guitar), Vanessa White (guitar), Kelly Southern (Bass) and Leanne Taylor (drums).  They released their debut record, "Magenta" on the Fierce Panda record label in February 2000, and played support slots for Muse and Coldplay.  The band broke up in 2002.

The Saturdays discography: English-Irish girl group The Saturdays have released five studio albums, one compilation album, two extended plays and eighteen singles.  The Saturdays were formed in 2007, with a number of different auditions through their management: Frankie Sandford, Rochelle Wiseman, Una Healy, Mollie King and Vanessa White were the successful auditionees and were granted a place within the band.

Ester Dean: Esther Renay Dean (born April 15, 1982), known professionally as Ester Dean, is an American singer, songwriter, record producer, and actress.  Her 2009 single "Drop It Low" featured singer Chris Brown.  Dean has also co-written songs for many artists including Christina Aguilera, Florence + The Machine, Katy Perry, Beyoncé, Nicole Scherzinger, Priyanka Chopra, Mary J. Blige, Nicki Minaj, Kelly Clarkson, Ciara, The Pussycat Dolls, Usher, Kelly Rowland, Girlicious, Keri Hilson, Rihanna, R. Kelly, Britney Spears, Melody Thornton, Vanessa White, Kevin McHale, Selena Gomez, G.R.L., Soulja Boy Tell 'Em, Little Mix, Pia Toscano, Tinie Tempah, Lil Wayne, Machine Gun Kelly, Fifth Harmony, and Eurovision Song Contest 2012 winner Loreen.

Bidu Sayão International Vocal Competition: The Bidu Sayão International Vocal Competition (Portuguese: Concurso Internacional de Canto Bidu Sayão) is a singing competition held at the city of Belo Horizonte in Brazil named after that country's most famous opera singer, Bidu Sayão.  It is a competition open to singers of any nationality for up-and-coming young singers and as such has an age restriction.  The competition is divided between male and female participants and is the most important vocal competition in Latin America.

Vanessa White: Vanessa Karen White (born 30 October 1989) is an English singer-songwriter, dancer and actress.  She rose to fame in 2008 as a member of British-Irish girl group The Saturdays, signed to Fascination and Polydor Records.  The group have achieved substantial success with numerous top-ten hits as well as a number one single.  She is the youngest member of the group.

The Slutcracker: The Slutcracker is a burlesque, satirical version of The Nutcracker that is the creation of Babes in Boinkland troupe director Vanessa White.  It has been performed in Somerville, Massachusetts, and Montreal, Canada.  The performance incorporates burlesque and tango dancers, drag kings, hoopers, ballerinas, acrobats, and belly dancers in a retelling of Pyotr Ilyich Tchaikovsky's ballet from the point of view of a young woman who experiences a sexual awakening during a holiday dream-like sequence.

The Saturdays: The Saturdays was a British-Irish girl group based in London, England.  The group formed during the summer of 2007.  The line up consisted of Frankie Bridge, Una Healy, Rochelle Humes, Mollie King and Vanessa White.  They were formed through Fascination Records, who gave them an instant record deal with the label as well as a sub-division of Polydor Records.  As soon as the contract was finalised The Saturdays went on tour with Girls Aloud during their Tangled Up Tour.  The group's music style is pop, however throughout their career their management have experimented with dance-pop and electropop.  To create this music, Ina Wroldsen, Steve Mac and Quiz & Larossi have been heavily involved.

Question: Do singers Vanessa White and Tim Howar have the same nationality?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1_name": {
      "type": "string",
      "description": "The name of the first person."
    },
    "person_1_nationality": {
      "type": "string",
      "description": "The nationality of the first person."
    },
    "person_2_name": {
      "type": "string",
      "description": "The name of the second person."
    },
    "person_2_nationality": {
      "type": "string",
      "description": "The nationality of the second person."
    },
    "same_nationality": {
      "type": "boolean",
      "description": "True if both persons have the same nationality, false otherwise."
    }
  },
  "required": [
    "person_1_name",
    "person_1_nationality",
    "person_2_name",
    "person_2_nationality",
    "same_nationality"
  ],
  "additionalProperties": false
}
