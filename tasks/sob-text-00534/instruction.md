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
2002 Webby Awards: The 6th Annual Webby Awards was held on June 21, 2002, at San Francisco's Legion of Honor auditorium.  It was presented by the International Academy of Digital Arts and Sciences and was hosted by Tiffany Shlain, the Webby Awards' founder, and Maya Draisin.  Coming on the heels of the dot-com bubble (which led to a reduced 2001 awards ceremony), a 2002 Internet bubble forced cutbacks in the event budget for this ceremony as well.

2016 Webby Awards: The 20th annual Webby Awards for 2016 was held at Cipriani Wall Street in New York City on May 16, 2016, which was hosted by comedian and actor Nick Offerman.  The awards ceremony was streamed live on the Webby Awards website.  Judges from the International Academy of Digital Arts and Sciences picked the over one hundred winners, which may or may not match the people's choice.

Fox Haven Plantation: Fox Haven Plantation is a historic plantation house located in Green Hill Township near Rutherfordton, Rutherford County, North Carolina.  It was built in 1823, and is a two-story, five bay by three bay, brick dwelling with Federal style design elements.  It sits on a low brick foundation and has two interior chimneys on the rear facade and one on the front facade.

Evergreen (Haymarket, Virginia): Evergreen, also known as Evergreen Plantation Manor House, is a historic plantation house located near Haymarket, Prince William County, Virginia.  It was built about 1827, and is a 2 1/2-story, five-bay, Greek Revival style stone dwelling.  It has a 1 1/2-story east wing and two-story west wing in the Colonial Revival style added about 1940.  It sits on an English basement, and gable roof and interior end chimneys.  The front facade features a three-bay, one-story, gable-roofed portico with a pedimented gable, and the rear facade has a full-length, five-bay, two-story portico with large Doric order columns.  The property was converted to a golf club about 1970.

2014 Webby Awards: The 18th annual Webby Awards for 2014 was held at Cipriani Wall Street in New York City on May 19, 2014, which was hosted by comedian and actor Patton Oswalt.  The awards ceremony was streamed live at the Webby Awards website.

War Memorial Opera House: The War Memorial Opera House in San Francisco, California is located on the western side of Van Ness Avenue across from the rear facade of City Hall.  It is part of the San Francisco War Memorial and Performing Arts Center.  It has been the home of the San Francisco Opera since opening night in 1932.

2001 Webby Awards: The 2001 Webby Awards were held in San Francisco at the War Memorial Opera House on July 18, 2001, hosted by Alan Cumming.

Cornwall House: Cornwall House is a town house located at numbers 56 and 58, Monnow Street in Monmouth, Wales.  It dates in part from the 17th century but was rebuilt in several stages later.  The street facade and rear facade are very different, but both are reworkings of a much older building.  It is a Grade II* listed building, and has been described in "The Buildings of Wales" as "the most imposing house in the street".  Part has been the main office of the "Monmouthshire Beacon" newspaper since 1987.

Cedar Dell: Cedar Dell, also known as Kennedy Memorial Home, is a historic plantation house located near Falling Creek, Lenoir County, North Carolina.  It was originally constructed about 1820 as a two-story, three bay, Federal style brick dwelling with a side-hall plan.  It was enlarged to five bays wide and converted to a Victorian Gothic central hall plan mansion.  The front facade features a one-story Eastlake-style porch with a low roof topped by a wrought iron balustrade and the rear facade has a two-tier porch.  Also on the front facade is a large bay window with a roof identical to that on the porch.  The house and property were deeded for use as an orphanage in 1912.

2015 Webby Awards: The 19th annual Webby Awards for 2015 was held at Cipriani Wall Street in New York City on May 19, 2015, which was hosted by comedian and actor Hannibal Buress.  The awards ceremony was streamed live at the Webby Awards webpage.  Judges from the International Academy of Digital Arts and Sciences picked the over one hundred winners, which may or may not match the people's choice.

Question: The 2001 Webby Awards were held an an opera house located across from the rear facade of what government building?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "event_year": {
      "type": "integer",
      "description": "The year the Webby Awards ceremony was held."
    },
    "event_name": {
      "type": "string",
      "description": "The name of the awards event."
    },
    "venue": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the venue where the event was held."
        },
        "city": {
          "type": "string",
          "description": "The city where the venue is located."
        }
      },
      "required": [
        "name",
        "city"
      ],
      "additionalProperties": false
    },
    "nearby_government_building": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the government building."
        },
        "relationship_to_venue": {
          "type": "string",
          "description": "Describes the spatial relationship of the government building to the venue."
        }
      },
      "required": [
        "name",
        "relationship_to_venue"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "event_year",
    "event_name",
    "venue",
    "nearby_government_building"
  ],
  "additionalProperties": false
}
