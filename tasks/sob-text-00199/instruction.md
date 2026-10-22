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
Oran: Oran (Arabic: وهران‎ ‎ , "Wahrān"; Berber: ⵡⴻⵂⵔⴰⵏ) is a coastal city that is located in the north-west of Algeria.  It is considered the second most important city of Algeria after the capital Algiers, due to its commercial, industrial, and cultural importance.  It is 432 km from Algiers.  The total population of the city was 759,645 in 2008, while the metropolitan area has a population of approximately 1,500,000 making it the second largest city in Algeria.

Steve Marriner: Steve Marriner, also known as Steve Gregg, (born 1984 in Ottawa, Ontario) is a Canadian multi-instrumentalist, singer, songwriter and record producer based in Ottawa, Ontario.  He first garnered attention in the Ottawa blues scene in his early teens as a prodigy blues harp (harmonica) player.  He also plays baritone guitar, electric guitar, piano, Hammond organ, upright bass and electric bass).  As of 2016, he is the frontman, singer, one of two guitarists and harmonica player for the Canadian rock'n'roll-blues group MonkeyJunk.  The band's album "To Behold" won the 2011 Juno Award for Blues Album of the Year.  Prior to forming MonkeyJunk, Marriner was a member of two Ottawa bands, the Johnny Russell Band and the JW-Jones Blues Band.  He appeared several times on the mainstage of the Ottawa Bluesfest as a member of the JW-Jones Blues Band.

