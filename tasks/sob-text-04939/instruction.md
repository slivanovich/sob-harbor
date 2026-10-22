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
Beehive Geyser: Beehive Geyser is a geyser in the Upper Geyser Basin of Yellowstone National Park in the United States.  The 4 ft tall cone resembles a beehive.  Beehive's Indicator is a small, jagged cone-type geyser located about 10 ft from Beehive.

Malcolm W. Martin Memorial Park: Malcolm W. Martin Memorial Park is a park on the east side of the Mississippi River in East St. Louis, Illinois, directly across from the Gateway Arch and the city of St. Louis, Missouri.  Its major feature is the Gateway Geyser, a fountain that lifts water up to 630 ft .  The Gateway Geyser is a counterpart to the equally tall St. Louis monument, and is visible from the west side of the river to the right of the prominent Cargill grain elevator.  Four smaller fountains around the Geyser represent the four rivers which converge near the two cities: The Mississippi, Missouri, Illinois, and Meramec.  The park also includes an elevated viewing point overlooking the river.

Infinity at Brickell: Infinity at Brickell is a skyscraper in Miami, Florida, United States.  It is located in Downtown's Brickell Financial District.  When it topped out, it was the 7th tallest building in Miami and Florida.  Although not in the same complex, it was built across the street from Infinity II site, hence its name.  The location is in southwestern Brickell, on South Miami Avenue near 13th Street.  The building opened in 2008.  It is 630 ft tall, and has 52 floors.  It is about 100 ft shorter than Infinity II was supposed to be.  The lower floors of the building are dedicated to office space and retail, while the upper floors are used for residential units.  The architects are Adache Group Architects and Borges & Associates.

Safeco Plaza (Seattle): Safeco Plaza, previously 1001 Fourth Avenue Plaza and the Seattle-First National Bank Building, is a 50-story, 630 ft skyscraper in downtown Seattle, Washington.  The building is referred to by locals as "The Box the Space Needle Came In".  When the tower was completed in 1969 by the by the Howard S. Wright Construction Company for Seattle First National Bank, it dwarfed Smith Tower, which had reigned as downtown's tallest building since 1914, and edged out the Space Needle (built in 1962) in Seattle Center by 25 ft to become the tallest structure in the city until 1985 with the completion of the Columbia Center.

New York Wheel: The New York Wheel is a 630 ft tall giant Ferris wheel under construction in St. George, Staten Island alongside the site of the proposed Empire Outlets retail complex.  Although the two projects are going through the approval process simultaneously and will share consultants on issues such as traffic and the waterfront, they are two separate projects, each funded separately.  The ride is to operate every day of the year, except during adverse weather or maintenance, from 10:00AM to 10:00PM or 12:00AM, with extra hours during summer.  A single ride is expected to last about 38 minutes.

Home Insurance Plaza: Home Insurance Plaza is a 630 ft tall skyscraper in New York City, New York.  It was completed in 1966 and has 44 floors.  Alfred Easton Poor designed the building, which is the 61st tallest in New York.  The building's plaza had a redevelopment in 1987 by Kohn Pedersen Fox.

BG Group Place: BG Group Place (formerly MainPlace) is a 630 ft (192 m) tall skyscraper in Downtown Houston, Texas.  It was completed in February 2011 and has 46 floors.  It is LEED Platinum Certified.  When it was completed, BG Group Place became the 15th tallest building in Houston and features a skygarden on the 39th floor.  It is the tallest building built in Houston in 23 years, after the Heritage Plaza was completed in 1987.

Gateway Arch: The Gateway Arch is a 630 ft monument in St. Louis in the U.S. state of Missouri.  Clad in stainless steel and built in the form of an inverted, weighted catenary arch, it is the world's tallest arch, the tallest man-made monument in the Western Hemisphere, and Missouri's tallest accessible building.  Built as a monument to the westward expansion of the United States, and officially dedicated to "the American people," it is the centerpiece of the Jefferson National Expansion Memorial and has become an internationally recognized symbol of St. Louis, as well as a popular tourist destination.

List of tallest buildings in St. Louis: The tallest buildings in St. Louis, Missouri, include the 630 ft Gateway Arch, which is also the tallest accessible structure in Missouri and the tallest monument in a national park, rising 75 ft higher than the Washington Monument.

1095 Avenue of the Americas: 1095 Avenue Of The Americas is a 630 ft (192m) tall skyscraper in New York City, New York.  It was constructed from 1972 to 1974 as headquarters of New York Telephone and has 41 floors.  The building also served as the headquarters of NYNEX and Bell Atlantic.  Kahn & Jacobs designed the building, which is the 61st tallest in New York.  The original facade was said to be designed to resemble the relays which were commonly found inside telephones of the time.  From 2006 to 2007 the tower received a $260 million renovation which upgraded the office space from Class B+ to Class A office space.  The phone company moved its headquarters to the Verizon Building in the early 2000s, and sold off most of the building, retaining a condominium interest in floors 6-12, where Verizon maintained offices and a telephone exchange serving landlines in Midtown Manhattan.  However, in 2013 the company moved its corporate headquarters back to 1095 Avenue of the Americas, following a sale of the upper floors of the Verizon Building.

Question: Which American city contains a park with a geyser that can lift water up to 630 ft and an monumental archway that is also 630 ft tall?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "city_name": {
      "type": "string",
      "description": "The name of the American city."
    },
    "state_name": {
      "type": "string",
      "description": "The name of the state where the city is located."
    },
    "park_details": {
      "type": "object",
      "properties": {
        "park_name": {
          "type": "string",
          "description": "The name of the park containing the geyser."
        },
        "geyser_name": {
          "type": "string",
          "description": "The name of the geyser in the park."
        },
        "geyser_water_height_ft": {
          "type": "integer",
          "description": "The maximum height the geyser can lift water, in feet."
        }
      },
      "required": [
        "park_name",
        "geyser_name",
        "geyser_water_height_ft"
      ],
      "additionalProperties": false
    },
    "monument_details": {
      "type": "object",
      "properties": {
        "monument_name": {
          "type": "string",
          "description": "The name of the monumental archway."
        },
        "monument_height_ft": {
          "type": "integer",
          "description": "The height of the monumental archway, in feet."
        }
      },
      "required": [
        "monument_name",
        "monument_height_ft"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "city_name",
    "state_name",
    "park_details",
    "monument_details"
  ],
  "additionalProperties": false
}
