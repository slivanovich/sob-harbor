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
2012–13 Utah Utes men's basketball team: The 2012–13 Utah Utes men's basketball team represented the University of Utah during the 2012–13 NCAA Division I men's basketball season.  They play their home games at the Jon M. Huntsman Center in Salt Lake City, Utah, and were a member of the Pac-12 Conference.  They were led by their second year head coach Larry Krystkowiak.  They finished the season 15–18, 5–13 in Pac-12 play to finish in tenth place.  They advanced to the semifinals of the Pac-12 Tournament where they lost to Oregon.

Utah Utes men's basketball: The Utah Utes men's basketball team represents the University of Utah as an NCAA Division I program that plays in the Pac-12 Conference.  They are currently led by head coach Larry Krystkowiak and play their home games at the Jon M. Huntsman Center.  The school has made the NCAA Tournament 27 times, which ranks 20th in NCAA history and tied for 3rd behind UCLA and the University of Arizona in the Western United States.  They last made the tournament in 2016.  Utah won the NCAA Championship in 1944, defeating Dartmouth College 42–40 for the school's only NCAA basketball championship.  However, the school also claims the 1916 AAU National Championship, which was awarded after winning the AAU national tournament.  They have also won the NIT once, defeating Kentucky in 1947.  In 1998 the Utes played in the NCAA championship game, losing to Kentucky.

2010–11 Utah Utes men's basketball team: The 2010–11 Utah Utes men's basketball team represented the University of Utah.  They played their home games at the Jon M. Huntsman Center in Salt Lake City, Utah, United States and were a member of the Mountain West Conference.  They finished the season 13–18, 6–10 in Mountain West play and lost in the quarterfinals of the 2011 Mountain West Conference Men's Basketball Tournament to San Diego State.  On March 12, 2011, the University of Utah fired head coach Jim Boylen after consecutive losing seasons.  Starting in July 2011, they will be leaving the Mountain West Conference and will join the Pac-12.  Their leading scorer Will Clyburn was granted a scholarship release at the end of the season and subsequently transferred to Iowa State.

1997–98 Utah Utes men's basketball team: The 1997–98 Utah Utes men's basketball team represented the University of Utah during the 1997–98 men's basketball season.

Shawn Glover: Shawn Glover (born September 25, 1990) is an American basketball player who currently plays for Ironi Kiryat Ata.  He competed with the Oral Roberts Golden Eagles men's basketball team in his final years of college, initially playing for the Utah Utes men's basketball program.  Glover was named First Team All-Southland in 2014 after being one of the top scorers in the NCAA and making school history.

2013–14 Utah Utes women's basketball team: The 2013–14 Utah Utes women's basketball team will represent the University of Utah during the 2013–14 NCAA Division I men's basketball season.  They will play their home games at the Jon M. Huntsman Center in Salt Lake City, Utah and are a member of the Pac-12 Conference.  The Utes are led by their fourth year head coach Anthony Levrets.  They finished with a record of 12–19 overall, 4–14 in Pac-12 play for an eleventh-place finish.  They lost in the quarterfinals in the 2014 Pac-12 Conference Women's Basketball Tournament to Oregon State.

Larry Krystkowiak: Larry Brett Krystkowiak ( ; born September 23, 1964) is a retired American professional basketball player, and current head coach of the Utah Utes men's basketball team.

2013–14 Utah Utes men's basketball team: The 2013–14 Utah Runnin' Utes men's basketball team represented the University of Utah during the 2013–14 NCAA Division I men's basketball season.  They played their home games at the Jon M. Huntsman Center in Salt Lake City, Utah and were a member of the Pac-12 Conference.  The Utes were led by their third year head coach Larry Krystkowiak.  Their last game was played in the first round of the NIT, where they lost to the Saint Mary's Gaels.

2009–10 Utah Utes men's basketball team: The 2009–10 Utah Utes men's basketball team represented the University of Utah.  They played their home games at the Jon M. Huntsman Center in Salt Lake City, Utah, United States, and were a member of the Mountain West Conference.  The Utes were led by third-year head coach Jim Boylen.  They finished the season 14–17 (7–9 in Mountain West play) and lost in the quarterfinals of the 2010 Mountain West Conference Men's Basketball Tournament to UNLV.

2011–12 Utah Utes men's basketball team: The 2011–12 Utah Utes men's basketball team represents the University of Utah.  They play their home games at the Jon M. Huntsman Center in Salt Lake City, Utah, and are a member of the Pac-12 Conference.  They are led by their first-year head coach Larry Krystkowiak.  They finished with a record of 6-25 overall, 3-15 in Pac-12 play and lost in the first round of the 2012 Pac-12 Conference Men's Basketball Tournament by Colorado.

Question: Which retired American professional basketball player led   2013–14 Utah Utes men's basketball team 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "coach_name": {
      "type": "string",
      "description": "The name of the head coach."
    },
    "team_season": {
      "type": "string",
      "description": "The specific basketball season for the team."
    },
    "coach_role": {
      "type": "string",
      "description": "The role of the individual with the team."
    },
    "is_retired_pro_player": {
      "type": "boolean",
      "description": "Indicates if the coach is a retired American professional basketball player."
    }
  },
  "required": [
    "coach_name",
    "team_season",
    "coach_role",
    "is_retired_pro_player"
  ],
  "additionalProperties": false
}
