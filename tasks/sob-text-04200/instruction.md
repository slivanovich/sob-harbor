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
Odawa Casino Resort: Odawa Casino Resort is a Northern Michigan casino resort.  Located in Resort Township near Petoskey, Michigan, the casino opened for business on June 20, 2007.  It is owned and operated by the Little Traverse Bay Bands of Odawa Indians.  The resort replaced Victories Casino in 2007, which had served as the tribe's casino until the new resort was opened.  In addition to gaming, Odawa Casino Resort features multiple restaurants and retail outlets, a concert venue (Ovation Hall), a nightclub (The O Zone Nightclub), and a circular lounge bar in the middle of the gaming floor (Rendezvous).  The resort also includes a AAA Diamond rated Hotel.  Full shuttle transportation is available to all resort guests.  Odawa Casino Resort is open to guests of all ages, however, the casino's gaming floor and the O Zone Nightclub are restricted to those of age 21 and older.  Starting in 2011, the minimum gaming age at Odawa Casino Resort has been approved to be lowered to 19 years old.

CityCenter: CityCenter (also known as CityCenter Las Vegas) is a 16797000 sqft mixed-use, urban complex on 76 acre located on the Las Vegas Strip in Paradise, Nevada.  The project was started by MGM Resorts International; Dubai World became a joint partner during the project's construction phase.  It is the largest privately funded construction project in the history of the United States.  The project is connected by a people mover system to adjacent MGM properties Monte Carlo Las Vegas and Bellagio Las Vegas.  As of 2015, the "CityCenter" branding has been largely retired, with the focus instead on the Aria brand of the development's centerpiece property in names such as the "Aria Express" (formerly "CityCenter Tram") and "Aria Art Collection" (formerly "CityCenter Art Collection").

Corey I. Sanders: Corey Sanders has served as Chief Operating Officer of MGM Resorts International since June 2010.  He oversees operations at the Company’s wholly owned properties, which in Nevada include Bellagio (resort), MGM Grand Las Vegas, Mandalay Bay, The Mirage, New York-New York Hotel and Casino, Monte Carlo Resort and Casino, Luxor Las Vegas, Excalibur Hotel and Casino, Circus Circus Las Vegas, Circus Circus Reno, Gold Strike Jean and Railroad Pass Casino.  He also oversees Beau Rivage (Mississippi) in Biloxi and Gold Strike Tunica, both in Mississippi, as well as MGM Grand Detroit.

The Venetian Macao: The Venetian Macao () is a luxury hotel and casino resort in Macau owned by the American Las Vegas Sands company.  The Venetian is a 39-story, casino hotel on the Cotai Strip in Macau.  The 10500000 sqft Venetian Macao is modeled on its sister casino resort The Venetian Las Vegas, and is the seventh-largest building in the world by floor area.  The Venetian Macao is also the largest casino in the world, and the largest single structure hotel building in Asia.

MGM Grand Detroit: The MGM Grand Detroit in Detroit, Michigan, is one of three casino resort hotels in the city, and one of four in the Detroit–Windsor area.  The luxury resort hotel opened on July 29, 1999, with a grand event which included models and celebrities including Ashanti, Kid Rock, and fireworks.  It is the first luxury casino resort hotel in a major metropolis outside of Las Vegas.  Detroit is one of the largest American cities and metropolitan regions to offer casino resort hotels.

Aria Resort and Casino: Aria Resort and Casino is a luxury resort and casino, part of the CityCenter complex on the Las Vegas Strip in Paradise, Nevada.  Aria consists of two curved glass and steel highrise towers adjoined at the center.  It opened on December 16, 2009 as a joint venture between MGM Resorts International and Infinity World Development.  At 4000000 sqft and 600 ft in height, it is the largest and tallest structure at CityCenter.

Gold Strike Casino Resort: Gold Strike Casino Resort (formerly Circus Circus Tunica) in Tunica Resorts, Mississippi is an MGM Resorts International resort located 20 minutes south of Memphis, Tennessee.

The Palazzo: The Palazzo is a luxury hotel and casino resort located on the Las Vegas Strip in Paradise, Nevada.  It is the tallest completed building in Nevada.  Designed by the Dallas based HKS, Inc., the hotel offers luxury in an Italian Renaissance ambiance.  The hotel and casino are part of a larger complex (operated as one hotel) comprising the adjoining Venetian Resort and Casino and the Sands Convention Center, all of which are owned and operated by the Las Vegas Sands Corporation.

MGM Resorts International: MGM Resorts International is a global hospitality and entertainment company operating destination resorts in Las Vegas, Mississippi, New Jersey and Detroit, including Bellagio, MGM Grand, Mandalay Bay and The Mirage.  The company recently opened MGM National Harbor in Maryland and is developing MGM Springfield in Massachusetts.  It has a majority interest in MGM China Holdings Limited, which owns the MGM Macau resort and casino and is developing a gaming resort in Cotai.  MGM Resorts owns 50 percent of CityCenter in Las Vegas, which features ARIA Resort & Casino.  It has a majority controlling interest in MGM Growth Properties, a real estate investment trust.

Mount Airy Casino Resort: The Mount Airy Casino Resort is a casino and hotel located in Mount Pocono, Pennsylvania.  The casino resort has 188 hotel rooms, a 62000 sqft casino with 1,800 slot machines and table games, four restaurants, a spa and salon, a nightclub and an 18-hole golf course.  Mount Airy Casino and Resort is one of two AAA 4 Diamond Casino Resorts in Pennsylvania, the other being the Sands Casino Resort Bethlehem.

Question: What percentage of CityCenter in Las Vegas does the owner of Gold Strike Casino Resort  own?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_name": {
      "type": "string",
      "description": "The name of the entity that owns CityCenter."
    },
    "ownership_percentage": {
      "type": "integer",
      "description": "The percentage of CityCenter owned by the specified entity."
    },
    "citycenter_location": {
      "type": "string",
      "description": "The location of CityCenter."
    }
  },
  "required": [
    "entity_name",
    "ownership_percentage",
    "citycenter_location"
  ],
  "additionalProperties": false
}
