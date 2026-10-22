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
Lupin Mine: Lupin Mine was a gold mine in Nunavut Territory, Canada.  It opened in 1982 and was originally owned and operated by Echo Bay Mines Limited, who in 2003 became a fully owned subsidiary of Kinross Gold Corporation.

Jackson Mine: The Jackson Mine is an open pit iron mine in Negaunee, Michigan, extracting resources from the Marquette Iron Range.  The first iron mine in the Lake Superior region, Jackson Mine was designated as a Michigan State Historic Site in 1956 and listed on the National Register of Historic Places in 1971.  The Lake Superior Mining Institute said, the mine "is attractive in the iron ore region of Michigan and the entire Lake Superior region, because of the fact it was here that the first discovery of iron ore was made, here the first mining was done, and from its ore the first iron was manufactured."  Multiple other mines soon followed the Jackson's lead, establishing the foundation of the economy of the entire region.  The mine is located northwest of intersection of Business M-28 and Cornish Town Road.

Lupin Airport: Lupin Airport (IATA: YWO, ICAO: CYWO) was an airport located at Lupin Mine, Nunavut, Canada that was operated by Echo Bay Mines Limited.  The airport closed sometime after the mine closed in 2005, but the runway is still present on the property.

List of lost mines: Lost mines are a popular form of lost treasure legend.  The mine involved is usually of a high-value commodity such as gold, silver or diamonds.  Often there is a map (sometimes called a "waybill") purportedly showing the location of the mine.  Common reasons given for the mines being lost include:

Burra Burra Mine (Tennessee): The Burra Burra Mine is a copper mine located in Ducktown, Tennessee, in the southeastern United States.  Named for the famous mine in Australia, the Burra Burra Mine extracted over 15 million tons (14 million metric tons) of copper ore during its 60 years of operation between 1899 and 1959.  The mine's remaining structures are listed on the National Register of Historic Places as part of the Burra Burra Mine Historic District.  The site is also home to the Ducktown Basin Museum, and the museum and mine are a Tennessee State Historic Site operated in partnership with the Tennessee Historical Commission.

Wopkaimin people: The Wopkaimin are a small aboriginal tribe that lives in the remote Star Mountains in western Papua New Guinea in what is known as the Fly River socio-ecological region.  The tribe speaks Faiwol.  The Ok Tedi Mine, the third largest open pit copper and gold mine in the world is located in their traditional territory.  Before the coming of the mine with construction starting in 1981 the Wopkaimin lived in a subsistence economy.  The mine severely impacted the tribe, totally disrupting their traditional patterns of life.  For one thing, Tabubil a town of 12,500 to house mine workers was built in the midst of their territory.  Work for wages was available to tribal members, but only at the unskilled level and not on a regular basis.  The Wopkaimin along with many other ethnic groups living in the area now live on a rotating basis between the town of Tabubil, roadside villages along the Kiunga-Tabubil Highway, and in villages away from the mine as jobs are lost or become available.

Gahcho Kue Diamond Mine Project: The Gahcho Kué Diamond Mine is located on the Canadian tundra in the Northwest Territories.  It is situated at Kennady Lake ( ), in the Akaitcho Treaty 8 Territory AK claim block, which is 85 km southeast of the Snap Lake Diamond Mine and approximately 280 km east northeast of Yellowknife.  The site is served by Gahcho Kue Aerodrome, which has both an ice runway in winter and a year-round gravel runway, and a spur of the Tibbitt to Contwoyto Winter Road from Lupin Mine.  the main camp is at , north of the ice strip, with a smaller site at , south of the runway.

Hollywood, Raleigh County, West Virginia: Hollywood was an unincorporated community located in Raleigh County, West Virginia .  Its Post Office no longer exists.  There is also a Hollywood in Monroe County, West Virginia.  Hollywood was renamed to MacArthur in 1942.  However, it was a distinct mining community with its own coal mines see mine map 336094, located in Beckley.  MacArthur used different mines see mine map 335329.

Lost Lemon Mine: The Lost Lemon Mine is a legendary lost mine said to be located in the Canadian Province of Alberta.  The story has been retold in countless books with the authoritative version being "The Lost Lemon Mine" by Tom Primrose.The story first appeared in the 1946 edition of the "Alberta Folklore Quarterly" and later in magazines such as "Canada West".  The Lost Lemon Mine has also been featured in television documentary series "Northern Mysteries", and worked into the plot of "The Final Sacrifice".  Countless people have searched for the mine.  A number of searchers have never returned.

Treasure map: A treasure map is a map that marks the location of buried treasure, a lost mine, a valuable secret or a hidden locale.  More common in fiction than in reality, "pirate treasure maps" are often depicted in works of fiction as hand drawn and containing arcane clues for the characters to follow.  Regardless of the term's literary use, anything that meets the broad definition of a "map" that describes the location of a "treasure" could appropriately be called a "treasure map."

Question: Are Lupin Mine and Lost Lemon Mine both places that can be located on a map?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "mines_compared": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "mine_name": {
            "type": "string",
            "description": "The name of the mine."
          },
          "is_locatable_on_map": {
            "type": "boolean",
            "description": "Indicates whether the mine can be located on a map based on the context."
          },
          "reason_for_locatability": {
            "type": "string",
            "description": "Explanation for why the mine is or is not locatable."
          }
        },
        "required": [
          "mine_name",
          "is_locatable_on_map",
          "reason_for_locatability"
        ],
        "additionalProperties": false
      }
    },
    "all_mines_locatable": {
      "type": "boolean",
      "description": "True if all specified mines can be located on a map, false otherwise."
    },
    "comparison_summary": {
      "type": "string",
      "description": "A brief summary of the comparison result."
    }
  },
  "required": [
    "mines_compared",
    "all_mines_locatable",
    "comparison_summary"
  ],
  "additionalProperties": false
}
