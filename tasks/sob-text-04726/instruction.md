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
Biagi-DenBeste Racing: Biagi-DenBeste Racing, originally Biagi Brothers Racing, is an American professional stock car racing team that currently competes in the NASCAR Xfinity Series.  The team is based in Mooresville, North Carolina.  The team currently fields the No. 98 Ford Mustang part-time for Aric Almirola and Casey Mears.

Ford Street Racing: Ford Street Racing is a game commissioned by Ford for the Xbox, PC, PlayStation 2 and PSP.  The game was sold as Ford Street Racing on the PC while the various console releases were given region specific names.  They are as follows: Ford Bold Moves Street Racing in the US and Canada, Ford Street Racing: LA Duel in the EU, and Ford Street Racing - XR Edition in Australia and New Zealand.  It was released September 19, 2006 in the United States.  It was developed by Razorworks and published by Empire Interactive under the Empire banner in the US and under the Xplosiv banner in the rest of the world.

Holman Moody: Holman-Moody was an American auto racing team, racecar manufacturer, and marine engine manufacturer.  The company currently operates out of Charlotte, North Carolina, but is no longer a race team.  Holman-Moody continues to manufacture racing vehicles using vintage parts and methods, along with special editions of modern Ford sports cars.  The race team built virtually all of the factory Ford racing vehicles of the 1950s, 1960s, and 1970s.  It owned race-cars that competed in NASCAR, drag racing, ocean boat racing, rallies, and sports car racing.  The team won NASCAR championships in 1968 and 1969 with driver David Pearson and also the 1967 Daytona 500 with Mario Andretti.  Their most recognized trademark is "Competition Proven."

Colchester Racing Developments: Colchester Racing Developments produced Merlyn racing cars from 1960 to 1979.  The company was founded by Selwyn Hayward and continued by his brother Clive Hayward.  When the manufacture of Merlyn racing cars stopped, Clive continued to manufacture Merlyn parts as CRD Tool and Engineering Ltd.  CRD Tool and Engineering stopped trading in November 2015, Clive Hayward continues to run Colchester Racing Developments, manufacturing Merlyn components and carrying out chassis repairs.

Ford Mustang: The Ford Mustang is an American car manufactured by Ford.  It was originally based on the platform of the second generation North American Ford Falcon, a compact car.  The original 1962 Ford Mustang I two-seater concept car had evolved into the 1963 Mustang II four-seater concept car which Ford used to pretest how the public would take interest in the first production Mustang.  The 1963 Mustang II concept car was designed with a variation of the production model's front and rear ends with a roof that was 2.7 inches shorter.  Introduced early on April 17, 1964 (16 days after the Plymouth Barracuda), and thus dubbed as a "1964½" by Mustang fans, the 1965 Mustang was the automaker's most successful launch since the Model A.  The Mustang has undergone several transformations to its current sixth generation.

Changan Ford: Changan Ford (officially Changan Ford Automobile Co., Ltd.) is an automotive manufacturing company headquartered in Chongqing, China and a 50:50 joint venture between Changan Automobile and Ford Motor Company.  The company's principal activity is the manufacture of Ford brand passenger cars for the Chinese market.  The company was formed in Dec. 2012 after the decision to restructure Changan Ford Mazda, whereby Ford and Mazda agreed to work with Changan as separate joint ventures.  Currently, Changan Ford's entire production base is the largest manufacturing location outside Detroit, Michigan for Ford.  It has plants in Chongqing, Hangzhou & Harbin.

Ford Racing (series): Ford Racing is a racing video game series with titles released for systems including the PlayStation, PlayStation 2, PC and Xbox.  The games in the "Ford Racing" series all center around racing modern and vintage Ford cars and trucks through specifically designed tracks, while competing against computer-driven (and sometimes player-driven) opponents.  There are currently four games in the series with the latest title, "Ford Racing: Off Road", being released on July 29, 2008.

Greyhound racing: Greyhound racing is an organized, competitive sport in which greyhound dogs are raced around a track.  There are two forms of greyhound racing, track racing (normally around an oval track) and coursing.  Track racing uses an artificial lure (now based on a windsock) that travels ahead of the dogs on a rail until the greyhounds cross the finish line.  As with horse racing, greyhound races often allow the public to bet on the outcome.  In coursing the dogs chase a "lure" (originally a live hare or rabbit that could be killed by the dog).

