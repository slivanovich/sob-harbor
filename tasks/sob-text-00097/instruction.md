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
Merle M. Rasmussen: Merle Martin Rasmussen is an American game designer and writer best known for creating the espionage role-playing game "Top Secret".

Top Secret (role-playing game): Top Secret is an espionage-themed role-playing game written by Merle M. Rasmussen and first published in 1980 by TSR, Inc.

Bionic Commando (NES video game): Bionic Commando, originally released as Hitler's Resurrection: Top Secret (ヒットラーの復活 <ruby><rb>TOP SECRET</rb><rp>(</rp><rt>トップシークレット</rt><rp>)</rp></ruby> , Hittorā no Fukkatsu: Toppu Shīkuretto ) in Japan, is an action-platformer video game released by Capcom for the Family Computer and Nintendo Entertainment System in 1988.  It is based on the 1987 arcade game of the same title.

Polo Step (code name): Classified as Top Secret, Polo Step was a United States Department of Defense code name or ‘compartment’ that was initially created in the late 1990s to designate closely held planning information on covert operations against Al Qaeda in Afghanistan.  A person could have a Top Secret clearance, but if they would not have a need to know about the planning as well, they did not have a ‘Polo Step’ authorization.

Australia–East Timor spying scandal: The Australia–East Timor spying scandal began in 2012 when the Australian Secret Intelligence Service (ASIS) was revealed to have planted covert listening devices in the cabinet office of East Timor in 2004, with the purpose of gathering top secret information related to bilateral negotiations over the Greater Sunrise oil and gas fields in the oil rich Timor Gap.  "Witness K", a former senior ASIS intelligence officer who was in charge of the bugging, provided information in 2012 which publicly revealed that the Australian Government had gained the top secret knowledge and used it during negotiations over the Treaty on Certain Maritime Arrangements in the Timor Sea (CMats).  This treaty put a 50-year hold on East Timor's pursuit of expanded underwater territory, an area that has an estimated $US40 billion in oil and gas reserves.  East Timor now disputes the validity of the treaty.

Order 7161: Order 7161 refers to the top secret USSR State Defense Committee Order no 7161ss (Постановление № 7161cc ГКО СССР) of December 16, 1944 about mobilisation and internment of able-bodied Germans for reparation works in the USSR.  (The Cyrillic "cc" after the order number is the Russian abbreviation for "top secret".)  It was part of the organisation of forced labor of Germans in the Soviet Union since the ending period of World War II.

Tunis Top Secret: Tunis Top Secret (Italian: "Tunisi top secret" , German: "Akte Sahara - streng vertraulich" ) is a 1959 Italian-German adventure-spy film written and directed by Bruno Paolinelli and starring Elsa Martinelli and Giorgia Moll.

Q clearance: A Q Clearance (or Q-type clearance) is a United States Department of Energy (DOE) security clearance that is roughly comparable to a United States Department of Defense Top Secret clearance with Sensitive Compartmentalized Information Access (TS-SCI).  It is the most permissive clearance granted by the United States Government, acting as the sole means of access to the vast compartmentalizations Top Secret and Secret Restricted Data, and DOE "security" areas.

Himitsu – Top Secret: Himitsu – Top Secret (Japanese: 秘密 -トップ·シークレット- , Hepburn: Himitsu - Toppu Shiikuretto - , lit.  The Top Secret) is a Japanese manga series written and illustrated by Reiko Shimizu.  It has been serialized in "Melody".

Top Secret Drum Corps: Top Secret Drum Corps is a drum corps based in Basel, Switzerland.  With 25 drummers and colorguard members, the corps became famous for its demanding six-minute routine performed at the Edinburgh Tattoo in 2003.  With its invitation to Edinburgh, Top Secret became one of the first non-military, non-British Commonwealth acts to perform on the Esplanade at Edinburgh Castle.

Question: What form of play does Merle M. Rasmussen and Top Secret have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "creator_name": {
      "type": "string",
      "description": "The name of the creator."
    },
    "game_title": {
      "type": "string",
      "description": "The title of the game."
    },
    "game_type": {
      "type": "string",
      "description": "The form of play or genre of the game."
    },
    "game_genre": {
      "type": "string",
      "description": "The specific genre of the game."
    },
    "publication_details": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year the game was first published."
        },
        "publisher": {
          "type": "string",
          "description": "The company that published the game."
        }
      },
      "required": [
        "year",
        "publisher"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "creator_name",
    "game_title",
    "game_type",
    "game_genre",
    "publication_details"
  ],
  "additionalProperties": false
}
