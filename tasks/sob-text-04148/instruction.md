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
Arrowhead Pawn Shop: Arrowhead Pawn Shop is a pawn shop and part of the Iron Pipeline.  It was founded in 1991 and is located in Jonesboro, Georgia.  The store was described as the most significant source outside of New York State of guns recovered by the New York Police Department in 2009.  After a gun from the shop was used in the murders of two New York City Police Department (NYPD) officers, the "New York Times" reported that Arrowhead ranked fifth on the U.S.-wide list of legal sources of guns used in crimes.  The newspaper quoted an anonymous federal official as stating that "[Arrowhead] were like a Crazy Eddie of gun dealers.  They had a lot of volume and they did a lot of business."  The Brady Center to Prevent Gun Violence describes Arrowhead as a "notorious 'bad apple' gun dealer", having sold over 1720 guns that were subsequently used in crimes.

Chumlee: Austin Lee Russell (born September 8, 1982), better known by his stage name of Chumlee, is an American actor, businessman and reality television personality, known as a cast member on the History Channel television show "Pawn Stars", which depicts the daily business at the Gold and Silver Pawn Shop in Las Vegas where Russell works as an employee.  Chumlee came to work at the pawn shop five years before filming of the first season, having been a childhood friend of Corey Harrison, whose father, Rick Harrison, and grandfather, Richard Benjamin Harrison, opened the shop in 1989.

Corey Harrison: Richard Corey "Big Hoss" Harrison (born April 27, 1983) is an American businessman and reality television personality, known as a cast member of the History TV series "Pawn Stars", which documents his work at the World Famous Gold & Silver Pawn Shop in Las Vegas, which he co-owns with his father, Rick Harrison, and grandfather, Richard Benjamin Harrison.

Pawn Shop Chronicles: Pawn Shop Chronicles, also known as Hustlers, is a 2013 crime comedy film directed by Wayne Kramer and written by Adam Minarovich.  The film stars an ensemble cast, led by Paul Walker, Matt Dillon, Brendan Fraser, Vincent D'Onofrio, Norman Reedus, and Chi McBride.  Centering on the events in and around a pawn shop, "Pawn Shop Chronicles" tells three overlapping stories involving items found within said pawn shop.  This was the final film featuring Walker to be released in his lifetime.

Benjamin Harrison Home: The Benjamin Harrison Presidential Site, previously known as the Benjamin Harrison Home, was the home of the Twenty-third President of the United States, Benjamin Harrison.  It is in the Old Northside Historic District of Indianapolis, Indiana.  Harrison had the sixteen-room house with its red brick exterior built in the 1870s.  It was from the front porch of the house that Harrison instituted his famous Front Porch Campaign in the 1888 United States Presidential Campaign, often speaking to crowds on the street.  In 1896, Harrison renovated the house and added electricity.  He died there in a second story bedroom in 1901.  Today it is owned by the Arthur Jordan Foundation and operated as a museum to the former president by the Benjamin Harrison Foundation.

List of Pawn Stars episodes: "Pawn Stars" is an American reality television series that premiered on History on July 19, 2009.  The series is filmed in Las Vegas, Nevada, where it chronicles the activities at the World Famous Gold & Silver Pawn Shop, a 24-hour family business operated by patriarch Richard "Old Man" Harrison, his son Rick Harrison, Rick's son Corey "Big Hoss" Harrison, and Corey's childhood friend, Austin "Chumlee" Russell.

Pawnography: Pawnography is an American game show broadcast by History.  Hosted by comedian Christopher Titus and featuring "Pawn Stars" personalities Rick Harrison, Corey Harrison and Austin "Chumlee" Russell as panelists, the series features contestants answering questions for a chance to win cash and items for sale from the Gold and Silver Pawn Shop (where "Pawn Stars" is taped).  The show premiered July 10, 2014, at 10 p.m. ET, following "Pawn Stars".

Richard Benjamin Harrison: Richard Benjamin Harrison Jr., (also known by the nicknames The Old Man and The Appraiser) (born March 4, 1941), is a Las Vegas businessman and reality television personality, best known as the co-owner of the World Famous Gold & Silver Pawn Shop, as featured on the History channel series "Pawn Stars".  Harrison was the co-owner of a pawn shop with his son Rick Harrison until he suffered a stroke, causing him to retire.They opened the store together in 1989.

Benjamin Harrison IV: Benjamin Harrison IV (1693 – July 12, 1745) was an American Virginia planter, politician, and Member of the Virginia House of Burgesses.  He was the son of Benjamin Harrison III, and the father of Benjamin Harrison V, who was a signer of the Declaration of Independence and the fifth Governor of Virginia.  Harrison is also known as the builder of Berkeley which is believed to be the oldest three-story brick mansion in Virginia and is the ancestral home to two Presidents of the United States: William Henry Harrison, his grandson, and Benjamin Harrison his great-great-grandson.  Two powerful and influential families in colonial Virginia, the Harrison family and the Carter family, were united when Harrison married Anne Carter, the daughter of Robert "King" Carter.  His family also forged ties to the Randolph family as four of his children married four grandchildren of William Randolph I.

Rick Harrison: Richard Kevin "Rick the Spotter" Harrison (born March 22, 1965) is an American, Las Vegas-based businessman and reality television personality, best known as the co-owner of the World Famous Gold & Silver Pawn Shop, as featured on the History series "Pawn Stars".  He co-owns the pawn shop with his father, Richard Benjamin Harrison, which they opened in 1989.  Harrison dropped out of high school to pursue his "$2,000-a-week business of selling fake Gucci bags".

Question: When did the pawn shop, that Richard Benjamin Harrison owns, open?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "pawn_shop_name": {
      "type": "string",
      "description": "The name of the pawn shop."
    },
    "owner_name": {
      "type": "string",
      "description": "The name of the individual who owns the pawn shop."
    },
    "opening_year": {
      "type": "integer",
      "description": "The year the pawn shop opened."
    },
    "location": {
      "type": "string",
      "description": "The city and state where the pawn shop is located."
    }
  },
  "required": [
    "pawn_shop_name",
    "owner_name",
    "opening_year",
    "location"
  ],
  "additionalProperties": false
}
