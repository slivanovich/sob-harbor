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
Apocalypse (Six Flags America): Apocalypse is a steel stand-up roller coaster located at Six Flags America in Prince George's County, Maryland.  The ride made its debut in 1990 as Iron Wolf at Six Flags Great America before being relocated to Six Flags America and renamed to Apocalypse.  The roller coaster was the first built by Swiss manufacturer Bolliger & Mabillard.  When known as Iron Wolf, the roller coaster held the records of the highest (100 ft ) and fastest (55 mph ) stand-up looping roller coaster in the world before losing them to other roller coasters in 1992 and 1996.

Temple of the Night Hawk: Temple of the Night Hawk is an enclosed roller coaster located at Phantasialand.  Founded in 1988 after 18 months of construction, the ride was originally called ‘'Space Center'’.  The ride led passengers past models of rockets and emulated asteroids and the darkened hall was dimly lit with thousands of tiny spots of light to resemble stars.  Due to the construction of the neighbouring Wurze Town in 2001, the roller coaster was redeveloped with a fantasy jungle theme and was renamed as the "Temple of the Night Hawk".  The roller coaster is now completely dark.  Until 2006 there were some green moving lights and strobe lights in the first lifthill, still present today, but not operational.  In 2008 the Lights on the coaster trains were turned off or broke down and have never been repaired since then.  Till 2010 there was a green laser projection with the outlines of a flying hawk and until June 2012, there were some red strobe-lights at the final brakerun.  In 2011, the park installed new strobe lights in the first lifthill, which broke down after about two months, and were never repaired since then.  The ride has four trains and one spare train for repairs each with seven cars.  Each car has two rows of seats each holding two people.  During the four-minute ride time the trains are lifted by three lift hill chains, 1.174 metres of track.  The roller coaster is therefore one of the longest indoor roller coasters in the World, slightly beaten by "Mindbender" in Galaxyland Amusement Park, Canada.  The hall in which the track is located is around 120,000m³ in size and rests on 180 concrete pillars which are 12 metres deep in the ground.  In the basement of the hall is the ‘'Hollywood Tour’' darkride.  The total investment for the ride was around 15 million DM.

Rollo Coaster: Rollo Coaster is a wooden roller coaster located at Idlewild and Soak Zone near Ligonier, Pennsylvania.  It was built in 1938 by the leading roller coaster builder of that era, the Philadelphia Toboggan Coasters.  It was Idlewild's first and only roller coaster for decades until the larger Wild Mouse coaster was erected in 1993.

Leviathan (roller coaster): Leviathan is a steel roller coaster in the Medieval Faire section of the park at Canada's Wonderland in Vaughan, Ontario, Canada.  It is the first roller coaster designed by Swiss firm Bolliger & Mabillard to exceed a height of 300 ft , putting it in a class of roller coasters commonly referred to as "giga".  At 5486 ft long, 306 ft tall, and with a top speed of 92 mph , Leviathan is the tallest and fastest roller coaster in Canada.  s of 2015 , Leviathan is ranked as the eighth-tallest, and the eighth-fastest roller coaster in the world, and the third-tallest traditional lift-style coaster in the world.  It was the 16th roller coaster to be built at Canada's Wonderland, and the ride's track was completed in February 2012, with the first test run being completed on 15 March 2012.  The coaster opened to season pass holders on 27 April 2012, and to the general public on 6 May 2012.

Intamin: Intamin Worldwide is a designing and manufacturing company in Wollerau, Switzerland.  It is best known for creating thrill rides and roller coasters worldwide.  The Intamin brand name is an abbreviation for "international amusement installations".  The company has offices throughout the world including three in Europe, three in Asia and two in the United States.

Roller Coaster (Dam Sen Park): Roller Coaster (Vietnamese: Tàu Lượn Siêu Tốc) is a steel roller coaster located at Dam Sen Cultural Park in Ho Chi Minh City, Vietnam.  Built in 1998, it is the first roller coaster in Vietnam.  Until the opening of a similar roller coaster at Đại Nam Văn Hiến which has 4 inversions, the Dam Sen roller coaster had the most inversions in Vietnam.

Wild Cat (Hersheypark): The Wild Cat (initially The Joy Ride) was a wooden roller coaster located at Hersheypark in Hershey, Pennsylvania, United States.  The roller coaster was constructed in 1923 by the Philadelphia Toboggan Company (PTC).  Under an agreement between Hersheypark and PTC, Hersheypark leased the land the coaster occupied, while PTC owned and operated the coaster.  The agreement was for 15 years, at which point they had the option to extend the contract.  The contract was ultimately extended to 1945.  The roller coaster operated from June 16, 1923, through September 1945.  PTC and Hershey Park elected to close The Wild Cat and construct a new roller coaster in 1946.

Stealth (roller coaster): Stealth is a steel roller coaster located in the Amity area of Thorpe Park in Surrey, England, UK.  Built and designed by Intamin of Switzerland for £12 million, the Accelerator Coaster model opened in 2006.  Riders reach a maximum height of 62.5 m and accelerate from 0-80 mph in 1.9 seconds.  It has the fastest acceleration of any coaster in the UK, and is the tallest among launch coasters in the country.  At the base of the top hat element on either side, riders may experience up to 4.5 G.

Griffon (roller coaster): Griffon is a steel Dive Coaster roller coaster located at the Busch Gardens Williamsburg amusement park in James City County, Virginia, United States.  Designed by Bolliger & Mabillard, it is 205 ft high, and is the second-fastest (71 mph ) Dive Coaster built.  The roller coaster features two Immelmann loops, a splashdown, two vertical drops and was the first of its kind to use floorless trains.  Griffon was announced to the public on August 23, 2006 and opened on May 18, 2007 to positive reviews by both newspapers and enthusiasts.  In 2007, "Amusement Today"' s annual Golden Ticket Awards voted it the third-best new steel roller coaster of that year and the 27th-best steel roller coaster.  It was voted the 33rd-best steel roller coaster in 2013.

The New Revolution (roller coaster): The New Revolution (formerly known as Revolution, Great American Revolution, and La Revolución) is a steel roller coaster located at Six Flags Magic Mountain in Valencia, California.  Manufactured by Anton Schwarzkopf and designed by Werner Stengel, the roller coaster opened to the public on May 8, 1976.  The New Revolution is the world's first modern roller coaster to feature a vertical loop and has been recognized for that accomplishment by American Coaster Enthusiasts (ACE), who awarded the roller coaster its Coaster Landmark status.

Question: In which Swiss city is the builder and designer the Stealth roller coaster located?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "roller_coaster_name": {
      "type": "string",
      "description": "The name of the roller coaster."
    },
    "designer_company": {
      "type": "string",
      "description": "The name of the company that designed and built the roller coaster."
    },
    "company_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the company is located."
        },
        "country": {
          "type": "string",
          "description": "The country where the company is located."
        }
      },
      "required": [
        "city",
        "country"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "roller_coaster_name",
    "designer_company",
    "company_location"
  ],
  "additionalProperties": false
}
