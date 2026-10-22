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
Summit League: The Summit League, or The Summit, is an NCAA Division I intercollegiate athletic conference with its membership mostly located in the Midwestern United States from Indiana and Illinois on the East of the Mississippi River to the Dakotas and Nebraska on the West, with additional members in the Western state of Colorado and the Southern state of Oklahoma.  Originally dubbed the Association of Mid-Continent Universities in 1982, on June 1, 2007, the conference changed its name from the Mid-Continent Conference.  League headquarters are in Elmhurst, Illinois.

Nebraska College Athletic Conference: The Nebraska College Athletic Conference (known as the Nebraska Intercollegiate Conference from 1916–1926) was an intercollegiate athletic conference that existed from 1916 to 1976.  The league had members, as its name suggests, in the state of Nebraska.  The public colleges in the conference departed for the separate Nebraska Intercollegiate Athletic Association (NIAA) in 1928 but re-joined after 1942.  The private colleges, in turn, broke away to form the Nebraska Intercollegiate Athletic Conference (now called the "Great Plains Athletic Conference") in 1969 and did not return before the NCAC folded in 1976.

NCAA Women's Water Polo Championship: The NCAA Women's Water Polo Championship has existed since the 2001 season.  Seven conferences have teams competing in women's water polo: the Big West Conference, the Collegiate Water Polo Association (CWPA), the single-sport Golden Coast Conference, the Metro Atlantic Athletic Conference (MAAC), the Mountain Pacific Sports Federation (MPSF), the Southern California Intercollegiate Athletic Conference (SCIAC) and the Western Water Polo Association (WWPA).  Some teams compete at Division III either as members of the Southern California Intercollegiate Athletic Conference or independently.

Don Maestri: Don Maestri (born October 25, 1946) is an American college basketball coach and the former head men's basketball coach at Troy University.  He held the same position from 1982 until 2013.  Prior to accepting this position, Maestri was an assistant coach at Mississippi State University from 1979 to 1980 and at the University of Alabama from 1980 to 1982.  Maestri coached the Trojans to a record of 500-404, one NCAA Basketball Tournament, five regular season conference titles, and one conference tournament title over the course of 26 seasons at Troy.  He has been named coach of the year in the East Coast Conference (1994), the Summit League (1997, then known as the Mid-Continent Conference), Atlantic Sun Conference (2000 and 2004) and the Sun Belt Conference (2009)

Central Intercollegiate Athletic Conference: The Central Intercollegiate Athletic Conference (CIAC) was an intercollegiate athletic conference that existed from 1928 to 1968.  The league had members in Kansas and Missouri.  Many of the league's members went on to form the Central States Intercollegiate Conference in 1976.

Great Plains Athletic Conference (NCAA): The Great Plains Athletic Conference (GPAC) was a collegiate athletic conference which operated in the western United States.  It was aligned with the Rocky Mountain Athletic Conference (RMAC).  The two allied conferences worked under the name of the Mountain and Plains Intercollegiate Athletic Association (MPIAA).  It was announced on May 15, 1972.  The founding schools were Fort Hays State; Kansas State College, Pittsburg; Kansas State College of Emporia; Southern Colorado State College; Nebraska-Omaha, Northern Colorado, and Washburn.  The conference only lasted four years, as Nebraska-Omaha and Northern Colorado left for the North Central Conference, Southern Colorado went back to the RMAC, and the rest of the schools started the Central States Intercollegiate Conference, which merged into the Mid-America Intercollegiate Athletics Association in 1989.

Michigan Intercollegiate Athletic Association: The Michigan Intercollegiate Athletic Association (MIAA) is an athletic conference that competes in the NCAA's Division III.  The nine teams in the conference are all located in the states of Michigan and Indiana.  The Michigan Intercollegiate Athletic Association was established on March 24, 1888, making it the oldest college athletic conference in the United States.  The current members of the MIAA include Adrian College, Albion College, Alma College, Calvin College, Hope College, Kalamazoo College, Olivet College, Saint Mary's College of Notre Dame, Indiana, and Trine University, formerly known as Tri-State University.  Olivet and Albion are the only charter members remaining in the conference.  Former members include such colleges as Michigan State University, previously Michigan Agricultural College, (1888–1907), Eastern Michigan University, previously Michigan State Normal College, (1892–1926), Hillsdale College (1888–1961), and Defiance College (1997–2000).

1956 Central Michigan Chippewas football team: The 1956 Central Michigan Chippewas football team was an American football team that represented Central Michigan College, renamed Central Michigan University in 1959, in the Interstate Intercollegiate Athletic Conference during the 1956 college football season.  In their sixth season under head coach Bill Kelly, the Chippewas compiled a perfect 9–0 record, won the Interstate Intercollegiate Athletic Conference (IIAC) championship for the fifth consecutive year, and outscored their opponents by a combined total of 313 to 92.  The team set multiple school records that still stand, including allowing 797 rushing yards (88.5 yards per game) and allowing only 1,292 net yards.  The 1956 season was part of the longest winning streak in school history, 15 games running from October 8, 1955, to November 10, 1956.

Great Plains Athletic Conference: The Great Plains Athletic Conference (GPAC) is a college athletic conference affiliated with the National Association of Intercollegiate Athletics (NAIA).  Member institutions are located in Iowa, Nebraska and South Dakota.  The conference was founded in 1969 as the Nebraska Intercollegiate Athletic Conference, later becoming the Nebraska-Iowa Athletic Conference (1992) before being renamed the Great Plains Athletic Conference (2000).

Leo Richardson: Leo Richardson is a former American basketball and football coach.  Richardson was the head basketball coach at Savannah State University from 1964 to 1971, and the University at Buffalo from 1973 to 1978.  He compiled an overall basketball coaching record of 146–176.  Richardson led the Savannah State basketball team to a Southern Intercollegiate Athletic Conference conference tournament title in 1970, for which he was named coach of the year.  He was the University at Buffalo's first African American head basketball coach.  He also served as the head football coach at Savannah State from 1964 to 1968, compiling an overall football record of 13–25–2.  Richardson was elected to the Savannah State University Sports Hall of Fame in 2010.

Question: What year was Don Maestri named coach of the year in the intercollegiate athletic conference headquartered in Elmhurst, Illinois?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "coach_name": {
      "type": "string",
      "description": "The name of the coach."
    },
    "award_received": {
      "type": "string",
      "description": "The specific award received by the coach."
    },
    "award_year": {
      "type": "integer",
      "description": "The year the coach received the award."
    },
    "conference_details": {
      "type": "object",
      "properties": {
        "conference_name": {
          "type": "string",
          "description": "The current name of the conference."
        },
        "former_conference_name": {
          "type": "string",
          "description": "The name of the conference at the time the award was given, if different."
        },
        "headquarters_location": {
          "type": "object",
          "properties": {
            "city": {
              "type": "string",
              "description": "The city where the conference headquarters is located."
            },
            "state": {
              "type": "string",
              "description": "The state where the conference headquarters is located."
            }
          },
          "required": [
            "city",
            "state"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "conference_name",
        "former_conference_name",
        "headquarters_location"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "coach_name",
    "award_received",
    "award_year",
    "conference_details"
  ],
  "additionalProperties": false
}
