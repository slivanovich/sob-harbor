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
Mall of America (Metro Transit station): Mall of America Transit Station is the busiest transit hub/station in Minnesota, with bus and light rail service linking the Mall of America to many destinations in the Minneapolis – St. Paul metro.  Public transit service is provided by Metro Transit and Minnesota Valley Transit Authority.  The station is served by METRO Blue Line and Red Line.  Many area hotels and Mystic Lake Casino offer free shuttles to their establishments.

2011 National Games of India: The 2011 National Games was held from 12 February 2011 to 26 February 2011 in Ranchi, Jharkhand, India.

Sheffield Interchange: Sheffield Interchange is the main bus station in central Sheffield, South Yorkshire, England.  The facility is served by buses operating across the Sheffield region, as well as National Express coaches which connect Sheffield with many destinations across the United Kingdom.  At the northern end of the Interchange is Castle Square tram stop, serving all three Sheffield Supertram routes.  A short distance away via a signposted covered walkway is Sheffield railway station, proving train services to locations across the country.

Air India: Air India is the flag carrier airline of India.  It is owned by Air India Limited, a government-owned enterprise, and operates a fleet of Airbus and Boeing aircraft serving 90 domestic and international destinations.  The airline has its hub at Indira Gandhi International Airport, New Delhi, alongside several focus cities across India.  Air India is the largest international carrier out of India with an 18.6% market share.  Over 60 international destinations are served by Air India across four continents.  Additionally, the carrier is the third largest domestic airline in India in terms of passengers carried (after IndiGo and Jet Airways) with a market share of 13.5% as of July 2017.  The airline became the 27th member of Star Alliance on 11 July 2014.

Indian Airlines destinations: Indian served the following destinations before being merged into Air India on 26 February 2011:

Anhoniyon Ka Andhera: Anhoniyon Ka Andhera was an Indian television horror series that premiered on 26 February 2011 on Colors channel, and aired weekly on every Saturday at 11 PM IST.  It ended on 9 July 2011.  The series is produced by Bollywood film producer Vikram Bhatt, and each story of the show revolves around Anahita Malik, a girl who has supernatural powers.  Vikram Bhatt film Haunted 3D stars Mahaakshay Chakraborty and Tia Bajpai also made their appearance on 30 April 2011 to promote their film.

T. Sreenidhi: T. Sreenidhi(Srinidhi | Sreenidhi Venkatesh) (born 26 January 1990), is an eminent Carnatic Musician, Playback Singer and Music Director.  Sreenidhi performed in major sabhas in India and presented her concerts in many destinations around the world.  She received multiple awards and honours.  Sreenidhi trained under legendary vocal stalwart Sangita Kalanidhi Dr. Nedunuri Krishnamurthy.

Hageland Aviation Services: Hageland Aviation Services was a regional FAR Part 135 airline based in Anchorage, Alaska, USA.  It currently operates as the Ravn Connect component of Ravn Alaska, serving many destinations throughout Alaska.

Nithyasree Mahadevan: Nithyasree Mahadevan (born 25 August 1973), also referred to as S. Nithyashri, is an eminent Carnatic musician and playback singer for film songs in many Indian languages.  Nithyashree has performed in all major sabhas in India and has presented her concerts in many destinations around the world.  She has received multiple awards and honours, and has released more than 500 albums.

2011 Mauritian League: The 2011 Mauritian League (also known as "Barclays League" for sponsorship reasons) was the sixty-seventh season of the Mauritian League since its establishment in 1935.  The 2011 fixtures were released in February 2011.  The season began on 26 February 2011, and concluded on 26 June 2011.  ASPL 2000 won the 2011 Mauritian League, winning their 5th title, their first since 2005.

Question: How many destinations are served by the airline that Indian merged into on 26 February 2011?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "airline_name": {
      "type": "string",
      "description": "The name of the airline that Indian merged into."
    },
    "merger_date": {
      "type": "string",
      "format": "date",
      "description": "The date when Indian merged into the specified airline."
    },
    "total_destinations_served": {
      "type": "integer",
      "description": "The total number of domestic and international destinations served by the airline."
    },
    "international_destinations_served": {
      "type": "integer",
      "description": "The number of international destinations served by the airline."
    },
    "continents_served_internationally": {
      "type": "integer",
      "description": "The number of continents served by the airline for international destinations."
    }
  },
  "required": [
    "airline_name",
    "merger_date",
    "total_destinations_served",
    "international_destinations_served",
    "continents_served_internationally"
  ],
  "additionalProperties": false
}
