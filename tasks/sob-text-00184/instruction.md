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
Lionel Hampton: Lionel Leo Hampton (April 20, 1908 – August 31, 2002) was an American jazz vibraphonist, pianist, percussionist, bandleader and actor.  Hampton worked with jazz musicians from Teddy Wilson, Benny Goodman, and Buddy Rich to Charlie Parker, Charles Mingus, and Quincy Jones.  In 1992, he was inducted into the Alabama Jazz Hall of Fame, and was awarded the National Medal of Arts in 1996.

UC Berkeley College of Chemistry: The UC Berkeley College of Chemistry is one of 14 schools and colleges at the University of California, Berkeley.  It houses the departments of Chemistry,Chemical and Engineering, and Chemical Biology and occupies six buildings flanking a central plaza.  US News and World Report has ranked its chemistry and chemical engineering programs first and second in the U.S., respectively, while the 2014 QS World University Rankings has ranked both its chemistry and chemical engineering programs second best in the world.  Its faculty and graduates have won numerous awards, including the Wolf Prize, the National Medal of Science, the National Medal of Technology, the Presidential Medal of Freedom, as well as thirteen Nobel Prizes.  s of 2012 -13, it has 815 undergraduates, 526 graduate students, and 187 postdoctoral fellows.

Robert Shaw (conductor): Robert Shaw (April 30, 1916January 25, 1999) was an American conductor most famous for his work with his namesake Chorale, with the Cleveland Orchestra and Chorus, and the Atlanta Symphony Orchestra and Chorus.  Shaw received 14 Grammy awards, four ASCAP awards for service to contemporary music, the first Guggenheim Fellowship ever awarded to a conductor, the Alice M. Ditson Conductor's Award for Service to American Music; the George Peabody Medal for outstanding contributions to music in America, the Gold Baton Award of the American Symphony Orchestra League for "distinguished service to music and the arts," the American National Medal of Arts, France's Officier des Arts et des Lettres, England's "Gramophone" Award, and was a 1991 recipient of the Kennedy Center Honors.

Johnny Comes Flying Home: Johnny Comes Flying Home is a 1946 film directed by Benjamin Stoloff and starring Richard Crane and Faye Marlowe; the supporting cast features Harry Morgan.  The plot involves postwar pilots starting a small aviation company.

List of National Medal of Science laureates: The National Medal of Science is an honor bestowed by the President of the United States to individuals in science and engineering who have made important contributions to the advancement of knowledge in the following six fields, behavioral and social sciences, biology, chemistry, engineering, mathematics and physical sciences.  The Committee on the National Medal of Science under the National Science Foundation (NSF) is responsible for recommending medal candidates to the President.

Flying Home: "Flying Home" is a jazz and jump blues composition written by Benny Goodman and Lionel Hampton with lyrics by Sid Robin.  It was reportedly developed around a tune Hampton whistled as he nervously waited for his first flight on an aircraft.

National Science and Technology Medals Foundation: The National Science and Technology Medals Foundation, a District of Columbia nonprofit, supports the National Medal of Science and the National Medal of Technology and Innovation, awarded by the President of the United States.

Hank Jones: Henry "Hank" Jones Jr. (July 31, 1918 – May 16, 2010) was an American jazz pianist, bandleader, arranger, and composer.  Critics and musicians described Jones as eloquent, lyrical, and impeccable.  In 1989, The National Endowment for the Arts honored him with the NEA Jazz Masters Award.  He was also honored in 2003 with the American Society of Composers, Authors, and Publishers (ASCAP) Jazz Living Legend Award.  In 2008, he was awarded the National Medal of Arts.  On April 13, 2009, the University of Hartford presented Jones with a Doctorate Degree for his musical accomplishments.

Illinois Jacquet: Jean-Baptiste Illinois Jacquet (October 30, 1919 – July 22, 2004) was an American jazz tenor saxophonist, best remembered for his solo on "Flying Home", critically recognized as the first R&B saxophone solo.

Saul Bellow: Saul Bellow (born Solomon Bellows; 10 June 1915 – 5 April 2005) was a Canadian-American writer.  For his literary work, Bellow was awarded the Pulitzer Prize, the Nobel Prize for Literature, and the National Medal of Arts.  He is the only writer to win the National Book Award for Fiction three times and he received the National Book Foundation's lifetime Medal for Distinguished Contribution to American Letters in 1990.

Question: Which writer of the jazz song "Flying Home" was awarded the National Medal of Arts in 1996?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person who wrote the song."
    },
    "role_in_song": {
      "type": "string",
      "description": "The role of the person in the creation of the song (e.g., writer, lyricist)."
    },
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "award_received": {
      "type": "string",
      "description": "The name of the award received by the person."
    },
    "award_year": {
      "type": "integer",
      "description": "The year the award was received."
    }
  },
  "required": [
    "person_name",
    "role_in_song",
    "song_title",
    "award_received",
    "award_year"
  ],
  "additionalProperties": false
}
