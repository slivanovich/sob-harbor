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
Al Coury: Albert Eli "Al" Coury (October 21, 1934 – August 8, 2013) was an Lebanese-American music record executive during the 1970s, vice-president of American record label Capitol Records and co-founder of RSO Records.  He joined Capitol Records in 1957 and rose to the position of vice-president of marketing, sales and promotion.  Coury helped develop the careers of many recording artists, including The Beatles, Nat King Cole, The Beach Boys, Pink Floyd, Glen Campbell, Bob Seger, Guns N' Roses, Aerosmith, Don Henley, Cher and Linda Ronstadt.

Capitol Riverfront: The Capitol Riverfront is a business improvement district (BID) located just south of the United States Capitol between Capitol Hill and the Anacostia River in Washington, D.C. It was created by the District of Columbia City Council and approved by Mayor Fenty in August 2007.  The BID is a mixed-use neighborhood.  It was a former industrial area that is being transformed into a business center, urban neighborhood, entertainment district and waterfront destination.  The project involves adding over 9,000 new apartments, condominiums and lofts, modern office towers, 1,200 hotel rooms, one million square feet of retail amenities including a two future grocery stores, new restaurants, shops, and cafes.  Over 33,900,000 square feet (3,150,000 m2) of new office, residential, hotel and retail space as well as four new parks are planned over the next 10–15 years.  The new 5 acre riverfront Yards Park opened in fall 2010.

Capitol Records Building: The Capitol Records Building, also known as the Capitol Records Tower, is a Hollywood Boulevard Commercial and Entertainment District building that is located in Hollywood, Los Angeles.  The building is a thirteen-story tower that was designed by Louis Naidorf (who was working at Welton Becket Associates at the time), and is one of the city's landmarks. Construction occurred soon after British company EMI acquired Capitol Records in 1955, and was completed in April 1956.  Located just north of the Hollywood and Vine intersection, the Capitol Records Tower houses the consolidation of Capitol Records' West Coast operations and is also home to the recording studios and echo chambers of Capitol Studios.  The building is a Los Angeles Historic-Cultural Monument.

Tonight, I Celebrate My Love: "Tonight, I Celebrate My Love" is a song written by Gerry Goffin and Michael Masser recorded as a duet single by Peabo Bryson and Roberta Flack and released in 1983.  It became a big hit for both singers, peaking at number sixteen on the "Billboard" Hot 100, number five on the Hot Black Singles chart, and number four on the Adult Contemporary chart.  In the UK, the song peaked at number two in September 1983.  In addition to becoming the biggest British hit for both Bryson and Flack, the song boosted the careers of both stars and brought them both a return to prominence.  Capitol Records' Bob Hart asked Martin Pitts to Direct the official video through One Heart Productions.  The video was a performance with the original band in the background at the Capitol studios on Vine Street in Hollywood.

Turner's Arena: Turner's Arena was the name given to a 2,000 seat arena, located near the northeast corner of 14th and W Streets, NW in Washington, DC, and originally owned by local wrestling promoter Joe Turner.  This venue was an early home to the Capitol Wrestling Corporation, a precursor to World Wrestling Entertainment, which was started by Vincent J. McMahon in January 1953.  McMahon took over the territory from Gabe Menendez, who had succeeded Turner after his death in 1947.  In addition, the arena hosted top professional boxing matches promoted by Goldie Ahearn featuring fighters such as Lou Gevinson, Lew Hanbury, and Jimmy Cooper.  It was also the birthplace of the Central Intercollegiate Athletic Association annual basketball tournament, as well as the host to top country music acts and Jazz performances.  It was renamed Capitol Arena in 1956 once Capitol Wrestling Corporation began broadcasting a syndicated weekly wrestling show from the arena every Thursday night.

Miss Hit and Run: "Miss Hit and Run" is a song written by Lynsey de Paul and Barry Blue.  Blue released the single in 1974 as a follow up single to "School Love" on Bell Records and recorded it with a "Beach Boys" type of arrangement.  The song was Blue's fourth consecutive hit, reaching number 26 on the UK Singles Chart in August 1974.  It also reached number 9 on Capitol Radio's "Capitol Countdown" chart.  It was also a track on the K-Tel album, "Music Explosion".  Notable TV performances of the song included appearances on 10 August 1974 on "TopPop", the Dutch pop music program as well as on the BBC programme "Top of the Pops".  It was re-released by Blue as the B-side to "Do You Wanna Dance" in 1980.

Careers (board game): Careers is a board game first manufactured by Parker Brothers in 1955 for $2.97 US, and was most recently produced by Winning Moves Games.  It was devised by the sociologist James Cooke Brown.  Victory conditions (a secret "Success Formula") consist of a minimum amount of fame, happiness and money that the player must gain.  Players (from two to six) set their own victory conditions before the game begins, the total of which must be sixty (or one hundred, recommended when only two are playing).

Capitol (board game): Capitol is a German-style building game set in the ancient Roman Empire, designed by Aaron Weissblum and Alan R. Moon.  The game was published by Schmidt Spiele in 2001.  It was redeveloped into a quicker-playing card game named "Clocktowers" and published by Jolly Roger Games.

Capitol Music Group: Capitol Music Group (abbreviated as CMG) is an American front line umbrella label owned by the Universal Music Group (UMG).  It oversees handling of record labels assigned to UMG's Capitol Records division and were inherited from its acquisition of EMI's catalog (save for Parlophone, which was sold to Warner Music Group (WMG) in 2013).  It is one of five umbrella labels owned by UMG, with the other four being Interscope Geffen A&M, Island Records, Def Jam Recordings and Republic Records.  Labels distributed under the CMG brand include Capitol Records, Virgin Records, Motown Records, Blue Note Records, Astralwerks, Harvest Records, Capitol Christian Music Group, Priority Records, Atom Factory Entertainment and Deep Well Records.

Don Li: Don Li Yat-long is a Hong Kong singer and actor of the Emperor Entertainment Group, Music Icon Records.  Don Li was a finalist in Talent Show 2002 in Hong Kong.  In 2003, he began his career in the entertainment industry by acting in television series.  In 2005, Li and Mandy Chiang began their music careers as a duet couple.  In January 2007, Chiang announced that she and Li will both continue their music careers as solo artists.

Question: Careers and Capitol, are which type of entertainment?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entertainment_type": {
      "type": "string",
      "description": "The general category of entertainment."
    },
    "entertainment_items": {
      "type": "array",
      "description": "Details about each specific entertainment item.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the entertainment item."
          },
          "description_snippet": {
            "type": "string",
            "description": "A brief description of the item from the context."
          }
        },
        "required": [
          "name",
          "description_snippet"
        ],
        "additionalProperties": false
      }
    },
    "number_of_items": {
      "type": "integer",
      "description": "The total number of entertainment items identified."
    }
  },
  "required": [
    "entertainment_type",
    "entertainment_items",
    "number_of_items"
  ],
  "additionalProperties": false
}
