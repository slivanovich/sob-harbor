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
Gun Shy (TV series): Gun Shy is an American sitcom that was shown on CBS from March 15 to April 19, 1983.  The series, produced by Walt Disney Productions, was based on its popular comedy-western films: "The Apple Dumpling Gang" and "The Apple Dumpling Gang Rides Again".

Dennis Fimple: Dennis Clarke Fimple (November 11, 1940 – August 23, 2002) was an American character actor.  He appeared in a variety of TV shows including "Here Come the Brides", "Petticoat Junction", "Matt Houston", "M*A*S*H", "Centennial", "Simon & Simon", "Sledge Hammer! ", "Knight Rider", "Quantum Leap" and "ER".  He also had roles in films such as "Truck Stop Women" (1974), "The Apple Dumpling Gang" (1975), "Mackintosh and T.J." (1975), "Stay Hungry" (1976), "King Kong" (1976), "The Shadow of Chikara" (1977), "Goin' South" (1978), "The Wild Women of Chastity Gulch" (1982) and "Maverick" (1994), and shared the lead in "Bootleggers" (1974) and "Creature from Black Lake" (1976).

The Apple Dumpling Gang Rides Again: The Apple Dumpling Gang Rides Again is a 1979 American comedy-western film produced by Walt Disney Productions and a sequel to "The Apple Dumpling Gang" (1975), starring the comedy duo of Tim Conway and Don Knotts reprising their respective roles as Amos and Theodore.  The film also stars Tim Matheson, Harry Morgan, and Kenneth Mars.  Ruth Buzzi appears in a small cameo as a wild farsighted woman.  Robert Totten, who directed installments of "Gunsmoke", also had a small part in the film.

Billardiera scandens: Billardiera scandens, commonly known as Apple Berry or Apple Dumpling, is a small shrub or twining plant of the Pittosporaceae family which occurs in forests in the coastal and tableland areas of all states and territories in Australia, apart from the Northern Territory and Western Australia.  It has a silky touch and appearance that becomes more brittle as the dense growth matures.  The inflorescence consists of a single or paired yellow flowers, pink-tinged yellow sepals and bright yellow petals and is attached to a hairy drooping peduncle.  The summer flush produces fruit of oblong berries up to 30 mm long, initially green in colour and covered in fine hair - somewhat akin to a tiny kiwifruit in appearance.

The Apple Dumpling Gang (film): The Apple Dumpling Gang is a 1975 American comedy-western film produced by Walt Disney Productions about a slick gambler named Russell Donovan (Bill Bixby) who is duped into taking care of a group of orphans who eventually strike gold during the California Gold Rush.

The Sasquatch Gang: The Sasquatch Gang (also known as The Sasquatch Dumpling Gang) is a 2006 comedy film written and directed by Tim Skousen, the first assistant director on "Napoleon Dynamite".

It's a Small World: It's a Small World (currently styled it's a small world) is a water-based dark ride located in the Fantasyland area at the various Walt Disney Parks and Resorts worldwide; these include: Disneyland Park in Anaheim, California, the Magic Kingdom at Walt Disney World Resort in Lake Buena Vista, Florida, Tokyo Disneyland, Disneyland Paris, and Hong Kong Disneyland.  The ride features over 300 audio-animatronic children in traditional costumes from cultures around the world, frolicking in a spirit of international unity, and singing the attraction's title song, which has a theme of global peace.

The Apple Dumpling Gang: The Apple Dumpling Gang is a 1971 novel by Jack Bickham, about a group of orphaned children during the California gold rush.  They encounter a gambler who reluctantly helps them, as well as a pair of hapless robbers who are after the gold the children have found.

Buddy Baker (composer): Norman Dale "Buddy" Baker (January 4, 1918 – July 26, 2002) was an American composer who, together with Paul J. Smith, scored many Disney films, such as "The Apple Dumpling Gang" in 1975, "The Apple Dumpling Gang Rides Again" in 1979, "The Shaggy D.A." in 1976, "The Many Adventures of Winnie the Pooh" in 1977, and "The Fox and the Hound" in 1981.

Jack Bickham: Jack Miles Bickham (September 2, 1930 – July 25, 1997) was an American author who wrote 75 published novels, of which two were made into movies, "The Apple Dumpling Gang" and "Baker's Hawk".

Question: It's a Small World and The Apple Dumpling Gang, have which related organization in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_organization_name": {
      "type": "string",
      "description": "The name of the organization common to both entities."
    },
    "entities_involved": {
      "type": "array",
      "description": "A list of the entities that share the common organization.",
      "items": {
        "type": "string"
      }
    },
    "organization_category": {
      "type": "string",
      "description": "The general category or type of the common organization."
    }
  },
  "required": [
    "common_organization_name",
    "entities_involved",
    "organization_category"
  ],
  "additionalProperties": false
}
