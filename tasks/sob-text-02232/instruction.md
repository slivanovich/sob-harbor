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
Pennsylvania Grade Crude Oil: Pennsylvania Grade Crude Oil is a type of sweet crude oil (sweet crude oil), found primarily in the Appalachian basin in the Marcellus Formation in the states of New York, Pennsylvania, Ohio, and West Virginia, and takes its name for the state of Pennsylvania, where it was first extracted in 1859 from the Drake Well.  The area's Pennsylvania Grade Crude Oil has superior qualities and is free of asphaltic constituents, contains only trace amounts of sulfur and nitrogen, and has excellent characteristics for refining into lubricants.  The success of drilling for oil at this well led to "an international search for petroleum, and in many ways eventually changed the way we live."  There is archaeological evidence that Native Americans harvested "the oil for medicinal purposes by digging small pits around active seeps and lining them with wood" at least as far back as 1410 AD.  European settlers skimmed the "oil from the seeps and using the petroleum as a source of lamp fuel and machinery lubrication."

Sandy Cioffi: Sandy Cioffi is a Seattle-based film and video artist.  She is director and producer of the documentary film Sweet Crude and has produced and/or directed the films Crocodile Tears, Terminal 187 and Just Us.  She is a tenured professor in the Film and Video Communications Department at Seattle Central Community College.

United States Oil Fund: The United States Oil Fund (NYSE Arca: [ USO] ) is an exchange-traded fund that attempts to track the price of West Texas Intermediate Light Sweet Crude Oil.

Sweet Crude: Sweet Crude is a documentary film by Sandy Cioffi about Nigeria's oil-rich Niger Delta.  The film premiered in April 2009 at the Full Frame Documentary Film Festival and has since screened at 30 film festivals around the world and has won numerous awards.

Gold Coast (region): The Gold Coast is the gold rich region that is now the nation of Ghana on the petroleum sweet crude oil and natural gas rich Gulf of Guinea in West Africa, Africa.

Enbridge Line 5: Enbridge Line 5 is a major oil pipeline in the Enbridge Lakehead System, which conveys petroleum from western Canada to eastern Canada via the Great Lakes states.  Line 5 is particularly notable for passing under the environmentally sensitive Straits of Mackinac, which connect Lake Michigan to Lake Huron.  As of December 2013, it is capable of carrying 540,000 oilbbl of oil per day.  It carries synthetic crude, natural gas liquids, sweet crude, and light sour crude.

Oil reserves in Libya: Oil reserves in Libya are the largest in Africa and among the ten largest globally with 46.4 Goilbbl as of 2010.  Oil production was 1.65 Moilbbl/d as of 2010, giving Libya 77 years of reserves at current production rates if no new reserves were to be found.  Libya is considered a highly attractive oil area due to its low cost of oil production (as low as $1 per barrel at some fields in 2002), low sulfur content, being classified as "sweet crude" and in its proximity to European markets.  Libya's challenge is maintaining production at mature fields, while finding and developing new oil fields.  Most of Libya remains under-explored as a result of past sanctions and disagreements with foreign oil companies.

Sweet crude oil: Sweet crude oil is a type of petroleum.  The New York Mercantile Exchange designates petroleum with less than 0.42% sulfur as "sweet".  Petroleum containing higher levels of sulfur is called sour crude oil.

Chernobyl Heart: Chernobyl Heart is a 2003 documentary film by Maryann DeLeo.  The film won the Best Documentary Short Subject award at The 76th Academy Awards.

White Horse (film): White Horse is a short documentary by filmmakers Maryann DeLeo and Christophe Bisson that features a man (Maxym Surkov) returning to his Ukraine home for the first time in twenty years.  Evacuated from the city of Pripyat, Ukraine in 1986 due to the Chernobyl disaster, he has not returned since then.  DeLeo is the same filmmaker of the 2004 Academy Award-winning short film "Chernobyl Heart".

Question: Which documentary was released first,  Sweet Crude or Chernobyl Heart?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_a_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the first film being compared."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the first film."
        },
        "director": {
          "type": "string",
          "description": "The director of the first film."
        }
      },
      "required": [
        "title",
        "release_year",
        "director"
      ],
      "additionalProperties": false
    },
    "film_b_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the second film being compared."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the second film."
        },
        "premiere_month": {
          "type": "string",
          "description": "The premiere month of the second film, if specified."
        },
        "director": {
          "type": "string",
          "description": "The director of the second film."
        }
      },
      "required": [
        "title",
        "release_year",
        "premiere_month",
        "director"
      ],
      "additionalProperties": false
    },
    "earliest_film_title": {
      "type": "string",
      "description": "The title of the documentary film that was released first."
    },
    "earliest_release_year": {
      "type": "integer",
      "description": "The release year of the earliest documentary film."
    }
  },
  "required": [
    "film_a_details",
    "film_b_details",
    "earliest_film_title",
    "earliest_release_year"
  ],
  "additionalProperties": false
}
