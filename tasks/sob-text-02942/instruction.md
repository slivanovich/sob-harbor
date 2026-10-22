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
Westward Ho (1935 film): Westward Ho is a 1935 American Western film released by Republic Pictures, produced by Paul Malvern, directed by Robert N. Bradbury and starring John Wayne in his first film for Republic.  The trio had previously filmed a series of "Lone Star Westerns" for Monogram Pictures until Monogram merged into Republic pictures.

Riders of Destiny: Riders of Destiny is a 1933 pre-Code Western musical film starring 26-year-old John Wayne as Singin' Sandy Saunders, the screen's second singing cowboy (the first being Ken Maynard in the 1929 film "The Wagon Master").  It was the first of a series of Lone Star Westerns made for Monogram Pictures by Wayne and director Robert N. Bradbury and the first pairing of Wayne with George "Gabby" Hayes.

Sitting Bull at the Spirit Lake Massacre: Sitting Bull at the Spirit Lake Massacre (also known as With Sitting Bull at the Spirit Lake Massacre) is a 1927 American Western film directed by Robert N. Bradbury, and starring Bryant Washburn as Donald, Chief Yowlachie as Sitting Bull, and Anne Schaefer as Mame Mulcain.

Robert N. Bradbury: Robert N. Bradbury (March 23, 1886 – November 24, 1949) was an American film director and screenwriter who directed 125 movies between 1918 and 1941.  He is most famous for directing early Western films starring John Wayne in the 1930s, including "Riders of Destiny" (1933; an early singing-cowboy movie), "The Lucky Texan" (1934), "West of the Divide" (1934), "Blue Steel" (1934), "The Man From Utah" (1934), "The Star Packer" (1934), "The Trail Beyond" (1934; co-starring Noah Beery, Sr. and Noah Beery, Jr.), "The Lawless Frontier" (1934), "Texas Terror" (1935), "Rainbow Valley" (1935), "The Dawn Rider" (1935), "Westward Ho" (1935), and "Lawless Range" (1935).  These were inexpensively shot "Poverty Row" movies; many were also written by Bradbury and almost all of them featured character actor George "Gabby" Hayes.  Bradbury also shot numerous similar films during this period starring his son Bob Steele or Johnny Mack Brown.  Bradbury occasionally billed himself as "Robert North Bradbury", "R.N. Bradbury", or "Robert Bradbury".

Rob Schneider: Robert Michael Schneider (born October 31, 1963) is an American actor, comedian, screenwriter, and director.  A stand-up comic and veteran of the NBC sketch comedy series "Saturday Night Live", he went on to a successful career in feature films, including starring roles in the comedy films "", "The Hot Chick", "The Benchwarmers", and "Grown Ups".

Robert Royston: Robert N. Royston (1918 – September 19, 2008) was one of America's most distinguished landscape architects, based in the San Francisco Bay Area of California in the United States.  His design work and university teaching in the years following World War II helped define and establish the California modernism style in the post-war period.  During his sixty years of professional practice Royston completed an array of award-winning projects that ranged from residential gardens to regional land use plans.  He is perhaps best known for his important innovations in park design.  A recent book, "Modern Public Gardens: Robert Royston and the Suburban Park", details this area of his professional creativity and philosophy.

Bob Steele filmography: Born Robert North Bradbury Jr. (January 23, 1907December 21, 1988), American actor Bob Steele and his twin brother Bill were the sons of film director Robert N. Bradbury.  The twins began their acting career in the silent film "The Adventures of Bob and Bill", directed by their father, and continued in a series of Bradbury Sr.'s film shorts.  Bill later pursued a career in medicine.  Bob continued to act under his real name, until "The Mojave Kid" when he was billed as Bob Steele.  During his career of more than 200 films and television shows between 1920 and 1974, he was known primarily for his work in Westerns.  Steele appeared as the recurring character of Tucson Smith in several of the Three Mesquiteers serials produced by Republic Pictures.  He became familiar to America's television audiences for his recurring role as Trooper Duffy in the comedy series "F Troop".

Headin' for Danger: Headin' for Danger (also known as Asking for Trouble) is a 1928 American western directed by Robert N. Bradbury for Film Booking Offices of America (FBO) and commercially released in the United States on 16 December 1928.  The film was written by Frank Howard Clark and stars Bob Steele, Jola Mendez and Al Ferguson.

Joyce Van Patten: Joyce Benignia Van Patten (born March 9, 1934) is an American stage, film, and television actress, best known for the wry, astringent, and neurotic characters she portrays.  Among many roles, one of her most recognized is that of the wise, elderly wife of Rob Schneider's character in the Adam Sandler comedy "Grown Ups" (2010).

The Man from Hell's Edges: The Man from Hell's Edges (also known as El Lobo) is a 1932 American Pre-Code short Western film directed and written by Robert N. Bradbury for Trem Carr Pictures.  It was released in the United States on June 15, 1932.

Question: Which director was best known for westerns, Robert N. Bradbury or Rob Schneider?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "director_name": {
      "type": "string",
      "description": "The name of the director best known for Westerns."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for why this director was chosen, referencing their work in Westerns and the other director's primary genre."
    },
    "films_directed_count": {
      "type": "integer",
      "description": "The total number of films directed by the identified director."
    },
    "notable_western_films": {
      "type": "array",
      "description": "A list of some notable Western films directed by the identified director.",
      "items": {
        "type": "string"
      }
    },
    "other_director_comparison": {
      "type": "object",
      "description": "Information about the other director for comparison.",
      "properties": {
        "name": {
          "type": "string"
        },
        "known_for_genre": {
          "type": "string"
        },
        "notable_films": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "name",
        "known_for_genre",
        "notable_films"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "director_name",
    "reasoning",
    "films_directed_count",
    "notable_western_films",
    "other_director_comparison"
  ],
  "additionalProperties": false
}
