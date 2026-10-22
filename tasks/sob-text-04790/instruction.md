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
Typhoon Rita (1975): Typhoon Rita was the most damaging typhoon to affect northern Japan since 1965.  A tropical depression developed on August 9, 1975 over the South China Sea.  The depression initially meandered offshore Taiwan, but after turning west, it was upgraded into a tropical storm on August 19, only to turn back to the east.  While growing considerably in size, Rita strengthened into a typhoon during the afternoon hours of the August 21.  Rita then accelerated to the north-northeast in response to a shortwave trough.  Midday on August 22, the typhoon reached its peak intensity, with winds of 145 km/h (90 mph) and a minimum barometric pressure of 965 mbar (28.5 inHg).  That evening, the typhoon weakened slightly before making landfall 55 km (35 mi) west of Osaka, with winds of 130 km/h (80 mph).  Quickly crossing central and northern Honshu, Rita veered slightly northward before weakening into a tropical storm early on August 23.  On the next day, Rita merged with a cold front before transiting into an extratropical cyclone.

Symphony No. 4 (Martins): Symphony No. 4, titled Buddha Dharma or rarely Buddha Dhamma was a symphony made by Vasco Martins in 2001.  It was the first fourth symphony made by a Cape Verdean and the fourth symphony made by a Cape Verdean.  The symphony was inspired by reading a book by Buddha.  He composed it slowly (metronome figure circa 45), the one-piece work took two weeks and was made in and around the island of São Vicente.  The first performance was premiered on September 3, 2001 in São Paulo, Brazil by Lutero Rodrigues and the local cultural symphony ("Sinfonia Cultura"), its length is 19-20 minutes.  It was performed in France in 2007 and was done by Henri-Claude Fantapié.  This work can be listened via the MP3 format via the website, this was done by the composer.  The symphony is also available on YouTube.  The work covers around 500 sizes and forms about five crescendos.

Symphony No. 5 (Rouse): The Symphony No. 5 is a symphony for orchestra by the American composer Christopher Rouse.  The work was jointly commissioned by the Dallas Symphony Orchestra, the Nashville Symphony, and the Aspen Music Festival.  It was completed in Baltimore on February 15, 2015, and was first performed by the Dallas Symphony Orchestra under the direction of Jaap van Zweden at the Morton H. Meyerson Symphony Center on February 9, 2017.

Jimmy López: Jimmy López (born 21 October 1978) is a classical music composer from Lima, Peru and is considered "one of the most interesting young composers anywhere today" He has won several international awards and pieces composed by him have been performed by leading orchestras around the world such as the Chicago Symphony Orchestra, Philadelphia Orchestra, Boston Symphony Orchestra, Fort Worth Symphony Orchestra, National Symphony Orchestra of Peru, Helsinki Philharmonic Orchestra, MDR Leipzig Radio Symphony Orchestra, Sydney Symphony Orchestra and Orchestre Philharmonique de Radio France.  His works have been performed in prestigious venues such as Carnegie Hall, Sydney Opera House, Gewandhaus Leipzig, and during the 2010 Youth Olympic games in Singapore.  His music has been featured in numerous festivals, including Tanglewood Music Festival, Aspen Music Festival, Grant Park Music Festival, Darmstadt International Course for New Music, and Donaueschingen Music Festival.

Wilson Sawyer: Wilson Sawyer (1917–1979) was an American composer, arranger and musician.  Born in Traverse City, Michigan, he showed musical talent at an early age and studied music at the University of Michigan.  Sawyer conducted the University's Women's Glee Club and led the Bill Sawyer Orchestra, a big band that was featured on WMAQ's "Fitch Summer Bandwagon" on July 7, 1940.  He composed several arrangements of choral works; popular songs for Perry Como, Fred Waring and Ray Eberle; music for the "Alaskan Stampede," a Leo Seltzer produced "musical extravaganza on ice" c. 1944, and an opera based on Mark Twain's Tom Sawyer.  He is best known for composing Symphony No. 1, known as the Alaskan Symphony, at Gypsy Trail, Carmel, New York in 1945.  The work includes text from the "Spell of the Yukon" by Robert W. Service sung by a baritone soloist in the third movement, as well as other thematic inspirations drawn from his study of the climate, topography and history of the then-territory.  The Alaskan Symphony was first performed in December 1945 by the American Symphony Orchestra and was broadcast across the United States and to overseas armed services at that time.  Wilson Sawyer conducted the piece and Gov. Ernest Gruening of Alaska was guest speaker on the program.  At Gruening's request, the original score was placed in the Alaskan Museum of Natural History [Alaska Historical Library and Museum] in Juneau, Alaska.  In 1960, Sawyer's wife Maxine was diagnosed with spinal cancer and they moved to Pawling, New York where he operated a chicken farm and laundromat.  He continued to compose.  The Alaskan Symphony was performed by the Hudson Valley Philharmonic in 1975 with Sawyer again conducting even though he had recently suffered a stroke.  Sawyer revised the Symphony in 1977, making substantial cuts to the fourth movement among other edits.  The revised Alaskan Symphony was premiered by the Juneau Symphony on June 14, 2008, conducted by music director Kyle Wiley Pickett.

