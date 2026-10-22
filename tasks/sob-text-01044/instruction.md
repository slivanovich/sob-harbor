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
Vail Resorts: Vail Resorts, Inc. runs four ski resorts in Colorado (Vail Ski Resort, Beaver Creek Resort, Keystone Resort, and Breckenridge Ski Resort), three in Lake Tahoe (Heavenly Mountain Resort, Kirkwood Mountain Resort, Northstar California), one in Utah (Park City Mountain Resort in Park City), one in Vermont (Stowe Mountain Resort), one in Minnesota (Afton Alps), one in Michigan (Mount Brighton), one in Wisconsin (Wilmot Mountain), one in New South Wales, Australia (Perisher Ski Resort), one in British Columbia (Whistler Blackcomb), and a summer resort in Wyoming.  They also own luxury resort hotels throughout the world.  The company trades on the New York Stock Exchange, symbol MTN.  The company is headquartered in Broomfield, Colorado.

Bullocks Flat: Bullocks Flat (or Bullock's Flat) is a flat portion of the Thredbo Valley adjacent to the Thredbo River, located in the Snowy Mountains region of New South Wales, Australia.

Thredbo, New South Wales: Thredbo is a village and ski resort in the Snowy Mountains of New South Wales, Australia, and a part of the Snowy Monaro Regional Council.

Ski Club of Australia: The Ski Club of Australia is a private club and ski lodge located in Thredbo, New South Wales, Australia.  It was founded in 1920 and as its foundation pre-dated the foundation of the Ski Council of New South Wales in 1929, it played a pivotal role in the history of skiing and ski racing in Australia.  Four members of the Ski Club, Herbert Schlink, Eric Fisher, William Gordon and John Laidley, made the first winter crossing of the Snowy Mountains Main Range from Kiandra to Kosciusko in 1927.  Slalom skiing was introduced into Australia by the club.  The club formerly had an official role in Australian skiing and its 75th Anniversary history was written by Olympian Bob Arnott.

Stuart Diver: Stuart Diver (born 14 January 1970 in New South Wales, Australia) is a ski instructor and was the sole survivor of the 1997 Thredbo landslide.

Smiggin Holes, New South Wales: Smiggin Holes is a village located in the ski resort area of Snowy Mountains of New South Wales, Australia, in the Snowy Monaro Regional Council.  It is primarily a winter-only resort village.  It is within the Kosciuszko National Park, and is administered by New South Wales Department of Environment and Climate Change.  Access to the village is via road.  There is an access fee payable to the national park, and motor vehicles are not permitted to stay overnight in the winter months.

Urban Search and Rescue New South Wales AUS-2: New South Wales Urban Search and Rescue Task Force 1 (or NSWTF/1) was first established as a USAR capability in the lead up to the 2000 Sydney Olympics.  After earlier large-scale collapses including the 1977 Granville Train Disaster, 1989 Newcastle earthquake and 1997 Thredbo landslide, Fire & Rescue NSW was legislated as the combat authority for responding to major structural collapse incidents within the state of New South Wales.

Hotham Alpine Resort: The Hotham Alpine Resort is an Australian ski resort, located in the Alpine region of Victoria.  Set on the slopes of Mount Hotham, the ski resort comprises an alpine village, situated at an altitude of 1750 m , making it the second highest resort village in Australia after Charlotte Pass village, in New South Wales.

1997 Thredbo landslide: The Thredbo landslide was a catastrophic landslide that occurred at the village and ski resort of Thredbo, New South Wales, Australia, on 30 July 1997.  Two ski lodges were destroyed and a total of 18 died.

Blue Cow Mountain: Blue Cow is a ski resort that is part of Perisher located in the Snowy Mountains of New South Wales, Australia, within the Snowy Monaro Regional Council.  The resort is situated within the Kosciuszko National Park and is administered by the NSW National Parks & Wildlife Service.  During winter months, the only access to the village is via the Skitube underground railway.  In summer, access is via off-road only.  Blue Cow is one of the four resort bases within Perisher, Australia's largest ski resort.

Question: Stuart Diver was the sole survivor of what catastrophic landslide occurred at the village and ski resort of Thredbo, New South Wales, Australia, on 30 July 1997?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "landslide_name": {
      "type": "string",
      "description": "The name of the catastrophic landslide."
    },
    "event_details": {
      "type": "object",
      "properties": {
        "location": {
          "type": "string",
          "description": "The village and ski resort where the landslide occurred."
        },
        "state": {
          "type": "string",
          "description": "The Australian state where the landslide occurred."
        },
        "country": {
          "type": "string",
          "description": "The country where the landslide occurred."
        },
        "date": {
          "type": "string",
          "format": "date",
          "description": "The date the landslide occurred."
        },
        "fatalities": {
          "type": "integer",
          "description": "The total number of deaths caused by the landslide."
        }
      },
      "required": [
        "location",
        "state",
        "country",
        "date",
        "fatalities"
      ],
      "additionalProperties": false
    },
    "survivor_details": {
      "type": "object",
      "properties": {
        "survivor_name": {
          "type": "string",
          "description": "The name of the sole survivor."
        },
        "role": {
          "type": "string",
          "description": "Description of the survivor's role in the event."
        }
      },
      "required": [
        "survivor_name",
        "role"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "landslide_name",
    "event_details",
    "survivor_details"
  ],
  "additionalProperties": false
}
