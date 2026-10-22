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
San Antonio Opera: The San Antonio Opera was an American opera company located in San Antonio, Texas that produced 16 seasons of opera before filing for bankruptcy and dissolving in 2012.  The company was founded as the Pocket Opera of San Antonio in 1997 by Mark Richter, and opened its first season in the fall of 1997 with Wolfgang Amadeus Mozart's "Der Schauspieldirektor" at the San Pedro Playhouse.  Initially the company's productions utilized local artists, but by the 1999-2000 season the company had begun employing internationally recognized artists.  It simultaneously rebranded itself as the Lyric Opera of San Antonio and began performing at the Lila Cockrell Theatre.  The opera company changed its name to the San Antonio Opera a few years later.  Notable artists to have performed with the company include Plácido Domingo, José Carreras, and Andrea Bocelli among others.

Buttrey Food &amp; Drug: Buttrey Food & Drug was a chain of grocery stores founded in Havre, Montana and formerly headquartered in Great Falls, Montana.  The company was founded in 1896 as a chain of department stores branded Buttrey Department Store.  The company opened grocery stores in 1935 and sold off its department store division following a 1966 acquisition by grocery company The Jewel Companies, Inc. Jewel was sold to American Stores in 1984 and Buttrey was sold off as separate company in 1990.  The company was sold to its main competitor, Boise, Idaho based Albertsons, in January 1998 and the Buttrey name was retired.  At that time, Buttrey was operating 44 stores in Montana, Wyoming, and North Dakota with a revenue of US$391.4 million.  As of today, most former Buttrey stores continue to operate under the Albertsons banner.

Rena Maverick Green: Rena Maverick Green (February 10, 1874 – November 29, 1962) was an artist, a suffragist and a co-founder of the San Antonio Conservation Society.  She was a pioneer female member of the San Antonio School Board and served on the board of trustees of the San Antonio Public Library.  She was a preservationist for San Antonio history, including the San Antonio Missions National Historical Park and the saving of many city parks.  Green helped preserve the Spanish Governor's Palace and the San Antonio River Walk.  She was the granddaughter of a signer of the Texas Declaration of Independence, and the widow of a Texas state Senator.

List of San Antonio Spurs head coaches: The San Antonio Spurs are an American professional basketball team based in San Antonio, Texas.  They are a member of the Southwest Division of the Western Conference in the National Basketball Association (NBA).  The franchise was founded as the Dallas Chaparrals of the American Basketball Association (ABA) in 1967.  The team suffered from poor attendance and general disinterest by fans in Dallas, and the name "Dallas" was dropped in favor of "Texas" during the 1970–71 season in an attempt to make the team regional.  This also proved to be a failure, and the team returned full-time to use "Dallas" for the 1971–72 season.  The team was put up for sale after missing the playoffs in the 1972–73 season.  The team was acquired by a group of 36 San Antonio businessmen, led by Angelo Drossos and Red McCombs, who relocated the team to San Antonio, Texas and renamed it to Spurs.  In 1976, the ABA folded, threatening the future of San Antonio's sole professional sports franchise.  The NBA, however, decided to admit four ABA teams into the league, including the Spurs, along with the Denver Nuggets, the Indiana Pacers and the New York Nets.

Terrell Hills, Texas: Terrell Hills is a city in Bexar County, Texas, United States; it is located 5 mi northeast of downtown San Antonio.  As of the 2010 census Terrell Hills had a population of 4,878.  It is part of a group of three cities — Terrell Hills, Alamo Heights, and Olmos Park — located between Uptown San Antonio, Midtown San Antonio, Downtown San Antonio, and Fort Sam Houston (a U.S. Army post).  Terrell Hills is bordered on the west by Alamo Heights, on the east by Fort Sam Houston, on the north by Uptown San Antonio, and on the south by San Antonio's Near East Side.  It is part of the San Antonio Metropolitan Statistical Area.

H-E-B Mexico: H-E-B, a grocery company based in San Antonio, Texas, USA, operates 51 stores in México.  It competes mainly with Soriana, Walmart México, S-Mart, Chedraui and Casa Ley.

