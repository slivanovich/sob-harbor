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
Collected (Black 'n Blue album): Collected is a five disc Black 'N Blue box set, released in 2005, with 4 audio CDs and one DVD.  This release contains the first four studio albums released by the hard rock/ glam metal band, Black 'n Blue.  The DVD contains an entire live concert performed by Black 'n Blue, containing most of Black 'n Blue's hits, while also including a few songs that were never released on any Black 'n Blue disc.  These include "Run Run", "Summer Heat", and "Rock n' Roll Animals", which later became "Knocking On Heaven's Door".

Disney's Typhoon Lagoon: Disney's Typhoon Lagoon is a water theme park located at the Walt Disney World Resort in Lake Buena Vista in Orlando, Florida and is one of two operating water parks at the resort.  It is the second water park to open at the resort after Disney's River Country, which closed in November 2001.

Pay 'n Save: Pay 'n Save was a retail company founded by Monte Lafayette Bean in Seattle, Washington; 1940.  Over the years, Pay 'n Save was the leading drugstore chain in Washington and was the owner of several Washington-based retailers including Lamonts and Ernst.  A 1984 sale of the company to The Trump Group and a 1986 attempt to transform the retailer into a bargain-basement merchandiser resulted in a loss of nearly $50 million.  By 1988, Pay 'n Save was sold to Thrifty Corporation who later sold the stores to PayLess Drug who retired the Pay 'n Save name.  As a result, most of the retailer's divisions were spun off as separate companies or shuttered.  As of 2011, Pay 'n Save's membership discount chain, Bi-Mart, is the lone surviving division of the company (as of 2017, Bi-Mart is an employee-owned company).

Bill Hay (radio announcer): Bill Hay was an American radio announcer who was famous for his many years of work on the "Amos 'n' Andy" show with Charles J. Correll and Freeman F. Gosden.  Gosden and Correll had a show similar to "Amos 'n' Andy" called "Sam 'n' Henry" at radio station WGN in Chicago, but after a dispute in 1927, they took the program's concept and WGN announcer Bill Hay across town to WMAQ.  The "Amos 'n' Andy" team created the first syndicated radio show in history.  The sponsor of "Amos 'n' Andy", Pepsodent, contractually stipulated that no one but Bill Hay was ever to announce their show.

AquaDuck: AquaDuck is a water coaster (a water slide with similar turns, drops and g-forces to a roller coaster) that is located on the deck of two Disney cruise ships.  It was first constructed on the "Disney Dream" in January 2011 and then later on the "Disney Fantasy" in February 2012.  It was developed by Walt Disney Imagineers, and despite a few exceptions, is accessible to almost anyone.  The AquaDuck is the first water coaster to exist on a cruise ship, and so far it is the only one of its kind.

Mammoth (ride): Mammoth is a water coaster at Holiday World & Splashin' Safari in Santa Claus, Indiana, United States.  It was designed and built beginning in 2011 by ProSlide Technology; it opened on May 11, 2012.  "Mammoth" is named after the Mammoth, a now-extinct prehistoric mammal, keeping with the water park's safari theme.  When it was completed in 2012, "Mammoth" became the world's longest water coaster at 1763 ft long.  It claimed that title from Holiday World's first water coaster, "Wildebeest", which is 1710 ft long.

Crush 'n' Gusher: Crush 'N' Gusher is a water coaster in Disney's Typhoon Lagoon on the Walt Disney World Resort property.

Loaf 'N Jug: Loaf 'N Jug is a chain of convenience stores, owned by Kroger, headquartered in Pueblo, Colorado.  The company was founded by 5 businessmen from southern Colorado.  Kroger purchased Loaf 'N Jug in 1986.  In 2006, Kroger reimaged its convenience stores brands (Loaf 'N Jug, Kwik Shop, Quik Stop, Tom Thumb, and Turkey Hill) under a common logo.  At about the same time, Kroger debranded the gasoline sold at its convenience stores, eliminating Conoco which had been sold at many Loaf 'N Jug locations.  As part of this re-branding all of the Mini-Mart Stores were now Loaf 'N Jug Stores.

Wildebeest (ride): Wildebeest is a water coaster at Holiday World & Splashin' Safari in Santa Claus, Indiana, United States.  It was designed and built beginning in 2009 by ProSlide Technology; it opened on May 7, 2010.  "Wildebeest" is named after the African mammal, keeping with the water park's safari theme.  When it was completed in 2010, "Wildebeest" held the record for the world's longest water coaster at 1710 ft long.  It held that record until May 11, 2012, when Mammoth, Holiday World's second water coaster, took over the title at 1763 ft long.  In 2010, "Wildebeest" was voted the world's "Best New Waterpark Ride" at the Golden Ticket Awards, which are presented annually by "Amusement Today" magazine.  "Wildebeest" was also awarded the Golden Ticket Award for "Best Waterpark Ride" in 2010 and 2011.

Crush 'Em: "Crush 'Em" is a song by American heavy metal band Megadeth and the lead single from their eighth studio album, "Risk".  It first appeared on the soundtrack to "" in July 1999 and debuted as the third most added track on alternative rock stations on July 5.  Intended as a hockey anthem, "Crush 'Em" has become associated with sporting events and was heavily promoted by World Championship Wrestling.  The 2004 remastered edition of "Risk" includes the bonus track "Crush 'Em" (Jock Mix).

Question: Which state is the water coaster Crush 'N' Gusher located in?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "water_coaster_name": {
      "type": "string",
      "description": "The name of the water coaster."
    },
    "location": {
      "type": "object",
      "properties": {
        "park_name": {
          "type": "string",
          "description": "The name of the water park where the coaster is located."
        },
        "city": {
          "type": "string",
          "description": "The city where the water park is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the water park is located."
        }
      },
      "required": [
        "park_name",
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "entity_type": {
      "type": "string",
      "description": "The type of entity being described."
    }
  },
  "required": [
    "water_coaster_name",
    "location",
    "entity_type"
  ],
  "additionalProperties": false
}
