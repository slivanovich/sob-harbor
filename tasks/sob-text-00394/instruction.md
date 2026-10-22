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
Peter Cacchione: Peter V. "Pete" Cacchione (November 1, 1897 – November 6, 1947) was a communist labor leader who was elected to the New York City Council in 1941.  He was born to Italian-American immigrant family in Syracuse, New York on November 1, 1897 and grew up in Sayre, Pennsylvania.  He became director of sports activities for the Catholic Welfare Council, later becoming a steel worker in Bethlehem, a street car conductor, riveter and later a trainman on the Lackawanna Railroad.  According to fellow communist city councilman Benjamin J. Davis and newspaper accounts, Cacchione served in World War I.  Cacchione joined the Communist Party USA in 1932 and led a delegation of the communist affiliated Workers Ex-Service Men's League in the 1932 Washington D.C. bonus march.  He became National Commander of the League in 1935.  Cacchione moved to New York City, Bronx, in 1932 and was later elected Bronx County Chairman of the Communist Party USA in 1934.  After relocating to Brooklyn, he was elected Kings County Chairman of the Communist Party in 1936.

Suimenkul Chokmorov: Suimenkul Chokmorov (Kyrgyz: Сүймөнкул Чокморов ; Russian: Суйменкул Чокморов ; 9 November 1939 – 26 September 1992) was a Kyrgyz film actor born in Chon Tash village, Kirghiz SSR (now Kyrgyzstan).  In 1964 he graduated from the Leningrad Academy of Arts and later taught painting and composition at the Arts School of Frunze.  In 1977 he was a member of the jury at the 10th Moscow International Film Festival.

Nick Dennis: Nick Dennis (April 26, 1904 – November 14, 1980) was a Greek American film actor born in Thessaly, Greece.  The supporting actor, who began in films in 1947, was known for playing ethnic types (usually Greek) in films such as "Kiss Me Deadly" and the Humphrey Bogart film "Sirocco".  Dennis, who spoke Greek fluently, appeared in a number of television programs in the 1960s and 1970s including playing the parts of Orderly Nick Kanavaras on the medical drama "Ben Casey" and Uncle Constantine on the detective show "Kojak".

Max Terhune: Max Terhune (12 February 1891 – 5 June 1973) was an American film actor born in Franklin, Indiana.  He appeared in nearly 70 films, mostly B-westerns, between 1936 and 1956.  Among these, Terhune starred in the Three Mesquiteers and Range Busters series.

George Dolenz: George Dolenz (born Jure Dolenc; a.k.a. "Giorgio Dolenz" and "George Dolentz"; 5 January 19088 February 1963) was an American film actor born in Trieste (then part of Austria-Hungary, now in Italy), in the city's Slovene community.

James Burke (actor): James Burke (September 24, 1886 – May 23, 1968) was an American film and television actor born in New York City.  He made his stage debut in New York around 1912 and went to Hollywood in 1933.  He made over 200 film appearances during his career, which ranged from 1932 to 1964; he was more often than not cast as a cop, usually a none-too-bright one, most notably as Sgt. Velie in Columbia's Ellery Queen mysteries in the early 1940s.  He appeared in "The Maltese Falcon", "At the Circus", "Lone Star", and many others.  One of his best roles was as Charles Ruggles' rowdy rancher pal in "Ruggles of Red Gap".

Ion Popescu-Gopo: Ion Popescu-Gopo (] ; 1 May 1923, Roești, Vâlcea – 28 November 1989, Bucharest) was a Romanian graphic artist and animator, but also writer, movie director and actor born in Bucharest, Romania.  He was a prominent personality in the Romanian cinematography and the founder of the modern Romanian cartoon school.  He was, together with Liviu Ciulei and Mirel Ilieşiu one of the few Romanian film artists who won an award at Cannes in the 20th century.  His film "Scurtă Istorie" ("A Brief History") won the "Short Film Palme d'Or" for best short film in 1957.  His 1965 film "The White Moor" was entered into the 4th Moscow International Film Festival where he won the award for Best Director.  In 1969 he was a member of the jury at the 6th Moscow International Film Festival.  In 1977 he was a member of the jury at the 10th Moscow International Film Festival.  In 1983 he was a member of the jury at the 13th Moscow International Film Festival.

The Black Marble: The Black Marble is a 1980 mystery/romantic comedy film directed by Harold Becker, based on a novel by Joseph Wambaugh.  It stars Robert Foxworth, Paula Prentiss and Harry Dean Stanton.

Pete Morrison: George D. "Pete" Morrison (August 8, 1890 – February 5, 1973) was an American silent western film actor born in Westminster, Colorado.  During his childhood he lived in Morrison, Colorado (named for his grandfather George Morrison) and Idaho Springs, and got his early tastes of horsemanship riding with his father Thomas during the summer.  They drove cattle and sheep from the summer ranges in Middle Park and Fall River in Colorado to supply beef and mutton to the mining camps of Georgetown, Idaho Springs, Nevadaville, Black Hawk and Central City.  During his mid-teens Pete worked in the mining industry, with his older brothers driving in sections of the Argo Tunnel where Pete was a motorman, hoist operator, topside helper, teamster hauler, assisting several of the larger miners in the Idaho Springs area.  In the summer of 1910 Pete Morrison was an engine fireman for the Colorado and Southern Railway when he was lured away by the early western movies.  Pete began working as a stunt man for the Essanay Studios of "Broncho Billy" films, soon discovering he could make more money working in movies in 2 weeks than he could make working for a month on the railroad.  Pete followed his older brother Chick Morrison to California, where he also became a star in early western pictures.  Through his career, Morrison transcended from very early film in 1909 to sound in 1935 starring in some 132 pictures.

Robert Foxworth: Robert Heath Foxworth (born November 1, 1941) is an American film, stage, and television actor.

Question: Who is the director of the film in which an American film actor born November 1, 1941 became a star?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_date": {
          "type": "string",
          "format": "date"
        },
        "nationality": {
          "type": "string"
        },
        "profession": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "birth_date",
        "nationality",
        "profession"
      ],
      "additionalProperties": false
    },
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "release_year": {
          "type": "integer"
        },
        "genre": {
          "type": "string"
        }
      },
      "required": [
        "title",
        "release_year",
        "genre"
      ],
      "additionalProperties": false
    },
    "director_name": {
      "type": "string"
    }
  },
  "required": [
    "actor_details",
    "film_details",
    "director_name"
  ],
  "additionalProperties": false
}
