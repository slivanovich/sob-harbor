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
Christina Booth: Christina Maria Booth (born 1965) is a Welsh progressive rock vocalist and singer-songwriter.

Corey Glover: Corey Glover (born November 6, 1964) is an American singer, guitarist and actor.  He is best known as the lead vocalist of the rock band Living Colour and has toured as the vocalist for the funk band Galactic.  As an actor, he is noted for playing Francis in the 1986 war movie "Platoon".

Roughlee: Roughlee is a village in Pendle, Lancashire, England, in the civil parish of Roughlee Booth.  It is close to Nelson, Barrowford and Blacko.  The village lies at the foot of Pendle Hill, well known for the Pendle Witches, and includes the hamlet of Crowtrees.  The parish adjoins the Pendle parishes of Blacko, Barrowford, Old Laund Booth, Goldshaw Booth and Barley-with-Wheatley Booth.  It is part of the Forest of Bowland Area of Outstanding Natural Beauty (AONB).

Edmund and Mary Ann Walworth Booth House: The Edmund and Mary Ann Walworth Booth House is a historic building located in Anamosa, Iowa, United States.  Raised in Longmeadow, Massachusetts, Edmund Booth contracted meningitis at age four and lost part of his hearing.  By the time he was eight he was totally deaf.  His wife Mary Ann was born in Connecticut and she was also four when she contracted meningitis, but lost all of her hearing at that time.  Booth became an early educator for the deaf, and his wife was one of his pupils.  They both relocated separately to Iowa in 1839, and married the following year.  After spending five years in the California gold fields while his family remained in Iowa, Booth returned to Iowa and resumed farming.  He was instrumental in establishing the Iowa School for the Deaf in 1855, and the Iowa Association of the Deaf in 1881.  He became the association's president in 1884.  Booth had a thirty-year career as the publisher and editor of the "Anamosa Eureka".  The Booth's had this brick Italianate house built in 1870.  They lived here until Mary Ann died in 1898 and Edmund in 1905.  It was listed on the National Register of Historic Places in 2001.

Christina River (Alberta): Christina River is a river in the Wood Buffalo region of northern Alberta, Canada.  It is a tributary of the Clearwater River.  Christina River is part of Christina Lake's 1250 km2 drainage basin.  Christina Lake's waters flow into the Jackson River, which flows 11 km before it empties into the Christina River.  Christina Lake and Christina River are named to honour Christine Gordon, originally from Scotland, who was the first white women to live permanently in the Fort McMurray area, where she remained until she died in the 1940s.

Hymns (Corey Glover album): Hymns is the first solo album by Living Colour vocalist Corey Glover, released on LaFace Records on April 7, 1998.

Booth Island: Booth Island (or Wandel Island) is a rugged, Y-shaped island, 5 mi long and rising to 980 m off the northwest coast of Kiev Peninsula in Graham Land, Antarctica in the northeastern part of the Wilhelm Archipelago.  Booth Island is located at .  Discovered and named by a German expedition under Eduard Dallmann 1873–74, probably for Oskar Booth or Stanley Booth, or both, members of the Hamburg Geographical Society at that time.  The Advisory Committee on Antarctic Names has rejected the name "Wandel Island", applied by the Belgian Antarctic Expedition —in honour of Danish polar explorer and hydrographer Carl Frederick Wandel, 1897–99, in favor of the original naming.  The narrow passage between the island and the mainland is the scenic Lemaire Channel.

Lavar Glover: Lavar Glover (born December 17, 1978 in Dayton, Ohio) is a former American football defensive back.  Most recently, Glover served as the Head Coach and General Manager of the Dayton Sharks of the Continental Indoor Football League.  He went to the University of Cincinnati and was drafted by the Pittsburgh Steelers (7th round, 212th overall) in the 2002 NFL Draft.  The Steelers released Glover and he was subsequently signed by the Cincinnati Bengals onto their practice squad.  He played 2 games with the Bengals in 2002 and spent time with the Detroit Lions and Denver Broncos.  In 2004, he played with the Columbus Destroyers and Orlando Predators of the Arena Football League.  There, Glover had 2 interceptions, 40 tackles and 3 pass knockdowns.  The BC Lions signed him as a free agent in 2006.  Lavar Glover had 2 interceptions and 29 tackles as part of the 2006 Grey Cup champion Lions team.  Now is a sub and in school suspension teacher at kettering middle school Ohio.

Joshua Glover: Joshua Glover was a fugitive slave from St. Louis, Missouri who sought asylum in Racine, Wisconsin in 1852.  Upon learning his whereabouts in 1854, slave owner Bennami Garland attempted to use the Fugitive Slave Act to recover him.  Glover was captured and taken to a Milwaukee jail.  A mob incited by Sherman Booth broke into the jail and rescued Glover, who then escaped to Canada via the Underground Railroad.  The rescue of Glover and the federal government's subsequent attempt to prosecute Booth helped to galvanize the abolitionist movement in the state that eventually led to Wisconsin becoming the only state to declare the Act unconstitutional.

Doug Grean: Doug Grean is an American record producer, audio engineer, guitarist, based in Los Angeles.  He has worked with artists Sheryl Crow, Ricki Lee Jones, Glen Campbell, Scott Weiland, Slash, Velvet Revolver, Stone Temple Pilots, The Crystal Method, Tim McGraw, Cyndi Lauper, Annabella Lwin (Bow Wow Wow), Corey Glover (Living Color), Camp Freddy, DJ Hurricane and John Taylor (Duran Duran).  Grean was formerly the lead guitarist and touring musical director for Scott Weiland and the Wildabouts.  Some of Grean's television appearances with Weiland include: VH1 Legends, Last Call with Carson Daly, The Tonight Show with Jay Leno, and the Grammy awards with Velvet Revolver as keyboardist, performing "All Across the Universe" with Stevie Wonder, Norah Jones, Bono, Steven Tyler, Brian Wilson, and Alison Krauss.

Question: What genre were both Christina Booth and Corey Glover a part of?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_music_genre": {
      "type": "string",
      "description": "The music genre that both artists are associated with."
    },
    "artists": {
      "type": "array",
      "description": "Details about the artists involved and their specific genres mentioned in the context.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the artist."
          },
          "specific_genre_mentioned": {
            "type": "string",
            "description": "The specific genre mentioned for this artist in the context."
          }
        },
        "required": [
          "name",
          "specific_genre_mentioned"
        ],
        "additionalProperties": false
      }
    },
    "genre_category": {
      "type": "string",
      "description": "A broader category for the common music genre, if applicable."
    }
  },
  "required": [
    "common_music_genre",
    "artists"
  ],
  "additionalProperties": false
}