Swansea: Swansea ( ; Welsh: ' ] ), officially known as the City and County of Swansea"' ( ), is a coastal city and county in Wales.  It is the second largest city in Wales after Cardiff, and the twenty-fifth largest city in the United Kingdom.  Swansea lies within the historic county boundaries of Glamorgan and the ancient Welsh commote of Gŵyr.  Situated on the sandy South West Wales coast, the county area includes the Gower Peninsula and the Lliw uplands.  According to its local council, the City and County of Swansea had a population of 241,300 in 2014.  The last official census stated that the city, metropolitan and urban areas combined concluded to be a total of 462,000 in 2011, making it the second most populous local authority area in Wales after Cardiff.  During its 19th-century industrial heyday, Swansea was a key centre of the copper industry, earning the nickname 'Copperopolis'.

Marching Owl Band: The Marching Owl Band (aka The MOB or the Blues Band of South Main) is the Rice University "marching band" in the sense that it is the official ensemble that performs during football games, some basketball games, parades, and other public events.  However, the MOB is not a traditional marching band, but rather a scatter band; members do not march, and some members play non-standard instruments (or no instrument at all).  For example, in the most recent season these instruments included violins, violas, a cello, electric guitar, electric bass and electric piano.  Extras known as Show Assistants are also a perennial inclusion in the MOB; these students play no instruments besides the kazoo (or an occasional didgeridoo), but are responsible for constructing and employing props in the half-time shows and acting out any mime or gag bits during performances.  Rather than wear traditional marching band attire, The MOB instead dons pinstriped three-piece suits, ties, sunglasses, fedoras, and (in the case of Show Assistants) tommy gun props.  (This attire is an obvious nod to the band's acronym, though in practice falls somewhere between the style of Capone-era mobsters and The Blues Brothers.)  The group is known for satirical football halftime shows which, as MOB director Chuck Throckmorton says, poke fun at rival universities' sacred cows.

Rick Estrin &amp; The Nightcats: Rick Estrin & the Nightcats are an American four-piece electric blues band (formed in 2008 after the dissolution of Little Charlie & The Nightcats, of which three of the band were members), and consisting of harmonicist/lead vocalist and songwriter Rick Estrin, guitarist Kid Andersen, bassist Lorenzo Farrell and drummer and songwriter J. Hansen.  "Blues Revue" magazine said, “The ‘Cats are one of modern blues’ most versatile bands.”  "Living Blues" said, “Estrin’s harp work is masterful” and their music is “intelligently conceived and executed and hugely entertaining.”

Michael Fonfara: Michael Fonfara (born August 11, 1946) is a Canadian keyboard player who is most notable for his work as a member of The Electric Flag and Rhinoceros in the 1960s, Rough Trade and Lou Reed's backing band in the 1970s and The Downchild Blues Band, from 1990 to the present.  He studied classical piano at the Toronto Conservatory of Music.  He is a multiple Maple Blues Award winner as Piano/Keyboardist of the year and a Juno Award winner with the Downchild Blues Band.  His distinguished musical career was so honoured by the Maple Blues Awards as early as 2000 and a Juno Award in 2014.

Wadi-e-Hussain: Wadi-e-Hussain (Urdu: وادئ حسین‎ , "The Valley of Hussain") is the largest organized and the first online cemetery in Pakistan, located in the northern part of the coastal city of Karachi on Karachi–Hyderabad Motorway; it is connected to the city by the main highway connecting Karachi with Hyderabad.  The cemetery has been an inspiration for the local people in the coastal city.  Apart from elders, there is a specific column/place for the children who die in their early ages.  However, the cemetery has been a common burial cite for the local Shiite Muslims.  The graveyard is also decorated with the special lights on special occasions such as Eid al-Fitr, Eid al-Adha, Mid-Sha'ban etc.

Electrofied: Electrofied (sometimes referred to as The Electrofied Blues Band) is an American electric blues band, featuring Tony Fazio on lead guitar, Rob Rusteberg on bass, Richard James Burgess on drums and singer, Scott Taylor, as lead vocalist.  Scott Taylor has also recorded for BackBeat Records.

The Electric Revelators: The Electric Revelators are a blues band, formed in Swansea 2004, Wales, added Jerry Donahue ex-member of Fairport Convention and Chris Rea Band to the line-up in 2011.  Originally called The Revelators they added Electric to the name in 2009 when they toured with The Animals and David "Honeyboy" Edwards.

The Electric Flag: The Electric Flag was an American blues rock soul group, led by guitarist Mike Bloomfield, keyboardist Barry Goldberg and drummer Buddy Miles, and featuring other musicians such as vocalist Nick Gravenites and bassist Harvey Brooks.  Bloomfield formed the Electric Flag in 1967, following his stint with the Butterfield Blues Band.  The band reached its peak with the 1968 release, "A Long Time Comin'", a fusion of rock, jazz, and R&B styles that charted well in the "Billboard" Pop Albums chart.  Their initial recording was a soundtrack for "The Trip", a movie about an LSD experience by Peter Fonda, written by Jack Nicholson and directed by Roger Corman.

Question: Which coastal city is the second largest in Wales and home to the blues band The Electric Revelators? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "city_name": {
      "type": "string",
      "description": "The name of the coastal city."
    },
    "is_coastal": {
      "type": "boolean",
      "description": "Indicates if the city is a coastal city."
    },
    "country": {
      "type": "string",
      "description": "The country where the city is located."
    },
    "size_ranking_details": {
      "type": "object",
      "properties": {
        "rank_description": {
          "type": "string",
          "description": "Description of the city's size ranking within its country."
        },
        "larger_city_after_which_it_is_ranked": {
          "type": "string",
          "description": "The name of the city that is larger, if applicable for the ranking."
        }
      },
      "required": [
        "rank_description",
        "larger_city_after_which_it_is_ranked"
      ],
      "additionalProperties": false
    },
    "associated_band": {
      "type": "object",
      "properties": {
        "band_name": {
          "type": "string",
          "description": "The name of the blues band associated with the city."
        },
        "band_genre": {
          "type": "string",
          "description": "The musical genre of the band."
        },
        "formation_year": {
          "type": "integer",
          "description": "The year the band was formed."
        },
        "formation_location": {
          "type": "string",
          "description": "The city where the band was formed."
        }
      },
      "required": [
        "band_name",
        "band_genre",
        "formation_year",
        "formation_location"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "city_name",
    "is_coastal",
    "country",
    "size_ranking_details",
    "associated_band"
  ],
  "additionalProperties": false
}
