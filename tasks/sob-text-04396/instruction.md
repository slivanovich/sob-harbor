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
Castro Theatre: The Castro Theatre is a popular San Francisco movie palace which became San Francisco Historic Landmark #100 in September 1976.  Located at 429 Castro Street, in the Castro district, it was built in 1922 with a Spanish Colonial Baroque façade that pays homage—in its great arched central window surmounted by a scrolling pediment framing a niche—to the recently rebuilt basilica of Mission Dolores nearby.  Its designer, Timothy L. Pflueger, also designed Oakland's Paramount Theater and other movie theaters in California in that period.  The theater has over 1,400 seats (approx 800 downstairs and 600 in the balcony).  The theater's ceiling is the last known "leatherette" ceiling in the USA & possibly the world.  Another "leatherette" ceiling was unfortunately demolished just a few years ago.  To achieve the ceiling's look as though it is leather requires a special technique regarded as "lost" today.

Moby Dick Records: Moby Dick Records was a small disco record label founded by Bill Motley (DJ Bill Motley) and Victor Swedosh in 1980.  Its headquarters were located at 573 Castro Street, San Francisco, California, United States.  Swedosh also owned the Moby Dick Bar (opened in 1977) located in the Castro district.

Castro station: Castro station is a Muni Metro station at the intersection of Market Street, Castro Street, and 17th Street in The Castro district of San Francisco, California.

Fear of a Black Republican: Fear of a Black Republican is an American independent political documentary which examines the lack of Minorities and especially African Americans in the Republican Party in the United States.  The documentary film had its theatrical premiere in Washington, DC on March 22, 2012 and has screened around the United States at theatres, film festivals, colleges and universities and museums.  Produced over six years by the married filmmaking team of Kevin and Tamara Williams, the film takes a non-partisan point-of-view of the American two-party political system and why the Republican Party has so few Black and Urban supporters.

Market Street Subway: The Market Street Subway is a double-decker subway tunnel that carries Muni Metro and BART train traffic in San Francisco, California.  It runs under the length of Market Street between Embarcadero Station and Castro Street Station.  The upper level is used by Muni Metro lines and the lower level is used by BART lines.  BART does not run through the whole subway; it turns south and runs under Mission Street southwest of Civic Center Station.  The northeastern end of the BART level is connected to the Transbay Tube.  On the Muni Metro level, the southwestern end of the Market Street Subway connects to the much-older Twin Peaks Tunnel, and the northeastern end connects to surface tracks along the Embarcadero.

Castro Street (film): Castro Street (1966) is a visual nonstory documentary film which uses the sounds and sights of a city street—in this case, Castro Street near the Standard Oil Refinery in Richmond, California—to convey the street's own mood and feel.  There is no dialogue in this non-narrative experimental film.  It was directed by Bruce Baillie.

Castro Creek: Castro Creek is a creek in Richmond, California in the western part of the city adjacent to the Chevron Oil Refinery.  Wildcat Creek drains into it directly and though other Wildcat Marsh tributaries into Castro Cove of San Pablo Bay.  The creek drains from the drainage basin of the surrounding area and was once part of the channel that separated the island of Point Richmond with the mainland.  The stream is waterway is named after Don Víctor Castro the owner of the area when it was Rancho San Pablo.  The Chevron Richmond Refinery dumps wastewater into the creek routinely 500 yards north of the confluence with Wildcat Creek and also in a drainage.  Other waste may only be dumped into the creek through a drainage ditch on Castro Street during high intensity rainfall.  Castro Creek is a fishing, shell-fishing, and recreation area.  Its estuarine habitat is essential habitat for several endangered species.  The creek is also a fish spawning and migration center.  The refinery creates 5.6 e6USgal per day of byproduct refinery process water, cooling water, storm water and other wastewater which it discharges into Castro Creek, Castro Cove, Wildcat Marsh, and San Pablo Bay.  Castro Cove has become very polluted from 85 years of unbridled discharge of waste waters with PAHs and mercury from the Chevron Oil Refinery and is scheduled to begin cleanup efforts in summer 2007.

S Castro Shuttle: The S Castro Shuttle is a Muni Metro line in San Francisco, California.  At its inception in 1995, it ran from Embarcadero Station downtown to the Castro Street Station during peak periods on weekdays.  The service stopped running in the early 2000s as the number of available light rail vehicles went down due to maintenance issues.

Pink Triangle Park: The Pink Triangle Park is a triangular shaped mini-park located in the Castro District of San Francisco, California, at the intersection of 17th Street and Market Street, directly above the Castro Street Station of Muni Metro.  It is the first permanent, free-standing memorial in America to the thousands of persecuted homosexuals in Nazi Germany during the Holocaust of World War II.

Castro Street Fair: The Castro Street Fair is a San Francisco LGBT street festival and fair usually held on the first Sunday in October in the Castro neighborhood, the main gay neighborhood and social center in the city.  The fair features multiples stages with live entertainment, DJs, food vendors, community-group stalls as well as a curated artisan alley with dozens of Northern California artists.  Due to community pressure the fair restructured the organization and partnered with local charities to collect gate donations and partner with groups at the beverage and beer booths to raise money for those charities.

Question: Fear of a Black Republican And Castro Street are what genre of film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_genres": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "film_title": {
            "type": "string"
          },
          "genre": {
            "type": "string"
          }
        },
        "required": [
          "film_title",
          "genre"
        ],
        "additionalProperties": false
      }
    },
    "common_genre_identified": {
      "type": "boolean",
      "description": "True if all listed films share a common genre."
    },
    "common_genre": {
      "type": "string",
      "description": "The common genre if identified."
    }
  },
  "required": [
    "film_genres",
    "common_genre_identified",
    "common_genre"
  ],
  "additionalProperties": false
}
