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
Viking expansion: Viking expansion is the process by which the Vikings sailed most of the North Atlantic, reaching south to North Africa and east to Russia, Constantinople and the Middle East as looters, traders, colonists and mercenaries.  Vikings under Leif Ericsson, the heir to Erik the Red, reached North America and set up a short-lived settlement in present-day L'Anse aux Meadows, Newfoundland and Labrador, Canada.  Longer and more established settlements were formed in Greenland, Iceland, Great Britain and Normandy.

Siege of Paris (845): The Siege of Paris and the Sack of Paris of 845 was the culmination of a Viking invasion of the kingdom of the West Franks.  The Viking forces were led by a Norse chieftain named "Reginherus", or Ragnar, who traditionally has been identified with the legendary saga character Ragnar Lodbrok.  Ragnar's fleet of 120 Viking ships, carrying thousands of men, entered the Seine in March and proceeded to sail up the river.  The West Frankish king Charles the Bald assembled a smaller army in response, but as the Vikings defeated one division, comprising half of the army, the remaining forces retreated.  The Vikings reached Paris at the end of the month, during Easter.  After plundering and occupying the city, the Vikings withdrew when they had been paid a ransom of 7,000 French livres (2570 kg ) of silver and gold from Charles the Bald.

Irminger Current: The Irminger Current is a north Atlantic ocean current setting westward off the southwest coast of Iceland.  It is composed of relatively warm and saline waters from the eastern North Atlantic that are fed by the North Atlantic Drift.  The Irminger Current is part of the North Atlantic subpolar gyre.

Viking raid warfare and tactics: Vikings were members of tribes, originally from Scandinavia, of Norse ancestry, who gained a reputation for their raids and piracy in many parts of Europe, especially England, Ireland, and Frankish territories.  The term "Viking Age" refers to the period roughly from 793 AD to the late 11th-century in Europe.  In this era Viking activity started with raids on Christian lands in England and eventually expanded to mainland Europe, including parts of present-day Russia.  While maritime battles were rare, Viking bands proved very successful in raiding coastal towns and monasteries due to their efficient ships, intimidating war-tactics, skilful hand-to-hand combat, and fearlessness.  What started as Viking raids on small towns transformed into the establishment of important agricultural spaces and commercial trading-hubs across Europe through rudimentary colonization.  Vikings' tactics in warfare gave them an enormous advantage in successfully raiding (and later colonizing) despite their small population in comparison to that of their enemies.

Norse colonization of North America: The Norse colonization of North America began in the late 10th century AD when Norsemen explored and settled areas of the North Atlantic including the northeastern fringes of North America.  Viking houses were found at L’Anse aux Meadows near the northern tip of Newfoundland in 1960.  This discovery aided the reignition of archaeological exploration for the Vikings in the north Atlantic.

Barbary pirates: The Barbary pirates, sometimes called Barbary corsairs or Ottoman corsairs, were pirates and privateers who operated from North Africa, based primarily in the ports of Salé, Rabat, Algiers, Tunis, and Tripoli.  This area was known in Europe as the Barbary Coast, a term derived from the name of its Berber inhabitants.  Their predation extended throughout the Mediterranean, south along West Africa's Atlantic seaboard and even South America, and into the North Atlantic as far north as Iceland, but they primarily operated in the western Mediterranean.  In addition to seizing ships, they engaged in "Razzias", raids on European coastal towns and villages, mainly in Italy, France, Spain, and Portugal, but also in the British Isles, the Netherlands and as far away as Iceland.  The main purpose of their attacks was to capture Christian slaves for the Ottoman slave trade as well as the general Muslim slavery market in North Africa and the Middle East.

