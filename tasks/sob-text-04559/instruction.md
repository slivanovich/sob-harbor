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
Rick Harrison: Richard Kevin "Rick the Spotter" Harrison (born March 22, 1965) is an American, Las Vegas-based businessman and reality television personality, best known as the co-owner of the World Famous Gold & Silver Pawn Shop, as featured on the History series "Pawn Stars".  He co-owns the pawn shop with his father, Richard Benjamin Harrison, which they opened in 1989.  Harrison dropped out of high school to pursue his "$2,000-a-week business of selling fake Gucci bags".

List of Pawn Stars episodes: "Pawn Stars" is an American reality television series that premiered on History on July 19, 2009.  The series is filmed in Las Vegas, Nevada, where it chronicles the activities at the World Famous Gold & Silver Pawn Shop, a 24-hour family business operated by patriarch Richard "Old Man" Harrison, his son Rick Harrison, Rick's son Corey "Big Hoss" Harrison, and Corey's childhood friend, Austin "Chumlee" Russell.

Pawn Shop Chronicles: Pawn Shop Chronicles, also known as Hustlers, is a 2013 crime comedy film directed by Wayne Kramer and written by Adam Minarovich.  The film stars an ensemble cast, led by Paul Walker, Matt Dillon, Brendan Fraser, Vincent D'Onofrio, Norman Reedus, and Chi McBride.  Centering on the events in and around a pawn shop, "Pawn Shop Chronicles" tells three overlapping stories involving items found within said pawn shop.  This was the final film featuring Walker to be released in his lifetime.

Richard Benjamin Harrison: Richard Benjamin Harrison Jr., (also known by the nicknames The Old Man and The Appraiser) (born March 4, 1941), is a Las Vegas businessman and reality television personality, best known as the co-owner of the World Famous Gold & Silver Pawn Shop, as featured on the History channel series "Pawn Stars".  Harrison was the co-owner of a pawn shop with his son Rick Harrison until he suffered a stroke, causing him to retire.They opened the store together in 1989.

Arrowhead Pawn Shop: Arrowhead Pawn Shop is a pawn shop and part of the Iron Pipeline.  It was founded in 1991 and is located in Jonesboro, Georgia.  The store was described as the most significant source outside of New York State of guns recovered by the New York Police Department in 2009.  After a gun from the shop was used in the murders of two New York City Police Department (NYPD) officers, the "New York Times" reported that Arrowhead ranked fifth on the U.S.-wide list of legal sources of guns used in crimes.  The newspaper quoted an anonymous federal official as stating that "[Arrowhead] were like a Crazy Eddie of gun dealers.  They had a lot of volume and they did a lot of business."  The Brady Center to Prevent Gun Violence describes Arrowhead as a "notorious 'bad apple' gun dealer", having sold over 1720 guns that were subsequently used in crimes.

EZCorp: EZMONEY Tario Inc is an American pawn shop operator based in Austin, Texas but providing services across Mexico and Canada.  It is a publicly traded company listed on the NASDAQ stock exchange and was the second largest pawn shop operator in the U.S.

Chumlee: Austin Lee Russell (born September 8, 1982), better known by his stage name of Chumlee, is an American actor, businessman and reality television personality, known as a cast member on the History Channel television show "Pawn Stars", which depicts the daily business at the Gold and Silver Pawn Shop in Las Vegas where Russell works as an employee.  Chumlee came to work at the pawn shop five years before filming of the first season, having been a childhood friend of Corey Harrison, whose father, Rick Harrison, and grandfather, Richard Benjamin Harrison, opened the shop in 1989.

Pawn Stars: Pawn Stars is an American reality television series, shown on History, and produced by Leftfield Pictures.  The series is filmed in Las Vegas, Nevada, where it chronicles the daily activities at the World Famous Gold & Silver Pawn Shop, a 24-hour family business opened in 1989 and operated by patriarch Richard "Old Man" Harrison, his son Rick Harrison, Rick's son Corey "Big Hoss" Harrison, and Corey's childhood friend, Austin "Chumlee" Russell.  The series, which became the network's highest rated show and the No. 2 reality show behind "Jersey Shore", debuted on July 26, 2009.

Value—Beyond Price: Value—Beyond Price is a 1910 American silent short drama produced by the Thanhouser Company.  The film focuses on a family beset by tragedy when the father is presumed dead after his ship is lost at sea.  The mother struggles to support her child and sells her possessions to a pawnbroker.  When she has nothing left, save her wedding ring, the pawnbroker asks to take care of the child and the mother consents.  The pawn broker gives her a pawn ticket for the girl stating "a precious jewel, a value beyond price" and tells her she can redeem it at any time.  Before her death, she entrusts the ticket to a friend.  Ten years pass, the shipwrecked father has discovered a great fortune on the island and is rescued by a passing steamship.  The father soon realizes his wife is dead and his child is missing, but he receives the pawn ticket and decides to claim this jewel his wife had left for him.  He redeems it at the pawn shop and finds it is his lost daughter.  The film was released on November 29, 1910 and it was met with positive reviews.  The film survives in the Library of Congress archives.

Pawnography: Pawnography is an American game show broadcast by History.  Hosted by comedian Christopher Titus and featuring "Pawn Stars" personalities Rick Harrison, Corey Harrison and Austin "Chumlee" Russell as panelists, the series features contestants answering questions for a chance to win cash and items for sale from the Gold and Silver Pawn Shop (where "Pawn Stars" is taped).  The show premiered July 10, 2014, at 10 p.m. ET, following "Pawn Stars".

Question: Chumlee is a friend of the pawn shop worker whose father is based in what city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person in question (Chumlee)."
    },
    "friend_name": {
      "type": "string",
      "description": "The full name of Chumlee's friend."
    },
    "friend_father_name": {
      "type": "string",
      "description": "The full name of the friend's father."
    },
    "father_base_city": {
      "type": "string",
      "description": "The city where the friend's father is based."
    },
    "pawn_shop_name": {
      "type": "string",
      "description": "The name of the pawn shop associated with these individuals."
    }
  },
  "required": [
    "person_name",
    "friend_name",
    "friend_father_name",
    "father_base_city",
    "pawn_shop_name"
  ],
  "additionalProperties": false
}
