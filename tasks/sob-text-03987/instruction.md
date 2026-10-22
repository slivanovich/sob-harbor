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
Anne Burrell: Anne W. Burrell (born September 21, 1969) is an American chef, TV personality and an instructor at the Institute of Culinary Education in New York City until 2007.  She is the host of the Food Network show "Secrets Of a Restaurant Chef" and co-host of "Worst Cooks in America".  She was also one of Iron Chef Mario Batali's sous chefs in the "Iron Chef America" series and appears on other programs on the network such as "The Best Thing I Ever Ate".  She was a contestant on the fourth season of The Food Network competition show, "The Next Iron Chef" Super Chefs being eliminated in episode 6.  She was also a contestant on the first season of Chopped All-Stars Tournament, winning the "Food Network Personalities" preliminary round to advance to the final round, where she placed second runner up to Nate Appleman (winner) and Aarón Sanchez.  In 2015, Burrell won the fourth installment of the Chopped All-Stars tournament winning $75,000 for the Juvenile Diabetes Foundation.  She also hosted the series "Chef Wanted with Anne Burrell" in 2012–2013.

Guy's Big Bite: Guy's Big Bite is a Food Network show starring Guy Fieri, winner of the second season of "The Next Food Network Star".  The inaugural six-episode season premiered on June 25, 2006 in the 10:00 am/EST timeslot.  Currently "Guy's Big Bite" airs Saturdays at 7:30am EST/PST & Sundays at 10:30am and 11am EST/PST.

Rachael Ray's Tasty Travels: Rachael Ray's Tasty Travels is a television show based on cook Rachael Ray and her travels around the world (somewhat similar to her 2002 Food Network show, "$40 a Day").  However, in this show she is not restricted by a budget and showcases food from more upscale eateries.  She tries different types of food from each place she visits, and gives a "Hot List of Values", which includes some of her favorite places visited from "$40 a Day".  The show airs on the Food Network and is her fourth Food Network program.  It first aired on August 26, 2005.  She provides voiceovers for most of the show and is shown at only one or two places.  Her husband, John Cusimano, usually accompanies her at the one or two restaurants she visits per episode.  The show was developed with Producer Wade Sheeler following the success of her first travel show on Food Network, "$40 a Day".

Damaris Phillips: Damaris Lennon Phillips (born December 8, 1980) is an American chef and television personality.  In 2013 she won the ninth season of the Food Network television series "Food Network Star".  She hosted the Food Network show "Southern at Heart" for five seasons from 2013 to 2016.  She currently co-hosts "The Bobby and Damaris Show" on Food Network with Bobby Flay.

Will Work for Food (TV series): Will Work For Food is a Food Network show starring Adam Gertler, one of three finalists of the fourth season of "The Next Food Network Star".  The show premiered on Monday, January 19, 2009 at 8:30 PM EDT.  According to Food Network, the series "exposes Adam to the world of little-known food jobs as he fearlessly puts his life – and mouth – on the line to try them all!  Whether taking honey from three million bees, sculpting ice with a chain saw, foraging for truffles, or digging a wine cave, Adam will do anything in the name of food."  The concept is somewhat similar to the Food Network program "Glutton for Punishment".

Ted Allen: Ted Allen is an American author and television personality.  He was the food and wine connoisseur on the Bravo network's television program "Queer Eye", and has been the host of the TV cooking competition series "Chopped" since its launch in 2009, as well as "Chopped Junior", which began in mid-2015.  In April 13, 2014, he became the host of another Food Network show, originally called "America's Best Cook"; a retooled version of that show, retitled "All-Star Academy," which debuted on March 1, 2015.  In early 2015, he also hosted a four-part special, "Best.  Ever." , which scoured America for its best burgers, pizza, breakfast, and barbecue.  He is a longtime contributing writer to "Esquire" magazine, the author of two cookbooks, and regularly appears on the Food Network show "The Best Thing I Ever Ate" and other television cooking shows.

Jim O'Connor: Jim O'Connor is an American actor and former host of the show "The Secret Life Of...".  O'Connor first appeared on the Food Network as the host of "All-American Festivals", replacing Tyler Florence as host.  Later O'Connor went on to host the new Food Network show, "The Secret Life Of..." for three years, until George Duran replaced him as host in early 2007.  O'Connor also has hosted a special called "Scoop", in which five Food Network viewers create a new flavor of ice cream.

Adam Gertler: Adam Gertler is an American chef, television personality and occasional actor.  He was the runner-up on season four of "The Next Food Network Star" and is a host of "FX Movie Download".

Party Line with the Hearty Boys: Party Line with The Hearty Boys is a Food Network show hosted by real-life couple Dan Smith (b. July 16, 1962) and Steve McDonagh (b. June 14, 1964).  Smith and McDonagh launched the show after winning the network's reality contest, The Next Food Network Star, which granted them a six-show Food Network series.  The original series was entitled "Party Line with Dan and Steve", but eventually the hosts were allowed to change the title in order to reflect and give credit to their independent Chicago catering business, The Hearty Boys, Co.

Down Home with the Neelys: Down Home with the Neelys is a Food Network show hosted by Patrick and Gina Neely.  The show depicts the Neelys sharing dishes and recipes.  Taped in their Memphis home, the show, which has a relaxed demeanor, now airs seven days a week on Food Network.  The Entertainment Network announced in September, 2014 that the couple would divorce after 20 years of marriage.  The fate of the company remains unknown.

Question: The host of "FX Movie Download" stars in what Food Network show that premiered in January of 2009?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "host_name": {
      "type": "string",
      "description": "The name of the host."
    },
    "host_other_show": {
      "type": "string",
      "description": "Another show hosted by the individual."
    },
    "food_network_show_name": {
      "type": "string",
      "description": "The name of the Food Network show starring the host."
    },
    "premiere_date": {
      "type": "string",
      "description": "The exact premiere date of the Food Network show."
    },
    "premiere_year": {
      "type": "integer",
      "description": "The premiere year of the Food Network show."
    }
  },
  "required": [
    "host_name",
    "host_other_show",
    "food_network_show_name",
    "premiere_date",
    "premiere_year"
  ],
  "additionalProperties": false
}