North Atlantic Deep Water: North Atlantic Deep Water (NADW) is a deep water mass formed in the North Atlantic Ocean.  Thermohaline circulation of the world's oceans involves the flow of warm surface waters from the southern hemisphere into the North Atlantic.  Water flowing northward becomes modified through evaporation and mixing with other water masses, leading to increased salinity.  When this water reaches the North Atlantic it cools and sinks through convection, due to its decreased temperature and increased salinity resulting in increased density.  NADW is the outflow of this thick deep layer, which can be detected by its high salinity, high oxygen content, nutrient minima, and chlorofluorocarbons (CFCs).  CFCs are anthropogenic substances that enter the surface of the ocean from gas exchange with the atmosphere.  This distinct composition allows its path to be traced as it mixes with Circumpolar Deep Water (CDW), which in turn fills the deep Indian Ocean and part of the South Pacific.  NADW and its formation is essential to the Atlantic Meridional Overturning Circulation (AMOC), which is responsible for transporting large amounts of water, heat, salt, carbon, nutrients and other substances from the Tropical Atlantic to the Mid and High Latitude Atlantic.  In the conveyor belt model of thermohaline circulation of the world's oceans, the sinking of NADW pulls the waters of the North Atlantic drift northward; however, this is almost certainly an oversimplification of the actual relationship between NADW formation and the strength of the Gulf Stream/North Atlantic drift.

North Atlantic Squadron: The North Atlantic Squadron was a section of the United States Navy operating in the North Atlantic.  It was renamed as the North Atlantic Fleet in 1902.  In 1905 the European and South Atlantic Squadrons were abolished and absorbed into the North Atlantic Fleet.  On 1 January 1906, the Navy's Atlantic Fleet was established by combining the North Atlantic Fleet with the South Atlantic Squadron.

North Atlantic Igneous Province: The North Atlantic Igneous Province (NAIP) is a large igneous province in the North Atlantic, centered on Iceland.  In the Paleogene, the province formed the Thulean Plateau, a large basaltic lava plain, which extended over at least 1.3×10 km in area and 6.6×10 km in volume.  The plateau was broken up during the opening of the North Atlantic Ocean leaving remnants existing in Northern Ireland, bits of northwestern Scotland, the Faroe Islands, bits of northwestern Iceland, eastern Greenland and western Norway and many of the islands located in the north eastern portion of the North Atlantic Ocean.  The igneous province is the origin of the Giant's Causeway and Fingal's Cave.  The province is also known as Brito-Arctic province (also known as the North Atlantic Tertiary Volcanic Province) and the portions of the province in the British Isles is also called the British Tertiary Volcanic Province or British Tertiary Igneous Province.

Leif Erikson: Leif Erikson or Leif Ericson (Old Norse: "Leifr Eiríksson" ; Icelandic: "Leifur Eiríksson"; Norwegian: "Leiv Eiriksson" 970 – c. 1020) was a Norse explorer from Iceland.  He was the first known European to have discovered continental North America (excluding Greenland), before Christopher Columbus (or possibly Saint Brendan).  According to the Sagas of Icelanders, he established a Norse settlement at Vinland, tentatively identified with the Norse L'Anse aux Meadows on the northern tip of Newfoundland in modern-day Canada.  Later archaeological evidence suggests that Vinland may have been the areas around the Gulf of St. Lawrence and that the L'Anse aux Meadows site was a ship repair station.

Question: Which Norse explorer from Iceland led the Viking expansion where Vikings sailed the North Atlantic and reached south to North Africa and Russia?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "explorer_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "origin": {
          "type": "string"
        },
        "title": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "origin",
        "title"
      ],
      "additionalProperties": false
    },
    "viking_expansion_contribution": {
      "type": "object",
      "properties": {
        "led_expedition_to": {
          "type": "string"
        },
        "settlement_established": {
          "type": "string"
        }
      },
      "required": [
        "led_expedition_to",
        "settlement_established"
      ],
      "additionalProperties": false
    },
    "overall_viking_expansion_scope": {
      "type": "object",
      "properties": {
        "regions_sailed": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "activities": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "regions_sailed",
        "activities"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "explorer_details",
    "viking_expansion_contribution",
    "overall_viking_expansion_scope"
  ],
  "additionalProperties": false
}
