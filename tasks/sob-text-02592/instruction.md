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
Mal Michael: Malcolm Robert "Mal" Michael (born 24 June 1977) is a Papua New Guinean born former Australian rules footballer.  He is notable for his successful professional career in the Australian Football League.  In a career spanning 238 games and three clubs in two Australian states he is best known as a triple premiership full-back with the Brisbane Lions.  Michael is recognised as being one of the best Queensland produced Australian rules footballers of all time, being named on the AFL Queensland Team of the 20th Century.

Matthew Burton: Matthew "Spider" Burton (born 19 May 1970) is a retired Australian rules footballer.  He played as a ruckman and began his Football career at Subiaco.  "Spider" Burton, as he's commonly known, because of his 210 cm frame, was formerly the AFL's tallest player.  He has since been eclipsed by another Docker in Aaron Sandilands, and Western Bulldog Peter Street.  Both stand at 211 cm tall.

Libby Birch: Libby Birch (born 3 December 1997) is an Australian rules footballer playing for the Western Bulldogs in the AFL Women's competition.  She previously played netball and captained Victoria at the National Netball Championships.  Birch is currently studying a Physiotherapy degree at Latrobe University.  In 2016, Birch switched from netball to Australian rules football and was recruited by the Western Bulldogs as a rookie after having only played football for three months for the Darebin Falcons in the VFL Women's.

Matthew Kennedy (footballer, born 1997): Matthew Kennedy (born 6 April 1997) is a professional Australian rules footballer playing for the Greater Western Sydney Giants in the Australian Football League (AFL).  Kennedy is one of two current Giants players from the small town of Collingullie, New South Wales, along with Harry Perryman.  They played together for most of their junior career.  Perryman was recruited from Collingullie-Glenfield Park Football Club in the Riverina Football Netball League, where he played in consecutive senior premierships in 2014 and 2015.  A member of the Giants' academy program, he was drafted by the Giants with the thirteenth selection in the 2015 AFL draft, matching a bid from Richmond .  Kennedy made his debut against the Essendon in round 13 of the 2016 AFL season.  In an impressive performance, he kicked three goals as the Giants defeated Essendon by a 27 points.

Aaron Sandilands: Aaron Sandilands (born 6 December 1982) is an Australian rules footballer who plays for the Fremantle Football Club in the Australian Football League (AFL).  Originally from Mount Barker, a small town in the Great Southern region of Western Australia, Sandilands played with the East Fremantle Football Club in the West Australian Football League (WAFL), before being rookie listed by Fremantle in the 2002 Rookie Draft.  Upgraded from the rookie list at the end of the 2002 season, he made his senior debut for the club in round one of the 2003 season.  At 211 cm tall, and with a peak weight of 120 kg , Sandilands became the heaviest and equal-tallest player to ever play in the AFL.  Due to his height, Sandilands plays almost exclusively as a ruckman, occasionally resting in the forward line.  At times, he has been described as the best ruckman in the competition, and was named in the All-Australian team in three consecutive years between 2008 and 2010.  Sandilands is a dual Doig Medallist as Fremantle's best and fairest player, won in 2009 and 2015.

Ron Barassi: Ronald Dale "Ron" Barassi Jr {'1': ", '2': ", '3': ", '4': "} (born 27 February 1936) is a retired Australian rules football player and coach.  During a long and decorated career, Barassi has been one of the most important figures in the history of Australian football.  His father Ron Barassi Sr., also a prominent Australian rules footballer, was killed at Tobruk during World War II.  The young Barassi spent his latter teenage years living with Norm Smith, coach of the Melbourne Football Club and a former teammate of his father.

Anthony Alexander Forrest: Anthony Alexander Forrest (20 November 1884 – 15 May 1901) was an Australian rules footballer and soldier who was killed in the Second Boer War.  The son of Alexander Forrest, a politician and twice Mayor of Perth, he attended The High School (now Hale School) in Perth, Western Australia.  Aged 15, he also played two games of senior football for the Perth Football Club in what is now the West Australian Football League (WAFL), becoming one of the youngest players to play in that league.  Forrest enlisted in the 5th Western Australian Mounted Infantry in 1900, and was killed the following year near Carolina, Transvaal, at the age of 16.  He was the first Western Australian footballer to be killed on active duty, and the only Western Australian footballer killed in the Boer War.

Harry Perryman: Harry Perryman (born 19 December 1998) is a professional Australian rules footballer playing for the Greater Western Sydney Giants in the Australian Football League (AFL).  He was drafted by Greater Western Sydney with their third selection and fourteenth overall in the 2016 national draft.  He made his debut in the three point win against Richmond at Spotless Stadium in round nine of the 2017 season.  Perryman is one of two current Giants players from the small town of Collingullie, New South Wales, along with Matthew Kennedy.  They played together for most of their junior career.

Russell Ebert: Russell Ebert OAM (born 22 June 1949) is a retired Australian rules footballer and coach.  He is considered one of the greatest players in the history of Australian rules football in South Australia.  Russell Ebert is the only player to have won four Magarey Medals which are awarded to the best and fairest player in the South Australian National Football League (SANFL).

Max Gawn: Max Gawn (born 30 December 1991) is a professional Australian rules footballer playing for the Melbourne Football Club in the Australian Football League (AFL).  A ruckman, 2.08 m tall and weighing 111 kg , Gawn is capable of contributing in both the ruck and forward line.  A basketballer and rugby union player at a young age, he pursued his career in Australian rules football and he was drafted to the Melbourne Football Club with the thirty-fourth selection in the 2009 AFL draft.  He made is AFL debut in the 2011 AFL season.  Knee and hamstring injuries hampered his first four seasons in the AFL before he moved into the number one ruck position at Melbourne in 2015 along with All-Australian selection in 2016.

Question: Which Australian rules footballer surpassed Matthew Burton as, currently, one of the tallest and heaviest players on the field?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the Australian rules footballer who surpassed Matthew Burton."
    },
    "player_height_cm": {
      "type": "integer",
      "description": "The height of the player who surpassed Matthew Burton in centimeters."
    },
    "player_weight_kg": {
      "type": "integer",
      "description": "The peak weight of the player who surpassed Matthew Burton in kilograms."
    },
    "previous_tallest_player_name": {
      "type": "string",
      "description": "The name of the player who was previously the tallest."
    },
    "previous_tallest_player_height_cm": {
      "type": "integer",
      "description": "The height of the player who was previously the tallest in centimeters."
    },
    "surpassing_details": {
      "type": "string",
      "description": "Details on how the player surpassed the previous record holder."
    }
  },
  "required": [
    "player_name",
    "player_height_cm",
    "player_weight_kg",
    "previous_tallest_player_name",
    "previous_tallest_player_height_cm",
    "surpassing_details"
  ],
  "additionalProperties": false
}
