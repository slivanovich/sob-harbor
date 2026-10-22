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
Dot (song): "Dot" is a song by the American punk rock band All, written by singer Scott Reynolds and released as a single and music video from the band's 1992 album "Percolater".  The single also includes the song "Can't Say", written by bassist Karl Alvarez and drummer Bill Stevenson, and a cover version of "A Boy Named Sue", a 1969 song written by Shel Silverstein and made famous by Johnny Cash.

Greatest Hits, Vol. 2 (Johnny Cash album): Greatest Hits, Vol.  2 is, as the title implies, a greatest hits compilation by country singer Johnny Cash, released on Columbia Records in 1971 (see 1971 in music).  It combines older songs from Cash's years with Sun Records ("Hey Porter" and "Folsom Prison Blues", among others) with more recent hits, such as "A Boy Named Sue" from Cash's "At San Quentin" album and the Kris Kristofferson-penned "Sunday Mornin' Comin' Down". " Big River", one of the songs from the Sun years, was released as a single.  The album was certified Gold on 1/25/1977 and Platinum on 2/16/1995 by the R.I.A.A.

A Boy Named Sue: "A Boy Named Sue" is a song written by Shel Silverstein, made popular by Johnny Cash.  He recorded the song live at California's San Quentin State Prison at a concert on February 24, 1969.  Cash also performed the song (with comical variations on the original performance) in December 1969 at Madison Square Garden.  The song became Cash's biggest hit on the "Billboard" Hot 100 chart and his only top ten single there, spending three weeks at No. 2 in 1969, held out of the top spot by "Honky Tonk Women" by The Rolling Stones.  The track also topped the Billboard Hot Country Songs and Hot Adult Contemporary Tracks charts that same year and was certified Gold on August 14, 1969, by the RIAA.

Twerp: Twerp is a 2013 children's book by Mark M. Goldblatt about a little boy named Julian who is friends with a boy named Lonnie.  This book is to help people remember "what makes a good friend".

Being Eve: Being Eve is a television series from New Zealand, originally shown on TV3 from 2001–2002, and rebroadcast on The N.  "Being Eve" focuses on a teenage girl, Eve Baxter, and her daily problems.  Her parents are divorced but live next door to each other.  Eve was in love with a boy named Adam.  They broke up at the beginning of the second season, and she ends up with another boy named Sam Hooper, with whom she had her first kiss when they were kids.

My Father and the Man in Black: My Father and the Man in Black is a 2012 Canadian documentary film directed and produced by Jonathan Holiff about the stormy relationship between country music star Johnny Cash and the filmmaker's father, Saul Holiff, Cash's personal manager.  It qualified for Oscar consideration in 2013.  Holiff was inspired to produce the film when he stumbled on his father's storage locker filled with audio diaries and a large assortment of other documents relating to his time in the 1960s and 1970s as Cash's manager.  The locker also included a framed gold record of "A Boy Named Sue" which went on display at the Grand Theatre during the running of their musical "Ring of Fire".

Burden of Dreams: Burden of Dreams is a 1982 "making-of" documentary film directed by Les Blank, shot during and about the chaotic production of Werner Herzog's 1982 film "Fitzcarraldo", and filmed on location in the jungles of South America.

A Boy Named Sue (film): A Boy Named Sue is a 2001 documentary film directed by Julie Wyman.  It shows the life and transition of Theo, a young adult, raised female, involved in a lesbian relationship, who undergoes various stages of a sex reassignment surgery (including a mastectomy and hormone therapy) to become male.  The protagonist is filmed extensively throughout, gives a number of interviews, and eventually settles down as a gay male.  The film's title is taken from the song "A Boy Named Sue".

Sue K. Hicks: Sue Kerr Hicks (December 12, 1895 – June 17, 1980) was an American jurist who practiced law and served as a circuit court judge in the state of Tennessee.  He is best known for his role as a co-instigator and prosecutor in the 1925 trial of John T. Scopes, a Dayton, Tennessee teacher accused of teaching the Theory of Evolution in violation of Tennessee state law.  Hicks may have also been the inspiration for the Shel Silverstein song "A Boy Named Sue," which was popularized by country music performer Johnny Cash in 1969.

McClean Lake mine: The McClean Lake mine is a uranium mine and milling operation located west of Wollaston Lake, about 700 kilometres north of Saskatoon, in the Athabasca Basin region of Saskatchewan, Canada.  The McClean ore body was discovered in 1979, followed by the discovery of the JEB ore body in 1982.  From 1985 to 1990, a cluster of deposits named Sue A, Sue B and Sue C were discovered.

Question: Are both the 1982 film "Burden of Dreams" and the 2001 film "A Boy Named Sue" considered documentaries?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_topic": {
      "type": "string",
      "description": "The main topic of the question."
    },
    "film_comparison": {
      "type": "object",
      "properties": {
        "film_1": {
          "type": "object",
          "properties": {
            "title": {
              "type": "string",
              "description": "Title of the first film."
            },
            "year": {
              "type": "integer",
              "description": "Release year of the first film."
            },
            "is_documentary": {
              "type": "boolean",
              "description": "Whether the first film is a documentary."
            }
          },
          "required": [
            "title",
            "year",
            "is_documentary"
          ],
          "additionalProperties": false
        },
        "film_2": {
          "type": "object",
          "properties": {
            "title": {
              "type": "string",
              "description": "Title of the second film."
            },
            "year": {
              "type": "integer",
              "description": "Release year of the second film."
            },
            "is_documentary": {
              "type": "boolean",
              "description": "Whether the second film is a documentary."
            }
          },
          "required": [
            "title",
            "year",
            "is_documentary"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "film_1",
        "film_2"
      ],
      "additionalProperties": false
    },
    "both_are_documentaries": {
      "type": "boolean",
      "description": "True if both films are considered documentaries, false otherwise."
    }
  },
  "required": [
    "question_topic",
    "film_comparison",
    "both_are_documentaries"
  ],
  "additionalProperties": false
}
