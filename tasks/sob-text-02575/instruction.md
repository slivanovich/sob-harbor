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
Don Friday: Don Friday (born April 17, 1968) is an American college basketball coach, and the former men's basketball head coach at Saint Francis University, being named to the post in April 2008.  He previously served as head coach at Lycoming College (2003–2008), assistant coach at Bucknell University (1994–2003), and assistant coach at Lebanon Valley College (1990–1994).  At Lebanon Valley and Bucknell, he coached under Pat Flannery, and in 1994 he assisted Flannery as Lebanon Valley won the 1994 Division III National Championship.  He was the MAC coach of the year twice as the men's head coach at Lycoming University.  Friday has a true knowledge of the game.  In 2012, he was forced out of his job at Saint Francis and in the following hours after his firing his assistant Rob Krimmel son of athletic director got the job with no nationwide search or interview of any other coaches, this led to a controversy of nepotism in which the hiring of a family member.  After his release at Saint Francis Friday was hired by Head Coach Frank Marcinek at Susquehanna University after that brief stop Friday is now The Head Coach at Penn State Harrisburg and is turning the program around.  This past year Friday captured a win on number 15th ranked Christopher Newport, one of the biggest upsets in program history.  Friday earned Bachelor's degree in Business from Lebanon Valley College.  He currently resides in Annville with his son Donald and wife Amy.  Friday also holds elite clinics and coaches clinics to help coaches and players perform at the best of their ability.

Keith Freeman: Keith Freeman (born December 11, 1963) is an assistant coach of the women's basketball team at Wright State University.  He is the former women's basketball program head coach at Valparaiso University.  Freeman, the sixth head coach in the history of the Valparaiso University Crusader women’s basketball program, was hired as the head coach before the 1994–1995 season.  Freeman also served as the head women's basketball coach at Saint Joseph's College in Rensselaer, Indiana, from 1990–1994, and was the Great Lakes Valley Coach of the Year in 1992.  Prior his tenure at Saint Joseph's, Freeman was the head men's basketball coach at Huntington (Ind.) College from 1985 to 1989.  Freeman took over the Huntington program at age 21, making him one of the youngest college coaches in the nation.  Freeman began coaching at the age of 19 when he was named the head women's basketball coach at Huntington, serving from 1983 to 1985.

Lafayette College: Lafayette College is a private liberal arts college based in Easton, Pennsylvania, with a campus in New York City, NY.  The school, founded in 1826 by James Madison Porter, son of General Andrew Porter of Norristown, and the citizens of Easton, first began holding classes in 1832.  The founders voted to name the school after General Lafayette, who famously toured the country in 1824–25, as "a testimony of respect for [his] talents, virtues, and signal services... in the great cause of freedom".

Danny Miles: Danny Miles (born October 9, 1945) is an American former basketball coach.  He served as the head men's basketball coach at Oregon Institute of Technology from 1971 to 2016.  He achieved his one thousandth win on February 1, 2014, in his 43rd year of coaching at OIT.  This is the fourth most of any college basketball coach all-time (NCAA & NAIA).  The only four other coaches at a four-year school with 1,000 or more wins are Pat Summitt, former coach of the Tennessee Lady Volunteers basketball, Harry Statham, coach of McKendree University, Mike Krzyzewski, coach of Duke University, and Herb Magee, coach of Philadelphia University.

Mike Legarza: Mike Legarza is an American basketball coach and entrepreneur, currently the Director of Legarza Basketball Camps, which is the largest day basketball camp in the country, over 100,000 players have attended.  Legarza also wrote coaching curriculum for the Positive Coaching Alliance at Stanford University.  These coaching techniques have been taught in all 50 states to over three million youth athletes.  A former college basketball coach, Legarza was named the California Community College State Coach of the Year.  In March 2012 Coach Mike Legarza was inducted into the California Community College Coaches Hall of Fame.  In 2012 Mike Legarza was inducted into the Reno High School Athletic Hall of Fame as a player for Basketball and Football.

