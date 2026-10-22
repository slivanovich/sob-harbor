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
Arlobi menhir: The Arlobi menhir is an archaeological heritage located at the Gorbea Natural Park, in Zuia, Álava (Basque part of Spain).  It was found by Oier Suárez Hernando, Miguel Martínez Fernández and Luis M. Martínez Torres on 20 March 2004.  The menhir was probably placed there in the Albian Age (Cretaceous 112–98 m.a.) and is basically made of stones coming from the Southern slope of Gorbea, Odoriaga and Usoteguieta mountains.  It is the most visited tourist attraction at the Gorbea Natural Park due to its peculiarity.  The discovery was very important because of the lack of menhirs in Álava.  In fact, the most common ancient sculptures are dolmens, usually as funerary monuments used to bury people in religious ceremonies.

Eugene T. Mahoney State Park: Eugene T. Mahoney State Park is a public recreation area located on the Platte River, just off Interstate 80, approximately 4 mi east of Ashland, Nebraska.  Among other features, the state park offers lodging and conferencing facilities, aquatic center, marina, trails, and theater.  It was named after Eugene T. Mahoney, a former state senator and long-time director of the Nebraska Game and Parks Commission, who is credited with reversing the fortunes of the moribund state park system during his directorship.  As of 2014, the park was the state's third most visited tourist attraction.

Skadarlija: Skadarlija (Serbian Cyrillic: Скадарлија) is a vintage street, an urban neighborhood and former municipality of Belgrade, the capital of Serbia.  It is located in the Belgrade municipality of Stari Grad (Old town) and generally considered the main bohemian quarter of Belgrade, similar to Paris' Montmartre.  After Kalemegdan, Skadarlija is the second most visited tourist attraction in Belgrade.

Helios (building): Helios, also known as 2nd & Pine, is a residential skyscraper in downtown Seattle, Washington.  The 40-story tower is 440 ft tall with 398 luxury apartments. Plans for the project were first proposed in 2013 and construction began in late 2014.  It is located at the intersection of 2nd Avenue and Pine Street near the Pike Place Market and the city's retail core.

33rd Street station (PATH): 33rd Street is a terminal station on the PATH system.  Located at the intersection of 32nd Street and Sixth Avenue in the Herald Square neighborhood of Manhattan, New York City, it is served by the Hoboken–33rd Street and Journal Square–33rd Street lines on weekdays, and by the Journal Square–33rd Street (via Hoboken) line on weekends.  33rd Street serves as the northern terminus of all three lines.

Dalsland Canal: Dalsland Canal (Swedish: "Dalslands kanal" ) is a Swedish canal which enables ships to sail between Lake Vänern and central parts of the Dalsland and southwestern Värmland lake districts.  The canal runs across the well-known aqueduct at Håverud and is a much visited tourist attraction during the summer months, drawing yachts, motor boats as well as canoeists.

Flåm Line: The Flåm Line (Norwegian: "Flåmsbana" ) is a 20.2 km long railway line between Myrdal and Flåm in Aurland, Norway.  A branch line of the Bergen Line, it runs through the valley of Flåmsdalen and connects the mainline with Sognefjord.  The line's elevation difference is 863 m ; it has ten stations, twenty tunnels and one bridge.  The maximum gradient is 5.5 percent (1:18).  Because of its steep gradient and picturesque nature, the Flåm Line is now almost exclusively a tourist service and has become the third-most visited tourist attraction in Norway.

Pike Place Market: Pike Place Market is a public market overlooking the Elliott Bay waterfront in Seattle, Washington, United States.  The Market opened August 17, 1907, and is one of the oldest continuously operated public farmers' markets in the United States.  It is a place of business for many small farmers, craftspeople and merchants. Named after the central street, Pike Place runs northwest from Union Street to Virginia Street.  With more than 10 million visitors annually, Pike Place Market is Seattle's most popular tourist destination and is the 33rd most visited tourist attraction in the world.

Belgrade Fortress: Belgrade Fortress (Serbian: Београдска тврђава"/Beogradska tvrđava"), consists of the old citadel (Upper and Lower Town) and Kalemegdan Park (Large and Little Kalemegdan) on the confluence of the River Sava and Danube, in an urban area of modern Belgrade, the capital of Serbia.  It is located in Belgrade's municipality of Stari Grad.  Belgrade Fortress was declared a Monument of Culture of Exceptional Importance in 1979, and is protected by the Republic of Serbia.  It is the most visited tourist attraction in Belgrade, with Skadarlija being the second.  Since the admission is free, it is estimated that the total number of visitors (foreign, domestic, citizens of Belgrade) is over 2 million yearly.

Fish River Canyon: The Fish River Canyon (Afrikaans: "Visrivier Canyon" or" Visrivier Afgronde", German: "Fischfluss Canyon" ), is located in the south of Namibia.  It is the largest canyon in Africa, as well as the second most visited tourist attraction in Namibia.  It features a gigantic ravine, in total about 100 mi long, up to 27 km wide and in places almost 550 meters deep.

Question: What is Helios located near that would qualify as the 33rd most visited tourist attraction in the world?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "tourist_attraction_name": {
      "type": "string",
      "description": "The name of the tourist attraction."
    },
    "world_ranking": {
      "type": "integer",
      "description": "The global ranking of the tourist attraction by visitor numbers."
    },
    "located_near_entity": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the entity that the tourist attraction is located near."
        },
        "type": {
          "type": "string",
          "description": "The type of the entity (e.g., building, park)."
        },
        "city": {
          "type": "string",
          "description": "The city where the entity is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the entity is located."
        }
      },
      "required": [
        "name",
        "type",
        "city",
        "state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "tourist_attraction_name",
    "world_ranking",
    "located_near_entity"
  ],
  "additionalProperties": false
}
