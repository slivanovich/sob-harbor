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
Flaming Pie: Flaming Pie is the tenth solo studio album by Paul McCartney under his own name, first released in 1997.  His first studio album in over four years, it was mostly recorded following McCartney's involvement in the highly successful "Beatles Anthology" project.  The album was recorded in several locations over two years, 1995 and 1997, featuring two songs dating from 1992.  The album featured several of McCartney's family members and friends, most notably McCartney's son, James McCartney.  In "Flaming Pie"'s liner notes, McCartney said: ""[The Beatles Anthology]" reminded me of The Beatles' standards and the standards that we reached with the songs.  So in a way it was a refresher course that set the framework for this album."

Me (James McCartney album): Me is the first full length studio album by James McCartney, son of Paul and Linda McCartney.  It was recorded between Abbey Road, Hog Mill, Select, Avatar and Nevo studios and was produced and mixed by David Kahne.  It also includes performances from Paul McCartney.  James McCartney said of the album "it's about having as much emotion as possible for me, musically and lyrically.  Cathartic, heartfelt and true."

Linda McCartney: Linda Louise McCartney, Lady McCartney (née Eastman; formerly See; September 24, 1941 – April 17, 1998) was an American musician, photographer, animal rights activist, entrepreneur and publisher who was married to Paul McCartney of the Beatles.  Prior to marrying Paul, she was a professional photographer of celebrities and contemporary musicians, with her work published in music industry magazines.  Her photos were also published in the book "Linda McCartney's Sixties: Portrait of an Era", in 1992.

The Linda McCartney Story: The Linda McCartney Story is a 2000 American drama television film directed by Armand Mastroianni, starring Elizabeth Mitchell and Gary Bakewell.  Based on the book "Linda McCartney: The Biography", presenting the life story of Linda McCartney and her life with Paul McCartney.  The film was shot in Vancouver, British Columbia, Canada for CBS and was released in 2000.

James McCartney: James Louis McCartney (born 12 September 1977) is a British musician and songwriter living in London.  He is the only son of songwriter and former Beatle Paul McCartney and Linda McCartney.  He has contributed to a number of solo albums by his parents, including "Flaming Pie" (1997) and "Driving Rain" (2001) by Paul McCartney and "Wide Prairie" (1998) by Linda McCartney.

Concert for Linda: The Concert for Linda was a benefit tribute to Linda McCartney, wife of Paul McCartney.  It was held at the Royal Albert Hall in London on 10 April 1999.  Linda McCartney died after a long battle with cancer nearly a year earlier, when she was 56.  They were married for 29 years.

Give My Regards to Broad Street (film): Give My Regards to Broad Street is a 1984 British musical drama film directed by Peter Webb, which starred Paul McCartney, Bryan Brown and Ringo Starr.  The film covers a fictional day in the life of Paul McCartney, who wrote the film for the screen, and McCartney, Starr and Linda McCartney all appeared as themselves.  Despite "Give My Regards to Broad Street" being unsuccessful in the box office financially and critically, its soundtrack album sold well.  The title is a take on George M. Cohan's classic show tune "Give My Regards to Broadway" which made reference to London's Broad Street railway station, which would close in 1986.

Lee Eastman: Lee Eastman, born Leopold Vail Epstein (12 January 1910 – 30 July 1991) was a New York City show business attorney, and art collector the son of Louis (b. Russia ~1887, imm.  1906) and Stella (Freyer) Epstein.  His sisters were Emmaline and Rose.  He married Louise Lindner, daughter of a prominent Cleveland department store executive; they had four children, including John Eastman and Linda McCartney, the late wife of former Beatle Paul McCartney.  Eastman became McCartney's business manager shortly before the breakup of The Beatles while his son John represented McCartney during his 1970 lawsuit to legally dissolve the Beatles.  He is the maternal grandfather of potter Heather McCartney, photographer Mary McCartney, fashion designer Stella McCartney, and musician/sculptor James Louis McCartney.  Eastman was also the friend and longtime lawyer for and collector of the works of the Abstract expressionist painter Willem de Kooning.

Close At Hand: Close At Hand is the second EP by James McCartney, son of Paul and Linda McCartney.  The EP was produced by David Kahne and Paul McCartney, and released on 30   2011 (2011--) .

Wide Prairie: Wide Prairie is a posthumous compilation by Linda McCartney.  The album is composed of songs recorded between 1972 and 1998, some of which were previously released while others are unreleased Wings era recordings.  The idea for the album was inspired by a fan who wrote in inquiring about "Seaside Woman", a reggae song which Wings had recorded in 1972 under the name Suzy and the Red Stripes featuring Linda on lead vocals.  Lead guitar on the song "The Light Comes from Within" is played by the McCartneys' son, musician/sculptor James McCartney.  The album reached number 127 in the UK charts, while the title track made the top 75, at number 74.  "The Light Comes from Within" also charted, at number 56 in the UK charts.

Question: Close At Hand is the second EP by James McCartney, son of Paul and Linda McCartney, a British musician and songwriter living in London, born on which date?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person."
    },
    "birth_date": {
      "type": "string",
      "description": "The birth date of the person in 'Day Month Year' format."
    },
    "birth_year": {
      "type": "integer",
      "description": "The birth year of the person."
    },
    "current_residence": {
      "type": "string",
      "description": "The city where the person is currently living."
    },
    "parental_relationship": {
      "type": "object",
      "properties": {
        "father_name": {
          "type": "string"
        },
        "mother_name": {
          "type": "string"
        }
      },
      "required": [
        "father_name",
        "mother_name"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "birth_date",
    "birth_year",
    "current_residence",
    "parental_relationship"
  ],
  "additionalProperties": false
}
