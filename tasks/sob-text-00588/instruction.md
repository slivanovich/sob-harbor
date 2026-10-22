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
George King (botanist): Sir George King, KCIE FRS (12 April 1840 – 12 February 1909), was a British botanist appointed superintendent of the Royal Botanic Garden, Calcutta in 1871, and the first Director of the Botanical Survey of India from 1890.  He was recognised for his work in the cultivation of cinchona and for setting up a system for the inexpensive distribution of quinine throughout India through the postal system.

Peter Chan: Peter Ho-sun Chan (born 28 November 1962) is a film director and producer.

George King (film director): George King (1899–26 June 1966) was an English actors' agent, film director, producer and screenplay writer.  He is associated with the production of quota quickies.  He helmed several of Tod Slaughter's melodramas, including 1936's "".

Gaiety George: Gaiety George is a 1946 British historical musical film directed by George King and Leontine Sagan and starring Richard Greene, Ann Todd and Peter Graves.  It is set in the late Victorian music hall, when an Irish impresario arrives in London.

Peter Chan Chi-kwan: Peter Chan Chi-kwan (Chinese: 陳子鈞, born on 7 March 1936 in Hong Kong) is the barrister-at-law and was a member of the Urban Council of Hong Kong for more than twenty years.  He is the founding member and was the Former vice-chairman of the Hong Kong Civic Association and legal adviser to the Hong Kong Federation of Trade Unions.  He was also the former Kowloon City District Board member (1982-1991), and Urban Councillor (1969-1991).  He was first elected to the Urban Council in 1969 and continued to be reelected in 1973, 1977, 1981, 1983, 1986, and 1989, until he got defeated in 1991.

Dragon (2011 film): Dragon () is a 2011 Hong Kong-Chinese martial arts film directed by Peter Chan, and starring Donnie Yen, Takeshi Kaneshiro and Tang Wei.  Yen also served as the film's action director.  It premiered on 13 May 2011 at the 2011 Cannes Film Festival in the Midnight Screenings category.  Donnie Yen and Peter Chan presided over the lighting of a billboard for "Dragon" that broke the Guinness Book of World Records for its size, 3591 square metres, previously held by a poster for a Michael Jackson album.

Kasper &quot;Stranger&quot; Malone: Kasper Delmar "Stranger" Malone (born October 25, 1909 near Lovelaceville, Kentucky – died May 30, 2005 in Rome, Georgia) was an American musician.  Malone's career as a recording artist spanned 77 years and, according to his biographer George King, is recognized as the longest by the Guinness Book of World Records.  His first recording, eight 78 rpm sides, was made by Columbia Records in 1926; his last one, with Elise Witt, by EMWorld Records in 2003.  Malone was one of the first documented clarinet players in country music.

Silent Strength: Silent Strength is the first solo studio album by American singer Shirley Jones of The Partridge Family music group.  The album features 11 tracks of contemporary christian music songs.  The track "You'll Never Walk Alone" is an updated cover version of the song Shirley Jones originally recorded for the film "Carousel".  "Silent Strength" was recorded in Nashville, Tennessee.  It was produced by George King and arranged by David T. Clydesdale who also co-produced.  "Silent Strength" was released in 1989 and issued on Diadem Records.  It was available on compact disc and on cassette tape but not on vinyl.

Han Sanping: Han Sanping (born 1953) is a Chinese film producer and distributor.  He is the chairman of China Film Group Corporation, which has been hailed as one of the largest distributors and exporters of Chinese films.  Han has also co-produced with established film directors such as Peter Chan, Chen Kaige, Stephen Chow and Johnnie To.

To Be a Lady: To Be a Lady is a 1934 British romance drama, directed and produced by George King, and starring Chili Bouchier (credited here as Dorothy Bouchier) and Bruce Lester.  The film is the first screen editing credit of American film editor Elmo Williams.

Question: Which film director was born first, Peter Chan or George King?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "directors_compared": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the film director."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the film director."
          }
        },
        "required": [
          "name",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "minItems": 2,
      "maxItems": 2,
      "description": "Details of the two film directors being compared."
    },
    "director_born_first": {
      "type": "string",
      "description": "The name of the film director who was born first."
    },
    "birth_year_difference": {
      "type": "integer",
      "description": "The difference in years between the birth years of the two directors."
    }
  },
  "required": [
    "directors_compared",
    "director_born_first",
    "birth_year_difference"
  ],
  "additionalProperties": false
}
