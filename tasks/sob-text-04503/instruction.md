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
Scott Special: The Scott Special, also known as the Coyote Special, the Death Valley Coyote or the Death Valley Scotty Special, was a one-time, record-breaking (and the best-known) passenger train operated by the Atchison, Topeka and Santa Fe Railway (Santa Fe) from Los Angeles, California, to Chicago, Illinois, at the request of "Death Valley Scotty".  At the time of its transit in 1905, the "Scott Special" made the 2265 mi trip between the two cities at the fastest speed recorded to date; in doing so, it established the Santa Fe as the leader in high-speed travel between Chicago and the West Coast.  The "Scott Special" made the trip in 44 hours and 54 minutes breaking the previous records, set in 1900 by the "Peacock Special", by 13 hours and 2 minutes, and in 1903 by the "Lowe Special", by 7 hours and 55 minutes.  Santa Fe's regular passenger service from Los Angeles to Chicago at the time was handled on a 2½-day schedule by the "California Limited".  It was not until the 1936 introduction of the "Super Chief" that Santa Fe trains would regularly exceed the speeds seen on the "Scott Special".

Santa Fe 1010: Santa Fe 1010 is a 2-6-2 type steam locomotive built by Baldwin Locomotive Works for Atchison, Topeka and Santa Fe Railway (Santa Fe).  It was used in the record breaking 1905 "Scott Special" on the segment between Needles, California, and Seligman, Arizona.  In 1955, 1010 was refurbished and used for a television re-enactment of the "Scott Special" for the "Death Valley Days" program about the special train.  This locomotive was also prominently featured in a 1958 episode of the TV series Sky King, entitled "Stop That Train".  In October 1984, Santa Fe donated 1010 to the California State Railroad Museum, where the locomotive resides today.

Santa Fe 5000: Santa Fe 5000 is a 2-10-4 steam locomotive constructed by Baldwin Locomotive Works in 1930 for the Atchison, Topeka and Santa Fe Railway.  No. 5000 was immediately nicknamed "Madame Queen" and remained a unique member of its own class.  It was donated to the city of Amarillo, Texas, in 1957 and is currently maintained by the Railroad Artifact Preservation Society.  Santa Fe 5000 is on the National Register of Historic Places.

Santa Fe Plaza: The Santa Fe Plaza is a National Historic Landmark in downtown Santa Fe, New Mexico in the style of traditional Spanish-American colonial cities.  The plaza, or "city-square", was originally, and is still to this day, the center gathering place in town.  Many know it as "the heart of Santa Fe".  The landmark has since grown into a playground for many tourists interested in Spanish, Native American, and Mexican cultures, and includes music, design, jewelry, art and dance.  Known to locals simply as the "Plaza," it is home to annual events including Fiestas de Santa Fe, the Spanish Market, the Santa Fe Bandstand, and the Santa Fe Indian Market.

Tecnológico de Monterrey, Campus Santa Fe: The Monterrey Institute of Technology and Higher Education, Santa Fe Campus (in Spanish: "Instituto Tecnológico y de Estudios Superiores de Monterrey, Campus Santa Fe" ) commonly shortened as Tecnológico de Monterrey, Campus Santa Fe, ITESM Campus Santa Fe or Tec Santa Fe, is a campus of the Monterrey Institute of Technology and Higher Education private university system in Santa Fe, Mexico City, Mexico.  It provides professional studies as well as high school programs.  International programs are also available.  The campus features modern architecture by the renowned Ricardo Legorreta, having more than 30,000 square meters of construction, with more than 3,000 students.

Santa Fe Relocation Services: Santa Fe Relocation provides relocation and global mobility services from 96 offices in 47 countries.  Services includes transportation, relocation services, logistics and storage.  Santa Fe was first established in Hong Kong in 1980, acquired by East Asiatic Company (EAC) in 1988, and has since then expanded globally.  On 1 April 2015, EAC and Santa Fe merged and the parent company's name was formally changed into Santa Fe Group.  Nowadays the trading name is still Santa Fe Group but the company is known as Santa Fe Relocation.

Santa Fe 2926: Santa Fe 2926 is a former Atchison, Topeka and Santa Fe Railway (Santa Fe) 4-8-4 steam locomotive originally built in 1944 by Baldwin (const #69814).  This locomotive was part of the last group of steam passenger locomotives (class 2900) built for the Santa Fe railway.  This class of locomotives were the heaviest 4-8-4's built in the United States, and among the largest.  The railroad used the locomotive in both fast freight and passenger service, accumulating over one million miles of usage before its last revenue run on December 24, 1953.  The locomotive and a caboose were donated to the city of Albuquerque, New Mexico in 1956 in recognition of the city's 250th anniversary, and placed in a city park.

José Manuel Corral: José Manuel Corral (born October 28, 1968 in Santa Fe, Santa Fe, Argentina) is a lawyer, a political activist of the Unión Cívica Radical party, and a member of the Coalition Frente Progresista Cívico y Social of Santa Fe.  He was the President of the Municipal Council of the City of Santa Fe de la Vera Cruz (2010–2011).  He has been reelected Mayor of the city of Santa Fe, Santa Fe province, Argentina, (2011–2015 / 2015–2019).

Atchison, Topeka and Santa Fe Railway: The Atchison, Topeka and Santa Fe Railway (reporting mark ATSF) , often referred to as the Santa Fe or AT&SF, was one of the larger railroads in the United States.  Chartered in February 1859, the railroad reached the Kansas-Colorado border in 1873 and Pueblo, Colorado, in 1876.  To create a demand for its services, the railroad set up real estate offices and sold farm land from the land grants that it was awarded by Congress.  Despite the name, its main line never served Santa Fe, New Mexico, as the terrain was too difficult; the town ultimately was reached by a branch line from Lamy.

Santa Fe 3751: Atchison, Topeka & Santa Fe 3751 is a 4-8-4 "Northern" type steam locomotive built in 1927 by the Baldwin Locomotive Works for the Atchison, Topeka and Santa Fe Railway.  Built as the first Northern type steam locomotive for the Santa Fe, the 3751 served in passenger duties until being retired in 1953.  The locomotive was then placed on display in San Bernardino, California until it was restored to operating condition in 1986.  The 3751 is currently located in the Central City East neighborhood of Los Angeles and is listed on the National Register of Historic Places.  Today, Santa Fe 3751 holds the distinction of being the oldest surviving 4-8-4 type steam locomotive in the world.  The locomotive is currently owned and operated by the San Bernardino Railroad Historical Society who use the locomotive to haul occasional mainline excursion trains.  It is currently due for its 15-year inspection, so it will be out of service for about 3-4 years.

Question: Ironically, which city did the Santa Fe 1010 locomotive never travel to?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "locomotive_name": {
      "type": "string",
      "description": "The name or identifier of the locomotive in question."
    },
    "owning_railway": {
      "type": "string",
      "description": "The name of the railway that owned the locomotive."
    },
    "city_not_visited": {
      "type": "string",
      "description": "The city that the locomotive, despite its name association, never traveled to."
    },
    "reason_railway_main_line_avoided_city": {
      "type": "string",
      "description": "The reason why the railway's main line did not serve the specified city."
    },
    "irony_noted": {
      "type": "boolean",
      "description": "Indicates if the ironic situation (locomotive name vs. city not visited) is highlighted."
    }
  },
  "required": [
    "locomotive_name",
    "owning_railway",
    "city_not_visited",
    "reason_railway_main_line_avoided_city",
    "irony_noted"
  ],
  "additionalProperties": false
}
