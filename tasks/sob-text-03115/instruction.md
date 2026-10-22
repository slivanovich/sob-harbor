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
Black Rock City, LLC: Black Rock City LLC is the company that organizes the annual Burning Man event ending on Labor Day, on the dry lake of the Black Rock Desert in northwestern Nevada.  Although the organization is largely volunteer-driven, it has a for-profit form.  Its mission states that its efforts are, and its primary goal is, to establish community.

Burning Man: Burning Man is an annual gathering that takes place at Black Rock City—a temporary city erected in the Black Rock Desert in Nevada.  The event is described as an experiment in community and art, influenced by 10 main principles: "radical" inclusion, self-reliance, and self-expression, as well as community cooperation, civic responsibility, gifting, decommodification, participation, immediacy, and leaving no trace.

Further Future: Further Future is a transformational festival held in southern Nevada.  The Further Future model is, “a shared experience that’s beyond our future,” and, "promises a carefully curated slate of, business and cultural leaders, chefs, mixologists and masseuses".  Further Future caters to a techie club of invitation only exclusives in a controlled setting.  Further Future's membership is currently at 4000-5000 and is structured around a corporate retreat setting.  Further Future, located on the Moapa River Indian Reservation, claims to offers an "all inclusive" festival experience, different than the, "vanish and leave no trace" principles instilled in those who participate in Burning Man.  Further Future is the brainchild of a group called Robot Heart, an art and music collective known for the parties it throws during the annual Burning Man gathering in Northern Nevada's Black Rock Desert.  The Further Future event, "aspires to be a gathering of people with the common goal to spend time together celebrating the infinite possibilities of the future, without necessarily being shackled to the dictates of the past or the cycles of present-day society."  the invitation-only festival for as many as 5,000 people, runs from April 29 to May 1.

Temple of Flux: The Temple of Flux was a large temporary art project created by The Flux Foundation for Burning Man 2010.  The Temple was the tenth built at the festival and one of the largest.  Built of white-washed wood, the design was notable for being highly abstract in nature, consisting of 5 landforms that described cave and canyon-like spaces (a reflection on the festival's theme of "Metropolis").  The piece was approximately 100'x200'x40'.  Designed by Jess Hobbs, Rebecca Anders and PK (Peter Kimelman) it was built by a crew of 300 over a period of 4 months.

Pink Mammoth: Pink Mammoth is a San Francisco-based non-profit artist collective, founded by Ryel K and Derek Hena in August, 2003.  It is based partially on the philosophy of Burning Man, a radically expressive temporary city held annually in the Black Rock Desert of Nevada, and dedicated to unconditional self-support and free expression.  It also is influenced by the Buddhist concept of the Boddhisattva, a being dedicated to enabling, supporting, and encouraging others to reach their ultimate state of enlightenment.

John Law (Burning Man): John Law is an American artist, culture-jammer, and co-founder of the Cacophony Society and a member of the Suicide Club.  He is also a co-founder of the Burning Man Festival (a.k.a. Zone Trip #4, a.k.a. Black Rock City) which evolved out of the spirit of the Cacophony Society when a precursor solstice party was banned from San Francisco's Baker Beach and merged with another Cacophony event on the Black Rock desert in Nevada.  Originally from Michigan, Law has lived in San Francisco, California since 1976.

BMIR: BMIR 94.5 FM (Burning Man Information Radio) is the unlicensed community radio station for Burning Man, an event held annually in Black Rock Desert, Nevada.  BMIR begins broadcasting on 94.5 FM on the playa in the week leading up to Burning Man and broadcasts over the internet year-round.  Currently, the station hosts more than 40 DJs that produce the programming played over the course of the event.

Taking My Parents to Burning Man: Taking My Parents to Burning Man is a 2014 Canadian documentary film directed by Joel Ashton McCarthy and Bryant H. Boesen that follows the latter's adventures with his 60-year-old parents at the "infamous", annual Burning Man arts festival in Black Rock Desert.  Their journey takes them on a road-trip from Vancouver, BC to northern Nevada in a 35-foot school bus.  It provides a, "intimate, behind-the-scenes look at the preparation for, the journey to and the adventures at the least-likely family vacation imaginable."

Black Rock Desert: The Black Rock Desert is a semi-arid region "(in the Great Basin shrub steppe eco-region)", of lava beds and playa, or alkali flats, situated in the Black Rock Desert-High Rock Canyon Emigrant Trails National Conservation Area, a silt playa 100 mi north of Reno, Nevada that encompasses more than 300000 acre of land and contains more than 120 mi of historic trails.  It is in the northern Nevada section of the Great Basin with a lakebed that is a dry remnant of Pleistocene Lake Lahontan.  The average annual precipitation "(years 1971-2000)" at Gerlach, Nevada (extreme south-west of the desert) is 7.90 in .  The Great Basin, named for the geography in which water is unable to flow out and remains in the basin, is a rugged land serrated by hundreds of mountain ranges, dried by wind and sun, with spectacular skies and scenic landscapes.  The region is notable for its paleogeologic features, as an area of 19th-century Emigrant Trails to California, as a venue for rocketry, and as an alternative to the Bonneville Salt Flats in northwestern Utah, for setting land speed records (Mach 1.02 in 1997).  It is also the location for the annual Burning Man festival.

Black Rock Desert Wilderness: The Black Rock Desert Wilderness is a U S Wilderness Area in Nevada under the Bureau of Land Management.  It is located in the east arm of the Black Rock Desert playa east of the Black Rock Range and west of the Jackson Mountains.

Question: The Temple of Flux was a large temporary art project created by The Flux Foundation for Burning Man, an annual gathering that takes place at Black Rock City—a temporary city erected in the Black Rock Desert in which location?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "art_project_name": {
      "type": "string",
      "description": "The name of the art project."
    },
    "event_name": {
      "type": "string",
      "description": "The name of the event where the art project was featured."
    },
    "location_details": {
      "type": "object",
      "properties": {
        "desert_name": {
          "type": "string",
          "description": "The name of the desert where the event takes place."
        },
        "state": {
          "type": "string",
          "description": "The state where the desert is located."
        }
      },
      "required": [
        "desert_name",
        "state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "art_project_name",
    "event_name",
    "location_details"
  ],
  "additionalProperties": false
}