Henry Ford Company: The Henry Ford Company was the second company for Henry Ford, founded November, 1901.  It resulted from the reorganization of the Detroit Automobile Company, his first unsuccessful attempt at automobile manufacture a year before.  In March 1902, Ford left the company following a dispute with his financial backers, William Murphy and Lemuel Bowen, as Ford was devoting considerable time to the sport of auto racing and his Ford 999 race car.  In a final settlement, Ford left with his name and US $900; he went on to start the Ford Motor Company in 1903 at the Ford Mack Avenue Plant.

Robert Boyer (chemist): Robert Allen Boyer (September 30, 1909 in Toledo, Ohio – November 11, 1989 in Dunedin, Florida) was a chemist employed by Henry Ford, he was extremely proficient at inventing ways to convert soybeans into paints and plastic parts used on Ford automobiles.Robert Allen Boyer, your average “B” chemistry student was given an extraordinary opportunity that changed his future and the future of automobile production in the U.S. (Plastic) Boyer, born on 30 September 1909 in Toledo, Ohio was given this chance when Ford hired his father to run the nation's oldest hotel, the Wayside Inn, in South Sudbury, Massachusetts.  Ford frequented the inn and that is where Boyer was discovered.  Ford claimed that Boyer had a “keen active mind”.  He asked Boyer to enroll in the new Henry Ford Trade School and participate in its unique work-study program instead of following his plans to enter Andover prep school and then Dartmouth College (Shurtleff).  Boyer excelled in the Ford Trade School and took to exploring concepts such as how to manufacture synthetic wool from soybeans.  These were the types of problems that stumped the experts (Plastic).  Boyer graduated the Ford Trade School at the age of 21 with a promising chemistry career in front of him.  He started this career as the head of the soybean lab at the Edison Institute (Shurtleff).  Here Boyer’s career took off.  He started working to use soybeans in ways they had never been used before.  Boyer has done things from extracting lubricating and paint oils from the soybean to creating a synthetic wool made from soybeans and pressing insulating varnish for starters and generators (Plastic).  One of Boyer’s first projects began in 1932 and included building “a small solvent extractor to separate the bean into soy oil and protein-rich meal” (Shurtleff).  The soybean oil became the most crucial commercial soy products on Ford cars.  In 1934 the five to eight coats of lacquer that cars previously had been finished with was replaced with a synthetic baked enamel paint which contained about 35% soy oil.  This new synthetic paint with soy oil saved considerable time and money.  In 1937, Boyer developed a curved plastic sheet which he hoped would replace steel in the auto bodies of ford cars.  He was so confident in his product that he took an axe to it in the middle of a crowd of reporters and critics.  He also jumped up and down on the curved sheet.  When there was no bending in the sheet and no shattering due to the axe and the weight of him jumping on the sheet, people were astounded (shurtleff).  This soy protein plastic sheet consist of 70% cellulose and 30% resin binder pressed into cloth.  “The new rust-free, dent-proof plastic was reportedly 50% lighter and 50% cheaper to produce than steel” (Shurtleff).  This new plastic body cut the total weight of the car from 3,000 lb.  to 2,000 (Dearborn).  The sheets look like polished steel and can be bent but just snap back into place, therefor when caught in fender benders, the fender would bounce back like “rubber balls” (Shurtleff).  Needless to say, this product was a breakthrough in the world of automobile production.  Boyer also used the soy isolates to produce the world's first plant protein fiber in 1938.  (Shurtleff.)  This fiber resembled a soft wool, it was tan in color, had a medium luster and a soft warm feel.  “it has 80% the strength of wool, took the same dyes, had good elongation, and did not wet as easily as wool.” (Shurtleff).  Boyer figured this fiber could be used for upholstery in cars, filling in felt hats, or for clothing.  Boyer changed the way the soybean was used and created innovative products we use daily.

Question: What does Ford manufacture, that BIagi-DenBest Racing uses?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "user_entity_name": {
      "type": "string",
      "description": "The name of the entity that uses the manufactured product."
    },
    "manufacturer_name": {
      "type": "string",
      "description": "The name of the company that manufactures the product."
    },
    "product_name": {
      "type": "string",
      "description": "The name of the product manufactured by Ford."
    },
    "product_type": {
      "type": "string",
      "description": "The general type or category of the product."
    },
    "racing_series_used_in": {
      "type": "string",
      "description": "The racing series in which the product is used by the entity."
    }
  },
  "required": [
    "user_entity_name",
    "manufacturer_name",
    "product_name",
    "product_type",
    "racing_series_used_in"
  ],
  "additionalProperties": false
}
