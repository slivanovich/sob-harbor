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
Anders Behring Breivik: Anders Behring Breivik (] ; born 13 February 1979), known as Fjotolf Hansen from 2017, is a Norwegian far-right terrorist who committed the 2011 Norway attacks.  On 22 July 2011 he killed eight people by detonating a van bomb amid Regjeringskvartalet in Oslo, then shot dead 69 participants of a Workers' Youth League (AUF) summer camp on the island of Utøya.  In August 2012 he was convicted of mass murder, causing a fatal explosion, and terrorism.

Camp Onyahsa: Camp Onyahsa is a YMCA summer camp located on Lake Chautauqua in Dewittville, New York, and one of the oldest summer camps in the U.S.  The word "Onyahsa" is purported to be Haudonosaunee in origin, and relates to the shape of the Lake.  The Camp was given this name by director, Roy Wagner, in 1924.  According to Camp legend, the word is used for "hello" and "goodbye."  It was established in 1898 by the Young Men's Christian Association of Jamestown, New York and served boys from this growing industrial town as well as males from Westfield, NY and Buffalo, NY during its first decades.  In 1924, the camp moved from rented acreage near Cheney's Point, on Chautauqua Lake to Dewittville, NY.  The property was purchased for $12,000 from funds generated through the Jamestown YMCA's capital campaign in 1925.  At this time, Roy A. Wagner directed both the summer camp and the Boys Department of the YMCA.  He led both programs until his resignation in 1946.  After several short-term directors, Spiro Bello became director in 1962 and directed Onyahsa and the Jamestown YMCA's Youth Department until his retirement in 1984.

Camp Summerlane: Camp Summerlane was an integrated humanist summer camp in Western North Carolina founded in 1963 by Rev. George von Hilsheimer with the support of Paul Krassner, editor of "The Realist".  On July 11, 1963, the camp was attacked by an armed mob, which burned down a building and shot out the window of a camp bus, leading to the closure of the camp.  In a statement to the Tuscaloosa News von Hilsheimer asserted that the attack was racially motivated and that, "the only issue the mob was interested in was integration."  An article distributed by the Rosman Chamber of Commerce prior to the attack alleged that the camp condoned free love and immorality.

2016 Berlin attack: On 19 December 2016, a truck was deliberately driven into the Christmas market next to the Kaiser Wilhelm Memorial Church at Breitscheidplatz in Berlin, leaving 12 people dead and 56 others injured a total of 68 people that were involved in this incident.  One of the victims was the truck's original driver, Łukasz Urban, who was found shot dead in the passenger seat.  The perpetrator was Anis Amri, a Tunisian failed asylum seeker, urged by Islamic State of Iraq and the Levant.  Four days after the attack, he was killed in a shootout with police near Milan in Italy.  An initial suspect was arrested and later released due to lack of evidence.  The event was designated as a terrorist attack.

Camp Deer Run: Camp Deer Run is a Christian summer camp for girls located on Lake Winnipesaukee in NH.  It was started in 1964 on the property of Camp Brookwoods a summer camp for boys.  Camp sessions are either two or four weeks long.  First time campers under the age of 10 can participate in a one-week explorer club program designed to introduce your child into the wonderful adventure of summer camp.

Arab Peace Initiative: The Arab Peace Initiative (Arabic: ‎ ‎ ), also known as the "Saudi Initiative", is a 10 sentence proposal for an end to the Arab–Israeli conflict that was endorsed by the Arab League in 2002 at the Beirut Summit and re-endorsed at the 2007 Arab League summit and at the 2017 Arab League summit.  The initiative calls for normalizing relations between the Arab region and Israel, in exchange for a full withdrawal by Israel from the occupied territories (including East Jerusalem) and a "just settlement" of the Palestinian refugee problem based on UN Resolution 194.  The Initiative was initially overshadowed by the Passover Massacre, a major terrorist attack that took place on March 27, 2002, the day before the Initiative was published.

The FREE Initiative: The Far-Right Extremism in Europe Initiative (The FREE Initiative) is an online resource for practitioners responding to far-right extremism and violence.  It was founded with support from the European Commission Prevention of and Fight Against Crime Programme, and a project led by the Ministry of Justice (Sweden) in partnership with the Ministry of Social Affairs (Denmark), Ministry of Security and Justice (Netherlands), Royal Norwegian Ministry of Justice and Public Safety, and the Ministry of the Interior (Finland).  It was the first project endorsed by governments and funded by the European Commission solely on far-right extremism and radicalisation in the aftermath of the 2011 Norway attacks perpetrated by a far-right terrorist Anders Behring Breivik.  The online resource launched on 1 September 2014.

2014 Jerusalem tractor attack: The 2014 Jerusalem tractor attack was a terrorist ramming attack that occurred on 4 August 2014, when an Arab drove an excavator type of tractor out of a construction site, injuring several pedestrians and killing one man before ramming the tractor into a public bus, overturning the bus and then hitting it repeatedly.  The terrorist was shot dead at the scene by a police officer while still seated at the wheel of the tractor and continuing to attack the bus by swinging the arm of the excavator against it.

1994 Shankill Road killings: The 1994 Shankill Road killings took place on 16 June 1994.  The Irish National Liberation Army (INLA) shot dead three Ulster Volunteer Force (UVF) members – high-ranking member Trevor King, Colin Craig and David Hamilton – on the Shankill Road in Belfast, close to the UVF HQ.The following day, the UVF launched two 'retaliatory' attacks.  In the first, UVF members shot dead a Catholic civilian taxi driver in Carrickfergus.  In the second, they shot dead two Protestant civilians in Newtownabbey, whom they believed were Catholics.  The Loughinisland massacre, two days later, is believed to have been a further retaliation.

1980 Antwerp summer camp attack: In 1980 Antwerp summer camp attack, on 28 July 1980, Said Al Nasr, a Syria-born Palestinian, used grenades to attack a group of 40 Jewish children waiting with their families for a bus to take them to summer camp.  One boy was killed and 20 other people were wounded in the attack.  The attacker was caught.

Question: The FREE Initiative was the first project endorsed by governments after an attack by a far-right terrorist who shot dead how many people at a summer camp?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "initiative_name": {
      "type": "string",
      "description": "The name of the initiative."
    },
    "first_project_endorsed_by_governments": {
      "type": "boolean",
      "description": "Indicates if this was the first project endorsed by governments on far-right extremism after the attack."
    },
    "related_attack": {
      "type": "object",
      "properties": {
        "attack_name": {
          "type": "string",
          "description": "The name of the attack that prompted the initiative."
        },
        "perpetrator_name": {
          "type": "string",
          "description": "The name of the far-right terrorist who committed the attack."
        },
        "summer_camp_victims": {
          "type": "object",
          "properties": {
            "count": {
              "type": "integer",
              "description": "The number of people shot dead at the summer camp."
            },
            "location": {
              "type": "string",
              "description": "The island where the summer camp attack occurred."
            },
            "victim_description": {
              "type": "string",
              "description": "A description of the victims at the summer camp."
            }
          },
          "required": [
            "count",
            "location",
            "victim_description"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "attack_name",
        "perpetrator_name",
        "summer_camp_victims"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "initiative_name",
    "first_project_endorsed_by_governments",
    "related_attack"
  ],
  "additionalProperties": false
}
