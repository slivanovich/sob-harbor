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
Jenny Wiley Theatre: Jenny Wiley Theatre is a non-profit organization that puts on productions of classic Broadway musicals, comedies, historical dramas and holiday productions at both the Jenny Wiley Amphitheatre, located within the Jenny Wiley State Resort Park, and surrounding venues.  The theater's first musical was "South Pacific", performed in the summer of 1965.  Some theater alumni have later achieved success in television, film and national theater.  These include: Michael Cerveris, who won two Tony awards, one for his performance in "Tommy" in 1994, and one for his performance in "Assassins" on Broadway; Christine Johnson, Nettie Fowler in the original Broadway cast of "Carousel"; Sharon Lawrence from ABC's "NYPD Blue" and "Desperate Housewives"; James Barbour, who played the Beast in Disney's Broadway production of "Beauty and the Beast" and was Tony-nominated for his role as Mr. Rochester in the musical, "Jane Eyre"; Jim Varney, "Ernest Goes to Camp"; Tommy Kirk, "Old Yeller"; Ron Palillo, "Welcome Back, Kotter"; Eileen Bittman Barnett, "Days of Our Lives"; Cynthia Bostick, "As the World Turns"; Lawrence Leritz, "Broadway and Beyond"; Jeff Silbar, composer of "The Wind Beneath My Wings"; Randy Jones of the Village People singing group; and Paige Davis, host of TLC's "Trading Spaces".

Terry Finn: Teresa Jo Ann Bernadette "Terry" Finn (born August 6, 1955) is an American actress best known for creating the role of Gussie Carnegie in the original Broadway cast of the Stephen Sondheim/Hal Prince/George Furth musical comedy "Merrily We Roll Along" and its Original Cast Album.

Alter Egos: Alter Egos is a 2012 American superhero comedy film written, edited, and directed by Jordan Galland.  The film, starring Kris Lemche, Sean Lennon, Danny Masterson, and Geneva Carr, was distributed by Kevin Smith's SModcast Pictures and Phase 4 Films.  It premiered was at the Fantasia Film Festival on July 24, 2012, where it was chosen as an official selection.

Putting It Together: Direct from Broadway: Putting It Together: Direct from Broadway is a 2001 film of the Broadway production of the musical revue "Putting It Together" as captured live in performance on Broadway featuring the show's original Broadway cast.  The show was captured at Broadway’s Barrymore Theatre in New York City February 20, 2000 utilizing multiple high definition cameras by Broadway Worldwide.

Gaelen Gilliland: Gaelen Gilliland is an American musical theatre actress.  She has appeared on Broadway in "Wicked", "Legally Blonde-Original Broadway Cast", and 9 to 5: The Musical-Original Broadway Cast, Honeymoon in Vegas-Original Broadway cast, and Kinky Boots.  She worked on the pre-production and out of town performance of Finding Neverland.  She appeared in

Nathan Lee Graham: Nathan Lee Graham (born September 9, 1968) is an American cabaret artist, stage, television and film actor, singer, writer and director.  His roles in feature film include Todd in "Zoolander", Frederick Montana in "Sweet Home Alabama" and Geoff in "Hitch".  He has appeared in independent films like "Confessions of an Action Star", "Bad Actress" and "Trophy Kids".  On the small screen he originated the role of Peter in "The Comeback", and had guest starring roles on "Scrubs", "Absolutely Fabulous" and "".  His stage appearances include Phil D'armano in the original Broadway cast of the Tony Awards and Grammy Award nominated "The Wild Party" and as Miss Understanding in the original Broadway cast of the Tony Awards nominated "Priscilla, Queen of the Desert".  He received a Drama League Award nomination for the role of Rey Rey in the off-Broadway production of "Wig Out" and won an Los Angeles Drama Critics Circle Award for Best Feature Performer in a Musical in "The Wild Party" LA Premiere in 2006.  More recently, he has appeared in the role of Carson in Hit the Wall at The Barrow Street Theatre and as Willy in The View UpStairs.  He earned a 2005 Best Classical Album Grammy Award for "Songs of Innocence and of Experience" as a soloist.

Geneva Carr: Geneva Carr (born May 6, 1971) is an American television and stage actress with an extensive acting resume.  She is best known for her performance as Margery in the original Broadway cast of "Hand To God", earning a nomination for the Tony Award for Best Actress in a Play.

Melissa Hart (actress): Melissa Hart is an American actress, singer, and teacher.  She made her Broadway debut in 1966 as an ensemble member in Jerry Bock's "The Apple Tree".  As Barbara Harris's understudy, she replaced the actress as the various heroines in that musical for several performances.  In 1969 she took over the role of Sally Bowles in the original production of John Kander's "Cabaret"; a role she had previously performed in the musical's first National Tour.  In 1970 she created the role of Meredith in the original Broadway cast of Tom Mankiewicz's "Georgy"; a performance for which she garnered a Tony Award nomination.  She soon after performed the role of Fran Kubelik in the National Tour of Burt Bacharach's "Promises, Promises".

Jennifer Leigh Warren: Jennifer Leigh Warren is an American stage, television, film, and voice-over actress/singer who first came to the world's attention for her work in professional musical theater.  She is best known for originating the role of Crystal in the Howard Ashman /Alan Menken hit musical "Little Shop of Horrors", for her performance in the original Broadway cast of the Michael John LaChiusa musical "Marie Christine" and for her show stopping performance of “Alice’s Daughter” in the original Broadway musical "Big River" with the song "How Blest We Are" written especially for her by Roger Miller.

Dreamgirls: Original Broadway Cast Album: Dreamgirls: Original Broadway Cast Album is the cast album for the original Broadway production of the musical "Dreamgirls", which debuted at the Imperial Theatre on December 20, 1981.  The album was issued by David Geffen, a co-financier of the musical and later producer of its 2006 film adaptation, on his Geffen Records label during the winter of 1982.  The "Dreamgirls" cast album features cast performances by the show's performers, including Jennifer Holliday, Sheryl Lee Ralph, Loretta Devine, Ben Harney, Cleavant Derricks, Obba Babatundé, and Vondie Curtis-Hall.

Question: The actress best known for her performance as Margery in the original Broadway cast of "Hand To God" appeared in what 2012 superhero comedy film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress."
    },
    "known_role": {
      "type": "object",
      "properties": {
        "character_name": {
          "type": "string",
          "description": "The character the actress is best known for."
        },
        "production_name": {
          "type": "string",
          "description": "The name of the production where the character appeared."
        },
        "production_type": {
          "type": "string",
          "description": "The type of production (e.g., musical, play)."
        }
      },
      "required": [
        "character_name",
        "production_name",
        "production_type"
      ],
      "additionalProperties": false
    },
    "film_appearance": {
      "type": "object",
      "properties": {
        "film_title": {
          "type": "string",
          "description": "The title of the film the actress appeared in."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the film."
        }
      },
      "required": [
        "film_title",
        "release_year",
        "genre"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actress_name",
    "known_role",
    "film_appearance"
  ],
  "additionalProperties": false
}
