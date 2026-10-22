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
Wallie Herzer: Wallie Herzer "(né" Walter Henry Herzer; 15 April 1885 San Francisco – 15 October 1961 Redwood City, California) was an American composer of popular music, music publisher, and pianist.  Herzer flourished in music prior to and during World War I.  The Columbia recording of his 1912 composition, "Everybody Two-Step" — performed by ragtime pianist Mike Bernard on December 2, 1912, in New York City — is the first recording of ragtime music.  It became a hit and coincided at the start of a renewed craze for ragtime and dance — fifteen years after William Krell's "Mississippi Rag" had been published, the first known published music with "rag" in the title.  Several other recordings of "Everybody Two-Step" became hits.  Herzer composed three other hits — a 1913 piano rag, "Tickle the Ivories" – which also became hit as a vocal arrangement; a 1914 foxtrot song, "Get Over, Sal"; and a 1916 Hawaiian waltz song, "Aloha Land".  Other compositions — including his 1908 piano ragtime two-step and barn dance, "The Rah-Rah Boy", and his 1913 rag turkey trot, "Let's Dance" — were internationally distributed.

Euday L. Bowman: Euday Louis Bowman (November 9, 1887 – May 26, 1949) was an American pianist and composer of ragtime and blues who represented the style of "Texas Ragtime".  He is chiefly remembered as the composer of the successful "Twelfth Street Rag", a rag from 1914 out of a series of ragtimes that Bowman wrote during or after a period in which he worked as a pianist in some of the better bordellos of Kansas City.  These tunes -- "Sixth Street Rag", "Tenth Street Rag", "Eleventh Street Rag" and "Twelfth Street Rag"—were named after streets of "Boss" Tom Pendergast's redlight district.

Classic rag: Classic rag (short for classical ragtime) is the style of ragtime composition pioneered by Scott Joplin and the Missouri school of ragtime composers.  These compositions were first considered "classic" by Joplin's publisher, John Stark, as a way to distinguish them from what he considered the "common" rags of other publishers.  Today, any composition fitting this particular ragtime structural form is considered classic rag.

Ragtime: Ragtime – also spelled rag-time or rag time – is a musical style that enjoyed its peak popularity between 1895 and 1918.  Its cardinal trait is its syncopated, or "ragged", rhythm.  The style has its origins in African-American communities in cities such as St. Louis.  Ernest Hogan (1865–1909) was a pioneer of ragtime and was the first composer to have his ragtime pieces (or "rags") published as sheet music, beginning with the song "LA Pas Ma LA," published in 1895.  Hogan has also been credited for coining the term "ragtime".  The term is actually derived from his hometown "Shake Rag" in Bowling Green, Kentucky.  Ben Harney, another Kentucky native, has often been credited for introducing the music to the mainstream public.  His first ragtime composition, "You've Been a Good Old Wagon But You Done Broke", helped popularize the style.  The composition was published in 1895, a few months after Ernest Hogan's "LA Pas Ma LA." Ragtime was also a modification of the march style popularized by John Philip Sousa, with additional polyrhythms coming from African music.  Ragtime composer Scott Joplin ("ca."  1868–1917) became famous through the publication of the "Maple Leaf Rag" (1899) and a string of ragtime hits such as "The Entertainer" (1902), although he was later forgotten by all but a small, dedicated community of ragtime aficionados until the major ragtime revival in the early 1970s.  For at least 12 years after its publication, "Maple Leaf Rag" heavily influenced subsequent ragtime composers with its melody lines, harmonic progressions or metric patterns.

Frog Legs Rag: "Frog Legs Rag" is a classic rag composed by James Scott and published by John Stillwell Stark in December 1906.  It was James Scott's first commercial success.  Prior to this composition Scott had published marches.  With "Frog Legs Rag", Scott embarked upon a career as a successful and important ragtime songwriter.

Scott Joplin: Scott Joplin ( ; 1867/68 or November 24, 1868– April 1, 1917) was an African-American composer and pianist.  Joplin achieved fame for his ragtime compositions and was dubbed the "King of Ragtime".  During his brief career, he wrote 44 original ragtime pieces, one ragtime ballet, and two operas.  One of his first, and most popular pieces, the "Maple Leaf Rag", became ragtime's first and most influential hit, and has been recognized as the rag.

Magnetic Rag: "Magnetic Rag" is a 1914 ragtime piano composition by American composer Scott Joplin.  It is significant for being the last rag which Joplin published in his lifetime, three years before his death in 1917.  It is also unique in form and in some of the musical techniques employed in the composition.

Searchlight Rag: Searchlight Rag is a ragtime composition by Scott Joplin, first published in 1907.  It was named after the town of Searchlight, Nevada, where his friends had gone prospecting, inspiring the title.

William Krell: William Henry Krell (1868–1933) composed what is regarded as the first rag or ragtime composition in 1897 called Mississippi Rag, published in New York by S. Brainard's Sons and copyrighted on January 27, 1897.  The sheet music stated that it was the first rag-time two step ever written and was first played by Krell's Orchestra in Chicago although the structure is in the form of a patrol march.  The cover shows a group of all ages dancing to a banjo player before onlookers sitting on a pile of stacked cotton bales on a dock on the Mississippi River.  Krell also composed the rag Shake Yo' Dusters!  or Piccaninny Rag in 1898.  The popularity of "Mississippi Rag" resulted in the emergence of the genre known as ragtime.

Rag pudding: Rag pudding (also known as Rag pie) is a savoury dish consisting of minced meat and onions wrapped in a suet pastry, which is then cooked in a cheesecloth.  The dish was invented during the 19th century in Oldham, a former mill town in Lancashire, previously at the centre of England's cotton industry.  Rag pudding pre-dates ceramic basins and plastic boiling bags in cookery, and so the cotton or muslin rag cloths common in Oldham were used in the dish's preparation.  Rag pudding is similar in composition and preparation to steak and kidney pudding, and may be purchased from traditional local butcher's shops in South East Lancashire.

Question: Searchlight Rag is a composition by a composer dubbed as the King of what ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "composition_title": {
      "type": "string",
      "description": "The title of the musical composition."
    },
    "composer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the composer."
        },
        "dubbed_as": {
          "type": "string",
          "description": "The title or nickname the composer was known by."
        },
        "associated_genre": {
          "type": "string",
          "description": "The primary musical genre the composer is associated with."
        }
      },
      "required": [
        "name",
        "dubbed_as",
        "associated_genre"
      ],
      "additionalProperties": false
    },
    "composition_publication_year": {
      "type": "integer",
      "description": "The year the composition was first published."
    }
  },
  "required": [
    "composition_title",
    "composer",
    "composition_publication_year"
  ],
  "additionalProperties": false
}
