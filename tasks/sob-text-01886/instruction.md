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
George Nunatak: George Nunatak ( ) is a nunatak, 1,050 m high, located midway between the eastern part of the Harold Byrd Mountains and Leverett Glacier in Antarctica.  It was named by the Advisory Committee on Antarctic Names for Paul George, a member of the U.S. Army helicopter unit which supported the United States Geological Survey Topo West and Topo East surveys of 1962–63.

Dirtbag Nunatak: Dirtbag Nunatak ( ) is a ridge-like nunatak rising to 940 m , 3.5 nmi south-southwest of Mount Manke, in the Harold Byrd Mountains in Antarctica.  The feature was mapped by the United States Geological Survey from ground surveys and U.S. Navy aerial photographs, 1960–63.  It was visited in 1977–78 by a United States Antarctic Research Program – Arizona State University geological party, led by Edmund Stump, and named in the spirit of Coalsack Bluff, as thin lenses of disintegrating mica and schist form a type of light soil on the slopes of the nunatak.

Cressey Peak: Cressey Peak is a peak, 870 m high, located 7 nmi east of the Harold Byrd Mountains between the southeast edge of the Ross Ice Shelf and the Watson Escarpment.  It was mapped by the United States Geological Survey from ground surveys and from U.S. Navy air photos, 1960–63, and named by the Advisory Committee on Antarctic Names for Richard N. Cressey, a storekeeper with the Byrd Station winter party in 1958.

Leverett Glacier: Leverett Glacier in Antarctica is about 50 nmi long and 3 to wide, draining northward from the Watson Escarpment, between California Plateau and Stanford Plateau, and then trending west-northwest between the Tapley Mountains and Harold Byrd Mountains to terminate at the head of the Ross Ice Shelf close east of Scott Glacier.  It was discovered in December 1929 by the Byrd Antarctic Expedition geological party under Laurence Gould, and named by him for Frank Leverett, an eminent geologist at the University of Michigan and an authority on the glacial geology of the central United States.

Mount Manke: Mount Manke ( ) is a mountain, 900 m high, marking the eastern limit of the Harold Byrd Mountains in Antarctica.  It was mapped by the United States Geological Survey from ground surveys and U.S. Navy air photos, 1960–63, and was named by the Advisory Committee on Antarctic Names for Robert M. Manke, a utilitiesman with the Byrd Station winter party in 1960.

Ivory Tower (Antarctica): Ivory Tower ( ) is a small peak rising to about 800 m , 1.5 mi east of Fadden Peak, between the Harold Byrd Mountains and the Bender Mountains in Antarctica.  The peak was visited by a United States Antarctic Research Program – Arizona State University geological party, 1977–78, and was so named from its composition of nearly all white marble.

William Womack Heath: William W. Heath was born in Normangee, Texas, to John Al and Runie (née Hill) Heath.  On July 14, 1929, William Womack Heath married Mavis Barnett (February 14, 1908 to April 9, 1998) and they will be a lifelong couple.  After his death, Mavis will marry a 2nd time to David Harold Byrd on her birthday, February 14, 1974.

Sarnoff Mountains: Sarnoff Mountains ( ) is a range of mountains, 25 nautical miles (46 km) long and 4 to 8 nautical miles (15 km) wide separating the west-flowing Boyd and Arthur Glaciers in the Ford Ranges of Marie Byrd Land.  The west end of the range was discovered and roughly plotted from photos taken by Byrd Antarctic Expedition (1928–30) on the flight of December 5, 1929.  The range was mapped in greater detail by the Byrd Antarctic Expedition (1933–35) and United States Antarctic Service (USAS) (1939–41), all expeditions led by R. Admiral Richard E. Byrd.  Named for David Sarnoff, president of RCA (Radio Corporation of America), who provided radio equipment for receiving and transmitting that was used in the field and at Little America by the Byrd Antarctic Expedition (1933–35).

Richard E. Byrd: Rear Admiral Richard Evelyn Byrd Jr., USN (October 25, 1888 – March 11, 1957) was an American naval officer who specialized in feats of exploration.  He was a recipient of the Medal of Honor, the highest honor for valor given by the United States, and was a pioneering American aviator, polar explorer, and organizer of polar logistics.  Aircraft flights in which he served as a navigator and expedition leader crossed the Atlantic Ocean, a segment of the Arctic Ocean, and a segment of the Antarctic Plateau.  Byrd claimed that his expeditions had been the first to reach both the North Pole and the South Pole by air.  However, his claim to have reached the North Pole is disputed.

David Harold Byrd: David Harold "Dry Hole" Byrd (24 April 1900 – 14 September 1986) was a noted Texan producer of petroleum, and a co-founder of the Civil Air Patrol.  Byrd's cousin, polar explorer Richard E. Byrd, named Antarctica's Harold Byrd Mountains for him.

Question: What honor was bestowed on the cousin of David Harold Byrd by the United States?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "honored_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the person who received the honor."
        },
        "relationship_to_david_byrd": {
          "type": "string",
          "description": "The relationship of the honored person to David Harold Byrd."
        }
      },
      "required": [
        "name",
        "relationship_to_david_byrd"
      ],
      "additionalProperties": false
    },
    "honor_details": {
      "type": "object",
      "properties": {
        "honor_name": {
          "type": "string",
          "description": "The name of the honor bestowed."
        },
        "awarding_entity": {
          "type": "string",
          "description": "The entity that bestowed the honor."
        }
      },
      "required": [
        "honor_name",
        "awarding_entity"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The name of the honor bestowed."
    }
  },
  "required": [
    "honored_person",
    "honor_details",
    "final_answer"
  ],
  "additionalProperties": false
}
