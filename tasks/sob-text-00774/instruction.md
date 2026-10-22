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
Heaven Hill: Heaven Hill Distilleries, Inc. is an American, private family-owned and operated distillery company headquartered in Bardstown, Kentucky that produces and markets the Heaven Hill brand of Kentucky Straight Bourbon Whiskey and a variety of other distilled spirits.  Its current distillery facility, called the Heaven Hill Bernheim distillery, is in Louisville, Kentucky.  It is the seventh-largest alcohol supplier in the United States, the second-largest holder of bourbon whiskey inventory in the world, the largest independent family-owned and operated producer and marketer of distilled spirits in the United States, and the only large family-owned distillery company headquartered in Kentucky (not counting the Brown-Forman Corporation, which is publicly traded but more than two-thirds family-controlled, or the Sazerac Company, which is family-owned but headquartered in Louisiana).

Candi Kubeck: Candalyn "Candi" Kubeck (née Chamberlain, May 10, 1961May 11, 1996) was an American commercial airline pilot and the captain of ValuJet Flight 592.  This flight crashed in the Everglades on May 11, 1996, after oxygen generators illegally placed in a cargo hold started and maintained a fire that disrupted aircraft functionality and flooded the cabin and cockpit with smoke.  The crash made Kubeck the first female captain to die in a commercial airline crash.

Lufthansa Flight 592: Lufthansa Flight 592 was a regularly scheduled passenger flight from Frankfurt, Germany to Addis Ababa, Ethiopia that was hijacked on February 11, 1993.  The Lufthansa-operated Airbus A310-300 was hijacked by Nebiu Demeke, an Ethiopian man seeking asylum who forced the pilot to fly to New York City's John F. Kennedy International Airport.  The aircraft landed safely, and the gunman surrendered peacefully and without incident.  He was charged with air piracy in United States district court, and was sentenced to 20 years in prison.

Universal Weather and Aviation: Universal Weather and Aviation, Inc. (commonly called Universal or Universal Weather) is a privately held company headquartered in Houston, Texas that provides products and services for the general aviation industry.  Its customers include owners and operators of business jets for corporate and personal air travel.  The company offers products and services including international flight planning and scheduling, weather briefings, fueling programs, aircraft ground handling, and aviation security.  It is the oldest company in the corporate flight planning industry.

SimCraft: SimCraft is a privately held company headquartered just outside Atlanta, Georgia and is in the business of motion simulation.  The company offers a range of products in the category of full motion simulation that provide a tactile true motion experience for Motorsport Simulation (sometimes referred to as simracing) and flight simulation.  The company's core innovation and technology is the simulation of vehicle (motorsport & aviation based) movement through proprietary physics based software interfaces and a patent pending hardware architecture based on Center of Mass principles of motion.  The company's product applications range principally by variation in chassis design and material and are found in usage from military training/research, professional training, to individual simulation and gaming enthusiast entertainment.

Red Food: Red Food Stores, Inc. (or simply Red Food) was a supermarket chain company headquartered in Chattanooga, Tennessee.  It operated stores mostly in northwest Georgia, northeast Alabama, and southeast Tennessee.  Around 55 stores were operated in the same three states.  According to The Chattanoogan, Red Food was a longtime icon in Chattanooga history.

Flying Blind, Flying Safe: Flying Blind, Flying Safe is a non-fiction book about the American airline industry and Federal Aviation Administration, written by Mary Schiavo with Sabra Chartrand.  The book was first published in March 1997 in hardcover format by Avon Books.  An updated paperback edition was published on April 1, 1998.  Schiavo is a former Inspector General of the United States Department of Transportation, and Chartrand a journalist for "The New York Times".  Schiavo was Inspector General of the United States Department of Transportation for six years, and resigned in 1996 shortly after the ValuJet Flight 592 airline crash in the Florida Everglades.  She became a whistleblower and was highly critical of the airline industry and its relationship with aviation safety agencies in the United States federal government.

ValuJet Airlines: ValuJet Airlines was an American low-cost carrier, headquartered in unincorporated Clayton County, Georgia, that operated regularly scheduled domestic and international flights in the Eastern United States and Canada during the 1990s.  The company was founded in 1992 and was known for its sometimes dangerous cost-cutting measures.  All of the airline's planes were purchased used from other airlines, very little training was provided to workers, and contractors were used for maintenance and other services.  The company quickly developed a reputation for its lax safety.  In 1995, the military refused ValuJet's bid to fly military personnel over safety worries, and officials at the FAA wanted the airline to be grounded.

ValuJet Flight 592: ValuJet Flight 592 was a regularly scheduled flight from Miami International Airport to Hartsfield-Jackson Atlanta International Airport.  On May 11, 1996, the ValuJet Airlines McDonnell-Douglas DC-9 operating the route crashed into the Everglades about 11 minutes after taking off from Miami as a result of a fire in the cargo compartment caused by improperly stored cargo.  All 110 people on board perished.  The airline already had a poor safety record before the crash, and the accident brought widespread attention to the airline's problems.  The airline was grounded for several months after the accident.  When operations resumed, ValuJet's reputation was so tarnished that it was forced to merge with AirTran Airways and rebrand itself as such to stay in business.  To date, the accident remains the deadliest in the history of Florida.

Urjanet, Inc.: Urjanet is an energy data company headquartered in Atlanta, Georgia.  The company develops and markets a form of big data coming from utilities.  Urjanet offers data-as-a-service products that enable organizations to understand their energy usage, which is fundamental to reducing energy costs and carbon emissions.  The company was founded in 2009 by Sanjoy Malik at the Georgia Tech VentureLab.  After Malik secured a National Science Foundation (NSF) grant, Urjanet graduated to the Advanced Technology Development Center (ATDC), then in 2013 after successfully raising $6.5 million in venture capital moved to the company's current location in Midtown Atlanta.  The company is funded with support from the Georgia Research Alliance, Imlay Investment, Grotech Ventures, Correlation Ventures, and Osage Venture Partners.

Question: ValuJet Flight 592 was operated by the company headquartered in what Georgia location?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "airline_name": {
      "type": "string",
      "description": "The name of the airline that operated the flight."
    },
    "flight_number": {
      "type": "string",
      "description": "The identifier for the specific flight."
    },
    "headquarters_location": {
      "type": "object",
      "properties": {
        "county": {
          "type": "string",
          "description": "The county where the airline's headquarters was located."
        },
        "state": {
          "type": "string",
          "description": "The state where the airline's headquarters was located."
        }
      },
      "required": [
        "county",
        "state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "airline_name",
    "flight_number",
    "headquarters_location"
  ],
  "additionalProperties": false
}
