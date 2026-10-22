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
Hell's Kitchen (U.S. season 15): The fifteenth season of the American competitive reality television series "Hell's Kitchen" took place in October 2014 and premiered on January 15, 2016 on Fox.  The prize was a head chef position at BLT Steak at Bally's Las Vegas.  Country Club Chef Ariel Malone won the competition.

Hell's Kitchen Italia: Hell's Kitchen is an Italian reality television cooking competition (based on the British series of the same name) and American version broadcast on Fox.  The Italian format is broadcast on Sky Uno since 2014.  It is hosted by celebrity chef Carlo Cracco.

Hell's Kitchen (U.S. season 13): Season 13 of the American competitive reality television series "Hell's Kitchen" premiered on September 10, 2014 on Fox.  The prize was a head chef position at Gordon Ramsay's Pub & Grill at Caesars Atlantic City.  Gordon Ramsay returned as head chef and Andi van Willigan and James Avery returned as sous chefs.  However, Jean-Philippe Susilovic did not return as maitre d' and was replaced by Marino Monferrato.  It also marks the first time since 2010 that two seasons of "Hell's Kitchen" aired in the same year.  Kitchen Supervisor La Tasha McCutchen from Winter Haven, Florida won the competition, becoming the first winner since Christina Wilson, Holli Ugalde and Dave Levey to completely avoid nomination for elimination throughout the entire season.  This is also the first time that the series had a new narrator.

Hell's Kitchen (U.S. season 16): The sixteenth season of the American competitive reality television series "Hell's Kitchen" premiered on September 23, 2016 on Fox.  Event Chef Kimberly-Ann "Ryan" Ryan from Traverse City, Michigan won the competition and a head chef position at Yardbird Southern Table & Bar at The Venetian Las Vegas.  In addition to Gordon Ramsay, who returned as host/head chef, Marino Monferrato and Aaron Mitrano returned as maitre d' and blue kitchen sous chef respectively while Andi van Willigan-Cutspec resumed her role as sous chef for the red team after Season 10 winner Christina Wilson filled in for her in the previous season while she got married.  This was also the first season since Season 13 to take a hiatus due to Fox's coverage of the 2016 World Series in addition to the holiday breaks.  The remaining episodes of the season were moved to Thursday nights on January 5, 2017 as part of the network's midseason schedule.

List of Hell's Kitchen episodes: "Hell's Kitchen" is an American reality television cooking competition (based on the British series of the same name) broadcast on Fox.  It is hosted by celebrity chef Gordon Ramsay.  s of 2, 2017 , 250 episodes have aired, concluding the sixteenth season.

Ted Allen: Ted Allen is an American author and television personality.  He was the food and wine connoisseur on the Bravo network's television program "Queer Eye", and has been the host of the TV cooking competition series "Chopped" since its launch in 2009, as well as "Chopped Junior", which began in mid-2015.  In April 13, 2014, he became the host of another Food Network show, originally called "America's Best Cook"; a retooled version of that show, retitled "All-Star Academy," which debuted on March 1, 2015.  In early 2015, he also hosted a four-part special, "Best.  Ever." , which scoured America for its best burgers, pizza, breakfast, and barbecue.  He is a longtime contributing writer to "Esquire" magazine, the author of two cookbooks, and regularly appears on the Food Network show "The Best Thing I Ever Ate" and other television cooking shows.

Hell's Kitchen (U.S. season 14): Season 14 of the American competitive reality television series "Hell's Kitchen" premiered on March 3, 2015 on Fox.  The prize is a head chef position at Gordon Ramsay Pub & Grill in Caesars Atlantic City.  Gordon Ramsay returned as head chef with Andi Van Willigan and James Avery returning as sous chefs for both their respective kitchens as well as Marino Monferrato as the maître d'.  Executive chef Meghan Gill from Roanoke, Virginia, won the competition, thus becoming the fourteenth winner of "Hell's Kitchen".

Dale Talde: Dale Talde (born October 25, 1978 in Chicago, Illinois) is an American chef best known for competing on two seasons of the Bravo reality television cooking competition series "Top Chef": "" in 2008 and "" in 2010-11.  Talde finished in sixth place in both seasons.  He currently runs the eponymous restaurant Talde in Brooklyn, New York.  Talde is Filipino-American.

Hell's Kitchen (U.S. TV series): Hell's Kitchen is an American reality television cooking competition (based on the British series of the same name) broadcast on Fox.  It is hosted by celebrity chef Gordon Ramsay.  Two teams of chefs compete for a job as head chef at a restaurant.

Hell's Kitchen (U.S. season 10): Season 10 of the American competitive reality television series "Hell's Kitchen" premiered on June 4, 2012 on Fox and concluded on September 10, 2012.  Chef de Cuisine Christina Wilson won the season and received a head chef position at Gordon Ramsay Steak at the Paris Las Vegas in the Las Vegas suburb of Paradise, Nevada.

Question: Who is the host of the reality television cooking competition where the prize is a head chef position at Pub & Grill? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "competition_series_name": {
      "type": "string",
      "description": "The name of the reality television cooking competition series."
    },
    "host_name": {
      "type": "string",
      "description": "The name of the host of the competition."
    },
    "prize_details": {
      "type": "object",
      "properties": {
        "position": {
          "type": "string",
          "description": "The job position offered as a prize."
        },
        "restaurant_name": {
          "type": "string",
          "description": "The name of the restaurant where the prize position is located."
        },
        "restaurant_location": {
          "type": "string",
          "description": "The location of the restaurant."
        }
      },
      "required": [
        "position",
        "restaurant_name",
        "restaurant_location"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "competition_series_name",
    "host_name",
    "prize_details"
  ],
  "additionalProperties": false
}
