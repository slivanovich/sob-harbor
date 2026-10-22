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
Kiwanis Kavaliers Drum and Bugle Corps: The Kiwanis Kavaliers Drum and Bugle Corps were a "World Class" drum and bugle corps based in Miami, Florida (Previously twin cities of Kitchener-Waterloo, Ontario.  This corps was Canada's only World Class drum corps until it moved its headquarters to Miami after the 2006 season.  The Kiwanis Kavaliers have appeared in both Division I and Division II (now "Open Class") competition throughout its history.

Govenaires Drum and Bugle Corps: The Govenaires Drum and Bugle Corps is an all age drum and bugle corps based in St. Peter, Minnesota (USA) that competes in Drum Corps Associates (DCA).  Founded in 1927, the Governaires are the oldest continuously active drum and bugle corps.  The Governaires are four time DCA Class A World Champions.

Phantom Regiment Drum and Bugle Corps: The Phantom Regiment Drum and Bugle Corps (commonly referred to as "Phantom") is a World Class competitive junior drum and bugle corps based in Rockford, Illinois, USA.  The corps is a long-standing member of Drum Corps International (DCI), having been a DCI World Championship Top Twelve Finalist every year since 1974 and DCI World Champions in 1996 and 2008.

Oflag II-D: Oflag II-D was a World War II German prisoner-of-war camp located at Gross Born, Pomerania (now Borne Sulinowo, West Pomeranian Voivodeship, Poland).  In the late 1930s the German Army built a large base and training ground at which the XIX Army Corps of General Heinz Guderian was based.

Capital Regiment Drum and Bugle Corps: The Capital Regiment Drum and Bugle Corps was a drum and bugle corps based in Columbus, Ohio, United States founded in 1999, and was a member of Drum Corps International.  Although having competed in DCI's World Class (formerly "Division I") from 2002 to 2006, the corps also competed in Open Class in 2009 before going inactive.  The Capital Regiment was one of six DCI corps in Ohio, the others being the Bluecoats , Cincinnati Glory, Glassmen , Limited Edition, and Marion Cadets.

Muchachos Drum and Bugle Corps: The Muchachos Drum and Bugle Corps is an all-age Drum Corps International affiliated drum and bugle corps based in Manchester, New Hampshire.  (This drum corps is not affiliated with the Hawthorne Muchachos of Hawthorne, NJ.  See the Hawthorne Caballeros Drum and Bugle Corps page or visit Hawthorne Muchachos Drum and Bugle Corps for more information.)  Founded in 1960 as the "Manchester Boys Club Drum & Bugle Corps", the Corps later changed their name to the "Muchachos."  The corps dissolved in 1986, but in 2007, resumed operations, performing as an all-age exhibition corps in DCI, continuing into the present day.

3rd Civil Affairs Group: 3rd Civil Affairs Group (3rd CAG) is a civil affairs (CA) unit of the United States Marine Corps based at Naval Station Great Lakes, Illinois.  The Marine Corps assigns civil affairs as a primary military specialty for enlisted and additional specialty for officers.  The Marine Corps uses its own civil affairs doctrine and runs the Marine Corps Civil-Military Operations School at Marine Corps Base Quantico to train civil affairs Marines.

Heinz Guderian: Heinz Wilhelm Guderian (] ; 17 June 1888 – 14 May 1954) was a German general (colonel-general from 1940) during World War II, noted for his success as a leader of "Panzer" units in Poland and France and for partial success in the Soviet Union.

Sacramento Freelancers Drum and Bugle Corps: The Sacramento Freelancers Drum and Bugle Corps was an American drum corps based in Sacramento, California.  It was a Drum Corps International World Class top 12 Finalist.  In other incarnations, the corps has been a Senior Alumni Corps, a Winter Guard and a Winter Guard International (WGI) Independent World Class percussion ensemble.  It was founded in 1932 as the George W. Manhart American Legion Post #391 Drum and Bugle Corps, and later renamed the Manhart Capitalaires, the Capitalaires, the Capital Freelancers before adopting its last name.

Southwind Drum and Bugle Corps: Southwind Drum and Bugle Corps is an Open Class competitive junior drum and bugle corps based in Mobile, Alabama.  The corps was a Division I (now World Class) competitive junior drum and bugle corps in Drum Corps International (DCI) from 1993 through 2007.  Prior to competing in Division I, Southwind competed in DCI's Class A/Division II and was that division's World Champion in 1991 and 1992.  Southwind performed at competitive and non-competitive SoundSport events in Alabama and surrounding states during the summer of 2014.  In early May 2015, DCI approved Southwind's return as an active Open Class corps.

Question: What year did the general of the corps based at Oflag II-D in the late 1930s die? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "general_name": {
      "type": "string",
      "description": "The full name of the general."
    },
    "corps_name": {
      "type": "string",
      "description": "The name of the army corps associated with the general."
    },
    "corps_base_location": {
      "type": "string",
      "description": "The location where the corps was based."
    },
    "death_year": {
      "type": "integer",
      "description": "The year the general died."
    }
  },
  "required": [
    "general_name",
    "corps_name",
    "corps_base_location",
    "death_year"
  ],
  "additionalProperties": false
}
