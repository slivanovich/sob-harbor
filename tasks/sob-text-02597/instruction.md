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
SummerSlam (2009): SummerSlam (2009) was a professional wrestling pay-per-view (PPV) event produced by World Wrestling Entertainment (WWE), which took place on August 23, 2009, at Staples Center in Los Angeles, California and was the first of six consecutive annual SummerSlam events to take place at the arena.  It was presented by 7-Eleven.  It was the twenty-second annual SummerSlam event and featured talent from the Raw, SmackDown, and ECW brands.  Eight matches were contested on the event's card.

SummerSlam (2002): SummerSlam (2002) was the fifteenth annual SummerSlam professional wrestling pay-per-view (PPV) event produced by World Wrestling Entertainment (WWE).  It was presented by Foot Locker.  It took place on August 25, 2002, at the Nassau Veterans Memorial Coliseum in Uniondale, New York.  With this event, SummerSlam became the first pay-per-view to have events in the three major indoor venues in the New York metropolitan area.  Madison Square Garden hosted the event in 1988, 1991, and 1998.  The Izod Center in East Rutherford, New Jersey hosted the event in 1989, 1997, and later in 2007.

Chat (mining): Chat is a term for fragments of siliceous rock, limestone, and dolomite waste rejected in the lead-zinc milling operations that accompanied lead-zinc mining in the first half of the 20th century.  Historic lead and zinc mining in the Midwestern United States was centered in two major areas: the Tri-State area covering more than 2500 sqmi in southwestern Missouri, southeastern Kansas, and northeastern Oklahoma and the Old Lead Belt covering about 110 sqmi in southeastern Missouri.  The first recorded mining occurred in the Old Lead Belt in about 1742.  The production increased significantly in both the Tri-state area and the Old Lead Belt during the mid-19th century and lasted up to 1970.

Illinois-Indiana-Kentucky tri-state area: The Illinois-Indiana-Kentucky tri-state area is a tri-state area where the U.S. states of Illinois, Indiana, and Kentucky intersect.  The area is defined mainly by the television viewing area and consists of ten Illinois counties, eleven Indiana counties, and nine Kentucky counties.

Tri-State PGA Championship: The Tri-State PGA Championship is a golf tournament that is the championship of the Tri-State section of the PGA of America.  The Tri-State area includes all of West Virginia, the northwest corner of Maryland, and western Pennsylvania.  It has been played annually since 1931 at a variety of courses in that area.

Tri-state area: There are a number of areas in the 48 contiguous United States known informally as tri-state areas.  Often, a tri-state area is a region associated with a particular town or metropolis that, with its adjacent suburbs, lies across three states. Some, but not all, of these involve a state boundary tripoint.  Other "tri-state" areas have a more diffuse population that shares a connected economy and geography, especially with respect to geology, botany, or climate, such as the tri-state area of New York, New Jersey, and Connecticut.  The use of the term "tri-state area" is often encountered in movies and radio and television commercials.

SummerSlam (2015): SummerSlam (2015) was a professional wrestling pay-per-view (PPV) event produced by WWE.  It took place on August 23, 2015, at Barclays Center in Brooklyn, New York.  The twenty-eighth event under the SummerSlam chronology, this was the first since 2008 to be held outside of Los Angeles as Staples Center was the exclusive home for "SummerSlam" from 2009 to 2014, and the eighth "SummerSlam" to be held in the New York metropolitan area.  The Izod Center was originally supposed to host "SummerSlam", but due to its closure in April 2015, the event was moved to Barclays Center.  The event was the first in the SummerSlam chronology to be four hours in length, a length previously reserved only for WrestleMania.

SummerSlam: SummerSlam is a professional wrestling pay-per-view (PPV) event, produced annually in August by professional wrestling promotion WWE.  Dubbed as "The Biggest Party of the Summer", it is one of the original "Big Four" pay-per-view events of WWE (along with WrestleMania, Royal Rumble, and Survivor Series).  The inaugural SummerSlam took place on August 29, 1988 at Madison Square Garden in New York City and was broadcast via pay-per-view.  SummerSlam has been touted by WWE as their second biggest event of the year after WrestleMania.  From 2009 to 2014, SummerSlam was held at the Staples Center in Los Angeles.  Since 2015, the event has taken place at the Barclays Center in the New York City borough of Brooklyn.

SummerSlam (1988): SummerSlam 1988 was the first annual SummerSlam professional wrestling pay-per-view (PPV) event.  It was produced by the World Wrestling Federation (WWF) and took place on August 29, 1988, in Madison Square Garden, located in New York City, New York.  The pay-per-view was created to help the company compete against rival promotion World Championship Wrestling (formerly Jim Crockett Promotions).  It was one of the first four annual pay-per-view events produced by the WWF, along with WrestleMania, the Royal Rumble, and Survivor Series.

New York metropolitan area: The New York metropolitan area, also referred to as the Tri-State Area, includes the most populous city in the United States (New York City), Long Island, and the Mid- and Lower Hudson Valley in the state of New York; the five largest cities in New Jersey: Newark, Jersey City, Paterson, Elizabeth, and Edison, and their vicinities; six of the seven largest cities in Connecticut: Bridgeport, New Haven, Stamford, Waterbury, Norwalk, and Danbury, and their vicinities; and five counties in northeastern Pennsylvania.

Question: which Tri-State Area has SummerSlam been the the first pay-per-view to have events

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "tri_state_area_name": {
      "type": "string",
      "description": "The name of the tri-state area."
    },
    "event_type": {
      "type": "string",
      "description": "The type of event that achieved the milestone."
    },
    "milestone_event_name": {
      "type": "string",
      "description": "The specific event that marked the milestone."
    },
    "milestone_description": {
      "type": "string",
      "description": "A description of the milestone achieved by the event in the tri-state area."
    },
    "major_venues": {
      "type": "array",
      "description": "A list of major indoor venues in the tri-state area where the event was held.",
      "items": {
        "type": "object",
        "properties": {
          "venue_name": {
            "type": "string",
            "description": "The name of the venue."
          },
          "host_years": {
            "type": "array",
            "items": {
              "type": "integer"
            },
            "description": "A list of years the event was hosted at this venue."
          }
        },
        "required": [
          "venue_name",
          "host_years"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "tri_state_area_name",
    "event_type",
    "milestone_event_name",
    "milestone_description",
    "major_venues"
  ],
  "additionalProperties": false
}
