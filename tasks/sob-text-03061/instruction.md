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
Nardcore: Nardcore is a hardcore punk movement that began in Southern California during the early 1980s, originating in Silver Strand Beach and Port Hueneme.  Early bands of the nardcore scene include Agression, Dr. Know, False Confession, Ill Repute, Habeas Corpus, RKL and Scared Straight.  The first venues to regularly host punk shows in the Oxnard area were Casa Tropical (a Quonset hut at the Oxnard Airport), Town and Country (Port Hueneme), Skate Palace (Port Hueneme), and Casa de la Raza (Santa Barbara).

Seabee: United States Naval Construction Battalions, better known as the Seabees, form the Naval Construction Force of the United States Navy.  Their nickname is a heterograph of the first initials "C.B." from the words Construction Battalion.

Naval Construction Battalion Center Port Hueneme: Naval Construction Battalion Center Port Hueneme is the West Coast homeport of the Navy’s Seabees (from "C.B.", the initials for "Construction Battalion").  Port Hueneme (pronounced "Why-nee-mee"), supports the training and mobilization requirements for more than 2,600 active-duty personnel.  The CBC also operates the 1600 acre Naval Base Ventura County - Port Hueneme installation.  The CBC is located on the vast agricultural Oxnard Plain, about 60 mi northwest of Los Angeles, on the Southern California coast.

Naval Base Ventura County: Naval Base Ventura County (NBVC) is a United States Navy base located near Oxnard, California.  The base was formed in 2000 through the merger of Naval Air Station Point Mugu and Naval Construction Battalion Center Port Hueneme.  NBVC is a diverse installation comprising three main facilities—Point Mugu, Port Hueneme and San Nicolas Island—and serving as an all-in-one mobilization site, deep water port, railhead, and airfield.  NBVC supports more than 100 tenant commands with a base population of more than 19,000 personnel, making it the largest employer in Ventura County.

NMCB 25: Naval Mobile Construction Battalion 25 or NMCB 25 is a Navy Reserve Seabee unit that is headquartered at Port Hueneme, CA.

Naval Surface Warfare Center Port Hueneme: Naval Surface Warfare Center, Port Hueneme Division (NSWC PHD), a component of the Naval Sea Systems Command (NAVSEA), is a tenant command located at Naval Base Ventura County in Port Hueneme, California.  In addition to its primary location at Port Hueneme, the division operates detachments at White Sands, New Mexico, N.M., Virginia Beach, Va. and Louisville, Ky.

Hueneme Glacier: Hueneme Glacier ( ) is a glacier, 8 nmi long, draining westward from the Wisconsin Range in Antarctica to enter Reedy Glacier between Griffith Peak and Mickler Spur.  It was mapped by the United States Geological Survey from surveys and U.S. Navy air photos, 1960–64, and was named by the Advisory Committee on Antarctic Names for Port Hueneme, California, the location of the Construction Battalion Center which handled west coast cargo for U.S. Navy Deep Freeze Operations.

Port Hueneme, California: Port Hueneme ( ) is a small beach city in Ventura County, California surrounded by the city of Oxnard and the Santa Barbara Channel.  The name derives from the Spanish spelling of the Chumash Native language word "wene me", meaning "Resting Place".  Juan Rodríguez Cabrillo explored this area and the adjacent Channel Islands in October 1542.  The town's name was officially changed to Port Hueneme in 1939 and was incorporated March 24, 1948.

Construction Battalion Maintenance Unit 302: Construction Battalion Maintenance Unit THREE ZERO TWO (CBMU-302) of the U.S. Navy was commissioned on 31 March 1967.  Along with a sister unit, CBMU-301, was also commissioned.  These units were the first of their kind since Korean War.  The official commissioning ceremony of CBMU-301 and CBMU-302 was held at the U.S. Naval Construction Battalion Center, Port Hueneme, CA on 7 April 1967.  LT Mel Harper was the first Commanding Officer.

Hueneme High School: Hueneme High School (HHS) ( ) is a public four-year high school serving grades 9-12 in Oxnard, California.  The school was founded in 1959 and sits in the heart of South Oxnard.  The school serves south central Oxnard, most of the city of Port Hueneme, and the Navy Base at Port Hueneme.

Question: Where did the Navy Reserve Unit that is headquartered at Port Hueneme, CA get its nickname?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "unit_name": {
      "type": "string",
      "description": "The official name of the Navy Reserve unit."
    },
    "unit_type": {
      "type": "string",
      "description": "The type of the Navy unit."
    },
    "headquarters_location": {
      "type": "string",
      "description": "The city and state where the unit is headquartered."
    },
    "nickname": {
      "type": "string",
      "description": "The common nickname for the unit type."
    },
    "nickname_origin": {
      "type": "string",
      "description": "The explanation of how the nickname was derived."
    }
  },
  "required": [
    "unit_name",
    "unit_type",
    "headquarters_location",
    "nickname",
    "nickname_origin"
  ],
  "additionalProperties": false
}
