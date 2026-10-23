{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBrandenburg Gate: The Brandenburg Gate (German: \"Brandenburger Tor\" ) is an 18th-century neoclassical monument in Berlin, built on the orders of Prussian king Frederick William II after the (temporarily) successful restoration of order during the early Batavian Revolution.  One of the best-known landmarks of Germany, it was built on the site of a former city gate that marked the start of the road from Berlin to the town of Brandenburg an der Havel, which used to be capital of the Margraviate of Brandenburg.\n\nFrederick William II of Prussia: Frederick William II (German: \"Friedrich Wilhelm II.\"  ; 25 September 1744 – 16 November 1797) was King of Prussia, from 1786 until his death.  He was in personal union the Prince-elector of Brandenburg and (via the Orange-Nassau inheritance of his grandfather) sovereign prince of the Canton of Neuchâtel.  Pleasure-loving and indolent, he is seen as the antithesis to his predecessor, Frederick II.  Under his reign, Prussia was weakened internally and externally, and he failed to deal adequately with the challenges to the existing order posed by the French Revolution.  His religious policies were directed against the Enlightenment and aimed at restoring a traditional Protestantism.  However, he was a patron of the arts and responsible for the construction of some notable buildings, among them the Brandenburg Gate in Berlin.\n\nPlane (river): The Plane is a river in Brandenburg, Germany, left tributary of the Havel.  Its total length is 57 km .  The Plane originates in the High Fläming Nature Park, near Rabenstein.  It flows north through Planetal and Golzow.  The Plane joins the Havel in the Breitlingsee lake west of Brandenburg an der Havel.\n\nBrandenburg Euthanasia Centre: The Brandenburg Euthanasia Centre (German: \"NS-Tötungsanstalt Brandenburg\" ), officially known as the Brandenburg an der Havel State Welfare Institute (\"Landes-Pflegeanstalt Brandenburg a. H.\") was established in 1939 and acted during the Nazi era as a killing centre as part of the Nazi Euthanasia Programme, subsequently referred to after the war as Action T4.\n\nTrams in Brandenburg an der Havel: The Brandenburg an der Havel tramway network (German: \"Straßenbahnnetz Brandenburg an der Havel\" ) is a network of tramways forming the centrepiece of the public transport system in Brandenburg an der Havel, a city in the federal state of Brandenburg, Germany.\n\nSilo Canal: The Silo Canal, or Silokanal in German, is a canal in the German state of Brandenburg.  It provides a short cut for vessels navigating the River Havel, avoiding the winding and constricted navigation through the city of Brandenburg an der Havel.\n\nBrandenburg an der Havel: Brandenburg an der Havel (also called Brandenburg or Brandenburg City in English) is a town in Brandenburg, Germany, which served as the capital of the Margraviate of Brandenburg until replaced by Berlin in 1417.\n\nBrandenburg Hauptbahnhof: Brandenburg Hauptbahnhof is the main railway station in the town of Brandenburg an der Havel in the German state of Brandenburg.  It lies on the Berlin–Magdeburg railway at the junction with the Brandenburg Towns Railway.  It has largely lost its former major role for long-distance passenger services and freight traffic, but it continues to serve regional traffic.  A water tower on the site of the former freight yard and a plaque commemorating French forced labourers at the station buildings are heritage-listed.  The station was renamed \"Brandenburg Hauptbahnhof\" at the end of World War II, previously it had been called \"Brandenburg Rb\" (Rb for Deutsche Reichsbahn) station.  It is classified by Deutsche Bahn as a category 3 station.\n\nHans Hermann von Katte: Hans Hermann von Katte (28 February 1704 – 6 November 1730) was a Lieutenant of the Prussian Army and the friend of the future King Frederick II of Prussia, who was at the time the Crown Prince.  He was executed by Frederick's father King Frederick William I of Prussia when Frederick II plotted to escape from the Kingdom of Prussia to the Kingdom of Great Britain.  Some believe that Frederick intended to defect to the service of George II of Great Britain (Frederick William's maternal first cousin and Frederick's maternal uncle) and possibly return to Prussia to depose Frederick William.\n\nWerder (Havel): Werder (Havel) (official name derived from \"Werder an der Havel\" (\"Werder upon Havel\"), colloquially just \"Werder\"), is a town in the state of Brandenburg, Germany, located on the Havel river in the Potsdam-Mittelmark district, west of the state's capital Potsdam.\n\nQuestion: which landmark built on the site of a former city gate that marked the start of the road from Berlin to the town of Brandenburg an der Havel, is Frederick William II of Prussia responsible for?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"landmark_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the landmark.\"\n    },\n    \"builder_king\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the king responsible for building the landmark.\"\n    },\n    \"landmark_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of monument or structure the landmark is.\"\n    },\n    \"original_site_description\": {\n      \"type\": \"string\",\n      \"description\": \"Description of what was on the site before the landmark was built.\"\n    },\n    \"road_start_point\": {\n      \"type\": \"string\",\n      \"description\": \"The city from which the road started.\"\n    },\n    \"road_end_point\": {\n      \"type\": \"string\",\n      \"description\": \"The town to which the road led.\"\n    }\n  },\n  \"required\": [\n    \"landmark_name\",\n    \"builder_king\",\n    \"landmark_type\",\n    \"original_site_description\",\n    \"road_start_point\",\n    \"road_end_point\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "landmark_name": {
        "type": "string",
        "description": "The name of the landmark."
      },
      "builder_king": {
        "type": "string",
        "description": "The name of the king responsible for building the landmark."
      },
      "landmark_type": {
        "type": "string",
        "description": "The type of monument or structure the landmark is."
      },
      "original_site_description": {
        "type": "string",
        "description": "Description of what was on the site before the landmark was built."
      },
      "road_start_point": {
        "type": "string",
        "description": "The city from which the road started."
      },
      "road_end_point": {
        "type": "string",
        "description": "The town to which the road led."
      }
    },
    "required": [
      "landmark_name",
      "builder_king",
      "landmark_type",
      "original_site_description",
      "road_start_point",
      "road_end_point"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
