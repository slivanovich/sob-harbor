{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nWoolly monkey sarcoma virus: Woolly monkey sarcoma virus (WMSV), with synonym Simian sarcoma virus (often abbreviated by SSV, but this may also stand for some species called 'Sulfolobus spindle-shaped virus', that belong to different genera in family Fuselloviridae) is a species of gammaretrovirus that infects primates.  First isolation was from a fibrosarcoma in a woolly monkey (genus \"Lagothrix\").  For its reproduction the virus needs a helper or associated virus which is called Simian sarcoma associated virus (SSAV).\n\nVoice of God Collective: Voice of God Collective is a British jazz music group led by guitarist Billy Jenkins, working mainly in the 1980s and 1990s.\n\nEddie Jenkins: Eddie Jenkins ((1895--)06 1895 – ) was a Welsh international footballer.  He was part of the Wales national football team, playing one match on 28 February 1925 against England.  He was the younger brother of Wales rugby union international Billy Jenkins.\n\nBurlesque (band): Burlesque were an English pub rock band formed in London in 1972 and disbanded in 1977.  Core members were Billy Jenkins and Ian Trimmer, who after Burlesque had disbanded went on to record and perform as Trimmer and Jenkins.\n\nBilly Sandow: Wilhelm Baumann (September 4, 1884 – September 15, 1972), better known as Billy Sandow, was an American professional wrestler and promoter.  He is best remembered as the manager of professional wrestler Ed \"Strangler\" Lewis and a subsequent member of the famed Gold Dust Trio promotion that changed the face of the industry during the 1920s (along with Lewis and Joseph \"Toots\" Mondt).  He may have taken his ring name from Eugen Sandow, a professional wrestler and strongman in the late 19th century; in turn, former WWE wrestler Damien Sandow would adopt his own ring name in honor of Sandow almost a century later.  Sandow also served as manager for such wrestling champions as Billy Jenkins, Marin Plestina, Jumping Joe Savoldi and Everett Marshall, and also used the ring name The Zebra Kid in 1951.  He was a charter inductee of the Wrestling Observer Newsletter Hall of Fame in 1996.\n\nBilly Jenkins (musician): Billy Jenkins (born 5 July 1956) is an English blues guitarist, composer, and bandleader.\n\nHepatitis E: Hepatitis E is a viral hepatitis (liver inflammation) caused by infection with a virus called hepatitis E virus.  It is one of five known human hepatitis viruses: A, B, C, D, and E. HEV is a positive-sense single-stranded non-enveloped RNA icosahedral virus, HEV has a fecal-oral transmission route.  Infection with this virus was first documented in 1955 during an outbreak in New Delhi, India.  A preventative vaccine (HEV 239) is approved for use in China.\n\nStewart Lee: Stewart Graham Lee (born 5 April 1968) is an English stand-up comedian, writer and director.  In the mid-1990s he was one half of the radio duo Lee and Herring, alongside Richard Herring.  He co-wrote and co-directed the mock Broadway hit \"\", a critical success that sparked a backlash from Christian groups who staged a series of protests outside its early stagings.\n\nScratches of Spain: Scratches of Spain is an album by English experimental jazz guitarist and bandleader Billy Jenkins, featuring the Voice of God Collective.  It was released on the Babel Records label in 1987.\n\nVirus Called The Blues: Virus Called The Blues was a 30-minute documentary spoof based on a day in the life of blues and jazz guitarist/songwriter Billy Jenkins and his band The Blues Collective.  The documentary was produced, directed by Craig Duncan who met Billy on the set of the BBC Two music series 'Jazz 606' in the mid nineties (filmed at the famous Jazz Venue 606 Club).  It features serious interviews and spoof action, plus actual performance from the band at The Blue Elephant Theatre, Camberwell, South-east London.  Also visible in the audience is stand up comedian Stewart Lee, a long-time friend of Jenkins.\n\nQuestion: What is the nationality of this stand up comedian and a friend of the guitarist/songwriter Billy Jenkins shown in the documentary spoof, Virus Called The Blues?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"comedian_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the stand-up comedian.\"\n    },\n    \"comedian_profession\": {\n      \"type\": \"string\",\n      \"description\": \"The profession of the comedian.\"\n    },\n    \"relationship_to_billy_jenkins\": {\n      \"type\": \"string\",\n      \"description\": \"The relationship between the comedian and Billy Jenkins.\"\n    },\n    \"documentary_spoof_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the documentary spoof where the comedian appeared.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the comedian.\"\n    }\n  },\n  \"required\": [\n    \"comedian_name\",\n    \"comedian_profession\",\n    \"relationship_to_billy_jenkins\",\n    \"documentary_spoof_title\",\n    \"nationality\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "comedian_name": {
        "type": "string",
        "description": "The name of the stand-up comedian."
      },
      "comedian_profession": {
        "type": "string",
        "description": "The profession of the comedian."
      },
      "relationship_to_billy_jenkins": {
        "type": "string",
        "description": "The relationship between the comedian and Billy Jenkins."
      },
      "documentary_spoof_title": {
        "type": "string",
        "description": "The title of the documentary spoof where the comedian appeared."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the comedian."
      }
    },
    "required": [
      "comedian_name",
      "comedian_profession",
      "relationship_to_billy_jenkins",
      "documentary_spoof_title",
      "nationality"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
