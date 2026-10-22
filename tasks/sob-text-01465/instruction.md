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
Halifax Explosion: The Halifax Explosion was a maritime disaster in Halifax, Nova Scotia, Canada, on the morning of 6 December 1917.   , a French cargo ship laden with high explosives, collided with the Norwegian vessel  in the Narrows, a strait connecting the upper Halifax Harbour to Bedford Basin.  A fire on board the French ship ignited her cargo, causing a large explosion that devastated the Richmond district of Halifax.  Approximately 2,000 people were killed by blast, debris, fires and collapsed buildings, and an estimated 9,000 others were injured.  The blast was the largest man-made explosion prior to the development of nuclear weapons, releasing the equivalent energy of roughly 2.9 kilotons of TNT.

Train dispatcher: A train dispatcher is employed by a railroad to direct and facilitate the movement of trains over an assigned territory, which is usually part, or all, of a railroad operating division.  The dispatcher is also responsible for cost effective movement of trains and other on-track railroad equipment to optimize physical (trains) and human resource (crews) assets.

Common Alerting Protocol: The Common Alerting Protocol (CAP) is an XML-based data format for exchanging public warnings and emergencies between alerting technologies]].  CAP allows a warning message to be consistently disseminated simultaneously over many warning systems to many applications, such as Google Public Alerts.  CAP increases warning effectiveness and simplifies the task of activating a warning for responsible officials.

Ilford rail crash (1944): The 1944 Ilford rail crash occurred on 16 January 1944 when, in darkness and dense fog, an express passenger train passed a signal at 'danger' and collided with another passenger train that was stopped at Ilford railway station in Essex.

Centralized traffic control: Centralized traffic control (CTC) is a form of railway signalling that originated in North America.  CTC consolidates train routing decisions that were previously carried out by local signal operators or the train crews themselves.  The system consists of a centralized train dispatcher's office that controls railroad interlockings and traffic flows in portions of the rail system designated as CTC territory.  One hallmark of CTC is a control panel with a graphical depiction of the railroad.  On this panel the dispatcher can keep track of trains' locations across the territory that the dispatcher controls.  Larger railroads may have multiple dispatcher's offices and even multiple dispatchers for each operating division.  These offices are usually located near the busiest yards or stations, and their operational qualities can be compared to air traffic towers.

St Johns train crash 1898: The St Johns train crash happened at 9 am on 21 March 1898 when, in thick fog, a passenger train waiting to enter St Johns Station on the South Eastern Railway, UK was run into by another passenger train.  Three people were killed and about 20 injured.

Ilford rail crash (1915): The 1915 Ilford rail crash occurred on 1 January 1915 when an express passenger train passed a signal at 'danger' and collided with another passenger train that was stopped at Ilford railway station on the Great Eastern Main Line in Essex.  The collision killed ten people and approximately 500 complained of injury.

Vince Coleman (train dispatcher): Patrick Vincent Coleman (13March 18726December 1917) was a train dispatcher for the Canadian Government Railways (formerly the ICR, Intercolonial Railway of Canada) who was killed in the Halifax Explosion, but not before he sent a message to an incoming passenger train to stop out of range of the explosion.  Today he is remembered as one of the heroic figures from the disaster.

Scanet: Scanet is a defunct, analog train radio system used by the Norwegian State Railways (NSB) and later the Norwegian National Rail Administration.  The system was developed by Ascom Radiocom and was installed on the primary railways in Norway between 1993 and 1996.  The system allows radio communication between a train dispatcher, and train drivers and other users involved in railway operations.  Scanet has three main components: the central traffic control, base stations which are located along the railway lines, and mobile station located in the trains.  The system is further connected to the internal railway telephone network, where it functions like a regular telephone.  Scanet is also connected to the automatic train control system.

Pontypridd railway accident: On Monday 23 January 1911, a collision between a passenger train and a coal train on the Taff Vale Railway line at Hopkinstown, outside Pontypridd in Wales, resulted in the loss of eleven (twelve according to the official report) lives.  The accident, also known as the Hopkinstown rail disaster or the Coke Ovens collision, occurred at 9:48 am, when the 09:10 passenger train from Treherbert to Cardiff, heading towards Pontypridd and carrying about 100 people, rounded the bend at Gyfeillion Lower signal box with a clear signal ahead.  The train collided with a stationary coal train that was using the same line.  The impact caused the underframe of the front carriage to rise up and pierce the carriage directly behind it.

Question: Who was the train dispatcher who sent a warning message to another passenger train in the December 6, 1917 Halifax maritime disaster?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "dispatcher_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the train dispatcher."
        },
        "role": {
          "type": "string",
          "description": "The role of the individual during the event."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "disaster_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the disaster."
        },
        "date": {
          "type": "string",
          "description": "The date of the disaster."
        }
      },
      "required": [
        "name",
        "date"
      ],
      "additionalProperties": false
    },
    "warning_action_description": {
      "type": "string",
      "description": "A description of the warning message sent by the dispatcher."
    }
  },
  "required": [
    "dispatcher_details",
    "disaster_details",
    "warning_action_description"
  ],
  "additionalProperties": false
}
