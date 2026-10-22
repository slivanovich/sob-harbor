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
Big Sky Brewing Company: Big Sky Brewing Company is a brewery located in Missoula, Montana, USA.  It brews six different styles of beer: Moose Drool (a brown ale), Scape Goat (Pale Ale), Big Sky (India Pale ale), Powder Hound (Winter Ale), Summer Honey (Seasonal Ale), and Trout Slayer Ale.

Genesee Brewing Company: Genesee Brewing Company is an American brewery located along the Genesee River in Rochester, New York.  In 1878, Genesee Brewing Company moved up into Rochester.  From 2000 to 2009, the company was known as the High Falls Brewing Company.  In 2009, High Falls was acquired by the capital investment firm KPS Capital.  Together with also newly acquired Labatt USA, KPS merged the two companies as North American Breweries.  Along with this change, High Falls Brewery changed its name back to the original "Genesee Brewing Company" operating under the North American Breweries name.  In October 2012, North American Breweries was purchased by FIFCO

Rocket Republic Brewing Company: Rocket Republic Brewing Company, Inc. is a craft brewery located in Madison, Alabama incorporated in Alabama in March 2013.  The brewery received their state ABC license in July 2013 and successfully launched their beers on September 6, 2013.  The launch day was held at The Nook, a beer bar in Huntsville, Alabama and launch beers were Vapor Trail Cream Ale and Astronut Brown Ale.  Rocket Republic is owned by Eric Crigger (brewer), Tatum Crigger, John Troy and Lynn Troy.

Cream ale: Cream ale is a style of American and Canadian beer, of which examples are often light in color and are well attenuated.  First crafted in the mid-1800s at various breweries in the United States, and in Canadian breweries such as Sleeman, cream ale remained a very localized form with different styles until the early 20th century.  During Prohibition in the United States, a great number of Canadian brewers took up brewing cream ale, refining it to some degree.  Following the end of Prohibition in the United States, cream ale from Canada became popular and the style was produced anew in both nations.

Korn (liquor): Korn (from German, "grain", "Brit. " "corn") also known as Kornbrand or Kornbranntwein (English: "grain brandy" or "grain spirit"), is a German colorless distilled beverage produced from fermented cereal grain seed.  In the production of "Korn" only the cereal grain types rye, wheat, barley, oat and buckwheat are permissible.  Most of the production is based on rye or wheat; barley and buckwheat are rarely used.  Barley is mainly used to obtain the required malt for the brewing process.  The addition of food color, flavorings, or sweeteners is not permitted.  Korn differs from vodka in that it is distilled to lower alcoholic proofs and less rigorously filtered, which leaves more of the cereal grain flavor in the finished spirit.

OpenRoad Brewery: OpenRoad Brewery is a brewery and tap room in Wayland, Michigan.  OpenRoad brews a variety of craft beers, including the Road Rage Double IPA, I.P.A. Lot, Citradisiac Pale Ale, My Coffee Stout, Bumpy Ride Brown, 90 mph IPA, Pennywise Porter, Good Rye-Brations IPA, Yell-Ale Submarine and Campout Cream Ale.  Several seasonal and experimental brews are planned.  The brewery opened in 2016.

Swamp Head Brewery: Swamp Head Brewery is a brewery in Gainesville, Florida and is frequented by graduate and professional students, faculty, and locals.  Year-round offerings include Wild Night Honey Cream Ale, Cottonmouth Belgian Witbier, Stump Knocker Pale Ale, Midnight Oil Oatmeal Coffee Stout, and Big Nose IPA along with many different seasonal and limited release beers.  Swamp Head brews their beer using a 30 Barrel brewhouse (930 Gallons) and is located on SW 34th Street just south of Archer Road and near I-75 in Gainesville, Fl.

Cameron's Brewing Company: Cameron's Brewing Company is a brewery just outside Toronto in Oakville, Ontario, Canada.  Founded in 1997, Cameron's produces many different beers including 4 core beers, Cameron's Cream Ale, Cameron's Auburn Ale, Cameron's Lager and Cameron's RPA (Rye Pale Ale).

Kentucky common beer: Kentucky Common Beer is a once-popular style of ale from the area in and around Louisville, Kentucky from the 1850s until Prohibition.  This style is rarely brewed commercially today.  It was also locally known as "Dark Cream Common Beer", "Cream Beer" or "Common Beer".  The beer was top-fermented and wasn't krausened, i.e., it was fermented once and sent out for sale which meant the gravity would be moderate, the carbonation low and the taste full and sweetish.  Like cream ale, it was consumed fresh, usually as draught beer.  In 1913 it was estimated that 80% of the beer consumed in Louisville was of this type.  Many local breweries made this style of beer exclusively.

Genesee Cream Ale: Genesee Cream Ale is a cold fermented, alcohlic beverage produced by the Genesee Brewing Company in Rochester, NY.  It is a light bodied ale.  It was first introduced in late 1960.  Genesee's brewmasters take an extra step of kräusening, a process in which finished beer is primed for carbonation with wort instead of sugar.

Question: Genesee Cream Ale is a cold fermented, alcohlic beverage produced by a brewery located along which river ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "beverage_name": {
      "type": "string",
      "description": "The name of the alcoholic beverage."
    },
    "producing_brewery": {
      "type": "string",
      "description": "The name of the brewery that produces the beverage."
    },
    "brewery_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the brewery is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the brewery is located."
        },
        "river_name": {
          "type": "string",
          "description": "The name of the river along which the brewery is located."
        }
      },
      "required": [
        "city",
        "state",
        "river_name"
      ],
      "additionalProperties": false
    },
    "fermentation_process": {
      "type": "string",
      "description": "The method of fermentation used for the beverage."
    }
  },
  "required": [
    "beverage_name",
    "producing_brewery",
    "brewery_location",
    "fermentation_process"
  ],
  "additionalProperties": false
}