Tara VanDerveer: Tara Ann VanDerveer (born June 26, 1953) is an American basketball coach who has been the head women's basketball coach at Stanford University since 1985.  Designated the Setsuko Ishiyama Director of Women's Basketball, VanDerveer led the Stanford Cardinal to two NCAA Women's Division I Basketball Championships: in 1990 and 1992.  She stepped away from the Stanford program for a year to serve as the U.S. national team head coach at the 1996 Olympic Games.  VanDerveer is the 1990 Naismith National Coach of the Year and a ten-time Pac-12 Coach of the Year.  She is also one of only six NCAA Women's Basketball coaches to win over 900 games, and one of three NCAA Division I coaches – men's or women's – to win 1,000 games.

Fran O'Hanlon: Francis Brian "Fran" O'Hanlon (born August 24, 1948) is an American college basketball coach and the current head men's basketball coach at Lafayette College.  Born in Philadelphia, Pennsylvania, O'Hanlon played college basketball at Villanova University, from where he graduated in 1970.  He played professional basketball for the Miami Floridians of the ABA in the 1970-71 season, despite being a Philadelphia 76ers draft pick in the 8th round of the 1970 NBA draft.

Larry Holley: Larry Holley (born June 28, 1945) is an American basketball coach.  He is the head men's basketball coach at his alma mater, William Jewell College in Liberty, Missouri.  With 877 wins at the end of the 2015–16 season he is among only 47 four-year college coaches (National Collegiate Athletic Association (NCAA) and National Association of Intercollegiate Athletics (NAIA)) to reach 700 wins.  He ranks 1st all-time in career wins among four-year, college coaches coaching only at Missouri colleges and universities.  He ranks 12th all-time in career wins nationally among four-year, college coaches.

Mike Krzyzewski: Michael William Krzyzewski ( ; nicknamed "Coach K"; born February 13, 1947) is an American college basketball coach and former player.  Since 1980, he has served as the head men's basketball coach at Duke University.  At Duke, Krzyzewski has led the Blue Devils to five NCAA Championships, 12 Final Fours, 12 ACC regular season titles, and 14 ACC Tournament championships.  Among men's college basketball coaches, only UCLA's John Wooden, with 10, has won more NCAA Championships.  Krzyzewski was also the coach of the United States men's national basketball team, which he has led to three gold medals at the 2008 Summer Olympics, 2012 Summer Olympics, and 2016 Summer Olympics.  He has additionally served as the head coach of the American team that won gold medals at the 2010 and the 2014 FIBA World Cup.  He was also an assistant coach for the 1992 "Dream Team".

Osborne Cowles: Osborne Bryan Cowles (August 25, 1899 – August 29, 1997) was an American basketball player and coach.  He was the head men's basketball coach at Carleton College (1924–1930), River Falls State Teachers College (now University of Wisconsin–River Falls) (1932–1936), Dartmouth College (1936–1946), University of Michigan (1946–1948), and University of Minnesota (1948–1959).  He was also the head baseball coach and assistant basketball and football coach at Iowa State Teachers College, now the University of Northern Iowa during 1923–24.  In 30 seasons as a collegiate head basketball coach, Cowles compiled a record of 416–189 ( ).  His teams competed in the NCAA basketball tournament six times.  At the time of his retirement in 1959, Cowles ranked among the top 15 college basketball coaches of all-time by number of games won.  He has been inducted into the Helms Foundation Hall of Fame, the Dartmouth "Wearers of the Green," the University of Minnesota "M" Club Hall of Fame, the Carleton College Hall of Fame, and the University of Wisconsin-River Falls Athletics Hall of Fame.

Question: Where was the basketball coach who coaches at the college in Easton, Pennsylvania which was founded in 1826 born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "college_info": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the college."
        },
        "location": {
          "type": "string",
          "description": "The city and state where the college is based."
        },
        "founding_year": {
          "type": "integer",
          "description": "The year the college was founded."
        }
      },
      "required": [
        "name",
        "location",
        "founding_year"
      ],
      "additionalProperties": false
    },
    "coach_info": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the basketball coach."
        },
        "coaching_role": {
          "type": "string",
          "description": "The coaching role of the individual at the college."
        },
        "birthplace": {
          "type": "string",
          "description": "The city and state where the coach was born."
        }
      },
      "required": [
        "name",
        "coaching_role",
        "birthplace"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The birthplace of the coach."
    }
  },
  "required": [
    "college_info",
    "coach_info",
    "final_answer"
  ],
  "additionalProperties": false
}
