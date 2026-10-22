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
Top Chef (season 3): Top Chef: Miami is the third season of the American reality television series "Top Chef".  It was first filmed in Miami, Florida, before concluding in Aspen, Colorado.  The season was Emmy nominated for Outstanding Reality Competition Series, and garnered the Emmy Award for Best Editing in the category.  Season 3 premiered on June 13, 2007 and ended on October 10, 2007.  Padma Lakshmi returned with Tom Colicchio, Gail Simmons, and new judge Ted Allen, who switched off with Simmons throughout the season. ""  contestant Lee Anne Wong was brought in as a food consultant and assisted in planning the challenges.  Production took place in April and May 2007 in Miami Beach, Florida, with production activity centered at the Fontainebleau Hotel.  The winning recipe from each week's episode of Season 3 was featured on Bravo's "Top Chef" website and prepared by Lee Anne Wong in a web series called "The Wong Way to Cook".  In the season finale, Hung Huynh was declared the Top Chef, defeating Dale Levitski and Casey Thompson.  Thompson received the Fan Favorite Award.

Top Chef (season 9): Top Chef: Texas is the ninth season of the American reality television series "Top Chef".  The season was filmed in various cities in Texas, including San Antonio, Dallas, and Austin, before moving on to British Columbia for the finale.  The season premiered on November 2, 2011.  This season of "Top Chef" featured a much larger number of contestants than any previous season, with 29 chefs.  "Top Chef: Texas" also introduced a new competition to the series; in addition to the Quickfire and Elimination Challenges featured in televised episodes, the "Last Chance Kitchen" competition allowed eliminated contestants to compete head-to-head in a series of webisodes, with the winner eventually returning to the main competition.  In the season finale, Paul Qui was declared the Top Chef, defeating Sarah Grueneberg.  Chris Crary received the Fan Favorite Award.

Brennan Howard: Brennan Howard (born July 16, 1968 in Glendale, California) is an American actor and director.  He has written, produced, directed, and starred in at least four films: "Dick Richards" (1996) featuring Ashley Judd, "The Temple of Phenomenal Things" (1997), "Straighten Up America" (2003), an ill-fated T.V. show known as "GamePro TV" (1991), and the voice of Cooler in 1988's "Pound Puppies and the Legend of Big Paw."

Top Chef (season 6): Top Chef: Las Vegas is the sixth season of the American reality television series "Top Chef".  It was first filmed in Las Vegas, Nevada, before concluding in Napa, California.  The season premiered on August 19, 2009, and ended on December 16, 2009.  Beginning with this season, the prize money awarded to the winner was increased from US$ to $125,000.  In the season finale, Michael Voltaggio was declared the Top Chef, defeating Bryan Voltaggio and Kevin Gillespie.  Gillespie received the Fan Favorite Award.  In 2010, "Top Chef: Las Vegas" received the Primetime Emmy Award for "Outstanding Reality Competition Program".

The Chopping Block (U.S. TV series): The Chopping Block is an American reality television series, based on the Australian reality television series of the same name.  The series aired on the NBC network and followed participants in an attempt to open a restaurant.  It is hosted by British celebrity chef Marco Pierre White.

Lucas Babin: Lucas Edwin Babin (born July 30, 1979) is an American film and television actor.  He speaks Portuguese fluently and has a twin sister named Kirsten.  Born in Beaumont, Texas, Lucas attended high school in Woodville TX, where his father, Brian Babin was the town mayor.  He then moved to California to live with his brother Leif.  After a couple of years he moved into an apartment in Hollywood with a friend Bryan Gay (also an actor from Woodville).  He pursued an acting modeling career for several years before landing a role in "School of Rock" starring Jack Black.  He then went on to act in several short and independent films before landing a role on the Brazilian T.V. show called "America".  Babin met and married a Brazilian woman and they now have two children.  His television work has included roles in "Undressed" and "Sex and the City".

Top Chef (season 14): Top Chef: Charleston is the fourteenth season of the American reality television series "Top Chef".  The season was announced by Bravo on October 13, 2016, which premiered on December 1, 2016, and concluded on March 2, 2017.  Filming initially took place in Charleston, South Carolina, beginning in May 2016, while the season's final episodes were filmed in areas across Mexico, including Guadalajara and the Yucatán Peninsula.  "Top Chef: Charleston" featured eight new contestants competing against eight returning contestants from previous seasons. " MasterChef" and "Top Chef Masters" alumnus Graham Elliot debuted as a recurring judge, alongside returning judges Padma Lakshmi, Tom Colicchio, and Gail Simmons.  In the season finale, "" runner-up Brooke Williamson was declared the Top Chef, defeating "" finalist Shirley Chung.  "Top Chef: Seattle" finalist Sheldon Simeon received the Fan Favorite Award, marking his second Fan Favorite win.

A-List Listings: A-List Listings is an American reality television series that debuted October 24, 2012, on E!.  Hosted by David Burtka and Catt Sadler, the series showcases America's most exclusive and extravagant homes.

Top Chef (season 1): Top Chef: San Francisco, originally broadcast simply as Top Chef, is the first season of the American reality television series "Top Chef".  It was first filmed in San Francisco, California, before concluding in Las Vegas, Nevada.  The season premiered on March 8, 2006 and ended on May 24, 2006.  The show featured chefs from around the United States living together in one house and competing in a series of culinary challenges.  The prizes for the winner of the competition included a feature in "Food & Wine Magazine", a showcase at the annual "Food & Wine" Classic in Aspen, Colorado, a Kenmore Elite kitchen set, and US$ .  The series was hosted by Katie Lee Joel, in her only season as a host, and judged by chef Tom Colicchio and food writer Gail Simmons.  In the season finale, Harold Dieterle was declared the Top Chef, defeating Tiffani Faison.

David Burtka: David Michael Burtka (born May 29, 1975) is an American actor and professional chef.  He is known for his acting roles in theatre and television shows such as "How I Met Your Mother" and "The Play About the Baby".  After his role on "How I Met Your Mother", Burtka gained media attention for dating Neil Patrick Harris, whom he later married in 2014.

Question: The American actor and professional chef who hosted an American reality television series that showcases America's most exclusive and extravagant homes, was known for starring on what t.v. show?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the American actor and professional chef."
    },
    "person_occupations": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The occupations of the person."
    },
    "hosted_series_name": {
      "type": "string",
      "description": "The name of the reality television series hosted by the person."
    },
    "hosted_series_description": {
      "type": "string",
      "description": "A description of what the hosted series showcases."
    },
    "known_for_tv_show": {
      "type": "string",
      "description": "The name of the television show the person was known for starring in."
    }
  },
  "required": [
    "person_name",
    "person_occupations",
    "hosted_series_name",
    "hosted_series_description",
    "known_for_tv_show"
  ],
  "additionalProperties": false
}
