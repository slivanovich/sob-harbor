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
2009 NBA draft: The 2009 NBA draft was held on June 25, 2009, at the WaMu Theatre at Madison Square Garden in New York City.  In this draft, the National Basketball Association (NBA) teams took turns selecting amateur U.S. college basketball players and other eligible players, including international players.

Madison Square Garden Towers: The Madison Square Garden Towers were the name of proposed twin 1400 ft residential skyscrapers that were to be constructed north of Madison Square Garden in Midtown Manhattan, New York City.  The project featured a complex of seven buildings, including a stadium and a new Penn Station.  The cost of the project was US$14 billion.  The architects Norman Foster and David Childs, and the architectural firm Skidmore, Owings and Merrill were designing the project.  The owners were Stephen Ross of Related Cos. and Steven Roth of Vornado Realty Trust.  The towers would have risen to be two of the tallest structures in the Midtown Manhattan skyline, with one rising higher than the Empire State Building, currently one of New York's tallest buildings at 1,250 feet (381 m) and would also have been higher than the roof, though not the spire, of One World Trade Center.  The towers are essentially canceled as Madison Square Garden is going ahead with renovations of the current arena, rather than a relocation that would have made the towers possible.

Gerald Henderson Jr.: Jerome McKinley "Gerald" Henderson Jr. (born December 9, 1987) is an American professional basketball player who last played for the Philadelphia 76ers of the National Basketball Association (NBA).  Henderson played college basketball for the Duke Blue Devils.  He was drafted with the 12th overall pick in the 2009 NBA draft by the Charlotte Bobcats.

2016–17 Philadelphia 76ers season: The 2016–17 Philadelphia 76ers season is the 78th season of the franchise in the National Basketball Association (NBA).  The 2016–17 season would have been the rookie season for number 1 overall pick in the 2016 NBA draft Ben Simmons, but a broken foot injury sidelined him for the whole season.  It would be the team's fourth straight season where a top prospect of theirs would be sidelined for an entire season due to an injury (the 76ers previously dealt with former center Nerlens Noel being out in the 2013–14 NBA season and Joel Embiid being out for two straight seasons before this one).  However, Joel Embiid, who was previously drafted 3rd in the 2014 draft, played in his first season after suffering multiple foot injuries before later being out for the rest of the season after playing a promising 31 games throughout the season.  Also, it was the first season of draft and stash prospect Dario Šarić, who was also taken in the 2014 NBA draft.  The 2016 season was also the first time in three years the Sixers made a splash in NBA free agency by adding guards Jerryd Bayless, Sergio Rodríguez and veteran Gerald Henderson Jr. to the team.

Jammy Award: The Jammy Award (also known as the Jammys) are an awards show for bands typically called jam bands and other artists associated with live, improvisational music, created by Dean Budnick and Peter Shapiro.  The Jammys are sponsored by Relix magazine, Jambands.com, and Shapiro.  The Jammy Awards returned in 2008 to the WAMU Theater at Madison Square Garden in New York City.

The King Stays King: The King Stays King (also known as Formula, Vol.  1 Tour) is an ongoing worldwide concert tour by American singer Romeo Santos.  The tour was a promotion for his debut solo album, "Formula, Vol.  1".  On December 13, 2011, Santos announced that he would begin his initial leg of his solo tour on February 11, 2012, in the United States.  His first concert began with two consecutive shows at Madison Square Garden which became sold-out twice.  During the concert at Madison Square Garden, Santos was accompanied by fellow American bachata singer-songer Prince Royce.  For "Debate de 4", three men from the audience were randomly selected to join Santos on the song.  Usher made an appearance on the encore for the duet "Promise".  At the final concert in the Madison Square Garden, Santos was joined by American rapper P. Diddy for the song "Mi Corazoncito".  The concerts at Madison Square Garden were recorded and later released as a live album titled "" on November 6, 2012.

Madison Square Garden (1890): Madison Square Garden was an indoor arena in New York City, the second by that name, and the second to be located at 26th Street and Madison Avenue in Manhattan.  Built in 1890 at the cost of a half-million dollars and closing in 1925, the arena hosted numerous events, including boxing matches, orchestral performances, light operas and romantic comedies, the annual French Ball, both the Barnum and the Ringling circuses, and the Democratic National Convention in 1924, which nominated John W. Davis after 103 ballots.  The 1890 version replaced the first Madison Square Garden, and was itself replaced by the third Madison Square Garden (which was the first to be located away from Madison Square).

Wintuk: Wintuk (pronounced "win-took"; amalgamating the English word "winter" with Inupiaq phonetics) was a semi-permanent and seasonal residency show created by Cirque du Soleil.  "Wintuk" played seasonally at the Theater at Madison Square Garden (formerly the WaMu Theater) entertainment complex in New York.

Elena Lev: Elena Lev, born in Moscow, Russia in 1981, began her training to become a rhythmic gymnast at an early age, assisted and coached by her mother, Elena Lev Sr.  She developed a signature hula hoop act incorporating gymnastics and contortion.  Her big breakthrough came when she was invited to join the "Alegría" touring troupe of Cirque du Soleil, of which she was a member from 1994 through 2000.  She also performed briefly with the "Quidam" troupe in 2002.  Lev performed with Cirque du Soleil's "Wintuk" at the WaMu Theater at Madison Square Garden in New York City.

Madison Square Garden: Madison Square Garden, often called "MSG" or simply "The Garden", is a multi-purpose indoor arena in the New York City borough of Manhattan.  Located in Midtown Manhattan between 7th and 8th Avenues from 31st to 33rd Streets, it is situated atop Pennsylvania Station.  It is the fourth venue to bear the name "Madison Square Garden", the first two (1879 and 1890) of which were located on Madison Square, on East 26th Street and Madison Avenue, with the third Madison Square Garden further uptown at Eighth Avenue and 50th Street.  The Garden is used for professional basketball and ice hockey, as well as boxing, concerts, ice shows, circuses, professional wrestling and other forms of sports and entertainment.  It is close to other midtown Manhattan landmarks, including the Empire State Building, Koreatown, and Macy's at Herald Square.  It is home to the New York Rangers of the National Hockey League (NHL), the New York Knicks of the National Basketball Association (NBA), and since 1997, the New York Liberty (WNBA).

Question: Gerald Henderson Jr. was selected with the 12th overall pick in which event held at the WaMu Theater at Madison Square Garden?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "event_name": {
      "type": "string",
      "description": "The name of the event where the player was drafted."
    },
    "event_location": {
      "type": "string",
      "description": "The specific venue where the event took place."
    },
    "event_date": {
      "type": "string",
      "description": "The date the event was held."
    },
    "player_draft_details": {
      "type": "object",
      "properties": {
        "player_name": {
          "type": "string",
          "description": "The name of the player drafted."
        },
        "draft_year": {
          "type": "integer",
          "description": "The year of the draft."
        },
        "overall_pick_number": {
          "type": "integer",
          "description": "The overall pick number of the player."
        },
        "drafting_team": {
          "type": "string",
          "description": "The team that drafted the player."
        }
      },
      "required": [
        "player_name",
        "draft_year",
        "overall_pick_number",
        "drafting_team"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "event_name",
    "event_location",
    "event_date",
    "player_draft_details"
  ],
  "additionalProperties": false
}
