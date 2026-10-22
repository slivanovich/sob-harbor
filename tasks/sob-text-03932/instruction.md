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
Lázaro Cárdenas: Lázaro Cárdenas del Río (] ; May 21, 1895 – October 19, 1970) was a general in the Mexican Revolution and a statesman who served as President of Mexico between 1934 and 1940.  He is best known for nationalization of the oil industry in 1938 and the creation of Pemex, the government oil company.

Tuxtla Gutiérrez Mexico Temple: The Tuxtla Gutiérrez Mexico Temple is the 75th operating temple of The Church of Jesus Christ of Latter-day Saints (LDS Church).  Tuxtla Gutiérrez is the capital of Chiapas, Mexico's southernmost state and is an area famous for its many archaeological ruins.  The city itself lies in a valley among the mountains.  In April 1998, LDS Church president Gordon B. Hinckley announced the church would build thirty-two smaller temples around the world before the end of 2000.  The Tuxtla Gutiérrez Mexico Temple is one of these small temples and was welcomed by the many local church members.  Because of the mountainous terrain, travel in and out of the area is difficult and the closest LDS temple for members was in Mexico City — a 20-hour drive.  The temple in Tuxtla Gutiérrez serves more than 18,000 members in southeastern Mexico.

Bicol Natural Park: The Bicol Natural Park is a protected area of the Philippines located in the Bicol Region of southern Luzon.  It straddles the mountainous border between the provinces of Camarines Norte and Camarines Sur in the northern interior of the Bicol Peninsula.  First declared as a national park covering 4225 ha on 13 February 1934 through Proclamation No. 657 of Governor General Frank Murphy, the Bicol National Park was later extended to its present area of 5201 ha through amendments made in Proclamation No. 655 signed by President Manuel Luis Quezon on 23 December 1940.  The area was reclassified as a natural park on 29 December 2000 by virtue of Proclamation No. 43 by President Joseph Estrada.

William J. Thompkins: William J. Thompkins (July 5, 1884 - August 11, 1944) was a physician and health administrator in Kansas City, Missouri and served as Recorder of Deeds for the District of Columbia from 1934 to his death.  He first received national notice when he challenged Jim Crow Laws in Oklahoma in Federal Courts in the early 1910s.  He was a successful physician and was appointed superintendent of the Old General Hospital in Kansas City, Missouri and the Assistant Commissioner of Health in that City.  He wrote an influential study of the relationship between housing conditions and tuberculosis in blacks and was active in Democratic politics which garnered him attention at the highest levels of the party.  He became president of the National Negro Democratic Association and was a major campaigner for the Democratic Presidential Candidates in campaigns from 1928 until 1940, gaining national level party appointments in 1932, 1936, and 1940.  In 1934 he was appointed Recorder of Deeds for Washington, DC.  This position was the highest federal appointment given to an African American, a tradition which was started with Frederick Douglass' appointment to the position in 1881.

Duke Ellington at Fargo, 1940 Live: Duke Ellington at Fargo, 1940 Live is a live album by the Duke Ellington Orchestra that won the Grammy Award for Best Large Jazz Ensemble Album in 1980.  The album was recorded at a dance in Fargo, North Dakota.

Dance in California: California is rich in dance history.  In classical ballet, California is home to the oldest professional ballet company in the United States.  The San Francisco Ballet, founded as the San Francisco Opera Ballet in 1933, predates both American Ballet Theater and New York City ballet.  Barbara Crockett founded the Sacramento Ballet in 1954 and hosted the first festival for the Pacific Western Region of Regional Dance America in 1966.  In modern dance, Ruth St. Denis established her second school in the Hollywood area of Los Angeles in 1940 while Lester Horton created the Horton Dance Group in 1934, also in Los Angeles.  Ann Halprin founded the San Francisco Dancers’ Workshop in 1950 and continues to live and work in the San Francisco Bay Area.  The Bay Area in also home to Alonzo King's Lines Ballet and Oberlin Dance Collective.

Miguel de la Madrid: Miguel de la Madrid Hurtado (] ; December 12, 1934 – April 1, 2012) was a Mexican politician affiliated with the Institutional Revolutionary Party (PRI) who served as the 52nd President of Mexico from 1982 to 1988.  His presidency was notorious for introducing sweeping neoliberal economic policies in Mexico (beginning an era of neoliberal presidents in Mexico) and for his administration's slow response to the 1985 Mexico City earthquake that occurred halfway throughout his administration.

Los Pinos: Los Pinos (from Spanish, "The Pines") is the official residence and office of the President of Mexico.  Located in the Bosque de Chapultepec (Chapultepec Forest) in central Mexico City, it became the presidential seat in 1934, when Gen. Lázaro Cárdenas became the first president to live here.  The term "Los Pinos" has become a metonym for the Presidency of Mexico.

Eugene Allen Gilmore: Eugene Allen Gilmore (July 4, 1871 – November 4, 1953) was Vice Governor-General of the Philippine Islands from 1922-1929, serving twice as acting Governor-General of the Philippines in 1927 and again in 1929; the Dean of the College of Law at the University of Iowa from 1930 to 1934; the twelfth President of the University of Iowa from 1934 to 1940; and the law dean at the University of Pittsburgh School of Law from 1940 to 1942.

Camden Catholic High School: Camden Catholic High School (CCHS) is a four-year comprehensive private coeducational Roman Catholic high school, located in Cherry Hill, New Jersey, in the Philadelphia metropolitan area and serving students from the Camden County area.  The school operates under the supervision of the Roman Catholic Diocese of Camden.  The school has been accredited by the Middle States Association of Colleges and Schools Commission on Secondary Schools since 1934.  Camden Catholic students come from the local area and from Norway, Nigeria, Italy, Germany, Mexico, Vietnam, Korea, and China.  Many of these students live on campus in the Nazareth House, a convent re-purposed to accommodate foreign students with full-time care-providers on staff, while others live with host families in the surrounding area.

Question: In what area did the President of Mexico between 1934 and 1940 live in?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "president_name": {
      "type": "string",
      "description": "The name of the President of Mexico during the specified period."
    },
    "presidency_start_year": {
      "type": "integer",
      "description": "The start year of the president's term."
    },
    "presidency_end_year": {
      "type": "integer",
      "description": "The end year of the president's term."
    },
    "official_residence_name": {
      "type": "string",
      "description": "The name of the official presidential residence."
    },
    "residence_location_area": {
      "type": "string",
      "description": "The specific area or forest where the residence is located."
    },
    "residence_location_city": {
      "type": "string",
      "description": "The city where the residence is located."
    }
  },
  "required": [
    "president_name",
    "presidency_start_year",
    "presidency_end_year",
    "official_residence_name",
    "residence_location_area",
    "residence_location_city"
  ],
  "additionalProperties": false
}
