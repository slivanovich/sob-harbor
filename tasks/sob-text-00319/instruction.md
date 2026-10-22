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
Development of Deus Ex: An approximately 20-person team at Ion Storm developed "Deus Ex", a cyberpunk-themed action-role playing video game, over the course of 34 months, culminating in a June 2000 release.  Team director and producer Warren Spector began to plan the game in 1993 after releasing "" with Origin Systems and attempted the game both there and at Looking Glass Technologies before going into production with Ion Storm.  Official preproduction began around August 1997, lasted for six months, and was followed by 28 months of production.  Spector saw their work as expanding on the precedent set by Origin, Looking Glass, and Valve Corporation.

Liz Phair (album): Liz Phair is the fourth studio album by American singer-songwriter Liz Phair, released June 24, 2003 on Capitol Records. " Why Can't I? " and "Extraordinary" were released as singles.  Phair began production on the album with Michael Penn.  "Liz Phair" debuted at #27 on the "Billboard" 200.  As of July 2010, the album had sold 433,000 copies.

Michael Penn: Michael Penn (born August 1, 1958) is an American singer, songwriter, and composer.  He is noted for the 1989 single "No Myth", a top 20 hit in the US and successful in several other countries.

Blanco family (Oaxacan potters): The Blanco family of Santa María Atzompa, Oaxaca, Mexico is noted for their ceramic production, especially decorative pieces.  Their fame began with Teodora Blanco, who as a young child added decorative elements to the more utilitarian wares made by her parents.  Eventually her work became noted by a foreigner who not only bought her entire production, also encouraged her to create new forms, leading to mostly human figures called “muñecas” (lit.  dolls).  Her form of decoration, called “pastillaje,” was also an innovation for the area’s pottery and consists of small pieces of clay added onto the main surfaces, often covering much of the area.  Teodora taught her children and although she intended that only the oldest daughter carry on her work, today three generations of the family continues making mostly decorative pottery, mostly following her work.  These include Irma García Blanco, who have been recognized by the Fomento Cultural Banamex and Fernando Félix Pegüero García, who has won prizes from the Friends of Oaxacan Folk Art in New York and Premio Nacional de Cerámica in Tlaquepaque, Jalisco.

It Takes a Nation of Millions to Hold Us Back: It Takes a Nation of Millions to Hold Us Back is the second studio album by American hip hop group Public Enemy, released on June 28, 1988, by Def Jam Recordings.  Public Enemy set out to make the hip hop equivalent to Marvin Gaye's "What's Going On", an album noted for its strong social commentary.  Recording sessions took place during 1987 at Chung King Studios, Greene St. Recording, and Sabella Studios in New York City.  Noting the enthusiastic response toward their live shows, Public Enemy intended with "Nation of Millions" to make the music of a faster tempo than the previous album for performance purposes.

Soak Up the Sun: "Soak Up the Sun" is the title of a song recorded by American artist Sheryl Crow.  It was released in March 2002 as the lead single from her album "C'mon C'mon".  The song, which features backing vocals by Liz Phair, peaked at number-one on the "Billboard" Adult Top 40 chart and hit number 5 on the Hot Adult Contemporary Tracks chart and #17 on the Hot 100 chart.  In addition, "Soak Up the Sun" (remixed by noted DJ Victor Calderone) spent one week at #1 on the "Billboard" Hot Dance Club Play chart in June 2002; to date, this is Crow's only song to top this chart.  It reached #16 on the UK Singles Chart.  It was covered by the Kidz Bop Kids in 2003.  The song was also included on the album "Nolee Mix" which was released to promote the My Scene dolls.  The song was a staple of radio airplay during the summer of 2002.

L.A. (Neil Young song): "L.A." is a song written and performed by Neil Young from the 1973 album "Time Fades Away", a live album noted for its abrasive experimentation and its "wild, agonized, deliberately jarring" vocals.

Foreign Born: Foreign Born is an American folk rock band.  They began in San Francisco during the late summer months of 2003, but soon relocated to Los Angeles.  They self-released their first 12" single ("We Had Pleasure" b/w "Escape"), and then their debut EP "In the Remote Woods" via StarTime International Records.  While touring the US and UK with Rogue Wave, Jason Collett, Cold War Kids, Giant Drag and We Are Scientists, they recorded their first full-length album, "On the Wing Now", in the fall/winter of 2005, self-released 500 or so copies that they sold on the previously mentioned tours, and officially released the album with Dim Mak on August 21, 2007.  They were featured in "Spin Magazine" in October 2007.  They released their latest album, "Person to Person", on June 23, 2009, under the record label Secretly Canadian.  As of August 2011, the band is on indefinite hiatus.

Brad Wood: Brad Wood is an American record producer.  He served as a drummer for the band Shrimp Boat.  He records, mixes and produces records and is based in Los Angeles, California.  He began his production career in 1988 with the launch of Idful Music Corporation, a recording studio in Chicago's Wicker Park.  While there he recorded and produced hundreds of records, including Liz Phair's "Exile in Guyville", Ben Lee's "Grandpa Would", Sunny Day Real Estate's "Diary" and "LP2", Red Red Meat, Seam, That Dog, and many more.  After relocating to Los Angeles, Brad has continued to work primarily from his Seagrass Studio in Valley Village on recordings by mewithoutYou, Say Anything, Pete Yorn, and Dar Williams.  He is from Rockford, Illinois.

Bollywood (Liz Phair song): "Bollywood" is a song by American recording artist Liz Phair.  The song was her first release after breaking from Capitol Records and Dave Matthews' record label, ATO Records, and discusses the discrimination and bureaucracy present in the music industry.  It was released as the lead single from her sixth album, "Funstyle", and was subject to negative reviews from critics, who criticized Phair's vocal performance and the production.

Question: For what was the person with which Phair began the production on his album noted?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person involved in the album production."
    },
    "role_in_album_production": {
      "type": "string",
      "description": "The role of the person in the production of Liz Phair's album."
    },
    "noted_for_work": {
      "type": "string",
      "description": "The specific work for which the person is noted."
    },
    "work_details": {
      "type": "object",
      "properties": {
        "release_year": {
          "type": "integer",
          "description": "The release year of the noted work."
        },
        "work_type": {
          "type": "string",
          "description": "The type of the noted work (e.g., single, album)."
        },
        "chart_performance": {
          "type": "string",
          "description": "Details about the chart performance of the noted work."
        }
      },
      "required": [
        "release_year",
        "work_type",
        "chart_performance"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "role_in_album_production",
    "noted_for_work",
    "work_details"
  ],
  "additionalProperties": false
}
