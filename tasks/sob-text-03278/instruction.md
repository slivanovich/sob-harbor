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
Chin Tsi-ang: Chin Tsi-Ang (February 22, 1909 – October 15, 2007), also romanized as Qian Siying, was one of the earliest martial arts actors of Chinese cinema, and the first female star.  She debuted in "South China Dream" (南华梦, Nanhua Meng) in 1925 at the age of 16, and played a leading role in "Southern Heroine" (江南女侠, Jiangnan Nüxia) in 1930.

Louise Lester: Louise Lester (August 8, 1867 – November 18, 1952) was an American silent film actress.  She was the first female star of Western films.

Eternally Yours (film): Eternally Yours is a 1939 American comedy drama film produced and directed by Tay Garnett with Walter Wanger as executive producer, from a screenplay by C. Graham Baker and Gene Towne.  It stars Loretta Young and David Niven.  Composer Werner Janssen was nominated for the Academy Award for Best Music.

Soap Opera Digest Award for Hottest Female Star: The Soap Opera Digest Award for Hottest Female Star has been given every year since the 9th Soap Opera Digest Award in 1993 until 1999.

Helen Twelvetrees: Helen Marie Twelvetrees (December 25, 1908 – February 13, 1958) was an American film and theatre actress, who became a top female star through a series of "women's pictures" in the early 1930s.

Katharine Hepburn: Katharine Houghton Hepburn (May 12, 1907 – June 29, 2003) was an American actress.  Known for her fierce independence and spirited personality, Hepburn was a leading lady in Hollywood for more than 60 years.  She appeared in a range of genres, from screwball comedy to literary drama, and she received four Academy Awards—a record for any performer—for Best Actress.  In 1999, Hepburn was named by the American Film Institute as the greatest female star of Classic Hollywood Cinema.

Fredrica Löf: Fredrica Löf, also known as Fredrique Löwen (née "Johanna Fredrika Löf"; Stockholm, October 1760 – Torsåker, Södermanland, 17 July 1813), was a Swedish stage actress.  She was the first female star at the newly founded national stage Royal Dramatic Theater, which was founded the year of her debut.

Andrea Palma (actress): Guadalupe Bracho Pérez-Gavilán, better known as Andrea Palma (16 April 1903 in Durango, Mexico – 6 October 1987 in Mexico City, Mexico) was a Mexican film stage and television actress.  She was considered the first major female star of the Mexican cinema after her role in the Mexican film "La Mujer del Puerto" (1934).

Jenni Rivera discography: American singer Jenni Rivera has released eleven studio albums, eight live albums, three compilation albums, 33 singles. Rivera has been said to be the top-selling Regional Mexican female star of her generation by "Billboard" with more than 20 million albums sold.

Loretta Young: Loretta Young (January 6, 1913 – August 12, 2000) was an American actress and singer.  Starting as a child actress, she had a long and varied career in film from 1917 to 1953.  She won the 1948 Academy Award for Best Actress for her role in the 1947 film "The Farmer's Daughter" and received an Oscar nomination for her role in "Come to the Stable" in 1949.  Young moved to the relatively new medium of television, where she had a dramatic anthology series, "The Loretta Young Show", from 1953 to 1961.  The series earned three Emmy Awards and was rerun successfully on daytime TV and later in syndication.  In the 1980s, Young returned to the small screen and won a Golden Globe for her role in "Christmas Dove" in 1986.  Young, a devout Roman Catholic, worked with various Catholic charities after her acting career.

Question: What was the religion of the female star of "Eternally Yours"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "female_star": {
      "type": "string",
      "description": "The name of the female star of the film."
    },
    "star_religion": {
      "type": "string",
      "description": "The religion of the female star."
    },
    "star_birth_date": {
      "type": "string",
      "format": "date",
      "description": "The birth date of the female star in YYYY-MM-DD format."
    },
    "star_death_date": {
      "type": "string",
      "format": "date",
      "description": "The death date of the female star in YYYY-MM-DD format."
    }
  },
  "required": [
    "film_title",
    "female_star",
    "star_religion",
    "star_birth_date",
    "star_death_date"
  ],
  "additionalProperties": false
}