Symphony No. 9 (Dvořák): The Symphony No. 9 in E minor, "From the New World", Op. 95, B. 178 (Czech: "„Z nového světa“" ), popularly known as the New World Symphony, was composed by Antonín Dvořák in 1893 while he was the director of the National Conservatory of Music of America from 1892 to 1895.  It is by far his most popular symphony, and one of the most popular of all symphonies.  In older literature and recordings, this symphony was often numbered as Symphony No. 5.  Neil Armstrong took a recording of the "New World Symphony" to the Moon during the Apollo 11 mission, the first Moon landing, in 1969.  The symphony was completed in the building that now houses the Bily Clocks Museum.

Rita Orlandi-Malaspina: Rita Orlandi-Malaspina (28 December 1937 – 8 April 2017) was an Italian operatic soprano who had a major international career from the 1960s through the 1980s.  She drew particular acclaim for her portrayals of Verdi heroines.  She also had a successful career as a concert soprano, particularly in performance of Verdi's "Requiem" and Ludwig van Beethoven's "Symphony No. 9".

Rita Connolly: Rita Connolly is a singer who has lived and worked in Ireland.  She is primarily known for her work with composer Shaun Davey who wrote a song cycle for her called "Granuaile" based on the 16th-century pirate queen Gráinne O'Malley as well as including her in other of his works such as "The Relief of Derry Symphony", "The Pilgrim Suite" and his Special Olympics music which was specially composed in 2003.  Rita Connolly and Ronan Tynan sang the anthem song "May We Never Have to Say Goodbye" which topped the Irish charts for two weeks.  She has also produced two solo albums, one with the eponymous title "Rita Connolly", and the second "Valpariso" on the Tara Music label.

Adam Schoenberg: Adam Schoenberg (born November 15, 1980) is one of the most performed living American composers.  A member of the Atlanta School of Composers, his works have been performed by the Amarillo Symphony, Atlanta Symphony Orchestra, Buffalo Philharmonic Orchestra, Charleston Symphony Orchestra, Charlotte Symphony Orchestra, The Cleveland Orchestra, Dallas Symphony Orchestra, The Florida Orchestra, Fort Worth Symphony Orchestra, Grand Rapids Symphony, Jacksonville Symphony, Kansas City Symphony, Knoxville Symphony Orchestra, Lake Forest Symphony Orchestra, Lexington Philharmonic, Los Angeles Philharmonic, National Symphony Orchestra, New West Symphony, New World Symphony (orchestra), New York Philharmonic, Orlando Philharmonic Orchestra, Pacific Symphony, Phoenix Symphony, Rochester Philharmonic Orchestra, San Diego Symphony, South Carolina Philharmonic, Tallahassee Symphony Orchestra, Waterloo-Cedar Falls Symphony, among other ensembles.  Schoenberg was the 2010-2012 guest composer for the Aspen Music Festival, the 2012-2013 composer-in-residence for the Kansas City Symphony, the 2013-2014 composer-in-residence for the Lexington Philharmonic, and the 2015-2017 composer-in-residence for the Fort Worth Symphony.  Schoenberg's honors include a 2009 and 2010 MacDowell Colony fellowship, the 2007 Morton Gould Young Composer Award from ASCAP, and the 2006 Charles Ives Prize from the American Academy of Arts & Letters.

Symphony No. 9 (Beethoven): The Symphony No. 9 in D minor, Op.  125, is the final complete symphony composed from 1822 to 1824 by the German composer Ludwig van Beethoven.  It was first performed in Vienna on 7 May 1824.  The symphony is one of the best-known works in common practice music.  It is widely viewed by critics as one of Beethoven's greatest works, the pinnacle of musical Classicism, and one of the greatest compositions in the western musical canon.  The symphony was the first example of a major composer using voices in a symphony (thus making it a choral symphony).  The words are sung during the final movement by four vocal soloists and a chorus.  They were taken from the "Ode to Joy", a poem written by Friedrich Schiller in 1785 and revised in 1803, with text additions made by the composer.  In the 2010s, it stands as one of the most performed symphonies in the world.

Question: Who composed Symphony No. 9 that was performed by Rita Orlandi-Malaspina?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "composer_name": {
      "type": "string",
      "description": "The name of the composer of the symphony."
    },
    "symphony_number": {
      "type": "integer",
      "description": "The number of the symphony."
    },
    "performer_name": {
      "type": "string",
      "description": "The name of the performer."
    },
    "performer_role": {
      "type": "string",
      "description": "The role of the performer in the context of the symphony."
    }
  },
  "required": [
    "composer_name",
    "symphony_number",
    "performer_name",
    "performer_role"
  ],
  "additionalProperties": false
}