Carl Wilhelm August Groos House (San Antonio): The Carl Wilhelm August Groos House is located in the Bexar County city of San Antonio in the U.S. state of Texas.  It was designated a Recorded Texas Historic Landmark in 1977.  Designed by Alfred Giles in 1880, the building contractor was John H. Kampmann.  Giles used a Victorian Gothic Revival on this limestone home.  Groos had immigrated from Germany to Texas in 1848, at which time he and his brothers started a freighting firm.  In 1871, he built the Carl W. A. Groos House in New Braunfels.  In 1872, he and his family settled in San Antonio.  Groos married Hulda Amalie Moureau and became a founding member of the Groos National Bank.  In 1880, Groos hired Giles to build his San Antonio home.  It is listed on the National Register of Historic Places listings in Bexar County, Texas as a contributing structure of the King William Historic District .  Groos died in 1893 and is interred at San Antonio City Cemetery No. 1.  In 1957, the house was purchased by the San Antonio Council of the Girl Scouts of the USA.  The Girl Scouts sold the home to Charles Butt.  It has been restored and is in private ownership.

Manzanita Sol: Manzanita Sol is a brand of apple-flavored soft drinks owned by PepsiCo and is predominant in Mexico.  In the United States it is sold in 12-pack cans, 2-liter, and 20-ounce bottles.  The drink is known to be available at Walmart, Albertsons, H-E-B, Ralphs, Kmart, Food 4 Less, Jewel-Osco, Dominick's, Target, Vons, Stater Bros., United Supermarkets in the Amarillo and Lubbock, Texas area, and other smaller chains and smaller family run stores.  In Latin American countries, Manzanita Sol will compete with The Coca-Cola Company's Manzana Lift.  Manzanita Sol is PepsiCo's number two brand in Mexico, with apple being Mexico's second most popular soft drink flavor.  It is also very popular in the borderlands such as the El Paso/Juarez border.

H-E-B: HEB Grocery Company, LP, also known as HEB Grocery Stores, is an American privately held supermarket chain based in San Antonio, Texas, with more than 350 stores throughout the U.S. state of Texas, as well as in northeast Mexico.  The company also operates Central Market, an upscale organic and fine foods retailer.  As of 2013, the company has a total revenue surpassing $20 billion USD (2013).  H-E-B ranked No. 15 on Forbes' 2014 list of "America's Largest Private Companies."  H-E-B was named Retailer of the Year in 2010 by "Progressive Grocer".  "Supermarket News" ranked H-E-B No. 13 in the 2008 "Top 75 North American Food Retailers."  Based on 2014 revenues, H-E-B is the twentieth largest retailer in the United States.  It donates 5 percent of pre-tax profits to charity.  Until 1976, it was closed on Sundays and did not sell alcohol.

Central Market (Texas): Central Market is an American gourmet grocery store chain owned by H-E-B Grocery Company based in San Antonio, Texas.  It specializes in high-quality, hard-to-find gourmet foods.  Most locations also have a full-service kitchen, offer cooking and wine classes in their culinary school, and offer catering services.  The chain has nine locations, all in Texas.  Central Market was named "Outstanding Specialty Food Retailer" by "Specialty Food Magazine" and the National Association for Specialty Food Trade.

Question: What is the name of  Grocery Company based in San Antonio, Texas where Manzanita Sol is also sold? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the grocery company."
    },
    "headquarters_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the company is headquartered."
        },
        "state": {
          "type": "string",
          "description": "The state where the company is headquartered."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "product_sold": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the product sold at the company."
        },
        "is_available": {
          "type": "boolean",
          "description": "Indicates if the product is available at this company."
        }
      },
      "required": [
        "name",
        "is_available"
      ],
      "additionalProperties": false
    },
    "company_attributes": {
      "type": "object",
      "properties": {
        "is_privately_held": {
          "type": "boolean",
          "description": "True if the company is privately held."
        },
        "stores_in_texas_count_description": {
          "type": "string",
          "description": "Description of the number of stores in Texas."
        },
        "stores_in_mexico_count": {
          "type": "integer",
          "description": "The number of stores the company operates in Mexico."
        }
      },
      "required": [
        "is_privately_held",
        "stores_in_texas_count_description",
        "stores_in_mexico_count"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "company_name",
    "headquarters_location",
    "product_sold",
    "company_attributes"
  ],
  "additionalProperties": false
}
