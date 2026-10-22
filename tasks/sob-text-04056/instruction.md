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
Brighton &amp; Hove Albion F.C.: Brighton & Hove Albion Football Club is a professional football club based in the city of Brighton and Hove, East Sussex, England.  They made their Premier League debut in the 2017–18 season after sealing automatic promotion from the EFL Championship.  Brighton's home ground is the 30,750-capacity Falmer Stadium, known for sponsorship purposes as the American Express Community Stadium, or simply the Amex.

Sport in Sussex: Sport in Sussex forms an important part of the culture of Sussex.  With a centuries-long tradition of sport, Sussex has played a key role in the early development of both cricket and stoolball.  Cricket is recognised as having been formed in the Weald and Sussex CCC is England's oldest county cricket club.  Slindon Cricket Club dominated the sport for a while in the 18th century.  The cricket ground at Arundel Castle traditionally plays host to a Duchess of Norfolk's XI which plays the national test sides touring England.  The sport of stoolball is also associated with Sussex, which has a claim to be where the sport originated and certainly where its revival took place in the early 20th century.  Sussex is represented in the Football League by Brighton & Hove Albion and Crawley Town.  Brighton has been a League member since 1920, whereas Crawley was promoted to the League in 2011.  Sussex has had its own football association, since 1882 and its own football league, which has since expanded into Surrey, since 1920.  In horse racing, Sussex is home to Goodwood, Fontwell Park, Brighton and Plumpton.  The All England Jumping Course show jumping facility at Hickstead is situated 8 mi north of Brighton and Hove.

Davy Pröpper: David Petrus Wenceslaus Henri Pröpper (born 2 September 1991) is a Dutch professional footballer who plays as a midfielder for Premier League club Brighton & Hove Albion.

Whitehawk F.C.: Whitehawk Football Club is a semi-professional English football club based in Whitehawk, in the city of Brighton and Hove, East Sussex.  The club plays in the National League South, the sixth tier of English football.  Whitehawk's home ground is the 2175-capacity Enclosed Ground, known for sponsorship purposes as The TerraPura Ground, situated in East Brighton Park, just north of Brighton Marina.  Prior to 2010, the club had never played above County League level, but after three promotions in four seasons, the Hawks reached Conference South in 2013 as well as the second round of the FA Cup in 2015.

Brighton and Hove Cricket Club: Brighton and Hove Cricket Club, nicknamed "The Mighty Bensons", is an amateur cricket club based in East Sussex, in southern England.  Their top team secured the Sussex Cricket League championship in 2000 and in 2007.  Based since 1991 at the Nevill Sports Ground in Hove, southern England, the club achieved success in 1979 when it won both the first and second eleven competitions in the Sussex League, while playing at Horsdean.

Geography of Sussex: Sussex is a historic county and cultural region in the south of England corresponding roughly in area to the ancient Kingdom of Sussex.  It is bounded on the north by Surrey, north-east by Kent, south by the English Channel, and west by Hampshire, and is divided for local government into West Sussex and East Sussex and the city of Brighton and Hove.  The city of Brighton & Hove was created a unitary authority in 1997, and was granted City status in 2000.  Until then Chichester had been Sussex's only city.

Brighton and Hove built-up area: The Brighton and Hove Built-up area or Brighton/Worthing/Littlehampton conurbation has a population of 474,485 (2011 census), making it England's 12th largest conurbation.  This was an increase of around 3% from the 2001 population of 461,181.  Named the Brighton/Worthing/Littlehampton conurbation by the Office for National Statistics for the 2001 census and Brighton and Hove Built-up area for the 2011 census, the area has also been known as "Greater Brighton" (although Greater Brighton can include Lewes).  The conurbation dominates West and East Sussex, with around 1 in 3 of Sussex's population living within its boundaries.  It is also the second largest conurbation in the South East region of England and the second largest conurbation on the English Channel coast, in either England or France.  In both of these cases the Brighton conurbation trails the Southampton and Portsmouth conurbation.  This identified conurbation was the largest on the Channel before Portsmouth and Southampton's conurbations were combined for much official data analysis after the 2011 census.

Sussex: Sussex ( ), from the Old English "Sūþsēaxe" (South Saxons), is a historic county in South East England corresponding roughly in area to the ancient Kingdom of Sussex.  It is bounded to the west by Hampshire, north by Surrey, north-east by Kent, south by the English Channel, and divided for many purposes into the ceremonial counties of West Sussex and East Sussex.  Brighton and Hove, though part of East Sussex, was made a unitary authority in 1997, and as such, is administered independently of the rest of East Sussex.  Brighton and Hove was granted City status in 2000.  Until then, Chichester was Sussex's only city.

List of Brighton &amp; Hove Albion F.C. seasons: Brighton & Hove Albion Football Club is an English association football club based in the city of Brighton and Hove, East Sussex.  The club was founded in 1901 and played in the Southern League from the 1901–02 season until 1920, when that league's first division was absorbed into the Football League.  In 1910, they won the Southern League title and defeated Football League champions Aston Villa in the FA Charity Shield.  As a Football League team, Albion have won three divisional titles at the third level of the English football league system and two at the fourth.  They played in the 1983 FA Cup Final, losing to Manchester United after a replay, and their best achievement in the League Cup was in 1978–79 when they reached the quarter-final.

The Keep, Brighton: The Keep is an archive and historical resource centre which stores, conserves and gives the public access to over 900 years of records relating to the English county of East Sussex and the Special Collections held by the University of Sussex.  It was funded by East Sussex County Council, the City Council of neighbouring Brighton and Hove and the University of Sussex, and was built on land close to the university in the Moulsecoomb area of Brighton and Hove.  The building, constructed with a budget of £19 million, superseded the present East Sussex Record Office in the county town of Lewes when it opened on 31 October 2013.

Question: Davy Pröpper plays on what professional football club based in the city of Brighton and Hove, East Sussex, England?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the football player."
    },
    "club_name": {
      "type": "string",
      "description": "The name of the professional football club."
    },
    "club_location": {
      "type": "string",
      "description": "The city and county where the club is based."
    },
    "league": {
      "type": "string",
      "description": "The league the club plays in."
    },
    "player_position": {
      "type": "string",
      "description": "The playing position of the player."
    }
  },
  "required": [
    "player_name",
    "club_name",
    "club_location",
    "league",
    "player_position"
  ],
  "additionalProperties": false
}
