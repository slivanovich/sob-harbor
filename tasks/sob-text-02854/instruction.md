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
The Rendlesham UFO Incident: The Rendlesham UFO Incident (released in the US as Hangar 10) is a 2014 British horror film directed by Daniel Simpson.  It stars Danny Shayle, Abbie Salt, and Robert Curtis as three friends who become lost in the Rendlesham Forest and discover evidence of UFO activity, decades after the Rendlesham Forest incident.  It premiered at the Colchester Film Festival on 22 October 2014 and was released in the UK on 9 February 2015.  It is shot in the style of found footage.

Charles I. Halt: Charles I. Halt (Born 1939) is a retired United States Air Force colonel and a former deputy base commander of RAF Bentwaters, near Woodbridge, Suffolk.  After serving in Vietnam, Japan and Korea, he was assigned to Bentwaters as deputy commander.  The Rendlesham Forest incident of late December 1980 occurred shortly afterwards, and he was an important witness to events on the second night of sightings.

Orang Mawas: There have been many reported sightings since the 1950s, and in 1995 in Johor large tracks with four toes were reported.  In November 2005 a much publicised sighting occurred when three workers clearing ground for a pond saw a Mawa family of two adults and a child walking near the Kincin River.  Later large humanoid footprints were found, including one 18 in (46 cm) long.  A photograph of a fresh footprint in tar, attributed to the Mawas, was printed in Malaysian newspapers in January 2006.  A government team has been searching for more evidence of the Mawas.  In late January 2006, the authorities in Johor announced an official expedition to prove the creature's existence, making it the first country to have an official hunt for a mystery hominid.  A news story on Cryptomundo.com said that an Orang Mawas was captured in Johor on the expedition of Johor, as reported on April 19, 2006 in the "Berita Harian", but an official report released by "Bernama" denied it.

Georgina Bruni: Georgina Bruni (born Linda Naylor; 1947 – 19 January 2008) was a British businesswoman and a UFO researcher best known for her book on the Rendlesham Forest incident, "You Can't Tell the People".  She worked as a celebrity events organizer and as the founder and Editor in Chief of the online magazine "Hot Gossip".

Flying saucer: A flying saucer (also referred to as a flying disc) is a descriptive term for a supposed type of flying craft having a disc or saucer-shaped body, commonly used generically to refer to an anomalous flying object.  The term was coined in 1930 but has generally been supplanted since 1952 by the United States Air Force term unidentified flying objects or UFO's.  Early reported sightings of unknown "flying saucers" usually described them as silver or metallic, sometimes reported as covered with navigation lights or surrounded with a glowing light, hovering or moving rapidly, either alone or in tight formations with other similar craft, and exhibiting high maneuverability.

Sandlings Forest: Sandlings Forest is a 2,483.8 hectare biological Site of Special Scientific Interest in two large blocks, Rendlesham Forest and Tunstall Forest, and two small ones, between Woodbrodge and Aldeburgh in Suffolk.  It is partly in the Sandlings Special Protection Area under the European Union Directive on the Conservation of Wild Birds.  It is in the Suffolk Coast and Heaths Area of Outstanding Natural Beauty.

Butley River: The Butley River or Butley Creek is a tributary of the River Ore in the English county of Suffolk.  The river has its source in the Rendlesham Forest area to the east of Eyke.

Identification studies of UFOs: Identifying unidentified flying objects is a difficult task due to the normally poor quality of the evidence provided by those who report sighting the objects.  Nevertheless, most officially investigated UFO sightings, such as from the U.S. Air Force's Project Blue Book, have been identified as being due to honest misidentifications of natural phenomena, aircraft, or other prosaic explanations.  In early U.S. Air Force attempts to explain UFO sightings, unexplained sightings routinely numbered over one in five reports.  However, in early 1953, right after the CIA's Robertson Panel, percentages of unexplained sightings dropped precipitously, usually being only a few percent in any given year.  When Project Blue Book closed down in 1970, only 6% of all cases were classified as being truly unidentified.

Rendlesham Forest incident: In late December 1980, there were a series of reported sightings of unexplained lights near Rendlesham Forest, Suffolk, England, which have become linked with claims of UFO landings.  The events occurred just outside RAF Woodbridge, which was used at the time by the U.S. Air Force.  USAF personnel, including deputy base commander Lieutenant Colonel Charles I. Halt, claimed to see things they described as a UFO sighting.

Michigan Dogman: The Michigan Dogman is a cryptozoological creature allegedly first reported in 1887 in Wexford County, Michigan.  The creature is described as a seven-foot tall, blue-eyed, or amber-eyed bipedal canine-like animal with the torso of a man and a fearsome howl that sounds like a human scream.  According to legends, the Michigan Dogman appears in a seven-year cycle.  Sightings have been reported in several locations throughout Michigan, primarily in the northwestern quadrant of the Lower Peninsula.  In 1987, the legend of the Michigan Dogman gained popularity when disc jockey Steve Cook at WTCM-FM recorded a song about the creature and its reported sightings.

Question: On what series of reported sightings of unexplained lights near Rendlesham Forest, Suffolk, England did Georgina Bruni report?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "researcher": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the researcher."
        },
        "role": {
          "type": "string",
          "description": "The role or profession of the researcher."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "researched_incident": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the incident researched."
        },
        "location": {
          "type": "string",
          "description": "The location where the incident occurred."
        },
        "description_summary": {
          "type": "string",
          "description": "A brief summary of the incident."
        },
        "year": {
          "type": "integer",
          "description": "The year the incident occurred."
        }
      },
      "required": [
        "name",
        "location",
        "description_summary",
        "year"
      ],
      "additionalProperties": false
    },
    "publication_about_incident": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the publication related to the incident."
        }
      },
      "required": [
        "title"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "researcher",
    "researched_incident",
    "publication_about_incident"
  ],
  "additionalProperties": false
}
