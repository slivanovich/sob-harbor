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
Star Tours – The Adventures Continue: Star Tours – The Adventures Continue (also known as Star Tours 3-D) is a 3D motion simulator attraction located at Disney's Hollywood Studios, Disneyland, Tokyo Disneyland, and Disneyland Paris.  Set in the fictional "Star Wars" universe "Star Tours – The Adventures Continue" takes guests on a turbulent excursion trip across the galaxy, as droids C-3PO and R2-D2 attempt to safely return a rebel spy to the Rebel Alliance.

Horizons (Epcot): Horizons was the name of a dark ride attraction at Epcot (then known as EPCOT Center), a theme park at Walt Disney World in Bay Lake, Florida.  Located on the eastern side of the "Future World" section of Epcot, the attraction used Disney's Omnimover conveyance system, which took guests past show scenes depicting visions of the future.  It is believed to be the sequel to Walt Disney's Carousel of Progress, an attraction in Tomorrowland at Walt Disney World's Magic Kingdom.  Horizons was the only attraction in "Future World" to showcase all of Epcot's "Future World" elements: communication, community interaction, energy, transportation, anatomy, physiology, along with man's relationship to the sea, land, air, and space.  The attraction officially opened on October 1, 1983, as part of Phase II of Epcot.  Horizons originally closed in December 1994, a little more than a year after General Electric had ended its sponsorship of the attraction.  Horizons re-opened in December 1995 due to the closure of two other attractions that were down for refurbishment in "Future World", Universe of Energy and World of Motion.  The attraction permanently closed on January 9, 1999, after which the attraction was dismantled and its structure demolished to make room for , a motion simulator thrill ride that opened on October 9, 2003.

Body Wars: Body Wars was a motion simulator attraction at several Disney theme parks, based on the successful "Fantastic Voyage" simulator ride at the Wonders of Life pavilion at Walt Disney World Resort's Epcot in which the riders were "shrunk" and carried out a mission inside a human body.  The ride was based upon the Advanced Technology Leisure Application Simulator.  The ride is no longer in operation along with the other attractions at the Wonders of Life pavilion, which opened on October 19, 1989, and closed on January 1, 2007.

Lego Star Wars II: The Original Trilogy: Lego Star Wars II: The Original Trilogy is a Lego-themed action-adventure video game developed by Traveller's Tales and published by LucasArts and TT Games Publishing.  It was released on 11 September 2006.  Part of the "Lego Star Wars" series, it is based on the "Star Wars" science fiction media franchise and Lego Group's "Star Wars"-themed toy line.  It follows the events of the "Star Wars" films "Star Wars", "The Empire Strikes Back" and "Return of the Jedi".  The game allows players to assume the roles of over 50 Lego versions of characters from the film series; customized characters can also be created.  Camera movement was improved from its predecessor—""; and the concept of "vehicle levels" was explored more thoroughly.  The game was revealed at American International Toy Fair 2006.  Promotions for the game were set up at chain stores across the United States.

Star Wars MUSH: Star Wars MUSH (commonly referred to as SW1) is a text-based online role-playing game.  "Star Wars MUSH" was created in May 1991 and was released to the public in January 1992.  The game predates the majority of ""Star Wars" expanded universe" and as such largely deviates from the established "Star Wars" universe set after "Return of the Jedi".  The game scenario system is based on the discontinued West End Games' .  The game persisted throughout the '90s as one of the net's more successful "Star Wars"-themed MUSHes, earning a feature in "The Incredible Internet Guide to Star Wars".

Europe in the Air: Europe in the Air was a motion simulator ride located at Busch Gardens Williamsburg, a theme park in Williamsburg, Virginia.  The attraction was similar in both ride and production to that of "Disney's Soarin' Over California" and "Star Tours".  Because of the theming of the park, Europe in the Air simulated flight over Europe's most notable icons.  The park stated the picture is "eight times clearer than HD."  Other features, such as fans, were used for a more realistic journey.  Europe in the Air replaced the Corkscrew Hill ride for the 2010 season.  It was previously sponsored by Aer Lingus.

Star Tours: Star Tours was a motion simulator attraction at several Disney theme parks, based on the successful "Star Wars" film series created by George Lucas.  Set in the "Star Wars" universe, the attraction sent guests on a excursion trip to Endor, whilst being caught in an altercation between the Rebel Alliance and the Galactic Empire.  The attraction featured Captain "Rex" RX-24 along with series regulars R2-D2 and C-3PO.

Soarin': Soarin' , also known as Soarin' Around the World and Soaring Over the Horizon, is a flight motion simulator attraction at Disney California Adventure, Epcot, and Shanghai Disneyland.  The ride employs a mechanical lift system, a 4K film presentation on an 80 ft concave 180-degree OMNIMAX laser projection screen, artificial scents and wind to simulate a hang gliding flight over several locations across six continents around the world.

Iron Man Experience: Iron Man Experience (Traditional Chinese: 鐵甲奇俠飛行之旅) is a 3-D motion simulator attraction in Tomorrowland at Hong Kong Disneyland, which opened on 11 January 2017.  The attraction is based on the Marvel Comics character Iron Man, becoming the first Disney attraction to be based on a Marvel property.  Set at the fictional Stark Expo, the attraction features Tony Stark recruiting guests to fend off extraterrestrial beings that are attacking Hong Kong.

Star Wars: Darth Plagueis: Star Wars: Darth Plagueis is a novel that is part of the "Star Wars" expanded universe.  It was written by James Luceno, and released on January 10, 2012.  The novel covers the later life and machinations of Sith lord Darth Plagueis, over a roughly fifty-year period pre-dating "Star Wars: The Phantom Menace".  The novel details Plagueis' overthrow of his own master Darth Tenebrous, his work as head of a powerful banking consortium on the Muun homeworld, his discovery, recruitment and training of the teenaged Sheev Palpatine of Naboo, and the efforts of Plagueis to undermine the Galactic Republic and ensure the dominance of the Dark Side of the Force.  The novel brings in scores of characters and locations already familiar in the "Star Wars" mythos, as well as introducing many others for the first time.  Events depicted on-screen in "Star Wars Episode I: The Phantom Menace", are re-told in "Star Wars: Darth Plagueis", often from a perspective not shown in the 1999 motion picture.

Question: What motion simulator attraction based on the successful "Star Wars" film series was Europe in the Air similar to?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "attraction_name": {
      "type": "string",
      "description": "The name of the motion simulator attraction."
    },
    "attraction_type": {
      "type": "string",
      "description": "The type of the attraction."
    },
    "based_on_franchise": {
      "type": "string",
      "description": "The media franchise the attraction is based on."
    },
    "similarity_context": {
      "type": "string",
      "description": "Context describing the similarity between Europe in the Air and the identified attraction."
    }
  },
  "required": [
    "attraction_name",
    "attraction_type",
    "based_on_franchise",
    "similarity_context"
  ],
  "additionalProperties": false
}
