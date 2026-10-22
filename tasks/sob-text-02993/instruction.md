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
Despoina: In Greek mythology, Despoina, Despoena or Despoine, was the daughter of Demeter and Poseidon and sister of Arion.  She was the goddess of mysteries of Arcadian cults worshipped under the title "Despoina", "the mistress" alongside her mother Demeter, one of the goddesses of the Eleusinian mysteries.  Her real name could not be revealed to anyone except those initiated to her mysteries.  Pausanias spoke of Demeter as having two daughters; Kore being born first, then later Despoina.  With Zeus being the father of Kore, and Poseidon as the father of Despoina.  Pausanias made it clear that Kore is Persephone, though he wouldn't reveal Despoina's proper name.

Miguel Roig-Francolí: Miguel Ángel Roig-Francolí (born 1953) is a Spanish/American composer, music theorist, and pedagogue.  His 1980 "Cinco piezas para orquesta" ("Five Pieces for Orchestra"), commissioned by Radio Nacional de España and written in a postmodern, neotonal style, won first prize in the National Composition Competition of the Spanish "Jeunesses Musicales" in 1981 and second prize at the UNESCO International Rostrum of Composers in 1982, and continues to be widely performed in Spain.  His later compositions often have spiritual themes and are based on sacred texts and the melodies of Gregorian chant.  In 2016 he won the American Prize in Composition (Band/Wind Ensemble Division) for Perseus, for symphonic band.  An expert on Renaissance composers Tomás de Santa María, Antonio de Cabezón, and Tomás Luis de Victoria, he has published numerous scholarly articles and monographs and two textbooks.  Roig-Francolí is a Distinguished Teaching Professor of Music Theory and Composition at the University of Cincinnati – College-Conservatory of Music.

Tim Kurkjian: Timothy Bell "Tom" Kurkjian ( ; born December 10, 1956) is a Major League Baseball analyst on ESPN's "Baseball Tonight" and "SportsCenter".  He is also a contributor to "ESPN The Magazine" and "ESPN.com."  He guests on "Mike and Mike in the Morning" on Thursdays at 7:44 AM, discussing the latest in happenings in Major League Baseball.  He is a frequent contributor to Buster Olney's podcast.  He also appears on The Dan LeBatard Show.

David Hallyday: David Hallyday (born David Michael Benjamin Smet; 14 August 1966) is a French singer, songwriter and amateur sports car racer.  He was born in Boulogne-Billancourt and is the son of the French singers Sylvie Vartan and Johnny Hallyday.  David Hallyday is a first cousin of actor Michael Vartan.

Tim Cantor: Tim Cantor (born August 10, 1969) is an American self-taught surrealism artist and writer.  Tim was raised in Marin County, California and began painting at the age of 5 using a box of oil paints and brushes that were his great-grandfather's.  Tim's great-grandfather was the English Artist, Lloyd Dundas Whiffen (1885-1951).  His first oil painting was created at the age of 5.  When Tim was 15, he won a Bank of America achievement in arts award.  Also at the age of 15, Tim was given his first gallery exhibition where one of his paintings was acquired to hang in the White House.  Tim has since had exhibitions in Athens, Tokyo, Singapore, Paris, Venice, New York, Beverly Hills and San Francisco.  He currently has galleries in both San Diego and Sausalito, California which are dedicated to his vision and his art.  Cantor currently lives and works in Southern California.

Vartan Gregorian: Vartan Gregorian (Armenian: Վարդան Գրիգորեան ; Persian: وارتان گرگوریان‎ ‎ , born April 8, 1934) is an Iranian-born Armenian-American academic, serving as the president of Carnegie Corporation of New York.

Augustine of Canterbury: Augustine of Canterbury (born first third of the 6th century – died probably 26 May 604) was a Catholic Benedictine monk who became the first Archbishop of Canterbury in the year 597.  He is considered the "Apostle to the English" and a founder of the Catholic Church in England.

List of Lab Rats characters: "Lab Rats", also known as "Lab Rats: Bionic Island" for its fourth season, is an American television sitcom that premiered on February 27, 2012, on Disney XD.  It focuses on the life of teenager Leo Dooley, whose mother, Tasha, marries billionaire genius Donald Davenport.  He meets Adam, Bree, and Chase, three bionic superhumans, with whom he develops an immediate friendship.  It should be noted that the names of the Lab Rats imply that they were originally known as subjects A, B, C and D. Adam was born first, then Bree, then Chase, and finally Daniel.

Wale Adebanwi: Professor Wale Adebanwi, (born 1969), is a Nigerian - born first Black African Rhodes Professor at Oxford University

Mihai Frățilă: Mihai Cătălin Frățilă (born December 10, 1970) is a Bishop of the Romanian Church United with Rome, Greek-Catholic.  Born in Alba Iulia, he studied at the Pontifical Gregorian and Urbaniana universities between 1991 and 1996, when he was ordained a priest.  In 2007, he was selected as auxiliary bishop of the Făgăraş and Alba Iulia Archdiocese and titular bishop of "Novae", and the following year he was installed in his headquarters in Bucharest.  In May 2014 Pope Francis erected the Eparchy of Saint Basil the Great of Bucharest with Mihai Frățilă as its first bishop.

Question: Who was born first, Vartan Gregorian or Tim Kurkjian?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_a_name": {
      "type": "string",
      "description": "The name of the first person being compared."
    },
    "person_a_birth_year": {
      "type": "integer",
      "description": "The birth year of the first person."
    },
    "person_b_name": {
      "type": "string",
      "description": "The name of the second person being compared."
    },
    "person_b_birth_year": {
      "type": "integer",
      "description": "The birth year of the second person."
    },
    "first_born_person_name": {
      "type": "string",
      "description": "The name of the person who was born first."
    },
    "first_born_person_birth_year": {
      "type": "integer",
      "description": "The birth year of the person who was born first."
    }
  },
  "required": [
    "person_a_name",
    "person_a_birth_year",
    "person_b_name",
    "person_b_birth_year",
    "first_born_person_name",
    "first_born_person_birth_year"
  ],
  "additionalProperties": false
}
