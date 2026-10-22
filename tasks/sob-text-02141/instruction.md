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
1994 Tooheys 1000: The 1994 Tooheys 1000 was a motor race held on 2 October 1994 at the Mount Panorama Circuit near Bathurst in New South Wales, Australia.  It was the 35th running of the Bathurst 1000 touring car race.  The race was open to cars complying with CAMS Group 3A Touring Car regulations, later known as V8 Supercars and those complying with FIA Class II Touring Car regulations, later known as Super Touring cars.  In the lead up to the 2003 event, Wheels Magazine voted the 1994 Bathurst 1000 to be the greatest of all time.

1992 Tooheys 1000: The 1992 Tooheys 1000 was the 33rd running of the Bathurst 1000 touring car race.  It was held on 4 October 1992, at the Mount Panorama Circuit just outside Bathurst.  The race was held for cars eligible for International Group A touring car regulations and a class available for those who had built cars eligible to the new for 1993 class, CAMS Group 3A touring car regulations.

1988 Tooheys 1000: The 1988 Tooheys 1000 was a 1000 km endurance motor race for Group A Touring Cars.  It was held on 2 October 1988 at the Mount Panorama Circuit just outside Bathurst in New South Wales, Australia.  The race was the opening round of the 1988 Asia-Pacific Touring Car Championship and was the 29th running of the "Bathurst 1000".

Bathurst 1000: The Bathurst 1000 (currently branded as the Supercheap Auto Bathurst 1000 for sponsorship reasons) is a 1,000 km touring car race held annually on the Mount Panorama Circuit in Bathurst, New South Wales, Australia.  It is currently run as a championship event for Supercars.

1995 Tooheys 1000: The 1995 Tooheys 1000 was the 36th running of the Bathurst 1000 touring car race.  It was held on 1 October 1995, at the Mount Panorama Circuit just outside Bathurst.  The race was held for cars eligible under CAMS Group 3A 5.0 Litre Touring Car regulations, that later became known as V8Supercars.  This was the first Bathurst 1000 to be contested by single class.

1997 AMP Bathurst 1000: The 1997 AMP Bathurst 1000 was the 38th running of the annual Bathurst 1000 touring car race.  It was held on 5 October 1997 at the Mount Panorama Circuit just outside Bathurst in New South Wales, Australia.  It was the first Bathurst 1000 race held after the controversial split between race organisers, the Australian Racing Drivers Club, and V8 Supercar, which led to Australia's leading touring car category contesting a separate 1000 kilometre race at Bathurst.  This race, the 1997 Primus 1000 Classic, was held two weeks after the AMP Bathurst 1000.

1993 Tooheys 1000: The 1993 Tooheys 1000 was the 34th running of the Bathurst 1000 touring car race.  It was held on 3 October 1993 at the Mount Panorama Circuit just outside Bathurst, New South Wales, Australia.  The race was held for cars eligible under CAMS Group 3A Touring Car regulations, which included 5.0 litre V8 engined cars (that later became known as V8Supercars), International Class II 2.0 litre Touring Cars (that later became known as Supertouring Cars and normally aspirated two wheel drive cars complying with 1992 CAMS Group 3A regulations (which had been based on international Group A rules).

2005 Supercheap Auto 1000: The 2005 Super Cheap Auto 1000 was an endurance motor race for V8 Supercars.  The race was held on 9 October 2005 at the Mount Panorama Circuit just outside Bathurst in New South Wales, Australia and was Round 10 of the 2005 V8 Supercar Championship Series.  It was the ninth running of the Australia 1000 race, first held after the organisational split over the Bathurst 1000 that occurred in 1997.  It was the 49th in a sequence of endurance races which commenced with the 1960 Armstrong 500 held at Phillip Island and 2005 was the 43rd year in which these races had been run at the Mount Panorama Circuit.  It was also the first to be run under new naming rights sponsor, Australian automotive retail chain SuperCheap Auto.

1991 Tooheys 1000: The 1991 Tooheys 1000 was the 32nd running of the Bathurst 1000 touring car race.  It was held on 6 October 1991 at the Mount Panorama Circuit just outside Bathurst.  The 1000 km race was held for cars complying with the provisions of Australian Group 3A Touring Car regulations with the field divided into three engine capacity divisions.  It was the Round 2 of both the 1991 Australian Endurance Championship and the 1991 Australian Manufacturers' Championship.

1990 Tooheys 1000: The 1990 Tooheys 1000 was a motor race held on 30 September 1990 at the Mount Panorama Circuit just outside Bathurst, New South Wales, Australia.  The event was open to cars eligible under CAMS Group 3A regulations, commonly known as Group A Touring Cars, with three engine capacity classes.  It was the 31st running of the "Bathurst 1000".

Question: The 1990 Tooheys 1000 was a motor race held on which date, at the Mount Panorama Circuit just outside Bathurst, New South Wales, it was the 31st running of which 1,000 km touring car race, for Supercars, held annually on the Mount Panorama Circuit in Bathurst?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "race_event_name": {
      "type": "string",
      "description": "The specific name of the motor race event."
    },
    "event_date": {
      "type": "string",
      "description": "The date on which the race was held."
    },
    "location_details": {
      "type": "object",
      "properties": {
        "circuit_name": {
          "type": "string",
          "description": "The name of the circuit where the race took place."
        },
        "city": {
          "type": "string",
          "description": "The city near which the circuit is located."
        },
        "state": {
          "type": "string",
          "description": "The state in which the circuit is located."
        },
        "country": {
          "type": "string",
          "description": "The country in which the circuit is located."
        }
      },
      "required": [
        "circuit_name",
        "city",
        "state",
        "country"
      ],
      "additionalProperties": false
    },
    "running_number": {
      "type": "integer",
      "description": "The sequential running number of the Bathurst 1000 series."
    },
    "parent_race_series_name": {
      "type": "string",
      "description": "The name of the overarching 1000 km touring car race series."
    },
    "race_regulations": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The regulations under which cars were eligible for this specific race."
    },
    "is_supercars_event": {
      "type": "boolean",
      "description": "Indicates if this specific race was run for V8 Supercars or Supercars."
    }
  },
  "required": [
    "race_event_name",
    "event_date",
    "location_details",
    "running_number",
    "parent_race_series_name",
    "race_regulations",
    "is_supercars_event"
  ],
  "additionalProperties": false
}
